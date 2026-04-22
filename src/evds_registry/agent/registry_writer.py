from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass

from ..records import Record
from ..storage import (
    RegistryPaths, load_document, write_record,
    id_to_filename,
)
from .draft_writer import DraftWriter

_DRAFT_FIELDS = frozenset({"draft_confidence", "draft_flags", "draft_source_type"})


def _strip_draft_fields(record: Record) -> Record:
    return {k: v for k, v in record.items() if k not in _DRAFT_FIELDS}


@dataclass(slots=True)
class RegistryWriter:
    paths: RegistryPaths

    def approve_draft(self, record_id: str) -> Record:
        draft_path = self.paths.drafts / id_to_filename(record_id)
        if not draft_path.exists():
            raise FileNotFoundError(f"Draft bulunamadı: {record_id}")
        draft = load_document(draft_path)
        record = _strip_draft_fields(deepcopy(draft))
        record["status"] = "approved"
        target_dir = self.paths.canonical_dir(record["record_type"])
        write_record(target_dir, record)
        DraftWriter(paths=self.paths).delete_draft(record_id)
        return record

    def reject_draft(self, record_id: str) -> None:
        DraftWriter(paths=self.paths).delete_draft(record_id)
