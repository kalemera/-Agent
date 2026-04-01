"""EVDS Registry MCP Server.

Turk merkez bankasi veri kayit defteri icin MCP arayuzu.
FastMCP 3.2.0 ile 6 tool sunar: search, get, map, fetch, analyze, audit.
"""

from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

from .records import Record, split_list
from .storage import RegistryPaths, load_registry, load_proposals

ROOT = Path(__file__).resolve().parents[2]
PATHS = RegistryPaths.from_root(ROOT)
load_dotenv(ROOT / ".env")

mcp = FastMCP("evds-registry")


def _load_all() -> dict[str, Record]:
    """Registry kayitlarini yukle (series, indicator, theme, source_dependency)."""
    return load_registry(PATHS)


def _collect_source_dependency_ids(
    theme_ids: set[str],
    indicator_ids: set[str],
    registry: dict[str, Record],
) -> set[str]:
    """Tema ve indicator'lara bagli source dependency ID'lerini topla."""
    source_dep_ids: set[str] = set()
    for theme_id in theme_ids:
        theme = registry.get(theme_id)
        if theme and theme["record_type"] == "theme":
            source_dep_ids.update(split_list(theme.get("source_dependency_ids")))
    for item in registry.values():
        if item["record_type"] != "source_dependency":
            continue
        if theme_ids.intersection(split_list(item.get("theme_ids"))):
            source_dep_ids.add(item["id"])
        if indicator_ids.intersection(split_list(item.get("indicator_ids"))):
            source_dep_ids.add(item["id"])
    return source_dep_ids


def _record_summary(record: Record) -> dict:
    """Record'dan minimal ozet dict dondur."""
    return {
        "id": record["id"],
        "title": record["title"],
        "record_type": record["record_type"],
        "status": record.get("status", ""),
    }


def _record_to_dict(record: Record) -> dict:
    """Record'u JSON-serializable dict'e cevir (path ve body dahil)."""
    return {k: v for k, v in record.items() if k != "path"}


def _related_list(ids: set[str], registry: dict[str, Record]) -> list[dict]:
    """ID setinden ilgili kayitlarin ozet listesini dondur."""
    result = []
    for rid in sorted(ids):
        rec = registry.get(rid)
        if rec:
            result.append(_record_summary(rec))
        else:
            result.append({"id": rid, "title": "(bulunamadi)", "record_type": "unknown", "status": ""})
    return result


# ---------------------------------------------------------------------------
# Tool 1: registry_search
# ---------------------------------------------------------------------------
@mcp.tool()
def registry_search(query: str) -> list[dict]:
    """Seri, indicator, tema ve source dependency arasinda arama yapar.
    ID ve baslik uzerinde buyuk-kucuk harf duyarsiz substring eslestirmesi.
    """
    registry = _load_all()
    q = query.lower()
    results = []
    for record in registry.values():
        if q in record["id"].lower() or q in record["title"].lower():
            results.append(_record_summary(record))
    return results


# ---------------------------------------------------------------------------
# Tool 2: registry_get
# ---------------------------------------------------------------------------
@mcp.tool()
def registry_get(record_id: str) -> dict:
    """Belirli bir kayit ID'si icin tam kayit verisini dondurur."""
    registry = _load_all()
    record = registry.get(record_id)
    if record is None:
        return {"error": f"Kayit bulunamadi: {record_id}"}
    return _record_to_dict(record)


# ---------------------------------------------------------------------------
# Tool 3: registry_map
# ---------------------------------------------------------------------------
@mcp.tool()
def registry_map(record_id: str) -> dict:
    """Bir kaydin baglanti grafigini dondurur.
    Tema, seri, indicator ve source dependency iliskilerini gosterir.
    """
    registry = _load_all()
    record = registry.get(record_id)
    if record is None:
        return {"error": f"Kayit bulunamadi: {record_id}"}

    rtype = record["record_type"]
    linked_series: set[str] = set()
    linked_indicators: set[str] = set()
    linked_themes: set[str] = set()
    linked_source_deps: set[str] = set()

    if rtype == "series":
        linked_indicators = set(split_list(record.get("indicator_ids")))
        linked_themes = set(split_list(record.get("theme_ids")))
        for item in registry.values():
            if item["record_type"] == "indicator" and record["id"] in split_list(item.get("input_ids")):
                linked_indicators.add(item["id"])
                linked_themes.update(split_list(item.get("theme_ids")))
            if item["record_type"] == "theme" and record["id"] in split_list(item.get("series_ids")):
                linked_themes.add(item["id"])
        linked_source_deps = _collect_source_dependency_ids(linked_themes, linked_indicators, registry)

    elif rtype == "indicator":
        linked_series = set(split_list(record.get("input_ids")))
        linked_themes = set(split_list(record.get("theme_ids")))
        for item in registry.values():
            if item["record_type"] == "theme" and record["id"] in split_list(item.get("indicator_ids")):
                linked_themes.add(item["id"])
        linked_source_deps = _collect_source_dependency_ids(linked_themes, {record["id"]}, registry)

    elif rtype == "theme":
        linked_series = set(split_list(record.get("series_ids")))
        linked_indicators = set(split_list(record.get("indicator_ids")))
        linked_source_deps = set(split_list(record.get("source_dependency_ids")))
        for item in registry.values():
            if item["record_type"] == "series" and record["id"] in split_list(item.get("theme_ids")):
                linked_series.add(item["id"])
            if item["record_type"] == "indicator" and record["id"] in split_list(item.get("theme_ids")):
                linked_indicators.add(item["id"])
            if item["record_type"] == "source_dependency" and record["id"] in split_list(item.get("theme_ids")):
                linked_source_deps.add(item["id"])

    elif rtype == "source_dependency":
        linked_themes = set(split_list(record.get("theme_ids")))
        linked_indicators = set(split_list(record.get("indicator_ids")))
        for item in registry.values():
            if item["record_type"] == "theme" and record["id"] in split_list(item.get("source_dependency_ids")):
                linked_themes.add(item["id"])
                linked_series.update(split_list(item.get("series_ids")))
                linked_indicators.update(split_list(item.get("indicator_ids")))
            if item["record_type"] == "indicator" and record["id"] in split_list(item.get("input_ids")):
                linked_indicators.add(item["id"])
                linked_themes.update(split_list(item.get("theme_ids")))
            if item["record_type"] == "series" and any(
                tid in split_list(item.get("theme_ids")) for tid in linked_themes
            ):
                linked_series.add(item["id"])

    return {
        "record": _record_summary(record),
        "linked_series": _related_list(linked_series, registry),
        "linked_indicators": _related_list(linked_indicators, registry),
        "linked_themes": _related_list(linked_themes, registry),
        "linked_source_deps": _related_list(linked_source_deps, registry),
    }


