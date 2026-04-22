from __future__ import annotations
from dataclasses import dataclass
from ..records import Record


def detect_source_type(record_id: str) -> str:
    """Infers data source from record ID prefix."""
    rid = record_id.strip().lower()
    if rid.startswith("evds:") or rid.startswith("tp."):
        return "evds"
    if rid.startswith("source:tufe") or rid.startswith("source:yufe"):
        return "tuik"
    if rid.startswith("source:"):
        return "source"
    if rid.startswith("derived:"):
        return "derived"
    if rid.startswith("theme:"):
        return "theme"
    return "unknown"


@dataclass(slots=True)
class EnrichmentFlag:
    field: str
    level: str   # "red" | "yellow"
    message: str

    def to_dict(self) -> dict[str, str]:
        return {"field": self.field, "level": self.level, "message": self.message}


@dataclass(slots=True)
class EnrichmentResult:
    record: Record
    flags: list[EnrichmentFlag]
    confidence: float
    source_type: str
