from __future__ import annotations

import csv
import io
import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .records import Record, normalize_catalog_input
from .storage import RegistryPaths, load_catalog, write_record


JsonDict = dict[str, Any]


FREQUENCY_ALIASES = {
    "daily": "daily",
    "gunluk": "daily",
    "günlük": "daily",
    "is gunu": "daily",
    "iş günü": "daily",
    "weekly": "weekly",
    "haftalik": "weekly",
    "haftalık": "weekly",
    "monthly": "monthly",
    "aylik": "monthly",
    "aylık": "monthly",
    "quarterly": "quarterly",
    "ceyreklik": "quarterly",
    "çeyreklik": "quarterly",
    "yearly": "yearly",
    "annual": "yearly",
    "yillik": "yearly",
    "yıllık": "yearly",
}

UNIT_HINTS = (
    "tl",
    "ytl",
    "try",
    "usd",
    "abd dolari",
    "abd doları",
    "euro",
    "eur",
    "milyon",
    "bin",
    "milyar",
    "yuzde",
    "yüzde",
    "%",
    "endeks",
    "puan",
    "adet",
    "ton",
    "varil",
    "mb",
)


class EVDSCatalogError(RuntimeError):
    """Raised when the EVDS catalog cannot be synced."""


@dataclass(slots=True, frozen=True)
class EVDSCatalogRecord:
    ticker: str
    title: str
    frequency: str
    unit: str
    source_version: str
    data_group: str
    category: str
    official_url: str
    raw_metadata: JsonDict

    @property
    def id(self) -> str:
        return f"catalog:{self.source_version}:{self.ticker}"

    def to_record(self) -> Record:
        return normalize_catalog_input(
            {
                "id": self.id,
                "ticker": self.ticker,
                "title": self.title,
                "frequency": self.frequency,
                "unit": self.unit,
                "source_version": self.source_version,
                "data_group": self.data_group,
                "category": self.category,
                "official_url": self.official_url,
                "raw_metadata": self.raw_metadata,
            }
        )


