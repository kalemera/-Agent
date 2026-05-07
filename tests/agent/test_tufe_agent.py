"""TUFEAnalystAgent + TUFESnapshot testleri."""

from __future__ import annotations

import pandas as pd
import pytest

from evds_registry.agent.base_analyst import IntentDefinition
from evds_registry.agent.tufe_analyst_agent import TUFEAnalystAgent, TUFESnapshot


# =============================================================================
# A) TestTUFESnapshot
# =============================================================================


class TestTUFESnapshot:
    def test_data_dataframe_ile_init(self):
        df = pd.DataFrame({"a": [1, 2]})
        snap = TUFESnapshot(data=df)
        assert snap.data is df

    def test_metadata_default_bos_dict(self):
        snap = TUFESnapshot(data=pd.DataFrame())
        assert snap.metadata == {}
        assert isinstance(snap.metadata, dict)

    def test_metadata_kullanici_verirse_korunur(self):
        snap = TUFESnapshot(data=pd.DataFrame(), metadata={"src": "evds"})
        assert snap.metadata == {"src": "evds"}


# =============================================================================
# B) TestTUFEIntentClassification
# =============================================================================


class TestTUFEIntentClassification:
    def test_yillik_tufe_classify(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        assert agent.classify_intent("Yıllık TÜFE ne kadar") == "tufe_yillik"

    def test_yillik_enflasyon_classify(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        assert agent.classify_intent("yıllık enflasyon nedir") == "tufe_yillik"

    def test_aylik_enflasyon_classify(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        assert agent.classify_intent("Aylık enflasyon ne") == "tufe_aylik"

    def test_cekirdek_tufe_classify(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        assert agent.classify_intent("Çekirdek TÜFE rakamı") == "cekirdek_tufe"

    def test_gida_kategori_classify(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        assert agent.classify_intent("Gıda enflasyonu nasıl") == "kategori_kirilim"

    def test_genel_tufe_fallback_classify(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        # Sadece "tüfe" geçen genel soru → tufe_genel_durum (p=50, fallback)
        assert agent.classify_intent("TÜFE genel hakkında") == "tufe_genel_durum"

    def test_cekirdek_b_grubu_priority(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        # "çekirdek" priority 8, "tüfe" tek başına priority 50
        # "çekirdek b grubu" iki keyword grubunu da match edebilir,
        # priority 8 olan cekirdek_tufe önce dönmeli
        assert agent.classify_intent("çekirdek b grubu") == "cekirdek_tufe"


# =============================================================================
# C) TestHandlers
# =============================================================================


class TestHandlers:
    def test_yillik_handler_dogru_sayiyi_doner(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        resp = agent.response("yıllık tüfe")
        assert resp.intent == "tufe_yillik"
        # Son tufe_yillik_pct = 55.1
        assert resp.data["tufe_yillik_pct"] == pytest.approx(55.1)
        # Önceki aya göre değişim: 55.1 - 58.3 = -3.2
        assert resp.data["onceki_aya_gore_puan"] == pytest.approx(-3.2)
        assert "55.10" in resp.text

    def test_aylik_handler_dogru_sayiyi_doner(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        resp = agent.response("aylık enflasyon")
        assert resp.intent == "tufe_aylik"
        # Son tufe_aylik_pct = 2.7
        assert resp.data["tufe_aylik_pct"] == pytest.approx(2.7)
        # Önceki: 2.7 - 2.4 = 0.3
        assert resp.data["onceki_aya_gore_puan"] == pytest.approx(0.3)
        assert "2.70" in resp.text

    def test_cekirdek_handler_b_ve_c_doner(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        resp = agent.response("çekirdek tüfe nedir")
        assert resp.intent == "cekirdek_tufe"
        assert resp.data["cekirdek_b_yillik"] == pytest.approx(52.0)
        assert resp.data["cekirdek_c_yillik"] == pytest.approx(50.0)
        assert "52.00" in resp.text
        assert "50.00" in resp.text

    def test_kategori_kirilim_gida_enerji_hizmet(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        resp = agent.response("gıda fiyatları")
        assert resp.intent == "kategori_kirilim"
        assert resp.data["gida_yillik"] == pytest.approx(70.0)
        assert resp.data["enerji_yillik"] == pytest.approx(38.0)
        assert resp.data["hizmet_yillik"] == pytest.approx(49.0)

    def test_genel_durum_endeks_yillik_aylik(self, mock_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=mock_tufe_snapshot)
        resp = agent.response("tüfe nedir")
        assert resp.intent == "tufe_genel_durum"
        assert resp.data["tufe_genel_endeks"] == pytest.approx(107.8)
        assert resp.data["tufe_yillik_pct"] == pytest.approx(55.1)
        assert resp.data["tufe_aylik_pct"] == pytest.approx(2.7)
        assert "107.80" in resp.text


# =============================================================================
# D) TestColumnOverride
# =============================================================================


class CustomTUFE(TUFEAnalystAgent):
    """Sütun adı override eden custom TUFE agent."""

    COL_TUFE_YILLIK = "my_yillik"


class TestColumnOverride:
    def test_subclass_kolon_override_calisir(self):
        df = pd.DataFrame(
            {
                "tufe_genel": [100.0, 110.0],
                "my_yillik": [40.0, 45.0],  # Custom sütun adı
                "tufe_aylik_pct": [2.0, 2.5],
                "cekirdek_b_yillik": [38.0, 42.0],
                "cekirdek_c_yillik": [36.0, 40.0],
            },
            index=pd.date_range("2026-03-01", periods=2, freq="MS"),
        )
        snap = TUFESnapshot(data=df)
        agent = CustomTUFE(snapshot=snap)
        resp = agent.response("yıllık tüfe")
        assert resp.intent == "tufe_yillik"
        assert resp.data["tufe_yillik_pct"] == pytest.approx(45.0)


# =============================================================================
# E) TestExtensionExample (README'deki örnek)
# =============================================================================


class _MyTUFEAgent(TUFEAnalystAgent):
    """README'deki örnek subclass — yeni intent ekler."""

    INTENTS = TUFEAnalystAgent.INTENTS + [
        IntentDefinition(
            name="ozel_grup_analizi",
            keywords=[
                ["özel", "grup"],  # priority < cekirdek_tufe (8) olmalı
            ],
            priority=5,
            description="Özel grup analizi",
        ),
    ]

    def _handle_ozel_grup_analizi(self, snapshot_date):
        gida = self.safe_get(self.snapshot.data, self.COL_GIDA)
        return self._build_response(
            intent="ozel_grup_analizi",
            text=f"Gıda enflasyonu: {self.format_number(gida, '%')}",
            data={"gida_yillik": gida},
            snapshot_date=snapshot_date,
        )


class TestExtensionExample:
    def test_subclass_yeni_intent_calisir(self, mock_tufe_snapshot):
        agent = _MyTUFEAgent(snapshot=mock_tufe_snapshot)
        resp = agent.response("özel grup analizi yap")
        assert resp.intent == "ozel_grup_analizi"
        assert resp.data["gida_yillik"] == pytest.approx(70.0)
        assert "70.00" in resp.text


# =============================================================================
# F) TestNullSafety
# =============================================================================


class TestNullSafety:
    def test_bos_dataframe_yillik_handler_veri_yok(self, empty_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=empty_tufe_snapshot)
        resp = agent.response("yıllık tüfe")
        assert resp.intent == "tufe_yillik"
        assert resp.data["tufe_yillik_pct"] is None
        assert "veri yok" in resp.text

    def test_bos_dataframe_aylik_handler_veri_yok(self, empty_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=empty_tufe_snapshot)
        resp = agent.response("aylık enflasyon")
        assert resp.intent == "tufe_aylik"
        assert resp.data["tufe_aylik_pct"] is None
        assert "veri yok" in resp.text

    def test_bos_dataframe_cekirdek_handler_veri_yok(self, empty_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=empty_tufe_snapshot)
        resp = agent.response("çekirdek tüfe")
        assert resp.intent == "cekirdek_tufe"
        assert resp.data["cekirdek_b_yillik"] is None
        assert resp.data["cekirdek_c_yillik"] is None

    def test_bos_dataframe_kategori_handler_veri_yok(self, empty_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=empty_tufe_snapshot)
        resp = agent.response("gıda enflasyonu")
        assert resp.intent == "kategori_kirilim"
        assert resp.data["gida_yillik"] is None

    def test_bos_dataframe_genel_handler_veri_yok(self, empty_tufe_snapshot):
        agent = TUFEAnalystAgent(snapshot=empty_tufe_snapshot)
        resp = agent.response("tüfe nedir")
        assert resp.intent == "tufe_genel_durum"
        assert resp.data["tufe_genel_endeks"] is None

    def test_snapshot_none_crash_etmez(self):
        agent = TUFEAnalystAgent(snapshot=None)
        resp = agent.response("yıllık tüfe")
        assert resp.intent == "tufe_yillik"
        # Crash etmemeli, tüm değerler None olmalı
        assert resp.data["tufe_yillik_pct"] is None

    def test_snapshot_none_latest_date_none(self):
        agent = TUFEAnalystAgent(snapshot=None)
        assert agent._latest_date() is None
