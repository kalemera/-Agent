from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

import yaml

from ..records import Record, split_list
from ..storage import RegistryPaths, load_documents, id_to_filename
from .enricher import EnrichmentResult


def _dump_draft(record: Record) -> str:
    """Writes draft record as YAML frontmatter + markdown.
    Does NOT call canonical_record() — preserves draft_* fields."""
    fm = deepcopy(record)
    for key in ("theme_ids", "indicator_ids", "input_ids", "series_ids"):
        if key in fm:
            fm[key] = split_list(fm[key])
    body = f"# {fm['title']}\n\n_Taslak kayıt — onay bekleniyor._\n"
    yaml_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{yaml_text}\n---\n{body}"


@dataclass(slots=True)
class DraftWriter:
    paths: RegistryPaths

    def write_draft(self, result: EnrichmentResult) -> Path:
        record = deepcopy(result.record)
        record["draft_confidence"] = round(result.confidence, 4)
        record["draft_source_type"] = result.source_type
        record["draft_flags"] = [f.to_dict() for f in result.flags]
        self.paths.drafts.mkdir(parents=True, exist_ok=True)
        path = self.paths.drafts / id_to_filename(record["id"])
        path.write_text(_dump_draft(record), encoding="utf-8")
        return path

    def list_drafts(self) -> list[Record]:
        return load_documents(self.paths.drafts)

    def delete_draft(self, record_id: str) -> None:
        path = self.paths.drafts / id_to_filename(record_id)
        if path.exists():
            path.unlink()