@dataclass(slots=True)
class TCMBEVDSCatalogClient:
    source_version: str
    api_key: str = ""
    base_url: str = ""
    fetch_text: Callable[[str, dict[str, str]], str] | None = None
    _category_cache: list[JsonDict] | None = field(default=None, init=False, repr=False)

    @classmethod
    def from_env(cls, source_version: str) -> "TCMBEVDSCatalogClient":
        api_key = os.getenv("EVDS_API_KEY") or os.getenv("EVDS_KEY") or ""
        base_url = os.getenv("EVDS_BASE_URL", "https://evds3.tcmb.gov.tr/igmevdsms-dis/")
        return cls(source_version=source_version, api_key=api_key, base_url=base_url.rstrip("/") + "/")

    def list_categories(self) -> list[JsonDict]:
        if self._is_modern_api():
            if self._category_cache is None:
                self._category_cache = self._fetch_rows("categories/withDatagroups/type=json")
            return list(self._category_cache)
        rows = self._fetch_rows("categories") or self._fetch_rows("main_categories")
        return rows

    def list_datagroups(self, category_id: str = "", group_code: str = "") -> list[JsonDict]:
        if self._is_modern_api():
            rows: list[JsonDict] = []
            for category in self.list_categories():
                current_category_id = first_value(category, "CATEGORY_ID", "code", "categoryId")
                if category_id and current_category_id != category_id:
                    continue
                datagroups = category.get("DATAGROUPS")
                if not isinstance(datagroups, list):
                    continue
                for datagroup in datagroups:
                    if not isinstance(datagroup, dict):
                        continue
                    current_group_code = first_value(datagroup, "DATAGROUP_CODE", "dataGroupCode")
                    if group_code and current_group_code != group_code:
                        continue
                    enriched = dict(datagroup)
                    enriched.setdefault("CATEGORY_ID", current_category_id)
                    enriched.setdefault(
                        "CATEGORY_NAME",
                        first_value(category, "TOPIC_TITLE_TR", "CATEGORY_NAME", "topicTitleTR"),
                    )
                    enriched.setdefault("TOPIC_TITLE_TR", first_value(category, "TOPIC_TITLE_TR", "topicTitleTR"))
                    enriched.setdefault("TOPIC_TITLE_ENG", first_value(category, "TOPIC_TITLE_ENG", "topicTitleEng"))
                    rows.append(enriched)
            return rows
        query = {}
        if category_id:
            query["code"] = category_id
        if group_code:
            query["code"] = group_code
        return self._fetch_rows("datagroups", query)

    def list_series(self, code: str) -> list[JsonDict]:
        if not code:
            return []
        if self._is_modern_api():
            return self._fetch_rows(f"serieList/fe/type=json&code={code}")
        return self._fetch_rows("serieList", {"code": code})

    def hydrate_ticker(self, ticker: str) -> JsonDict | None:
        if self._is_modern_api():
            payload = self._fetch_json("searchResults", {"searchVal": ticker})
            if not isinstance(payload, dict):
                return None
            series_rows = payload.get("seriler")
            if not isinstance(series_rows, list):
                return None
            for row in series_rows:
                if not isinstance(row, dict):
                    continue
                code = first_value(row, "serieCode", "SERIE_CODE", "serie_code", "CODE", "code")
                if code != ticker:
                    continue
                merged = dict(row)
                data_group_code = first_value(row, "dataGroupCode", "DATAGROUP_CODE")
                if data_group_code:
                    for group_row in self.list_series(data_group_code):
                        group_code = first_value(group_row, "SERIE_CODE", "serieCode", "code")
                        if group_code == ticker:
                            base_row = dict(group_row)
                            base_row.update(merged)
                            merged = base_row
                            break
                    if "dataGroup" not in merged:
                        group_rows = self.list_datagroups(group_code=data_group_code)
                        if group_rows:
                            merged["dataGroup"] = dict(group_rows[0])
                return merged
            return None
        rows = self.list_series(ticker)
        for row in rows:
            code = first_value(row, "SERIE_CODE", "serie_code", "CODE", "code")
            if code == ticker:
                return row
        return None

    def _is_modern_api(self) -> bool:
        return "igmevdsms-dis" in self.base_url

    def _fetch_rows(self, service: str, query: dict[str, str] | None = None) -> list[JsonDict]:
        if self._is_modern_api():
            try:
                return self._decode_rows(self._fetch_text(self._build_url(service, query)))
            except Exception as exc:  # noqa: BLE001
                raise EVDSCatalogError(f"Failed to fetch EVDS {service}: {exc}") from exc
        last_error: Exception | None = None
        for url in self._candidate_urls(service, query or {}):
            try:
                return self._decode_rows(self._fetch_text(url))
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                continue
        if last_error:
            raise EVDSCatalogError(f"Failed to fetch EVDS {service}: {last_error}") from last_error
        raise EVDSCatalogError(f"Failed to fetch EVDS {service}")

    def _candidate_urls(self, service: str, query: dict[str, str]) -> list[str]:
        variants: list[str] = []
        query_pairs = dict(query)
        query_pairs.setdefault("type", "json")
        encoded = urlencode(query_pairs)
        service_url = f"{self.base_url}{service}"
        variants.append(f"{service_url}/?{encoded}")
        variants.append(f"{service_url}?{encoded}")
        variants.append(f"{service_url}/{encoded}")
        if "code" in query_pairs:
            code = query_pairs["code"]
            variants.append(f"{service_url}/{code}/?type=json")
            variants.append(f"{service_url}/{code}?type=json")
        return variants

    def _fetch_text(self, url: str) -> str:
        headers = {"Accept": "application/json,text/csv;q=0.9,*/*;q=0.8"}
        if self.api_key:
            headers["key"] = self.api_key
        if self.fetch_text is not None:
            return self.fetch_text(url, headers)
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:  # noqa: S310
            return response.read().decode("utf-8-sig")

    def _fetch_json(self, service: str, query: dict[str, str] | None = None) -> Any:
        return json.loads(self._fetch_text(self._build_url(service, query)))

    def _build_url(self, service: str, query: dict[str, str] | None = None) -> str:
        if service.startswith("http://") or service.startswith("https://"):
            return service
        service_url = f"{self.base_url}{service.lstrip('/')}"
        if not query:
            return service_url
        separator = "&" if "?" in service_url else "?"
        return f"{service_url}{separator}{urlencode(query)}"

    @staticmethod
    def _decode_rows(raw_text: str) -> list[JsonDict]:
        text = raw_text.strip()
        if not text:
            return []
        if text.startswith("{") or text.startswith("["):
            payload = json.loads(text)
            if isinstance(payload, list):
                return [item for item in payload if isinstance(item, dict)]
            if isinstance(payload, dict):
                for value in payload.values():
                    if isinstance(value, list) and all(isinstance(item, dict) for item in value):
                        return value
                return [payload]
        reader = csv.DictReader(io.StringIO(text))
        return [dict(row) for row in reader]


