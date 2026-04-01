from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Protocol

from .evds_catalog import TCMBEVDSCatalogClient, row_to_catalog_record, first_value


class SourceAdapter(Protocol):
    def search_series(self, query: str) -> list[dict]:
        """Return matching series metadata from the source."""

    def hydrate_metadata(self, ticker: str) -> dict:
        """Return canonical metadata for a known series identifier."""

    def fetch_observations(self, ticker: str, start: str | None = None, end: str | None = None) -> list[dict]:
        """Return time-series observations for a known series identifier."""


@dataclass(slots=True)
class EVDSAdapter:
    api_key: str = ""
    source_version: str = "evds2"

    @classmethod
    def from_env(cls) -> "EVDSAdapter":
        api_key = os.getenv("EVDS_API_KEY") or os.getenv("EVDS_KEY") or ""
        return cls(api_key=api_key)

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def search_series(self, query: str) -> list[dict]:
        client = TCMBEVDSCatalogClient.from_env(self.source_version)
        client.api_key = self.api_key
        payload = client._fetch_json("searchResults", {"searchVal": query})
        if not isinstance(payload, dict):
            return []
        series_rows = payload.get("seriler")
        if not isinstance(series_rows, list):
            return []
        results = []
        for row in series_rows:
            if not isinstance(row, dict):
                continue
            results.append({
                "ticker": first_value(row, "serieCode", "SERIE_CODE"),
                "title": first_value(row, "serieName", "SERIE_NAME"),
                "frequency": first_value(row, "frequencyStr", "FREQUENCY_STR"),
                "data_group": first_value(row, "dataGroupCode", "DATAGROUP_CODE"),
            })
        return results

    def hydrate_metadata(self, ticker: str) -> dict[str, Any]:
        client = TCMBEVDSCatalogClient.from_env(self.source_version)
        client.api_key = self.api_key
        row = client.hydrate_ticker(ticker)
        if row is None:
            return {}
        record = row_to_catalog_record(row, self.source_version)
        if record is None:
            return {}
        return {
            "ticker": record.ticker,
            "title": record.title,
            "frequency": record.frequency,
            "unit": record.unit,
            "data_group": record.data_group,
            "category": record.category,
        }

    def fetch_observations(
        self,
        tickers: list[str],
        start: str = "",
        end: str = "",
        frequency: str = "",
    ) -> Any:
        """Fetch live data using the evds library. Returns a pandas DataFrame."""
        from evds import evdsAPI
        evds = evdsAPI(self.api_key)
        kwargs: dict[str, Any] = {}
        if frequency:
            kwargs["frequency"] = frequency
        return evds.get_data(tickers, startdate=start, enddate=end, **kwargs)
