from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import yaml

from .records import Record, canonical_record, render_body


@dataclass(slots=True, frozen=True)
class RegistryPaths:
    root: Path
    drafts: Path
    series: Path
    indicators: Path
    themes: Path
    source_dependencies: Path
    catalog: Path
    memory: Path
    proposals: Path

    @classmethod
    def from_root(cls, root: Path) -> "RegistryPaths":
        return cls(
            root=root,
            drafts=root / "drafts",
            series=root / "registry" / "series",
            indicators=root / "registry" / "indicators",
            themes=root / "registry" / "themes",
            source_dependencies=root / "registry" / "source_dependencies",
            catalog=root / "registry" / "catalog",
            memory=root / "registry" / "memory",
            proposals=root / "proposals",
        )

    def ensure_layout(self) -> None:
        self.drafts.mkdir(parents=True, exist_ok=True)
        self.series.mkdir(parents=True, exist_ok=True)
        self.indicators.mkdir(parents=True, exist_ok=True)
        self.themes.mkdir(parents=True, exist_ok=True)
        self.source_dependencies.mkdir(parents=True, exist_ok=True)
        self.catalog.mkdir(parents=True, exist_ok=True)
        self.memory.mkdir(parents=True, exist_ok=True)
        self.proposals.mkdir(parents=True, exist_ok=True)

    def canonical_dir(self, record_type: str) -> Path:
        if record_type == "series":
            return self.series
        if record_type == "indicator":
            return self.indicators
        if record_type == "theme":
            return self.themes
        if record_type == "source_dependency":
            return self.source_dependencies
        if record_type == "catalog":
            return self.catalog
        if record_type == "memory_rule":
            return self.memory
        if record_type == "proposal":
            return self.proposals
        raise ValueError(f"Unknown record_type: {record_type}")


def id_to_filename(record_id: str) -> str:
    return f"{quote(record_id, safe='._-')}.md"


def write_record(base_dir: Path, record: Record) -> Path:
    base_dir.mkdir(parents=True, exist_ok=True)
    path = base_dir / id_to_filename(record["id"])
    document = dump_document(canonical_record(record), render_body(record))
    path.write_text(document, encoding="utf-8")
    return path


def delete_record(base_dir: Path, record_id: str) -> None:
    path = base_dir / id_to_filename(record_id)
    if path.exists():
        path.unlink()


def load_record(base_dir: Path, record_id: str) -> Record | None:
    path = base_dir / id_to_filename(record_id)
    if not path.exists():
        return None
    return load_document(path)


def load_documents(base_dir: Path) -> list[Record]:
    if not base_dir.exists():
        return []
    records: list[Record] = []
    for path in sorted(base_dir.glob("*.md")):
        if path.name == ".gitkeep":
            continue
        records.append(load_document(path))
    return records


def load_registry(paths: RegistryPaths) -> dict[str, Record]:
    records: dict[str, Record] = {}
    for folder in (paths.series, paths.indicators, paths.themes, paths.source_dependencies):
        for record in load_documents(folder):
            records[record["id"]] = record
    return records


def load_catalog(paths: RegistryPaths) -> dict[str, Record]:
    records: dict[str, Record] = {}
    for record in load_documents(paths.catalog):
        records[record["id"]] = record
    return records


def load_memory_rules(paths: RegistryPaths) -> dict[str, Record]:
    records: dict[str, Record] = {}
    for record in load_documents(paths.memory):
        records[record["id"]] = record
    return records


def load_proposals(paths: RegistryPaths) -> dict[str, Record]:
    records: dict[str, Record] = {}
    for record in load_documents(paths.proposals):
        records[record["id"]] = record
    return records


def load_drafts(paths: RegistryPaths) -> dict[str, Record]:
    drafts: dict[str, Record] = {}
    for record in load_documents(paths.drafts):
        drafts[record["id"]] = record
    return drafts


def dump_document(frontmatter: Record, body: str) -> str:
    yaml_text = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    body_text = body.rstrip() + "\n"
    return f"---\n{yaml_text}\n---\n{body_text}"


def load_document(path: Path) -> Record:
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not raw.startswith("---\n"):
        raise ValueError(f"Record file lacks YAML front matter: {path}")
    marker = "\n---\n"
    end_index = raw.find(marker, 4)
    if end_index == -1:
        raise ValueError(f"Record file has invalid front matter markers: {path}")
    try:
        frontmatter = raw[4:end_index]
        body = raw[end_index + len(marker) :]
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"Record file has invalid front matter markers: {path}") from exc
    data = yaml.safe_load(frontmatter) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Front matter must parse to an object: {path}")
    data["body"] = body
    data["path"] = str(path)
    return canonical_record(data)


def diff_fields(candidate: Record, current: Record | None) -> list[str]:
    if current is None:
        return ["new record"]
    changed: list[str] = []
    keys = sorted(set(candidate.keys()) | set(current.keys()))
    for key in keys:
        if key in {"path", "body"}:
            continue
        if candidate.get(key) != current.get(key):
            changed.append(key)
    if candidate.get("body") != current.get("body"):
        changed.append("body")
    return changed