def first_value(row: JsonDict, *keys: str) -> str:
    for key in keys:
        value = row.get(key)
        if value is None:
            continue
        text = str(value).strip()
        if text:
            return text
    return ""


def first_nested_value(row: JsonDict, *paths: tuple[str, ...]) -> str:
    for path in paths:
        current: Any = row
        for key in path:
            if not isinstance(current, dict):
                current = None
                break
            current = current.get(key)
        if current is None:
            continue
        text = str(current).strip()
        if text:
            return text
    return ""


def normalize_frequency(value: str) -> str:
    normalized = value.strip().casefold()
    for key, mapped in FREQUENCY_ALIASES.items():
        if key in normalized:
            return mapped
    return normalized or "unknown"


def infer_unit(title: str, explicit_unit: str = "") -> str:
    if explicit_unit:
        return explicit_unit.strip()
    if "(" not in title or ")" not in title:
        return ""
    candidates = [part.strip() for part in title.split("(")[1:]]
    for candidate in reversed(candidates):
        value = candidate.rstrip(")").strip().casefold()
        if any(marker in value for marker in UNIT_HINTS):
            return candidate.rstrip(")").strip()
    return ""


def row_to_catalog_record(row: JsonDict, source_version: str, category: str = "", data_group: str = "") -> EVDSCatalogRecord | None:
    ticker = first_value(row, "SERIE_CODE", "serieCode", "serie_code", "CODE", "code")
    title = first_value(row, "SERIE_NAME", "serieName", "serie_name", "NAME", "name", "TOPIC_TITLE")
    if not ticker or not title:
        return None
    frequency = normalize_frequency(first_value(row, "FREQUENCY_STR", "frequencyStr", "FREQUENCY", "frequency"))
    unit = infer_unit(
        title,
        first_value(row, "UNIT_STR", "UNIT", "UNIT_DESC", "unit")
        or first_nested_value(row, ("dataGroup", "birimi"), ("dataGroup", "birimiEn")),
    )
    official_url = first_value(row, "METADATA_LINK", "metaDataLink", "URL", "url", "WEB_URL") or first_nested_value(
        row,
        ("dataGroup", "metaDataLink"),
        ("dataGroup", "METADATA_LINK"),
    )
    resolved_group = data_group or first_value(row, "DATAGROUP_CODE", "dataGroupCode", "GROUP_CODE", "group_code")
    resolved_category = (
        category
        or first_value(row, "CATEGORY_NAME", "TOPIC_TITLE", "category_name")
        or first_nested_value(
            row,
            ("dataGroup", "category", "topicTitleTR"),
            ("dataGroup", "category", "TOPIC_TITLE_TR"),
            ("dataGroup", "dataGroupType"),
            ("dataGroup", "DATAGROUP_TYPE"),
        )
    )
    return EVDSCatalogRecord(
        ticker=ticker,
        title=title,
        frequency=frequency or "unknown",
        unit=unit or "unknown",
        source_version=source_version,
        data_group=resolved_group,
        category=resolved_category,
        official_url=official_url,
        raw_metadata=dict(row),
    )


