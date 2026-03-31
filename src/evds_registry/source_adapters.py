from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class SourceAdapter(Protocol):
    def search_series(self, query: str) -> list[dict]:
        """Return matching series metadata from the source."""

    def hydrate_metadata(self, ticker: str) -> dict:
        """Return canonical metadata for a known series identifier."""

    def fetch_observations(self, ticker: str, start: str | None = None, end: str | None = None) -> list[dict]:
        """Return time-series observations for a known series identifier."""


@dataclass(slots=True)
class StubEVDSAdapter:
    source: str = "evds"

    def search_series(self, query: str) -> list[dict]:
        raise NotImplementedError("Phase 1 only defines the EVDS adapter contract.")

    def hydrate_metadata(self, ticker: str) -> dict:
        raise NotImplementedError("Phase 1 only defines the EVDS adapter contract.")

    def fetch_observations(self, ticker: str, start: str | None = None, end: str | None = None) -> list[dict]:
        raise NotImplementedError("Phase 1 only defines the EVDS adapter contract.")
