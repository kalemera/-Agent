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


from evds_registry.agent.enricher import Enricher, EnrichmentResult
from evds_registry.llm import DisabledLLMClient


def _make_catalog(tickers: dict[str, dict]) -> dict:
    return {
        f"catalog:evds2:{t}": {"id": f"catalog:evds2:{t}", "title": v["title"],
                                 "frequency": v.get("frequency", "monthly"),
                                 "unit": v.get("unit", "")}
        for t, v in tickers.items()
    }


def test_enricher_evds_ticker_uses_catalog():
    catalog = _make_catalog({"TP.ODANA6.Q01": {"title": "Cari İşlemler Hesabı", "unit": "milyon ABD doları"}})
    enricher = Enricher(llm=DisabledLLMClient(), catalog=catalog, known_themes=["theme:cari-denge"])
    result = enricher.enrich("evds:TP.ODANA6.Q01")
    assert result.record["title"] == "Cari İşlemler Hesabı"
    assert result.record["unit"] == "milyon ABD doları"
    assert result.source_type == "evds"


def test_enricher_missing_catalog_adds_red_flag():
    enricher = Enricher(llm=DisabledLLMClient(), catalog={}, known_themes=[])
    result = enricher.enrich("evds:TP.BILINMEYEN.X99")
    red_flags = [f for f in result.flags if f.level == "red"]
    assert len(red_flags) >= 1
    assert result.confidence < 0.5


def test_enricher_disabled_llm_adds_yellow_theme_flag():
    catalog = _make_catalog({"TP.TEST.X01": {"title": "Test Serisi"}})
    enricher = Enricher(llm=DisabledLLMClient(), catalog=catalog, known_themes=["theme:cari-denge"])
    result = enricher.enrich("evds:TP.TEST.X01")
    yellow_flags = [f for f in result.flags if f.level == "yellow" and f.field == "theme_ids"]
    assert len(yellow_flags) >= 1