def parse_scope(scope: str) -> tuple[str, str]:
    value = scope.strip()
    if value == "all":
        return "all", ""
    if ":" not in value:
        raise ValueError("Scope must be one of: all, category:<id>, group:<code>, ticker:<code>.")
    kind, target = value.split(":", 1)
    kind = kind.strip().lower()
    target = target.strip()
    if kind not in {"category", "group", "ticker"} or not target:
        raise ValueError("Scope must be one of: all, category:<id>, group:<code>, ticker:<code>.")
    return kind, target


def build_catalog_index(records: dict[str, Record], source_version: str = "") -> dict[str, Record]:
    index: dict[str, Record] = {}
    for record in records.values():
        if record.get("record_type") != "catalog":
            continue
        if source_version and record.get("source_version") not in {source_version, ""}:
            continue
        ticker = str(record.get("ticker") or "").strip()
        if ticker:
            index[ticker] = record
    return index


def sync_evds_catalog(paths: RegistryPaths, source_version: str, scope: str, client: TCMBEVDSCatalogClient | None = None) -> list[Record]:
    evds_client = client or TCMBEVDSCatalogClient.from_env(source_version)
    kind, target = parse_scope(scope)
    written: dict[str, Record] = {}

    def add_record(row: JsonDict, category: str = "", data_group: str = "", group_metadata: JsonDict | None = None) -> None:
        merged_row = dict(row)
        if group_metadata:
            merged_row.setdefault("dataGroup", dict(group_metadata))
        item = row_to_catalog_record(merged_row, source_version, category=category, data_group=data_group)
        if item is None:
            return
        record = item.to_record()
        write_record(paths.catalog, record)
        written[record["id"]] = record

    if kind == "ticker":
        row = evds_client.hydrate_ticker(target)
        if row is None:
            raise EVDSCatalogError(f"Ticker could not be hydrated from EVDS: {target}")
        add_record(row)
        return list(written.values())

    if kind == "group":
        group_rows = evds_client.list_datagroups(group_code=target)
        group_metadata = group_rows[0] if group_rows else None
        category_name = ""
        if group_metadata is not None:
            category_name = first_value(group_metadata, "CATEGORY_NAME", "TOPIC_TITLE_TR", "category_name")
        for row in evds_client.list_series(target):
            add_record(row, category=category_name, data_group=target, group_metadata=group_metadata)
        return list(written.values())

    if kind == "category":
        category_rows = evds_client.list_datagroups(category_id=target)
        for group_row in category_rows:
            group_code = first_value(group_row, "DATAGROUP_CODE", "GROUP_CODE", "code")
            category_name = first_value(group_row, "CATEGORY_NAME", "TOPIC_TITLE", "category_name")
            if not group_code:
                continue
            for row in evds_client.list_series(group_code):
                add_record(row, category=category_name, data_group=group_code, group_metadata=group_row)
        return list(written.values())

    for category_row in evds_client.list_categories():
        category_id = first_value(category_row, "CATEGORY_ID", "TOPIC_ID", "code", "CODE")
        category_name = first_value(category_row, "CATEGORY_NAME", "TOPIC_TITLE", "category_name")
        if not category_id:
            continue
        for group_row in evds_client.list_datagroups(category_id=category_id):
            group_code = first_value(group_row, "DATAGROUP_CODE", "GROUP_CODE", "code")
            resolved_category = category_name or first_value(group_row, "CATEGORY_NAME", "TOPIC_TITLE", "category_name")
            if not group_code:
                continue
            for row in evds_client.list_series(group_code):
                add_record(row, category=resolved_category, data_group=group_code, group_metadata=group_row)
    return list(written.values())


def ensure_catalog_entry(paths: RegistryPaths, ticker: str, source_version: str, client: TCMBEVDSCatalogClient | None = None) -> Record | None:
    catalog_index = build_catalog_index(load_catalog(paths), source_version)
    if ticker in catalog_index:
        return catalog_index[ticker]
    evds_client = client or TCMBEVDSCatalogClient.from_env(source_version)
    row = evds_client.hydrate_ticker(ticker)
    if row is None:
        return None
    item = row_to_catalog_record(row, source_version)
    if item is None:
        return None
    record = item.to_record()
    write_record(paths.catalog, record)
    return record
