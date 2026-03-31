from __future__ import annotations

import ast
import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Pattern


MOJIBAKE_MARKERS = ("\u00c3", "\u00c4", "\u00c5", "\u00c2")
UNRESOLVED = "unresolved_from_notebook"
GENERIC_TICKER_PATTERN = re.compile(r"TP\.[A-Z0-9]+(?:\.[A-Z0-9]+)*")
TOP_LEVEL_PREFIXES = ("A.", "B.", "C.", "D.", "TOPLAM")
NUMERIC_PREFIX = re.compile(r"^\d+\.\s")
LETTER_PREFIX = re.compile(r"^[a-z]\.\s", re.IGNORECASE)
ROMAN_PREFIX = re.compile(r"^[IVXLCDM]+\.\s", re.IGNORECASE)
SERIES_TABLE_LINE = re.compile(
    r"(?P<code>TP\.[A-Z0-9]+(?:\.[A-Z0-9]+)*)\s+(?P<name>.+?)(?:\s{2,}\d{2}-\d{2}-\d{4}|\s{2,}\d{4}-\d{2}-\d{2}|$)"
)


@dataclass(slots=True, frozen=True)
class IndicatorTemplate:
    id: str
    title: str
    input_ids: tuple[str, ...]
    formula_expression: str = ""
    formula_description: str = ""
    output_frequency: str = ""
    output_unit: str = ""
    economic_meaning: str = ""
    validation_note: str = ""
    theme_ids: tuple[str, ...] = ()


@dataclass(slots=True, frozen=True)
class ThemeTemplate:
    id: str
    title: str
    description: str = ""
    questions: tuple[str, ...] = ()
    theme_series_ids: tuple[str, ...] = ()
    indicator_ids: tuple[str, ...] = ()
    source_dependency_ids: tuple[str, ...] = ()


@dataclass(slots=True, frozen=True)
class SourceDependency:
    id: str
    title: str
    source_kind: str
    requiredness: str
    description: str
    usage: str
    source_uri: str = ""
    local_hint: str = ""
    linked_theme_ids: tuple[str, ...] = ()
    linked_indicator_ids: tuple[str, ...] = ()
    validation_note: str = ""
    notes: str = ""


@dataclass(slots=True)
class TickerAnalysis:
    ticker: str
    table_group: str
    official_series_name: str
    notebook_label: str
    context_title: str
    frequency: str
    unit: str
    notebook_status: str
    notebook_role: str
    linked_theme_ids: tuple[str, ...] = ()
    linked_indicator_ids: tuple[str, ...] = ()
    linked_source_dependency_ids: tuple[str, ...] = ()
    notes: str = ""


@dataclass(slots=True, frozen=True)
class NotebookSpec:
    slug: str
    notebook_stem: str
    lane: str
    series_code_pattern: Pattern[str]
    series_families: tuple[str, ...]
    group_descriptions: dict[str, str]
    default_source_version: str
    frequency_resolver: Callable[[str], str]
    source_dependencies: tuple[SourceDependency, ...]
    indicators: tuple[IndicatorTemplate, ...]
    themes: tuple[ThemeTemplate, ...]
    status_resolver: Callable[[str], str]
    role_resolver: Callable[[str, str, str], str]
    manual_series_overrides: dict[str, str] = field(default_factory=dict)
    manual_unit_overrides: dict[str, str] = field(default_factory=dict)
    manual_notes_overrides: dict[str, str] = field(default_factory=dict)
    extra_tickers: tuple[str, ...] = ()
    known_blockers: tuple[str, ...] = ()


@dataclass(slots=True)
class NotebookAnalysisResult:
    notebook_path: Path
    spec_slug: str
    analyses: list[TickerAnalysis]
    source_dependencies: list[SourceDependency]
    indicators: list[IndicatorTemplate]
    themes: list[ThemeTemplate]
    unresolved_items: list[str]
    group_descriptions: dict[str, str]
    lane: str
    known_blockers: list[str]
    default_source_version: str


