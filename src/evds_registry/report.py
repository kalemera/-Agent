from __future__ import annotations

from pathlib import Path
from typing import Any

from .records import Record, split_list
from .source_adapters import EVDSAdapter
from .storage import RegistryPaths, load_registry


def generate_theme_report(
    paths: RegistryPaths,
    theme_id: str,
    adapter: EVDSAdapter,
    start: str,
    end: str,
) -> str:
    """Generate a Markdown report for a theme with live data."""
    registry = load_registry(paths)
    theme = registry.get(theme_id)
    if theme is None or theme.get("record_type") != "theme":
        raise ValueError(f"Tema bulunamadi: {theme_id}")

    sections: list[str] = []
    sections.append(_render_tema_ozeti(theme))

    series_ids, indicator_ids, source_dep_ids = _collect_linked_ids(theme, registry)

    sections.append(_render_bagli_seriler(series_ids, registry))
    sections.append(_render_bagli_indicatorler(indicator_ids, registry))
    sections.append(_render_source_dependencies(source_dep_ids, registry))
    sections.append(_render_canli_veri_ozeti(series_ids, registry, adapter, start, end))
    sections.append(_render_baglanti_grafigi(theme, series_ids, indicator_ids, registry))

    return "\n".join(sections)


def _collect_linked_ids(
    theme: Record, registry: dict[str, Record]
) -> tuple[set[str], set[str], set[str]]:
    """Collect series, indicator, and source dependency IDs linked to a theme.

    Uses both the theme's own fields and reverse lookups from registry records.
    Same logic as render_theme_map in cli.py.
    """
    series_ids = set(split_list(theme.get("series_ids")))
    indicator_ids = set(split_list(theme.get("indicator_ids")))
    source_dep_ids = set(split_list(theme.get("source_dependency_ids")))

    theme_id = theme["id"]
    for item in registry.values():
        item_theme_ids = split_list(item.get("theme_ids"))
        if item["record_type"] == "series" and theme_id in item_theme_ids:
            series_ids.add(item["id"])
        if item["record_type"] == "indicator" and theme_id in item_theme_ids:
            indicator_ids.add(item["id"])
        if item["record_type"] == "source_dependency" and theme_id in item_theme_ids:
            source_dep_ids.add(item["id"])

    return series_ids, indicator_ids, source_dep_ids


def _render_tema_ozeti(theme: Record) -> str:
    title = theme.get("title") or theme["id"]
    description = theme.get("description") or "-"
    questions = split_list(theme.get("questions"))

    lines = [
        f"# {title}",
        "",
        "## Tema Ozeti",
        "",
        f"**Baslik:** {title}",
        f"**Aciklama:** {description}",
        "",
    ]
    if questions:
        lines.append("**Analiz Sorulari:**")
        for q in questions:
            lines.append(f"- {q}")
    else:
        lines.append("**Analiz Sorulari:** -")
    lines.append("")
    return "\n".join(lines)


def _render_bagli_seriler(series_ids: set[str], registry: dict[str, Record]) -> str:
    lines = [
        "## Bagli Seriler",
        "",
    ]
    if not series_ids:
        lines.append("Bagli seri bulunamadi.")
        lines.append("")
        return "\n".join(lines)

    lines.append("| Ticker | Baslik | Frekans | Birim |")
    lines.append("|--------|--------|---------|-------|")
    for sid in sorted(series_ids):
        rec = registry.get(sid)
        if rec is None:
            lines.append(f"| {sid} | _(kayit yok)_ | - | - |")
            continue
        ticker = rec.get("ticker") or sid
        title = rec.get("title") or "-"
        freq = rec.get("frequency") or "-"
        unit = rec.get("unit") or "-"
        lines.append(f"| {ticker} | {title} | {freq} | {unit} |")
    lines.append("")
    return "\n".join(lines)


def _render_bagli_indicatorler(indicator_ids: set[str], registry: dict[str, Record]) -> str:
    lines = [
        "## Bagli Indicatorler",
        "",
    ]
    if not indicator_ids:
        lines.append("Bagli indicator bulunamadi.")
        lines.append("")
        return "\n".join(lines)

    lines.append("| ID | Baslik | Formul | Girdi ID'leri |")
    lines.append("|----|--------|--------|---------------|")
    for iid in sorted(indicator_ids):
        rec = registry.get(iid)
        if rec is None:
            lines.append(f"| {iid} | _(kayit yok)_ | - | - |")
            continue
        title = rec.get("title") or "-"
        formula = rec.get("formula_expression") or rec.get("formula_description") or "-"
        input_ids = ", ".join(split_list(rec.get("input_ids"))) or "-"
        lines.append(f"| {iid} | {title} | {formula} | {input_ids} |")
    lines.append("")
    return "\n".join(lines)


def _render_source_dependencies(source_dep_ids: set[str], registry: dict[str, Record]) -> str:
    lines = [
        "## Source Dependencies",
        "",
    ]
    if not source_dep_ids:
        lines.append("Source dependency bulunamadi.")
        lines.append("")
        return "\n".join(lines)

    lines.append("| ID | Baslik | Tur | Zorunluluk |")
    lines.append("|----|--------|-----|------------|")
    for did in sorted(source_dep_ids):
        rec = registry.get(did)
        if rec is None:
            lines.append(f"| {did} | _(kayit yok)_ | - | - |")
            continue
        title = rec.get("title") or "-"
        kind = rec.get("source_kind") or "-"
        req = rec.get("requiredness") or "-"
        lines.append(f"| {did} | {title} | {kind} | {req} |")
    lines.append("")
    return "\n".join(lines)


