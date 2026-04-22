import tempfile
from pathlib import Path
import pytest
from evds_registry.agent.draft_writer import DraftWriter
from evds_registry.agent.enricher import EnrichmentFlag, EnrichmentResult
from evds_registry.storage import RegistryPaths


def _make_paths(tmp: Path) -> RegistryPaths:
    return RegistryPaths.from_root(tmp)


def _make_result(record_id: str, confidence: float = 0.8, flags=None) -> EnrichmentResult:
    return EnrichmentResult(
        record={
            "id": record_id, "record_type": "series", "status": "draft",
            "title": "Test Serisi", "source": "evds", "source_version": "evds2",
            "ticker": record_id.replace("evds:", ""), "frequency": "monthly",
            "unit": "milyon USD", "description": "", "usage": "",
            "official_url": "", "theme_ids": [], "indicator_ids": [],
        },
        flags=flags or [],
        confidence=confidence,
        source_type="evds",
    )


def test_write_draft_creates_file():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        paths.ensure_layout()
        writer = DraftWriter(paths=paths)
        result = _make_result("evds:TP.TEST.X01")
        path = writer.write_draft(result)
        assert path.exists()


def test_written_draft_has_confidence_field():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        paths.ensure_layout()
        writer = DraftWriter(paths=paths)
        writer.write_draft(_make_result("evds:TP.TEST.X01", confidence=0.65))
        drafts = writer.list_drafts()
        assert len(drafts) == 1
        assert drafts[0]["draft_confidence"] == pytest.approx(0.65)


def test_list_drafts_returns_all():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        paths.ensure_layout()
        writer = DraftWriter(paths=paths)
        writer.write_draft(_make_result("evds:TP.TEST.X01"))
        writer.write_draft(_make_result("evds:TP.TEST.X02"))
        assert len(writer.list_drafts()) == 2


def test_delete_draft_removes_file():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        paths.ensure_layout()
        writer = DraftWriter(paths=paths)
        writer.write_draft(_make_result("evds:TP.TEST.X01"))
        writer.delete_draft("evds:TP.TEST.X01")
        assert writer.list_drafts() == []


def test_flags_stored_in_draft():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        paths.ensure_layout()
        writer = DraftWriter(paths=paths)
        flags = [EnrichmentFlag(field="theme_ids", level="yellow", message="Emin değilim")]
        writer.write_draft(_make_result("evds:TP.TEST.X01", flags=flags))
        drafts = writer.list_drafts()
        stored_flags = drafts[0]["draft_flags"]
        assert len(stored_flags) == 1
        assert stored_flags[0]["level"] == "yellow"