DTH_FETCHED_ONLY_CODES = {
    "TP.HPBITABLO4.1",
    "TP.HPBITABLO4.13",
    "TP.HPBITABLO4.14",
    "TP.HPBITABLO4.15",
    "TP.HPBITABLO4.16",
    "TP.HPBITABLO4.17",
    "TP.HPBITABLO4.18",
    "TP.HPBITABLO4.19",
    "TP.HPBITABLO4.20",
    "TP.HPBITABLO4.21",
}
DTH_LISTED_ONLY_CODES = {
    "TP.HPBITABLO3.1",
    "TP.HPBITABLO3.2",
    "TP.HPBITABLO3.18",
    "TP.HPBITABLO3.21",
    "TP.HPBITABLO3.24",
}
DTH_SERIES_OVERRIDES = {
    "TP.HPBITABLO5.12": "Yabanci para mevduatta haftalik degisim ve parite etkisi",
}
YI_SERIES_OVERRIDES = {
    "TP.DK.USD.A.YTL": "USD/TL (Alis Kuru)",
    "TP.HPBITABLO2.23": "1. Yurt Ici Yerlesikler (Bin TL)",
    "TP.HPBITABLO2.24": "a. TL (Bin TL)",
    "TP.HPBITABLO2.28": "b. YP (Bin TL)",
    "TP.HPBITABLO2.32": "2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL)",
    "TP.HPBITABLO2.33": "a. TL (Bin TL)",
    "TP.HPBITABLO2.34": "b. YP (Bin TL)",
}
YI_UNIT_OVERRIDES = {
    "TP.EBONDPIYDEG.S14": "Milyon ABD Dolari",
    "TP.YDOSBAPIYDEG.S15": "Milyon ABD Dolari",
    "TP.YDOSBAPIYDEG.S34": "Milyon ABD Dolari",
    "TP.YDOSBAPIYDEG.S53": "Milyon ABD Dolari",
    "TP.YDOSBAPIYDEG.S72": "Milyon ABD Dolari",
}
YI_NOTES_OVERRIDES = {
    "TP.EBONDPIYDEG.S14": "Notebookta USD/TL ile carpilarak 'Eurobond (Gercek Kisi)' TL karsiligina cevriliyor.",
    "TP.YDOSBAPIYDEG.S15": "Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.",
    "TP.YDOSBAPIYDEG.S34": "Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.",
    "TP.YDOSBAPIYDEG.S53": "Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.",
    "TP.YDOSBAPIYDEG.S72": "Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.",
}
RZRV_SERIES_OVERRIDES = {
    "TP.AB.N06": "Net Rezerv TL (Bin TL)",
    "TP.DOVVARNC.K18": "Swap (Aylik, MB)",
}
UNIT_HINTS = (
    "tl",
    "ytl",
    "try",
    "usd",
    "abd dolari",
    "abd doları",
    "dolar",
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
NON_UNIT_HINTS = (
    "ihrac",
    "ihraç",
    "hanehalk",
    "bankalar",
    "kurulus",
    "kuruluş",
    "yerlesik",
    "yerleşik",
    "gercek kisi",
    "gerçek kişi",
    "tuzel kisi",
    "tüzel kişi",
    "toplam, bankalar haric",
    "toplam, bankalar hariç",
    "alis kuru",
    "alış kuru",
)


def fix_mojibake(value: str) -> str:
    text = str(value or "").strip()
    for _ in range(3):
        if not any(marker in text for marker in MOJIBAKE_MARKERS):
            break
        try:
            repaired = text.encode("latin1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
        if repaired == text:
            break
        text = repaired
    return text


def build_notebook_analysis(notebook_path: str | Path, spec: str = "auto") -> NotebookAnalysisResult:
    notebook_file = Path(notebook_path)
    notebook = json.loads(notebook_file.read_text(encoding="utf-8"))
    notebook_spec = resolve_notebook_spec(notebook_file, spec)
    official_names = extract_output_mapping(notebook)
    notebook_labels = extract_source_mapping(notebook)
    codes = extract_codes(notebook, notebook_spec)
    analyses: list[TickerAnalysis] = []

    for ticker in codes:
        official_series_name = resolve_label(ticker, official_names, notebook_spec.manual_series_overrides)
        notebook_label = resolve_label(ticker, notebook_labels, {})
        if notebook_label == UNRESOLVED:
            notebook_label = ""
        if official_series_name == UNRESOLVED and notebook_label:
            official_series_name = notebook_label
        if official_series_name != UNRESOLVED and not notebook_label:
            notebook_label = official_series_name
        status = notebook_spec.status_resolver(ticker)
        label_for_semantics = official_series_name if official_series_name != UNRESOLVED else notebook_label
        role = notebook_spec.role_resolver(ticker, label_for_semantics, status)
        indicator_ids = tuple(
            indicator.id for indicator in notebook_spec.indicators if f"evds:{ticker}" in indicator.input_ids
        )
        theme_ids = tuple(
            theme.id
            for theme in notebook_spec.themes
            if not theme.theme_series_ids or f"evds:{ticker}" in theme.theme_series_ids or set(indicator_ids).intersection(theme.indicator_ids)
        )
        source_dependency_ids = tuple(
            item.id
            for item in notebook_spec.source_dependencies
            if set(theme_ids).intersection(item.linked_theme_ids) or set(indicator_ids).intersection(item.linked_indicator_ids)
        )
        note_parts: list[str] = []
        if official_series_name == UNRESOLVED:
            note_parts.append("Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi.")
        manual_note = notebook_spec.manual_notes_overrides.get(ticker)
        if manual_note:
            note_parts.append(manual_note)
        analyses.append(
            TickerAnalysis(
                ticker=ticker,
                table_group=table_group_for(ticker),
                official_series_name=official_series_name,
                notebook_label=notebook_label,
                context_title="",
                frequency=notebook_spec.frequency_resolver(ticker),
                unit=resolve_unit(ticker, label_for_semantics, notebook_spec.manual_unit_overrides),
                notebook_status=status,
                notebook_role=role,
                linked_theme_ids=theme_ids,
                linked_indicator_ids=indicator_ids,
                linked_source_dependency_ids=source_dependency_ids,
                notes=" ".join(note_parts),
            )
        )

    analyses = apply_context_titles(analyses)
    unresolved_items = [item.ticker for item in analyses if item.official_series_name == UNRESOLVED]
    return NotebookAnalysisResult(
        notebook_path=notebook_file,
        spec_slug=notebook_spec.slug,
        analyses=analyses,
        source_dependencies=list(notebook_spec.source_dependencies),
        indicators=list(notebook_spec.indicators),
        themes=list(notebook_spec.themes),
        unresolved_items=unresolved_items,
        group_descriptions=notebook_spec.group_descriptions,
        lane=notebook_spec.lane,
        known_blockers=list(notebook_spec.known_blockers),
        default_source_version=notebook_spec.default_source_version,
    )


def build_dth_notebook_analysis(notebook_path: str | Path) -> NotebookAnalysisResult:
    return build_notebook_analysis(notebook_path, spec="dth-blg-v7")


def resolve_notebook_spec(notebook_path: Path, spec: str) -> NotebookSpec:
    available = {item.slug: item for item in ALL_SPECS}
    available["dth"] = DTH_SPEC
    if spec == "auto":
        stem = notebook_path.stem.casefold()
        for candidate in available.values():
            if candidate.notebook_stem.casefold() == stem:
                return candidate
        raise ValueError(f"No notebook spec found for stem: {notebook_path.stem}")
    if spec not in available:
        raise ValueError(f"Unknown notebook spec: {spec}")
    return available[spec]


def extract_codes(notebook: dict, spec: NotebookSpec) -> list[str]:
    found: set[str] = set()
    for text in iter_cell_sources(notebook):
        found.update(extract_active_codes_from_source(text, spec.series_code_pattern))
    found.update(spec.extra_tickers)
    filtered = {code for code in found if family_of(code) in spec.series_families}
    return sorted(filtered, key=ticker_sort_key)


def extract_output_mapping(notebook: dict) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for cell in notebook.get("cells", []):
        for output in cell.get("outputs", []):
            for text in output_texts(output):
                stripped = text.strip()
                parsed = parse_mapping_dict(stripped)
                if parsed:
                    mapping.update(parsed)
                mapping.update(parse_series_table_mapping(stripped))
    return mapping


def extract_source_mapping(notebook: dict) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for text in iter_cell_sources(notebook):
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Dict):
                continue
            for key_node, value_node in zip(node.value.keys, node.value.values):
                if not isinstance(key_node, ast.Constant):
                    continue
                if not isinstance(key_node.value, str):
                    continue
                extracted = extract_literal_label(value_node)
                if extracted:
                    mapping[str(key_node.value)] = extracted
    return mapping


def extract_literal_label(node: ast.AST) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return fix_mojibake(str(node.value))
    if isinstance(node, (ast.List, ast.Tuple)):
        string_values = [
            fix_mojibake(str(item.value))
            for item in node.elts
            if isinstance(item, ast.Constant) and isinstance(item.value, str)
        ]
        if string_values:
            return string_values[-1]
    return ""


def extract_active_codes_from_source(source: str, pattern: Pattern[str]) -> set[str]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set(pattern.findall(source))

    assign_parents(tree)
    found: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
            continue
        if isinstance(getattr(node, "parent", None), ast.Expr):
            continue
        found.update(pattern.findall(node.value))
    return found


def assign_parents(tree: ast.AST) -> None:
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            setattr(child, "parent", parent)


def parse_mapping_dict(text: str) -> dict[str, str]:
    if not (text.startswith("{") and text.endswith("}")):
        return {}
    try:
        parsed = ast.literal_eval(text)
    except (SyntaxError, ValueError):
        return {}
    if not isinstance(parsed, dict):
        return {}
    mapping: dict[str, str] = {}
    for key, value in parsed.items():
        if isinstance(key, str) and isinstance(value, str):
            mapping[key] = fix_mojibake(value)
    return mapping


def parse_series_table_mapping(text: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for line in text.splitlines():
        match = SERIES_TABLE_LINE.search(line.strip())
        if not match:
            continue
        code = match.group("code")
        name = fix_mojibake(match.group("name").strip())
        if name:
            mapping[code] = name
    return mapping


def iter_cell_sources(notebook: dict) -> list[str]:
    values: list[str] = []
    for cell in notebook.get("cells", []):
        source = cell.get("source", [])
        if isinstance(source, list):
            values.append("".join(source))
        else:
            values.append(str(source))
    return values


def output_texts(output: dict) -> list[str]:
    texts: list[str] = []
    if isinstance(output.get("text"), list):
        texts.append("".join(output["text"]))
    elif output.get("text"):
        texts.append(str(output["text"]))
    data = output.get("data") or {}
    plain = data.get("text/plain")
    if isinstance(plain, list):
        texts.append("".join(plain))
    elif plain:
        texts.append(str(plain))
    return texts


def resolve_label(ticker: str, mapping: dict[str, str], overrides: dict[str, str]) -> str:
    normalized = ticker.replace(".", "_")
    for key in (normalized, ticker):
        value = mapping.get(key)
        if value:
            return fix_mojibake(value)
    return overrides.get(ticker, UNRESOLVED)


def family_of(ticker: str) -> str:
    parts = ticker.split(".")
    if len(parts) < 2:
        return ticker
    return ".".join(parts[:2])


def table_group_for(ticker: str) -> str:
    parts = ticker.split(".")
    return parts[1] if len(parts) > 1 else "UNKNOWN"


def ticker_sort_key(ticker: str) -> tuple[str, int]:
    parts = ticker.split(".")
    if len(parts) >= 3 and parts[-1].isdigit():
        return parts[1], int(parts[-1])
    return ticker, 0


def extract_unit(label: str) -> str:
    if not label or label == UNRESOLVED:
        return ""
    matches = re.findall(r"\(([^)]+)\)", label)
    for candidate in reversed(matches):
        if looks_like_unit(candidate):
            return candidate.strip()
    return ""


def looks_like_unit(value: str) -> bool:
    normalized = fix_mojibake(value).strip().casefold()
    if not normalized:
        return False
    if re.fullmatch(r"s\.\d+", normalized):
        return False
    if any(marker in normalized for marker in NON_UNIT_HINTS):
        return False
    return any(marker in normalized for marker in UNIT_HINTS)


def resolve_unit(ticker: str, label: str, overrides: dict[str, str]) -> str:
    manual = overrides.get(ticker, "")
    if manual:
        return manual
    return extract_unit(label)


def apply_context_titles(analyses: list[TickerAnalysis]) -> list[TickerAnalysis]:
    grouped: dict[str, list[TickerAnalysis]] = {}
    for item in analyses:
        grouped.setdefault(item.table_group, []).append(item)
    resolved: list[TickerAnalysis] = []
    for group in sorted(grouped):
        top_parent = ""
        numeric_parent = ""
        for item in sorted(grouped[group], key=lambda candidate: ticker_sort_key(candidate.ticker)):
            label = item.official_series_name if item.official_series_name != UNRESOLVED else item.notebook_label
            if not label or label == UNRESOLVED:
                item.context_title = ""
            elif label.startswith(TOP_LEVEL_PREFIXES) or label.upper().startswith("TOPLAM"):
                top_parent = label
                numeric_parent = ""
                item.context_title = label
            elif NUMERIC_PREFIX.match(label):
                item.context_title = f"{top_parent} / {label}" if top_parent else label
                numeric_parent = item.context_title
            elif LETTER_PREFIX.match(label):
                parent = numeric_parent or top_parent
                item.context_title = f"{parent} / {label}" if parent else label
            elif ROMAN_PREFIX.match(label):
                parent = numeric_parent or top_parent
                item.context_title = f"{parent} / {label}" if parent else label
            else:
                item.context_title = label
            resolved.append(item)
    return sorted(resolved, key=lambda candidate: ticker_sort_key(candidate.ticker))


def write_markdown_report(result: NotebookAnalysisResult, output_path: str | Path) -> Path:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    status_counts = count_values(item.notebook_status for item in result.analyses)
    role_counts = count_values(item.notebook_role for item in result.analyses)
    group_lines = "\n".join(
        f"- `{group}`: {description} ({sum(1 for item in result.analyses if item.table_group == group)} seri)"
        for group, description in result.group_descriptions.items()
    )
    external_lines = "\n".join(
        f"- `{item.id}` | {item.title} | {item.source_kind} | {item.requiredness}"
        for item in result.source_dependencies
    ) or "-"
    table_rows = "\n".join(
        f"| `{item.ticker}` | {item.official_series_name} | {item.context_title or '-'} | {item.notebook_status} | "
        f"{item.notebook_role} | {item.unit or '-'} | {item.notes or '-'} |"
        for item in result.analyses
    )
    source_rows = "\n".join(
        f"| `{item.id}` | {item.title} | {item.source_kind} | {item.requiredness} | "
        f"{', '.join(item.linked_theme_ids) or '-'} | {', '.join(item.linked_indicator_ids) or '-'} | {item.notes or '-'} |"
        for item in result.source_dependencies
    )
    content = "\n".join(
        [
            "# Kisa Ozet",
            "",
            f"- Notebook: `{result.notebook_path.name}`",
            f"- Spec: `{result.spec_slug}`",
            f"- Lane: `{result.lane}`",
            f"- Toplam benzersiz ticker: `{len(result.analyses)}`",
            f"- Unresolved ticker: `{len(result.unresolved_items)}`",
            "",
            "## Kod Gruplari",
            "",
            group_lines or "-",
            "",
            "## Dis Kaynaklar",
            "",
            external_lines,
            "",
            "## Durum Etiketleri",
            "",
            "\n".join(f"- `{key}`: {value}" for key, value in status_counts.items()),
            "",
            "## Rol Etiketleri",
            "",
            "\n".join(f"- `{key}`: {value}" for key, value in role_counts.items()),
            "",
            "## Tam Ticker Eslestirme",
            "",
            "| Ticker | Resmi Seri Adi | Baglamli Ad | Durum | Rol | Birim | Notlar |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            table_rows,
            "",
            "## Source Dependency Eslestirme",
            "",
            "| ID | Baslik | Kaynak Turu | Zorunluluk | Bagli Temalar | Bagli Gostergeler | Notlar |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            source_rows or "| - | - | - | - | - | - | - |",
            "",
            "## Belirsizlikler",
            "",
            *([f"- {item}" for item in result.known_blockers] or []),
            *([f"- `{item}`" for item in result.unresolved_items] or ["-"]),
            "",
        ]
    )
    output_file.write_text(content, encoding="utf-8")
    return output_file


def write_import_csv(result: NotebookAnalysisResult, output_path: str | Path) -> Path:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "record_type", "id", "title", "ticker", "source_version", "frequency", "unit", "description", "usage",
        "official_url", "theme_ids", "indicator_ids", "input_ids", "formula_expression", "formula_description",
        "output_frequency", "output_unit", "economic_meaning", "validation_note", "series_ids",
        "source_dependency_ids", "questions", "source_kind", "requiredness", "source_uri", "local_hint",
    ]
    with output_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for item in result.analyses:
            writer.writerow(
                {
                    "record_type": "series",
                    "id": f"evds:{item.ticker}",
                    "title": item.official_series_name or item.notebook_label or item.ticker,
                    "ticker": item.ticker,
                    "source_version": result.default_source_version,
                    "frequency": item.frequency,
                    "unit": item.unit,
                    "description": compose_series_description(item),
                    "usage": f"Notebook rolu: {item.notebook_role}",
                    "theme_ids": join_values(item.linked_theme_ids),
                    "indicator_ids": join_values(item.linked_indicator_ids),
                }
            )
        for item in result.indicators:
            writer.writerow(
                {
                    "record_type": "indicator",
                    "id": item.id,
                    "title": item.title,
                    "input_ids": join_values(item.input_ids),
                    "formula_expression": item.formula_expression,
                    "formula_description": item.formula_description,
                    "output_frequency": item.output_frequency,
                    "output_unit": item.output_unit,
                    "economic_meaning": item.economic_meaning,
                    "validation_note": item.validation_note,
                    "theme_ids": join_values(item.theme_ids),
                }
            )
        for item in result.themes:
            theme_series_ids = item.theme_series_ids or tuple(f"evds:{analysis.ticker}" for analysis in result.analyses)
            writer.writerow(
                {
                    "record_type": "theme",
                    "id": item.id,
                    "title": item.title,
                    "description": item.description,
                    "series_ids": join_values(theme_series_ids),
                    "indicator_ids": join_values(item.indicator_ids),
                    "source_dependency_ids": join_values(item.source_dependency_ids),
                    "questions": join_values(item.questions),
                }
            )
        for item in result.source_dependencies:
            writer.writerow(
                {
                    "record_type": "source_dependency",
                    "id": item.id,
                    "title": item.title,
                    "description": item.description,
                    "usage": item.usage,
                    "theme_ids": "",
                    "indicator_ids": "",
                    "validation_note": item.validation_note,
                    "source_kind": item.source_kind,
                    "requiredness": item.requiredness,
                    "source_uri": item.source_uri,
                    "local_hint": item.local_hint,
                }
            )
    return output_file


def join_values(values: tuple[str, ...] | list[str]) -> str:
    return "|".join(value for value in values if value)


def compose_series_description(item: TickerAnalysis) -> str:
    parts = [
        f"Resmi seri adi: {item.official_series_name}",
        f"Durum: {item.notebook_status}",
    ]
    if item.context_title and item.context_title != item.official_series_name:
        parts.append(f"Notebook baglami: {item.context_title}")
    elif item.notebook_label and item.notebook_label not in {"", item.official_series_name}:
        parts.append(f"Notebook etiketi: {item.notebook_label}")
    if item.notes:
        parts.append(f"Not: {item.notes}")
    return " | ".join(parts)


def count_values(values) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def constant_frequency(value: str) -> Callable[[str], str]:
    return lambda _ticker: value


def mapped_frequency(default: str, overrides: dict[str, str]) -> Callable[[str], str]:
    def resolve(ticker: str) -> str:
        return overrides.get(ticker, overrides.get(family_of(ticker), default))

    return resolve


def status_from_sets(
    listed_only: tuple[str, ...] = (),
    fetched_only: tuple[str, ...] = (),
    reported_output: tuple[str, ...] = (),
    default: str = "derived_input",
) -> Callable[[str], str]:
    listed = set(listed_only)
    fetched = set(fetched_only)
    reported = set(reported_output)

    def resolve(ticker: str) -> str:
        if ticker in listed:
            return "listed_only"
        if ticker in fetched:
            return "fetched_only"
        if ticker in reported:
            return "reported_output"
        return default

    return resolve


def make_role_resolver(
    family_roles: dict[str, str],
    explicit_roles: dict[str, str] | None = None,
    default_role: str = "stock_component",
) -> Callable[[str, str, str], str]:
    explicit = explicit_roles or {}

    def resolve(ticker: str, label: str, status: str) -> str:
        if ticker in explicit:
            return explicit[ticker]
        if status == "listed_only":
            return "dormant_candidate"
        if status == "fetched_only":
            return "supporting_external_input"
        upper = label.upper()
        if "TOPLAM" in upper or upper.endswith(".ST") or upper.endswith(".TOPLAM"):
            return "stock_total"
        if LETTER_PREFIX.match(label):
            return "currency_split_line"
        if NUMERIC_PREFIX.match(label) or ROMAN_PREFIX.match(label):
            return "owner_split_line"
        return family_roles.get(family_of(ticker), default_role)

    return resolve


def dth_status_for(ticker: str) -> str:
    if ticker in DTH_LISTED_ONLY_CODES:
        return "listed_only"
    if ticker in DTH_FETCHED_ONLY_CODES:
        return "fetched_only"
    if ticker == "TP.HPBITABLO5.12":
        return "reported_output"
    return "derived_input"


def dth_role_for(ticker: str, label: str, status: str) -> str:
    if ticker == "TP.HPBITABLO5.12":
        return "parity_effect_input"
    if status == "listed_only":
        return "dormant_candidate"
    if ticker in {"TP.HPBITABLO4.14", "TP.HPBITABLO4.15"}:
        return "currency_split_line"
    text = label.upper()
    if "TOPLAM" in text:
        return "stock_total"
    if LETTER_PREFIX.match(label):
        return "currency_split_line"
    if NUMERIC_PREFIX.match(label):
        return "owner_split_line"
    return "stock_component"


DTH_SPEC = NotebookSpec(
    slug="dth-blg-v7",
    notebook_stem="DTH_Blg_V7",
    lane="L2_EVDS_plus_external",
    series_code_pattern=GENERIC_TICKER_PATTERN,
    series_families=("TP.HPBITABLO2", "TP.HPBITABLO3", "TP.HPBITABLO4", "TP.HPBITABLO5"),
    group_descriptions={
        "HPBITABLO2": "Toplam mevduat, kredi ve DTH payi hesaplarinin ana EVDS girdileri",
        "HPBITABLO3": "Notebookta listelenen ancak aktif akisa baglanmayan TL mevduat alt kirilimlari",
        "HPBITABLO4": "Yurt ici yerlesiklerin YP mevduat kirilimlari ve kisi turu/para cinsi ayrimlari",
        "HPBITABLO5": "Parite etkisi ve haftalik degisim baglami",
    },
    default_source_version="evds2",
    frequency_resolver=constant_frequency("weekly"),
    source_dependencies=(
        SourceDependency(
            id="source:dth-old-series-excel",
            title="DTH eski seri Excel backfill",
            source_kind="excel_local",
            requiredness="required_input",
            source_uri="",
            local_hint="/content/drive/MyDrive/DataFiles/dth_old_series_19022025.xlsx",
            description="Eski DTH serilerini guncel kolonlarla birlestirmek icin kullanilan yerel Excel girdisi.",
            usage="Uzun tarihli DTH serilerinin notebookta backfill edilmesini saglar.",
            linked_theme_ids=("theme:dth",),
        ),
    ),
    indicators=(
        IndicatorTemplate(
            id="derived:dth-share-in-total-deposits",
            title="Toplam Mevduat icinde DTH Payi",
            input_ids=("evds:TP.HPBITABLO4.2", "evds:TP.HPBITABLO2.1"),
            formula_expression="evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1",
            formula_description="Yurt ici yerlesiklerin YP mevduatinin toplam mevduata orani.",
            output_frequency="weekly",
            output_unit="ratio",
            economic_meaning="Toplam mevduat tabani icindeki DTH agirligini izler.",
            validation_note="Paydanin sifir olmadigi dogrulanmali.",
            theme_ids=("theme:dth",),
        ),
        IndicatorTemplate(
            id="derived:dth-share-in-resident-deposits",
            title="Yurtici Yerlesiklerin Mevduati icinde DTH Payi",
            input_ids=("evds:TP.HPBITABLO4.2", "evds:TP.HPBITABLO2.2"),
            formula_expression="evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.2",
            formula_description="Yurt ici yerlesiklerin mevduati icindeki YP payi.",
            output_frequency="weekly",
            output_unit="ratio",
            economic_meaning="Yerlesiklerin mevduat tercihini TL/YP ayriminda izler.",
            validation_note="Paydanin sifir olmadigi dogrulanmali.",
            theme_ids=("theme:dth",),
        ),
        IndicatorTemplate(
            id="derived:resident-deposit-share-in-total-deposits",
            title="Toplam Mevduat icinde Yurtici Yerlesiklerin Payi",
            input_ids=("evds:TP.HPBITABLO2.2", "evds:TP.HPBITABLO2.1"),
            formula_expression="evds:TP.HPBITABLO2.2 / evds:TP.HPBITABLO2.1",
            formula_description="Yurt ici yerlesiklerin toplam mevduat icindeki payi.",
            output_frequency="weekly",
            output_unit="ratio",
            economic_meaning="Toplam mevduat tabaninin yerlesik kompozisyonunu izler.",
            validation_note="Paydanin sifir olmadigi dogrulanmali.",
            theme_ids=("theme:dth",),
        ),
    ),
    themes=(
        ThemeTemplate(
            id="theme:dth",
            title="DTH",
            description="DTH ve mevduat kompozisyonu temasi",
            questions=(
                "Toplam mevduat icinde DTH payi ne soyluyor?",
                "Yerlesiklerin mevduat tercihi hangi yone gidiyor?",
            ),
            indicator_ids=(
                "derived:dth-share-in-total-deposits",
                "derived:dth-share-in-resident-deposits",
                "derived:resident-deposit-share-in-total-deposits",
            ),
            source_dependency_ids=("source:dth-old-series-excel",),
        ),
    ),
    status_resolver=dth_status_for,
    role_resolver=dth_role_for,
    manual_series_overrides=DTH_SERIES_OVERRIDES,
    known_blockers=(
        "TP.HPBITABLO4.14 ve TP.HPBITABLO4.15 notebooktan cozumlenemiyor.",
    ),
)


PYS_SPEC = NotebookSpec(
    slug="pys-ktilmclr-v2",
    notebook_stem="Pys_Ktlmclr_V2",
    lane="L1_EVDS_standard",
    series_code_pattern=GENERIC_TICKER_PATTERN,
    series_families=("TP.BEK",),
    group_descriptions={
        "BEK": "TCMB beklenti anketi serileri; aktif notebook akisinda kullanilan cekirdek beklenti kodlari",
    },
    default_source_version="evds2",
    frequency_resolver=constant_frequency("monthly"),
    source_dependencies=(),
    indicators=(
        IndicatorTemplate("derived:policy-rate-expectation-current", "Cari Ay Politika Faizi Beklentisi", ("evds:TP.BEK.S01.D.U",), output_frequency="monthly", output_unit="pct", economic_meaning="Cari ay politika faizi beklentisini izler.", theme_ids=("theme:survey-expectations",)),
        IndicatorTemplate("derived:policy-rate-expectation-3m", "Uc Ay Sonrasi Politika Faizi Beklentisi", ("evds:TP.BEK.S01.E.U",), output_frequency="monthly", output_unit="pct", economic_meaning="Uc ay sonrasi politika faizi beklentisini izler.", theme_ids=("theme:survey-expectations",)),
        IndicatorTemplate("derived:policy-rate-expectation-12m", "On Iki Ay Sonrasi Politika Faizi Beklentisi", ("evds:TP.BEK.S01.F.U",), output_frequency="monthly", output_unit="pct", economic_meaning="On iki ay sonrasi politika faizi beklentisini izler.", theme_ids=("theme:survey-expectations",)),
        IndicatorTemplate("derived:inflation-expectation-12m", "On Iki Ay Sonrasi Enflasyon Beklentisi", ("evds:TP.BEK.S04.A.U",), output_frequency="monthly", output_unit="pct", economic_meaning="Bir yil sonraki TUFE beklentisini izler.", theme_ids=("theme:survey-expectations",)),
        IndicatorTemplate("derived:inflation-expectation-24m", "Yirmi Dort Ay Sonrasi Enflasyon Beklentisi", ("evds:TP.BEK.S04.B.U",), output_frequency="monthly", output_unit="pct", economic_meaning="Iki yil sonraki TUFE beklentisini izler.", theme_ids=("theme:survey-expectations",)),
        IndicatorTemplate("derived:usdtry-expectation-12m", "On Iki Ay Sonrasi USDTRY Beklentisi", ("evds:TP.BEK.S06.A.U",), output_frequency="monthly", output_unit="level", economic_meaning="On iki ay sonrasi USDTRY beklentisini izler.", theme_ids=("theme:survey-expectations",)),
        IndicatorTemplate("derived:growth-expectation", "GSYH Buyume Beklentisi", ("evds:TP.BEK.S05.B.U",), output_frequency="monthly", output_unit="pct", economic_meaning="Buyume beklentisinin yonunu izler.", theme_ids=("theme:survey-expectations",)),
        IndicatorTemplate("derived:current-account-expectation", "Cari Denge Beklentisi", ("evds:TP.BEK.S07.A.U",), output_frequency="monthly", output_unit="usd_bn", economic_meaning="Cari denge beklentisini izler.", theme_ids=("theme:survey-expectations",)),
    ),
    themes=(
        ThemeTemplate(
            id="theme:survey-expectations",
            title="Beklenti Anketi",
            description="Piyasa katilimcilari beklenti anketi temasi",
            questions=("Faiz, enflasyon ve kur beklentileri hangi yone gidiyor?",),
            indicator_ids=(
                "derived:policy-rate-expectation-current",
                "derived:policy-rate-expectation-3m",
                "derived:policy-rate-expectation-12m",
                "derived:inflation-expectation-12m",
                "derived:inflation-expectation-24m",
                "derived:usdtry-expectation-12m",
                "derived:growth-expectation",
                "derived:current-account-expectation",
            ),
        ),
    ),
    status_resolver=status_from_sets(),
    role_resolver=make_role_resolver({"TP.BEK": "commentary_driver"}, default_role="commentary_driver"),
    known_blockers=("TP.PKAUO serileri notebookta yorum satirina alinmis, aktif extraction akisina dahil degil.",),
)


YI_SPEC = NotebookSpec(
    slug="yi-yrlsk-fnsl-vrlk-v1",
    notebook_stem="Yi_Yrlsk_Fnsl_Vrlk_V1",
    lane="L1_EVDS_standard",
    series_code_pattern=GENERIC_TICKER_PATTERN,
    series_families=("TP.DIBSPIYDEG", "TP.DK", "TP.EBONDPIYDEG", "TP.HPBITABLO1", "TP.HPBITABLO2", "TP.YDOSBAPIYDEG", "TP.YIOSBAPIYDEG"),
    group_descriptions={
        "DIBSPIYDEG": "Ozel sektor tahvil stogu ve alt kirilimlari",
        "DK": "Kur cevirim girdisi",
        "EBONDPIYDEG": "Ozel sektor eurobond stogu ve alt kirilimlari",
        "HPBITABLO1": "Fon ve benzeri mevduat/fon kalemleri",
        "HPBITABLO2": "TL ve YP mevduat kirilimlari",
        "YDOSBAPIYDEG": "Yurt disi yerlesiklerin tahvil/eurobond alt kirilimlari",
        "YIOSBAPIYDEG": "Yurt ici yerlesiklerin tahvil/eurobond alt kirilimlari",
    },
    default_source_version="evds2",
    frequency_resolver=constant_frequency("weekly"),
    source_dependencies=(
        SourceDependency("source:yiyrlsk-mkk-hisse-manual", "MKK hisse manuel ledger", "manual_inline", "required_input", "Notebook icindeki hisse ledger bloklari yerli hisse portfoyunu besler.", "Yerli hisse portfoy degeri ve gercek kisi kirilimi icin kullanilir.", linked_theme_ids=("theme:resident-financial-assets", "theme:resident-securities")),
        SourceDependency("source:yiyrlsk-mkk-fon-manual", "MKK fon manuel ledger", "manual_inline", "required_input", "Notebook icindeki fon ledger bloklari yatirim fonu portfoy degerini besler.", "Yatirim fonu portfoy degeri ve gercek kisi kirilimi icin kullanilir.", linked_theme_ids=("theme:resident-financial-assets", "theme:resident-securities")),
        SourceDependency("source:yiyrlsk-vap-scrape-attempt", "VAP scrape denemesi", "web_scrape", "optional_replacement", "Notebookta bulunan VAP/MKK scrape denemesi aktif olmayan alternatif kaynak niteligindedir.", "Manuel MKK ledger girdisinin potansiyel yerine gelebilecek aday kaynaktir.", linked_theme_ids=("theme:resident-securities",)),
    ),
    indicators=(
        IndicatorTemplate("derived:private-sector-bond-total", "Ozel Sektor Tahvil Toplami", ("evds:TP.DIBSPIYDEG.S15",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Ozel sektor tahvil varlik toplamaini izler.", theme_ids=("theme:resident-securities",)),
        IndicatorTemplate("derived:private-sector-eurobond-total", "Ozel Sektor Eurobond Toplami", ("evds:TP.EBONDPIYDEG.S15",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Ozel sektor eurobond varlik toplamaini izler.", theme_ids=("theme:resident-securities",)),
        IndicatorTemplate("derived:tl-deposit-total", "TL Mevduat Toplami", ("evds:TP.HPBITABLO2.14", "evds:TP.HPBITABLO2.24"), output_frequency="weekly", output_unit="try_bn", economic_meaning="Yerlesiklerin TL mevduat toplamaini izler.", theme_ids=("theme:resident-deposits",)),
        IndicatorTemplate("derived:fx-deposit-total", "YP Mevduat Toplami", ("evds:TP.HPBITABLO2.15", "evds:TP.HPBITABLO2.28"), output_frequency="weekly", output_unit="try_bn", economic_meaning="Yerlesiklerin YP mevduat toplamaini izler.", theme_ids=("theme:resident-deposits",)),
        IndicatorTemplate("derived:local-equity-total", "Yerli Hisse Toplami", ("source:yiyrlsk-mkk-hisse-manual",), formula_description="MKK hisse manuel ledger'inden uretilir.", output_frequency="weekly", output_unit="try_bn", economic_meaning="Yerlesiklerin hisse senedi varligini izler.", theme_ids=("theme:resident-securities", "theme:resident-financial-assets")),
        IndicatorTemplate("derived:local-fund-total", "Yerli Fon Toplami", ("source:yiyrlsk-mkk-fon-manual",), formula_description="MKK fon manuel ledger'inden uretilir.", output_frequency="monthly", output_unit="try_bn", economic_meaning="Yerlesiklerin yatirim fonu varligini izler.", theme_ids=("theme:resident-securities", "theme:resident-financial-assets")),
        IndicatorTemplate("derived:resident-financial-assets-total", "Yerli Finansal Varlik Toplami", ("evds:TP.HPBITABLO2.2", "source:yiyrlsk-mkk-hisse-manual", "source:yiyrlsk-mkk-fon-manual"), formula_description="Mevduat, menkul kiymet ve MKK kaynakli varlik bloklarini birlestirir.", output_frequency="weekly", output_unit="try_bn", economic_meaning="Yerlesiklerin temel finansal varlik toplamaini izler.", theme_ids=("theme:resident-financial-assets",)),
        IndicatorTemplate("derived:real-person-share", "Gercek Kisi Payi", ("source:yiyrlsk-mkk-hisse-manual", "source:yiyrlsk-mkk-fon-manual"), formula_description="MKK kaynaklarindaki gercek kisi kirilimindan hesaplanir.", output_frequency="weekly", output_unit="ratio", economic_meaning="Yerlesik varlik kompozisyonunda gercek kisi payini izler.", theme_ids=("theme:resident-financial-assets",)),
    ),
    themes=(
        ThemeTemplate("theme:resident-financial-assets", "Yerlilerin Finansal Varliklari", "Yurt ici yerlesiklerin finansal varlik kompozisyonu", indicator_ids=("derived:resident-financial-assets-total", "derived:real-person-share", "derived:local-equity-total", "derived:local-fund-total"), source_dependency_ids=("source:yiyrlsk-mkk-hisse-manual", "source:yiyrlsk-mkk-fon-manual")),
        ThemeTemplate("theme:resident-securities", "Yerlilerin Menkul Kiymetleri", "Menkul kiymet ve MKK kaynakli varlik bloklari", indicator_ids=("derived:private-sector-bond-total", "derived:private-sector-eurobond-total", "derived:local-equity-total", "derived:local-fund-total"), source_dependency_ids=("source:yiyrlsk-mkk-hisse-manual", "source:yiyrlsk-mkk-fon-manual", "source:yiyrlsk-vap-scrape-attempt")),
        ThemeTemplate("theme:resident-deposits", "Yerlilerin Mevduati", "TL ve YP mevduat omurgasi", indicator_ids=("derived:tl-deposit-total", "derived:fx-deposit-total")),
    ),
    status_resolver=status_from_sets(),
    role_resolver=make_role_resolver({"TP.DIBSPIYDEG": "stock_component", "TP.DK": "ratio_input", "TP.EBONDPIYDEG": "stock_component", "TP.HPBITABLO1": "balance_sheet_line", "TP.HPBITABLO2": "balance_sheet_line", "TP.YDOSBAPIYDEG": "stock_component", "TP.YIOSBAPIYDEG": "stock_component"}),
    manual_series_overrides=YI_SERIES_OVERRIDES,
    manual_unit_overrides=YI_UNIT_OVERRIDES,
    manual_notes_overrides=YI_NOTES_OVERRIDES,
    known_blockers=("MKK manuel ledger bloklari notebook icinde gomulu oldugundan source dependency olarak izlenmelidir.", "VAP scrape denemesi aktif bir veri kaynagi degildir."),
)


EUROBND_SPEC = NotebookSpec(
    slug="eurobnd-blg-v4",
    notebook_stem="Eurobnd_Blg_V4",
    lane="L2_EVDS_plus_external",
    series_code_pattern=GENERIC_TICKER_PATTERN,
    series_families=("TP.EBONDYAZDEG", "TP.YDOSBAYAZDEG"),
    group_descriptions={
        "EBONDYAZDEG": "Hazine eurobond stogu ve yabanci sahipligi serileri",
        "YDOSBAYAZDEG": "Ozel sektor eurobond stogu ve yabanci sahipligi serileri",
    },
    default_source_version="evds2",
    frequency_resolver=constant_frequency("weekly"),
    source_dependencies=(
        SourceDependency("source:eurobnd-bbg-upload", "Eurobond BBG upload", "excel_upload", "required_input", "Kullanici yuklemeli BBG workbook eurobond ihraclari ve vade dagilimini tasir.", "Eurobond ihraclari ve vade dagilimi tablolarinda kullanilir.", linked_theme_ids=("theme:eurobond", "theme:external-financing")),
        SourceDependency("source:eurobnd-tcmb-vade-pdf", "TCMB vade PDF", "pdf_table", "required_input", "TCMB vade PDF'i ozel sektor dis borc vade bilgisini tasir.", "Ozel sektor eurobond vade analizinde kullanilir.", linked_theme_ids=("theme:eurobond", "theme:external-financing")),
        SourceDependency("source:eurobnd-hmb-odeme-projeksiyonu", "HMB odeme projeksiyonu", "excel_local", "required_input", "HMB aylik dis borc odeme projeksiyonu workbook'u", "Hazine eurobond odeme projeksiyonu baglamini saglar.", linked_theme_ids=("theme:eurobond", "theme:external-financing")),
    ),
    indicators=(
        IndicatorTemplate("derived:eurobond-total-stock", "Eurobond Toplam Stok", ("evds:TP.EBONDYAZDEG.ST", "evds:TP.YDOSBAYAZDEG.S11T"), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Toplam eurobond stokunu izler.", theme_ids=("theme:eurobond",)),
        IndicatorTemplate("derived:eurobond-foreign-stock", "Eurobond Yabanci Stok", ("evds:TP.EBONDYAZDEG.S2D", "evds:TP.YDOSBAYAZDEG.S19"), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Toplam eurobond yabanci stokunu izler.", theme_ids=("theme:eurobond",)),
        IndicatorTemplate("derived:eurobond-foreign-share", "Eurobond Yabanci Payi", ("evds:TP.EBONDYAZDEG.ST", "evds:TP.EBONDYAZDEG.S2D", "evds:TP.YDOSBAYAZDEG.S11T", "evds:TP.YDOSBAYAZDEG.S19"), formula_description="Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.", output_frequency="weekly", output_unit="ratio", economic_meaning="Toplam eurobond stokundaki yabanci payini izler.", theme_ids=("theme:eurobond",)),
        IndicatorTemplate("derived:hazine-eurobond-total", "Hazine Eurobond Toplam", ("evds:TP.EBONDYAZDEG.ST", "source:eurobnd-hmb-odeme-projeksiyonu"), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Hazine eurobond toplam stokunu izler.", theme_ids=("theme:eurobond", "theme:external-financing")),
        IndicatorTemplate("derived:hazine-eurobond-foreign-stock", "Hazine Eurobond Yabanci Stok", ("evds:TP.EBONDYAZDEG.S2D",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Hazine eurobond yabanci stokunu izler.", theme_ids=("theme:eurobond",)),
        IndicatorTemplate("derived:hazine-eurobond-foreign-share", "Hazine Eurobond Yabanci Payi", ("evds:TP.EBONDYAZDEG.ST", "evds:TP.EBONDYAZDEG.S2D"), formula_expression="evds:TP.EBONDYAZDEG.S2D / evds:TP.EBONDYAZDEG.ST", output_frequency="weekly", output_unit="ratio", economic_meaning="Hazine eurobond stokundaki yabanci payini izler.", theme_ids=("theme:eurobond",)),
        IndicatorTemplate("derived:ozel-sektor-eurobond-total", "Ozel Sektor Eurobond Toplam", ("evds:TP.YDOSBAYAZDEG.S11T", "source:eurobnd-bbg-upload", "source:eurobnd-tcmb-vade-pdf"), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Ozel sektor eurobond toplam stokunu izler.", theme_ids=("theme:eurobond", "theme:external-financing")),
        IndicatorTemplate("derived:ozel-sektor-eurobond-foreign-stock", "Ozel Sektor Eurobond Yabanci Stok", ("evds:TP.YDOSBAYAZDEG.S19",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Ozel sektor eurobond yabanci stokunu izler.", theme_ids=("theme:eurobond",)),
        IndicatorTemplate("derived:ozel-sektor-eurobond-foreign-share", "Ozel Sektor Eurobond Yabanci Payi", ("evds:TP.YDOSBAYAZDEG.S11T", "evds:TP.YDOSBAYAZDEG.S19"), formula_expression="evds:TP.YDOSBAYAZDEG.S19 / evds:TP.YDOSBAYAZDEG.S11T", output_frequency="weekly", output_unit="ratio", economic_meaning="Ozel sektor eurobond stokundaki yabanci payini izler.", theme_ids=("theme:eurobond",)),
    ),
    themes=(
        ThemeTemplate("theme:eurobond", "Eurobond", "Hazine ve ozel sektor eurobond anlatisi", indicator_ids=("derived:eurobond-total-stock", "derived:eurobond-foreign-stock", "derived:eurobond-foreign-share", "derived:hazine-eurobond-total", "derived:hazine-eurobond-foreign-stock", "derived:hazine-eurobond-foreign-share", "derived:ozel-sektor-eurobond-total", "derived:ozel-sektor-eurobond-foreign-stock", "derived:ozel-sektor-eurobond-foreign-share"), source_dependency_ids=("source:eurobnd-bbg-upload", "source:eurobnd-tcmb-vade-pdf", "source:eurobnd-hmb-odeme-projeksiyonu")),
        ThemeTemplate("theme:external-financing", "Dis Finansman", "Eurobond ve dis borc odeme baglami", indicator_ids=("derived:hazine-eurobond-total", "derived:ozel-sektor-eurobond-total"), source_dependency_ids=("source:eurobnd-bbg-upload", "source:eurobnd-tcmb-vade-pdf", "source:eurobnd-hmb-odeme-projeksiyonu")),
    ),
    status_resolver=status_from_sets(),
    role_resolver=make_role_resolver({"TP.EBONDYAZDEG": "stock_component", "TP.YDOSBAYAZDEG": "stock_component"}),
    known_blockers=("Upload sheet isimleri ve HMB workbook baslik satirlari degisken olabilir.", "TCMB vade PDF baglantisi notebook icinde dinamik bulunur."),
)


PRBNK_SPEC = NotebookSpec(
    slug="prbnk-mnklkymt-v5",
    notebook_stem="PrBnk_MnklKymt_V5",
    lane="L2_EVDS_plus_external",
    series_code_pattern=GENERIC_TICKER_PATTERN,
    series_families=("TP.AB", "TP.DIBSPIYDEG", "TP.DK", "TP.HPBITABLO5", "TP.MKNETHAR"),
    group_descriptions={
        "AB": "Rezerv/swap ve destekleyici analitik bilanco serileri",
        "DIBSPIYDEG": "DIBS stogu ve yabanci sahipligi",
        "DK": "Kur cevirim girdisi",
        "HPBITABLO5": "Mevduat ve parite yardimci serileri",
        "MKNETHAR": "Menkul kiymet stok ve net hareket serileri",
    },
    default_source_version="evds2",
    frequency_resolver=constant_frequency("weekly"),
    source_dependencies=(
        SourceDependency("source:prbnk-weekly-zip", "TCMB haftalik ZIP/XLSX", "http_download", "required_input", "TCMB haftalik paketinden gelen XLSX tablo", "Portfoy akimlari ve ek menkul kiymet bloklarinda kullanilir.", linked_theme_ids=("theme:portfolio-flows", "theme:foreign-ownership")),
        SourceDependency("source:prbnk-swap-pdf", "TCMB swap PDF", "pdf_table", "required_input", "TCMB swap islemleri PDF tablosu", "Swap stok ve net degisim anlatilarinda kullanilir.", linked_theme_ids=("theme:swap-and-securities",)),
    ),
    indicators=(
        IndicatorTemplate("derived:equity-stock", "Hisse Stogu", ("evds:TP.MKNETHAR.M1", "evds:TP.MKNETHAR.M2"), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Hisse stogunun seviyesini izler.", theme_ids=("theme:portfolio-flows", "theme:foreign-ownership")),
        IndicatorTemplate("derived:equity-foreign-share", "Hisse Yabanci Payi", ("evds:TP.MKNETHAR.M1", "source:prbnk-weekly-zip"), formula_description="Hisse stogu ve haftalik ZIP tablosundan turetilen yabanci pay.", output_frequency="weekly", output_unit="ratio", economic_meaning="Hisse senedi stokundaki yabanci payini izler.", theme_ids=("theme:foreign-ownership",)),
        IndicatorTemplate("derived:dibs-stock", "DIBS Stogu", ("evds:TP.DIBSPIYDEG.ST",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="DIBS stok seviyesini izler.", theme_ids=("theme:foreign-ownership", "theme:swap-and-securities")),
        IndicatorTemplate("derived:dibs-foreign-share", "DIBS Yabanci Payi", ("evds:TP.DIBSPIYDEG.ST", "source:prbnk-weekly-zip"), formula_description="DIBS stok ve haftalik ZIP tablosundan turetilen yabanci pay.", output_frequency="weekly", output_unit="ratio", economic_meaning="DIBS stokundaki yabanci payini izler.", theme_ids=("theme:foreign-ownership",)),
        IndicatorTemplate("derived:equity-plus-dibs-flow", "Hisse ve DIBS Net Degisimi", ("evds:TP.MKNETHAR.M20", "evds:TP.DIBSPIYDEG.ST"), formula_description="Hisse ve DIBS akimlarinin birlestirilmis net degisimi.", output_frequency="weekly", output_unit="usd_bn", economic_meaning="Portfoy akislarinin toplam yonunu izler.", theme_ids=("theme:portfolio-flows",)),
        IndicatorTemplate("derived:swap-stock", "Swap Stogu", ("source:prbnk-swap-pdf", "evds:TP.AB.A01"), formula_description="Swap PDF ve analitik bilanco destek serilerinden uretilir.", output_frequency="weekly", output_unit="usd_bn", economic_meaning="Swap stok seviyesini izler.", theme_ids=("theme:swap-and-securities",)),
        IndicatorTemplate("derived:swap-net-change", "Swap Net Degisimi", ("source:prbnk-swap-pdf",), formula_description="Swap PDF tablosundaki haftalik degisimlerden uretilir.", output_frequency="weekly", output_unit="usd_bn", economic_meaning="Swap pozisyonundaki haftalik yonu izler.", theme_ids=("theme:swap-and-securities",)),
        IndicatorTemplate("derived:portfolio-flow-total", "Toplam Portfoy Akimi", ("evds:TP.MKNETHAR.M20", "evds:TP.MKNETHAR.M21", "source:prbnk-weekly-zip"), formula_description="Hisse, DIBS ve ilgili destek tablolarindan portfoy akis toplami uretilir.", output_frequency="weekly", output_unit="usd_bn", economic_meaning="Toplam portfoy giris-cikis yonunu izler.", theme_ids=("theme:portfolio-flows",)),
    ),
    themes=(
        ThemeTemplate("theme:portfolio-flows", "Portfoy Akimlari", "Hisse ve menkul kiymet akimlari", indicator_ids=("derived:equity-stock", "derived:equity-plus-dibs-flow", "derived:portfolio-flow-total"), source_dependency_ids=("source:prbnk-weekly-zip",)),
        ThemeTemplate("theme:foreign-ownership", "Yabanci Sahipligi", "Hisse ve DIBS yabanci payi anlatisi", indicator_ids=("derived:equity-foreign-share", "derived:dibs-stock", "derived:dibs-foreign-share"), source_dependency_ids=("source:prbnk-weekly-zip",)),
        ThemeTemplate("theme:swap-and-securities", "Swap ve Menkul Kiymet", "Swap stogu ve menkul kiymet anlatilarinin baglantisi", indicator_ids=("derived:swap-stock", "derived:swap-net-change", "derived:dibs-stock"), source_dependency_ids=("source:prbnk-swap-pdf",)),
    ),
    status_resolver=status_from_sets(),
    role_resolver=make_role_resolver({"TP.AB": "balance_sheet_line", "TP.DIBSPIYDEG": "stock_component", "TP.DK": "ratio_input", "TP.HPBITABLO5": "commentary_driver", "TP.MKNETHAR": "stock_component"}, explicit_roles={"TP.HPBITABLO5.12": "parity_effect_input"}),
    known_blockers=("Notebookta aktif ve legacy/commented extraction bloklari birlikte duruyor; dormant adaylar aktif akisla karistirilmamali.",),
)


RZRV_SPEC = NotebookSpec(
    slug="rzrv-blg-v7",
    notebook_stem="Rzrv_Blg_V7",
    lane="L3_manual_or_fallback",
    series_code_pattern=GENERIC_TICKER_PATTERN,
    series_families=("TP.AB", "TP.DK", "TP.DOVVARNC"),
    group_descriptions={
        "AB": "Analitik bilanco rezerv ve yukumluluk serileri",
        "DK": "Kur cevirim girdisi",
        "DOVVARNC": "Dormant swap serisi adayi",
    },
    default_source_version="evds2",
    frequency_resolver=mapped_frequency("daily", {"TP.AB.C1": "weekly", "TP.AB.C2": "weekly", "TP.AB.N06": "weekly", "TP.DOVVARNC": "monthly"}),
    source_dependencies=(
        SourceDependency("source:rzrv-swap-pdf", "TCMB swap PDF", "pdf_table", "required_input", "TCMB swap islemleri PDF tablosu", "Swap tarafli net rezerv hesaplarinda kullanilir.", linked_theme_ids=("theme:reserves", "theme:net-reserve-estimate")),
        SourceDependency("source:rzrv-manual-swap-ledger", "Manuel swap ledger", "manual_inline", "required_input", "Notebook icindeki manuel swap tutari tablosu", "Tahmini net rezerv hesabinda diger ulke MB swap kalemini besler.", linked_theme_ids=("theme:net-reserve-estimate",)),
    ),
    indicators=(
        IndicatorTemplate("derived:reserve-total", "Rezerv Toplam", ("evds:TP.AB.C1", "evds:TP.AB.C2"), formula_description="Rezerv altin ve rezerv doviz toplamindan uretilir.", output_frequency="weekly", output_unit="usd_bn", economic_meaning="Toplam rezerv seviyesini izler.", theme_ids=("theme:reserves",)),
        IndicatorTemplate("derived:reserve-gold", "Rezerv Altin", ("evds:TP.AB.C1",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Altin rezerv seviyesini izler.", theme_ids=("theme:reserves",)),
        IndicatorTemplate("derived:reserve-fx", "Rezerv Doviz", ("evds:TP.AB.C2",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Doviz rezerv seviyesini izler.", theme_ids=("theme:reserves",)),
        IndicatorTemplate("derived:net-reserve-standby", "Net Rezerv Stand-By", ("evds:TP.AB.N06", "evds:TP.DK.USD.A.YTL"), formula_description="Net rezerv TL serisinin USD cinsine cevrilmis stand-by tanimi.", output_frequency="weekly", output_unit="usd_bn", economic_meaning="Stand-by tanimli net rezerv seviyesini izler.", theme_ids=("theme:reserves", "theme:net-reserve-estimate")),
        IndicatorTemplate("derived:estimated-net-reserve", "Tahmini Net Rezerv", ("evds:TP.AB.A02", "evds:TP.AB.A10", "evds:TP.AB.A11", "evds:TP.AB.A13", "evds:TP.AB.A14", "evds:TP.DK.USD.A.YTL", "source:rzrv-manual-swap-ledger"), formula_description="Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir.", output_frequency="daily", output_unit="usd_bn", economic_meaning="Tahmini net rezerv seviyesini izler.", theme_ids=("theme:net-reserve-estimate",)),
        IndicatorTemplate("derived:swap-adjusted-net-reserve", "Swap Haric Net Rezerv", ("derived:estimated-net-reserve", "source:rzrv-swap-pdf"), formula_description="Tahmini net rezervden swap kalemleri dusulur.", output_frequency="daily", output_unit="usd_bn", economic_meaning="Swap duzeltilmis net rezerv seviyesini izler.", theme_ids=("theme:net-reserve-estimate",)),
        IndicatorTemplate("derived:gold-share-in-reserves", "Altin Payi", ("evds:TP.AB.C1", "evds:TP.AB.C2"), formula_description="Altin rezervinin toplam rezerv icindeki payi.", output_frequency="weekly", output_unit="ratio", economic_meaning="Rezerv kompozisyonunda altin agirligini izler.", theme_ids=("theme:reserves",)),
    ),
    themes=(
        ThemeTemplate("theme:reserves", "Rezervler", "Brut rezerv ve kompozisyon temasi", indicator_ids=("derived:reserve-total", "derived:reserve-gold", "derived:reserve-fx", "derived:net-reserve-standby", "derived:gold-share-in-reserves"), source_dependency_ids=("source:rzrv-swap-pdf",)),
        ThemeTemplate("theme:net-reserve-estimate", "Tahmini Net Rezerv", "Swap duzeltilmis net rezerv anlatisi", indicator_ids=("derived:estimated-net-reserve", "derived:swap-adjusted-net-reserve", "derived:net-reserve-standby"), source_dependency_ids=("source:rzrv-swap-pdf", "source:rzrv-manual-swap-ledger")),
    ),
    status_resolver=status_from_sets(listed_only=("TP.DOVVARNC.K18",)),
    role_resolver=make_role_resolver({"TP.AB": "balance_sheet_line", "TP.DK": "ratio_input", "TP.DOVVARNC": "manual_backfill"}),
    manual_series_overrides=RZRV_SERIES_OVERRIDES,
    extra_tickers=("TP.DOVVARNC.K18",),
    known_blockers=("TP.DOVVARNC.K18 aktif akis disi triple-quoted bloktan izlenir; dormant candidate olarak korunur.", "Resmi seri adlarinin bir bolumu notebook output fallback'inden gelir."),
)


TBL_APKO_SPEC = NotebookSpec(
    slug="tbl-apko",
    notebook_stem="Tbl_Apko",
    lane="L3_manual_or_fallback",
    series_code_pattern=GENERIC_TICKER_PATTERN,
    series_families=("TP.AB", "TP.DB", "TP.DIBSPIYDEG", "TP.DK", "TP.EBONDPIYDEG", "TP.FDVY37", "TP.HPBITABLO4", "TP.KALANVADE", "TP.MKNETHAR", "TP.ODANA6", "TP.YDOSBAYAZDEG"),
    group_descriptions={
        "AB": "Rezerv ve likidite serileri",
        "DB": "Ceyreklik borc stogu serileri",
        "DIBSPIYDEG": "DIBS stok serisi",
        "DK": "Gunluk kur girdisi",
        "EBONDPIYDEG": "Eurobond stok serisi",
        "FDVY37": "GSYH / oran yardimci serisi",
        "HPBITABLO4": "Yabanci para mevduat alt kirilimlari",
        "KALANVADE": "Kalan vade aylik serileri",
        "MKNETHAR": "Menkul kiymet akim serileri",
        "ODANA6": "Cari denge / odeme serisi",
        "YDOSBAYAZDEG": "Yabanci eurobond sahipligi serileri",
    },
    default_source_version="evds2",
    frequency_resolver=mapped_frequency("weekly", {"TP.DK": "daily", "TP.ODANA6": "monthly", "TP.KALANVADE": "monthly", "TP.DB": "quarterly", "TP.FDVY37": "quarterly"}),
    source_dependencies=(
        SourceDependency("source:tblapko-bbg-upload", "BBG workbook upload", "excel_upload", "required_input", "Kullanici yuklemeli BBG workbook", "Eurobond ihrac ve vade tablolarini besler.", linked_theme_ids=("theme:apko-summary", "theme:external-financing")),
        SourceDependency("source:tblapko-hmb-ab-borc-xls", "HMB AB borc stok XLS", "excel_local", "required_input", "HMB AB tanimli genel yonetim borc stogu XLS", "Dis borc ve kamu borcu bloklarini besler.", linked_theme_ids=("theme:external-financing",)),
        SourceDependency("source:tblapko-swap-pdf", "TCMB swap PDF", "pdf_table", "required_input", "TCMB tarafli swap islemleri PDF tablosu", "Rezerv ve likidite bloklarini besler.", linked_theme_ids=("theme:reserves-and-liquidity",)),
        SourceDependency("source:tblapko-bddk-weekly-bulletin", "BDDK haftalik bulten", "web_scrape", "required_input", "BDDK haftalik bulten scrape sonucu", "Bankacilik bilanco ve YPNG/ozkaynak bloklarini besler.", linked_theme_ids=("theme:banking-balance-sheet",)),
    ),
    indicators=(
        IndicatorTemplate("derived:usdtry-buy-rate", "USDTRY Alis Kuru", ("evds:TP.DK.USD.A.YTL",), output_frequency="daily", output_unit="level", economic_meaning="Makro tablo icin gunluk kur girdisi.", theme_ids=("theme:apko-summary",)),
        IndicatorTemplate("derived:bank-tl-loans", "Banka TL Krediler", ("evds:TP.DB.B01", "source:tblapko-bddk-weekly-bulletin"), formula_description="BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.", output_frequency="weekly", output_unit="try_bn", economic_meaning="Banka TL kredi buyuklugunu izler.", theme_ids=("theme:banking-balance-sheet",)),
        IndicatorTemplate("derived:bank-fx-loans", "Banka YP Krediler", ("evds:TP.DB.B02", "source:tblapko-bddk-weekly-bulletin"), formula_description="BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.", output_frequency="weekly", output_unit="try_bn", economic_meaning="Banka YP kredi buyuklugunu izler.", theme_ids=("theme:banking-balance-sheet",)),
        IndicatorTemplate("derived:ypng-to-equity", "YPNG / Yasal Ozkaynak", ("source:tblapko-bddk-weekly-bulletin",), formula_description="BDDK bulten scrape verisinden uretilir.", output_frequency="weekly", output_unit="ratio", economic_meaning="Banka yabanci para net genel pozisyonunun ozkaynaklara oranini izler.", theme_ids=("theme:banking-balance-sheet",)),
        IndicatorTemplate("derived:foreign-dibs-stock-all-in", "Yurtdisi Yerlesikler DIBS Stoku All-In", ("evds:TP.DIBSPIYDEG.ST",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Yurtdisi yerlesiklerin DIBS stokunu izler.", theme_ids=("theme:external-financing", "theme:apko-summary")),
        IndicatorTemplate("derived:bank-fx-deposit-precious-metals", "Banka YP Mevduat Kiymetli Maden", ("evds:TP.HPBITABLO4.7", "evds:TP.HPBITABLO4.20"), output_frequency="weekly", output_unit="usd_bn", economic_meaning="Bankacilik kesimi kiymetli maden mevduatini izler.", theme_ids=("theme:banking-balance-sheet",)),
        IndicatorTemplate("derived:12m-cumulative-current-account", "12 Aylik Kumulatif Cari Denge", ("evds:TP.ODANA6.Q01",), output_frequency="monthly", output_unit="usd_bn", economic_meaning="Cari denge trendini izler.", theme_ids=("theme:apko-summary",)),
        IndicatorTemplate("derived:foreign-resident-deposits-short-term", "Yurtdisi Yerlesikler Mevduati Kisa Vade", ("evds:TP.KALANVADE.K3", "evds:TP.KALANVADE.K7"), output_frequency="monthly", output_unit="usd_bn", economic_meaning="Kisa vadeli yurtdisi yerlesik mevduatini izler.", theme_ids=("theme:external-financing",)),
        IndicatorTemplate("derived:gross-external-debt-to-gdp", "Brut Dis Borc / GSYH", ("evds:TP.DB.B37", "evds:TP.FDVY37", "source:tblapko-hmb-ab-borc-xls"), formula_description="Dis borc stoku ve GSYH yardimci serisinden uretilir.", output_frequency="quarterly", output_unit="ratio", economic_meaning="Brut dis borcun GSYH'ye oranini izler.", theme_ids=("theme:external-financing", "theme:apko-summary")),
        IndicatorTemplate("derived:tcmb-gross-reserves", "TCMB Brut Rezerv", ("evds:TP.AB.TOPLAM",), output_frequency="weekly", output_unit="usd_bn", economic_meaning="TCMB brut rezerv seviyesini izler.", theme_ids=("theme:reserves-and-liquidity", "theme:apko-summary")),
        IndicatorTemplate("derived:tcmb-net-reserves", "TCMB Net Rezerv", ("evds:TP.AB.N06", "source:tblapko-swap-pdf"), formula_description="Net rezerv ve swap duzeltme bloklarindan uretilir.", output_frequency="weekly", output_unit="usd_bn", economic_meaning="TCMB net rezerv seviyesini izler.", theme_ids=("theme:reserves-and-liquidity", "theme:apko-summary")),
    ),
    themes=(
        ThemeTemplate("theme:apko-summary", "APKO Ozet", "Makro APKO ozet tablosu", indicator_ids=("derived:usdtry-buy-rate", "derived:foreign-dibs-stock-all-in", "derived:12m-cumulative-current-account", "derived:gross-external-debt-to-gdp", "derived:tcmb-gross-reserves", "derived:tcmb-net-reserves"), source_dependency_ids=("source:tblapko-bbg-upload", "source:tblapko-hmb-ab-borc-xls", "source:tblapko-swap-pdf")),
        ThemeTemplate("theme:external-financing", "Dis Finansman", "Eurobond, DIBS ve brut dis borc baglami", indicator_ids=("derived:foreign-dibs-stock-all-in", "derived:foreign-resident-deposits-short-term", "derived:gross-external-debt-to-gdp"), source_dependency_ids=("source:tblapko-bbg-upload", "source:tblapko-hmb-ab-borc-xls")),
        ThemeTemplate("theme:banking-balance-sheet", "Bankacilik Bilancosu", "Kredi, mevduat ve YPNG bloklari", indicator_ids=("derived:bank-tl-loans", "derived:bank-fx-loans", "derived:ypng-to-equity", "derived:bank-fx-deposit-precious-metals"), source_dependency_ids=("source:tblapko-bddk-weekly-bulletin",)),
        ThemeTemplate("theme:reserves-and-liquidity", "Rezerv ve Likidite", "Swap ve rezerv bloklari", indicator_ids=("derived:tcmb-gross-reserves", "derived:tcmb-net-reserves"), source_dependency_ids=("source:tblapko-swap-pdf",)),
    ),
    status_resolver=status_from_sets(),
    role_resolver=make_role_resolver({"TP.AB": "balance_sheet_line", "TP.DB": "stock_component", "TP.DIBSPIYDEG": "stock_component", "TP.DK": "ratio_input", "TP.EBONDPIYDEG": "stock_component", "TP.FDVY37": "ratio_input", "TP.HPBITABLO4": "balance_sheet_line", "TP.KALANVADE": "term_split_line", "TP.MKNETHAR": "stock_component", "TP.ODANA6": "commentary_driver", "TP.YDOSBAYAZDEG": "stock_component"}),
    known_blockers=("Notebookta serie_info output'u yok; resmi adlar source dict ve fallback zincirinden cozumlenir.", "Coklu frekans bloklari ayni makro tabloda birlesir."),
)


ALL_SPECS = (
    DTH_SPEC,
    EUROBND_SPEC,
    PRBNK_SPEC,
    PYS_SPEC,
    RZRV_SPEC,
    TBL_APKO_SPEC,
    YI_SPEC,
)
