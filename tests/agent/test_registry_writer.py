import tempfile
from pathlib import Path
import pytest
from evds_registry.agent.draft_writer import DraftWriter
from evds_registry.agent.enricher import EnrichmentResult
from evds_registry.agent.registry_writer import RegistryWriter
from evds_registry.storage import RegistryPaths, load_registry


def _make_paths(tmp: Path) -> RegistryPaths:
    paths = RegistryPaths.from_root(tmp)
    paths.ensure_layout()
    return paths


def _make_result(record_id: str) -> EnrichmentResult:
    return EnrichmentResult(
        record={
            "id": record_id, "record_type": "series", "status": "draft",
            "title": "Test Serisi", "source": "evds", "source_version": "evds2",
            "ticker": record_id.replace("evds:", ""), "frequency": "monthly",
            "unit": "milyon USD", "description": "Açıklama", "usage": "Kullanım",
            "official_url": "", "theme_ids": [], "indicator_ids": [],
        },
        flags=[], confidence=0.9, source_type="evds",
    )


def test_approve_draft_writes_to_registry():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        DraftWriter(paths=paths).write_draft(_make_result("evds:TP.TEST.X01"))
        RegistryWriter(paths=paths).approve_draft("evds:TP.TEST.X01")
        registry = load_registry(paths)
        assert "evds:TP.TEST.X01" in registry


def test_approve_strips_draft_fields():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        DraftWriter(paths=paths).write_draft(_make_result("evds:TP.TEST.X01"))
        RegistryWriter(paths=paths).approve_draft("evds:TP.TEST.X01")
        registry = load_registry(paths)
        record = registry["evds:TP.TEST.X01"]
        assert "draft_confidence" not in record
        assert "draft_flags" not in record
        assert "draft_source_type" not in record


def test_approve_sets_status_approved():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        DraftWriter(paths=paths).write_draft(_make_result("evds:TP.TEST.X01"))
        RegistryWriter(paths=paths).approve_draft("evds:TP.TEST.X01")
        registry = load_registry(paths)
        assert registry["evds:TP.TEST.X01"]["status"] == "approved"


def test_approve_deletes_draft():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        dw = DraftWriter(paths=paths)
        dw.write_draft(_make_result("evds:TP.TEST.X01"))
        RegistryWriter(paths=paths).approve_draft("evds:TP.TEST.X01")
        assert dw.list_drafts() == []


def test_reject_draft_removes_without_writing():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        dw = DraftWriter(paths=paths)
        dw.write_draft(_make_result("evds:TP.TEST.X01"))
        RegistryWriter(paths=paths).reject_draft("evds:TP.TEST.X01")
        registry = load_registry(paths)
        assert "evds:TP.TEST.X01" not in registry
        assert dw.list_drafts() == []


def test_approve_raises_if_draft_missing():
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_paths(Path(tmp))
        with pytest.raises(FileNotFoundError):
            RegistryWriter(paths=paths).approve_draft("evds:TP.YOK.X00")
