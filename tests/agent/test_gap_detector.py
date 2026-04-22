from evds_registry.agent.gap_detector import GapDetector


def _make_registry(ids: list[str]) -> dict:
    return {rid: {"id": rid, "record_type": "series", "title": rid} for rid in ids}


def test_is_gap_returns_true_for_missing():
    det = GapDetector(registry=_make_registry(["evds:TP.AB.A01"]))
    assert det.is_gap("evds:TP.ODANA6.Q99") is True


def test_is_gap_returns_false_for_existing():
    det = GapDetector(registry=_make_registry(["evds:TP.AB.A01"]))
    assert det.is_gap("evds:TP.AB.A01") is False


def test_find_gaps_filters_missing():
    det = GapDetector(registry=_make_registry(["evds:A", "evds:B"]))
    result = det.find_gaps(["evds:A", "evds:C", "evds:D"])
    assert result == ["evds:C", "evds:D"]


def test_find_gaps_empty_when_all_known():
    det = GapDetector(registry=_make_registry(["evds:A"]))
    assert det.find_gaps(["evds:A"]) == []