# ---------------------------------------------------------------------------
# Tool 4: registry_fetch
# ---------------------------------------------------------------------------
@mcp.tool()
def registry_fetch(tickers: str, start: str, end: str) -> dict:
    """EVDS API'den canli veri ceker.
    tickers: virgul-ayirmali ticker listesi (ornek: 'TP.DK.USD.A,TP.DK.EUR.A').
    start/end: tarih formati 'DD-MM-YYYY'.
    """
    from .source_adapters import EVDSAdapter

    adapter = EVDSAdapter.from_env()
    if not adapter.is_configured():
        return {"error": "EVDS_API_KEY ortam degiskeni ayarlanmamis."}
    ticker_list = [t.strip() for t in tickers.split(",") if t.strip()]
    if not ticker_list:
        return {"error": "En az bir ticker gerekli."}
    df = adapter.fetch_observations(ticker_list, start=start, end=end)
    return {
        "tickers": ticker_list,
        "start": start,
        "end": end,
        "row_count": len(df),
        "data": df.to_dict(orient="records"),
    }


# ---------------------------------------------------------------------------
# Tool 5: registry_analyze
# ---------------------------------------------------------------------------
@mcp.tool()
def registry_analyze(notebook_path: str) -> dict:
    """Notebook analizi calistirir. Ticker, tema, indicator ve source dependency cikarir."""
    from .notebook_analysis import build_notebook_analysis

    result = build_notebook_analysis(notebook_path, spec="auto")
    return {
        "spec_slug": result.spec_slug,
        "ticker_count": len(result.analyses),
        "unresolved_count": len(result.unresolved_items),
        "unresolved_items": result.unresolved_items,
        "themes": [{"id": t.id, "title": t.title} for t in result.themes],
        "indicators": [{"id": i.id, "title": i.title} for i in result.indicators],
        "source_dependencies": [
            {"id": sd.id, "title": sd.title} for sd in result.source_dependencies
        ],
    }


# ---------------------------------------------------------------------------
# Tool 6: registry_audit
# ---------------------------------------------------------------------------
@mcp.tool()
def registry_audit() -> dict:
    """Registry butunluk denetimi. Eksik referanslar ve yetim kayitlari bulur."""
    registry = _load_all()
    issues: list[str] = []

    series = {k: v for k, v in registry.items() if v["record_type"] == "series"}
    indicators = {k: v for k, v in registry.items() if v["record_type"] == "indicator"}
    themes = {k: v for k, v in registry.items() if v["record_type"] == "theme"}
    source_deps = {k: v for k, v in registry.items() if v["record_type"] == "source_dependency"}

    # Indicator input referanslari
    for iid, ind in indicators.items():
        for input_id in split_list(ind.get("input_ids")):
            if input_id not in registry:
                issues.append(f"Indicator '{iid}' eksik input referansi: {input_id}")

    # Theme referanslari
    for tid, theme in themes.items():
        for sid in split_list(theme.get("series_ids")):
            if sid not in registry:
                issues.append(f"Theme '{tid}' eksik series referansi: {sid}")
        for iid in split_list(theme.get("indicator_ids")):
            if iid not in registry:
                issues.append(f"Theme '{tid}' eksik indicator referansi: {iid}")
        for sdid in split_list(theme.get("source_dependency_ids")):
            if sdid not in registry:
                issues.append(f"Theme '{tid}' eksik source_dependency referansi: {sdid}")

    # Source dependency referanslari
    for sdid, sd in source_deps.items():
        for tid in split_list(sd.get("theme_ids")):
            if tid not in registry:
                issues.append(f"Source dependency '{sdid}' eksik theme referansi: {tid}")
        for iid in split_list(sd.get("indicator_ids")):
            if iid not in registry:
                issues.append(f"Source dependency '{sdid}' eksik indicator referansi: {iid}")

    # Yetim seriler (hicbir tema'ya bagli degil)
    all_theme_series = set()
    for theme in themes.values():
        all_theme_series.update(split_list(theme.get("series_ids")))
    for sid, s in series.items():
        has_theme_ref = sid in all_theme_series or bool(split_list(s.get("theme_ids")))
        if not has_theme_ref:
            issues.append(f"Yetim seri (hicbir tema'ya bagli degil): {sid}")

    return {
        "series_count": len(series),
        "indicator_count": len(indicators),
        "theme_count": len(themes),
        "source_dep_count": len(source_deps),
        "issue_count": len(issues),
        "issues": issues,
    }


if __name__ == "__main__":
    mcp.run()
