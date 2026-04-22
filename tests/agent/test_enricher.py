import pytest
from evds_registry.agent.enricher import detect_source_type


def test_evds_tp_prefix():
    assert detect_source_type("evds:TP.ODANA6.Q01") == "evds"


def test_evds_raw_ticker():
    assert detect_source_type("TP.DK.USD.A") == "evds"


def test_tuik_source():
    assert detect_source_type("source:tufe-ozel-kapsamli") == "tuik"


def test_derived_indicator():
    assert detect_source_type("derived:cekirdek-tufe-c") == "derived"


def test_unknown_falls_back():
    assert detect_source_type("bilinmeyen:xyz") == "unknown"