def _render_canli_veri_ozeti(
    series_ids: set[str],
    registry: dict[str, Record],
    adapter: EVDSAdapter,
    start: str,
    end: str,
) -> str:
    lines = [
        "## Canli Veri Ozeti",
        "",
    ]
    if not adapter.is_configured():
        lines.append("EVDS_API_KEY ayarlanmadigi icin canli veri alinamadi.")
        lines.append("")
        return "\n".join(lines)

    if not series_ids:
        lines.append("Bagli seri bulunamadi, canli veri yok.")
        lines.append("")
        return "\n".join(lines)

    tickers: list[str] = []
    for sid in sorted(series_ids):
        rec = registry.get(sid)
        if rec is not None:
            ticker = rec.get("ticker") or ""
            if ticker:
                tickers.append(ticker)
        else:
            clean = sid.removeprefix("evds:")
            if clean:
                tickers.append(clean)

    # Limit to 10 series
    tickers = tickers[:10]

    lines.append("| Ticker | Son Deger | Min | Max | Trend |")
    lines.append("|--------|-----------|-----|-----|-------|")

    for ticker in tickers:
        row = _fetch_single_series_summary(adapter, ticker, start, end)
        lines.append(
            f"| {ticker} | {row['son_deger']} | {row['min']} | {row['max']} | {row['trend']} |"
        )
    lines.append("")
    return "\n".join(lines)


def _fetch_single_series_summary(
    adapter: EVDSAdapter, ticker: str, start: str, end: str
) -> dict[str, str]:
    """Fetch observations for a single ticker and compute summary stats."""
    try:
        df = adapter.fetch_observations([ticker], start=start, end=end)
        # DataFrame columns: Tarih + TP_XXX_YYY (ticker with dots replaced by underscores)
        value_cols = [c for c in df.columns if c != "Tarih"]
        if not value_cols or df.empty:
            return {"son_deger": "-", "min": "-", "max": "-", "trend": "-"}

        col = value_cols[0]
        import pandas as pd

        numeric = pd.to_numeric(df[col], errors="coerce").dropna()
        if numeric.empty:
            return {"son_deger": "-", "min": "-", "max": "-", "trend": "-"}

        son = numeric.iloc[-1]
        vmin = numeric.min()
        vmax = numeric.max()

        # Trend: compare last value to first value
        if len(numeric) >= 2:
            first = numeric.iloc[0]
            if son > first:
                trend = "yukari"
            elif son < first:
                trend = "asagi"
            else:
                trend = "yatay"
        else:
            trend = "yatay"

        return {
            "son_deger": _fmt_num(son),
            "min": _fmt_num(vmin),
            "max": _fmt_num(vmax),
            "trend": trend,
        }
    except Exception:
        return {"son_deger": "Veri alinamadi", "min": "-", "max": "-", "trend": "-"}


def _fmt_num(val: Any) -> str:
    """Format a numeric value for display."""
    try:
        f = float(val)
        if f == int(f) and abs(f) < 1e15:
            return str(int(f))
        return f"{f:,.4f}"
    except (ValueError, TypeError):
        return str(val)


def _render_baglanti_grafigi(
    theme: Record,
    series_ids: set[str],
    indicator_ids: set[str],
    registry: dict[str, Record],
) -> str:
    theme_id = theme["id"]
    theme_label = theme.get("title") or theme_id

    lines = [
        "## Baglanti Grafigi",
        "",
        "```mermaid",
        "graph LR",
        f'    T["{_mermaid_escape(theme_label)}"]',
    ]

    for sid in sorted(series_ids):
        rec = registry.get(sid)
        label = (rec.get("ticker") if rec else None) or sid
        safe_id = _mermaid_id(sid)
        lines.append(f'    T --> S_{safe_id}["{_mermaid_escape(label)}"]')

    for iid in sorted(indicator_ids):
        rec = registry.get(iid)
        label = (rec.get("title") if rec else None) or iid
        safe_id = _mermaid_id(iid)
        lines.append(f'    T --> I_{safe_id}["{_mermaid_escape(label)}"]')

        # Show indicator -> series input connections
        if rec is not None:
            for input_id in split_list(rec.get("input_ids")):
                input_rec = registry.get(input_id)
                input_label = (input_rec.get("ticker") if input_rec else None) or input_id
                safe_input = _mermaid_id(input_id)
                lines.append(
                    f'    I_{safe_id} --> S_{safe_input}["{_mermaid_escape(input_label)}"]'
                )

    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def _mermaid_escape(text: str) -> str:
    """Escape characters that break Mermaid syntax."""
    return text.replace('"', "'").replace("\n", " ")


def _mermaid_id(raw: str) -> str:
    """Convert a record ID to a safe Mermaid node identifier."""
    return "".join(c if c.isalnum() else "_" for c in raw)
