from __future__ import annotations
from dataclasses import dataclass
from ..records import Record
from ..storage import RegistryPaths, load_registry


@dataclass(slots=True)
class GapDetector:
    registry: dict[str, Record]

    @classmethod
    def from_paths(cls, paths: RegistryPaths) -> "GapDetector":
        return cls(registry=load_registry(paths))

    def is_gap(self, record_id: str) -> bool:
        return record_id not in self.registry

    def find_gaps(self, ids: list[str]) -> list[str]:
        return [rid for rid in ids if self.is_gap(rid)]
