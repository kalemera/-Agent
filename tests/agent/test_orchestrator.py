"""Orchestrator testleri — domain routing + agent dispatch + extension."""

from __future__ import annotations

import datetime as _dt

import pandas as pd
import pytest

from evds_registry.agent.base_analyst import (
    AnalystResponse,
    BaseAnalystAgent,
    IntentDefinition,
)
from evds_registry.agent.orchestrator import (
    AGENT_DOMAIN_KEYWORDS,
    AGENT_REGISTRY,
    Orchestrator,
    register_agent,
    unregister_agent,
)
from evds_registry.agent.tufe_analyst_agent import TUFESnapshot
from evds_registry.rezerv.pipeline import RezervSnapshot


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_rezerv_snapshot() -> RezervSnapshot:
    """Mock RezervSnapshot — minimum doldurulmuş."""
    dates = pd.date_range("2026-04-01", periods=4, freq="W")
    raw = pd.DataFrame(
        {
            "AB.TOPLAM": [165_000.0, 168_000.0, 170_000.0, 168_900.0],  # Milyon USD
            "AB.C1": [60_000.0, 61_000.0, 62_000.0, 62_500.0],           # Altın
            "AB.C2": [105_000.0, 107_000.0, 108_000.0, 106_400.0],       # Döviz
            "BL0021": [600_000_000.0, 605_000_000.0, 608_000_000.0, 610_000_000.0],
            "DOVVARNC.K14": [38.0, 40.0, 41.0, 42.5],
            "DOVVARNC.K18": [25.0, 26.0, 27.0, 28.0],
            "DOVVARNC.K22": [12.0, 13.0, 14.0, 14.5],
            "DOVVARNC.K23": [1.0, 1.0, 0.0, 0.0],
        },
        index=dates,
    )
    calc = pd.DataFrame(
        {
            "NetAltinUSD": [55.0, 56.0, 57.0, 57.5],
            "NetDovizUSD": [12.0, 14.0, 16.0, 14.5],
            "SHNetAltin": [55.0, 56.0, 57.0, 57.5],
            "SHNetDoviz": [-15.0, -14.0, -13.0, -14.0],
            "SHNetRezervGunluk": [40.0, 42.0, 44.0, 43.5],
            "SHNetRezervURDL": [40.5, 42.5, 44.5, 43.7],
            "BilancoNetDovizPozisyonu": [10.0, 12.0, 14.0, 12.5],
            "BilancoTahminiNetRezerv": [25.0, 27.0, 29.0, 27.5],
            "MBSwapToplam": [37.0, 39.0, 41.0, 42.5],
        },
        index=dates,
    )
    return RezervSnapshot(
        raw=raw,
        transformed=raw.copy(),
        calculated=calc,
        validation=pd.DataFrame(index=dates),
        metadata={"version": "test"},
    )


@pytest.fixture
def mock_orch(mock_tufe_snapshot, mock_rezerv_snapshot) -> Orchestrator:
    """İki agent'i de yüklenmiş Orchestrator."""
    return Orchestrator(
        snapshots={
            "rezerv": mock_rezerv_snapshot,
            "tufe": mock_tufe_snapshot,
        }
    )


# =============================================================================
# A) TestDomainClassification
# =============================================================================


class TestDomainClassification:
    def test_brut_rezerv_query_rezerv_domain(self, mock_orch):
        assert mock_orch.classify_domain("Brüt rezerv ne kadar?") == "rezerv"

    def test_yillik_enflasyon_query_tufe_domain(self, mock_orch):
        assert mock_orch.classify_domain("Yıllık enflasyon nasıl?") == "tufe"

    def test_cekirdek_tufe_query_tufe_domain(self, mock_orch):
        assert mock_orch.classify_domain("Çekirdek TÜFE B grubu") == "tufe"

    def test_swap_query_rezerv_domain(self, mock_orch):
        assert mock_orch.classify_domain("Swap hariç net rezerv") == "rezerv"

    def test_altin_rezerv_query_rezerv_domain(self, mock_orch):
        assert mock_orch.classify_domain("TCMB altın rezervi ne durumda") == "rezerv"

    def test_aylik_tufe_query_tufe_domain(self, mock_orch):
        assert mock_orch.classify_domain("Aylık tüfe değişim") == "tufe"

    def test_nir_query_rezerv_domain(self, mock_orch):
        assert mock_orch.classify_domain("NIR ne durumda?") == "rezerv"

    def test_alakasiz_soru_none_doner(self, mock_orch):
        assert mock_orch.classify_domain("Bugün hava nasıl?") is None

    def test_bos_string_none_doner(self, mock_orch):
        assert mock_orch.classify_domain("") is None

    def test_whitespace_only_none_doner(self, mock_orch):
        assert mock_orch.classify_domain("   ") is None

    def test_tr_normalize_calisir(self, mock_orch):
        # "TÜFE" olmadan, ASCII normalize eden 'tufe' bile olsa
        assert mock_orch.classify_domain("tufe rakamlari") == "tufe"

    def test_tr_normalize_rezerv(self, mock_orch):
        assert mock_orch.classify_domain("brut rezerv durumu") == "rezerv"


# =============================================================================
# B) TestRoutingToRezervAgent
# =============================================================================


class TestRoutingToRezervAgent:
    def test_brut_rezerv_handle_metni_doner(self, mock_orch):
        text = mock_orch.handle("Brüt rezerv ne kadar?")
        assert "Brüt Rezerv" in text or "Brut Rezerv" in text or "rezerv" in text.lower()

    def test_brut_rezerv_response_dict_yapisi(self, mock_orch):
        resp = mock_orch.response("Brüt rezerv ne kadar?")
        assert resp["domain"] == "rezerv"
        assert resp["intent"] == "brut_rezerv_durum"
        assert isinstance(resp["text"], str)
        assert isinstance(resp["data"], dict)
        assert resp["snapshot_date"] == _dt.date(2026, 4, 26)

    def test_swap_haric_intent_dispatch(self, mock_orch):
        resp = mock_orch.response("Swap hariç net rezerv")
        assert resp["domain"] == "rezerv"
        assert resp["intent"] == "swap_haric_rezerv"

    def test_altin_intent_dispatch(self, mock_orch):
        resp = mock_orch.response("Altın rezerv kompozisyonu")
        assert resp["domain"] == "rezerv"
        assert resp["intent"] == "altin_kompozisyon"

    def test_data_alanlarinda_sayisal_deger_var(self, mock_orch):
        resp = mock_orch.response("Brüt rezerv ne kadar?")
        # Brüt rezerv handler 'brut_rezerv_milyar_usd' anahtarini doldurur
        assert "brut_rezerv_milyar_usd" in resp["data"]
        assert resp["data"]["brut_rezerv_milyar_usd"] is not None


# =============================================================================
# C) TestRoutingToTUFEAgent
# =============================================================================


class TestRoutingToTUFEAgent:
    def test_yillik_enflasyon_handle(self, mock_orch):
        text = mock_orch.handle("Yıllık enflasyon ne kadar")
        assert "TÜFE" in text or "tufe" in text.lower() or "yıllık" in text.lower()

    def test_yillik_response_dict_yapisi(self, mock_orch):
        resp = mock_orch.response("Yıllık TÜFE ne kadar")
        assert resp["domain"] == "tufe"
        assert resp["intent"] == "tufe_yillik"
        assert isinstance(resp["data"], dict)
        assert resp["snapshot_date"] == _dt.date(2026, 5, 1)

    def test_aylik_tufe_dispatch(self, mock_orch):
        resp = mock_orch.response("Aylık enflasyon nedir?")
        assert resp["domain"] == "tufe"
        assert resp["intent"] == "tufe_aylik"

    def test_cekirdek_tufe_dispatch(self, mock_orch):
        resp = mock_orch.response("Çekirdek TÜFE rakamı")
        assert resp["domain"] == "tufe"
        assert resp["intent"] == "cekirdek_tufe"

    def test_data_yillik_pct_dolu(self, mock_orch):
        resp = mock_orch.response("Yıllık TÜFE ne kadar")
        assert "tufe_yillik_pct" in resp["data"]
        assert resp["data"]["tufe_yillik_pct"] == pytest.approx(55.1)


# =============================================================================
# D) TestMissingSnapshot — Snapshot yoksa graceful hata
# =============================================================================


class TestMissingSnapshot:
    def test_tufe_yok_ama_tufe_sorulursa_anlamli_mesaj(self, mock_rezerv_snapshot):
        """rezerv yüklü, tufe yok → tufe sorulduğunda anlamlı uyarı."""
        orch = Orchestrator(snapshots={"rezerv": mock_rezerv_snapshot})
        resp = orch.response("Yıllık enflasyon ne kadar")
        # Domain eşleşti ama agent yok
        assert resp["domain"] == "tufe"
        assert resp["intent"] is None
        assert "tufe" in resp["text"].lower()
        assert "snapshot" in resp["text"].lower()

    def test_rezerv_yok_ama_rezerv_sorulursa_anlamli_mesaj(self, mock_tufe_snapshot):
        orch = Orchestrator(snapshots={"tufe": mock_tufe_snapshot})
        resp = orch.response("Brüt rezerv durumu")
        assert resp["domain"] == "rezerv"
        assert resp["intent"] is None
        assert "rezerv" in resp["text"].lower()
        assert "snapshot" in resp["text"].lower()

    def test_hic_snapshot_yok_help_doner(self):
        orch = Orchestrator(snapshots={})
        resp = orch.response("Bugün hava nasıl")
        assert resp["domain"] is None
        assert resp["text"]  # Help text
        assert resp["data"] == {}

    def test_snapshots_none_olsa_bile_crash_etmez(self):
        orch = Orchestrator(snapshots=None)
        assert orch.list_agents() == []
        # Help text üretilir, crash yok
        text = orch.handle("alakasiz soru")
        assert isinstance(text, str)
        assert len(text) > 0


# =============================================================================
# E) TestEmptyQuery
# =============================================================================


class TestEmptyQuery:
    def test_bos_string_help_doner(self, mock_orch):
        resp = mock_orch.response("")
        assert resp["domain"] is None
        assert resp["intent"] is None
        assert "yardımcı" in resp["text"].lower() or "yard" in resp["text"].lower()

    def test_whitespace_only_help_doner(self, mock_orch):
        text = mock_orch.handle("    \t\n  ")
        assert isinstance(text, str)
        assert len(text) > 0


# =============================================================================
# F) TestHelpText
# =============================================================================


class TestHelpText:
    def test_help_text_tum_agent_isimlerini_listeler(self, mock_orch):
        resp = mock_orch.response("alakasiz soru icerik")
        text = resp["text"]
        # AGENT_NAME alanları görünmeli
        assert "RezervAnalyst" in text or "rezerv" in text.lower()
        assert "TUFEAnalyst" in text or "tufe" in text.lower()

    def test_help_text_aktif_agent_isaret(self, mock_orch):
        resp = mock_orch.response("rastgele kelime grubu")
        text = resp["text"]
        # Yüklenmiş agent için ✓ işareti olmalı (her ikisi de yüklü)
        assert "✓" in text

    def test_help_text_yuklenmemis_agent_isaret(self, mock_tufe_snapshot):
        orch = Orchestrator(snapshots={"tufe": mock_tufe_snapshot})
        resp = orch.response("alakasiz soru")
        text = resp["text"]
        # rezerv yüklenmemiş → ✗
        assert "✗" in text


# =============================================================================
# G) TestExtensionAPI — Runtime register_agent
# =============================================================================


class _DummySnapshot:
    """Minimal snapshot — sadece data DataFrame içeriyor."""

    def __init__(self):
        self.data = pd.DataFrame(
            {"deger": [1.0, 2.0]},
            index=pd.date_range("2026-01-01", periods=2, freq="MS"),
        )


class _DummyAgent(BaseAnalystAgent):
    AGENT_NAME = "DummyAnalyst"
    AGENT_DESCRIPTION = "Test için basit dummy agent"

    INTENTS = [
        IntentDefinition(
            name="dummy_durum",
            keywords=[["dummy"], ["test", "metrik"]],
            priority=10,
            description="Dummy metrik durumu",
        ),
    ]

    def _handle_dummy_durum(self, snapshot_date) -> AnalystResponse:
        return self._build_response(
            intent="dummy_durum",
            text="Dummy yanıtı",
            data={"deger": 42.0},
            snapshot_date=snapshot_date,
        )


class TestExtensionAPI:
    def teardown_method(self):
        """Her test sonrası dummy domain'i temizle."""
        unregister_agent("dummy")

    def test_register_agent_runtime_calisir(self, mock_tufe_snapshot):
        register_agent(
            domain_name="dummy",
            agent_cls=_DummyAgent,
            keywords=[["dummy"]],
        )

        snap = _DummySnapshot()
        orch = Orchestrator(snapshots={"tufe": mock_tufe_snapshot, "dummy": snap})
        assert "dummy" in orch.list_agents()

        resp = orch.response("dummy testi")
        assert resp["domain"] == "dummy"
        assert resp["intent"] == "dummy_durum"
        assert resp["data"]["deger"] == 42.0

    def test_unregister_agent_kaldirir(self):
        register_agent("dummy", _DummyAgent, [["dummy"]])
        assert "dummy" in AGENT_REGISTRY
        assert unregister_agent("dummy") is True
        assert "dummy" not in AGENT_REGISTRY
        assert "dummy" not in AGENT_DOMAIN_KEYWORDS

    def test_unregister_olmayan_domain_false_doner(self):
        assert unregister_agent("hicboyle_yok") is False

    def test_list_registered_domains_default_iki_domain(self, mock_orch):
        registered = mock_orch.list_registered_domains()
        assert "rezerv" in registered
        assert "tufe" in registered


# =============================================================================
# H) TestErrorHandling — Agent crash ederse exception yakala
# =============================================================================


class _CrashingAgent(BaseAnalystAgent):
    AGENT_NAME = "CrashAgent"
    AGENT_DESCRIPTION = "Test için bilerek crash eden agent"

    INTENTS = [
        IntentDefinition(
            name="crash_intent",
            keywords=[["crashtest"]],
            priority=10,
        ),
    ]

    def _handle_crash_intent(self, snapshot_date):
        raise RuntimeError("bilerek patladim")


class TestErrorHandling:
    def teardown_method(self):
        unregister_agent("crashy")

    def test_agent_handler_crash_ederse_anlamli_mesaj_doner(self):
        register_agent("crashy", _CrashingAgent, [["crashtest"]])
        orch = Orchestrator(snapshots={"crashy": _DummySnapshot()})
        resp = orch.response("crashtest soru")
        assert resp["domain"] == "crashy"
        assert resp["intent"] is None
        # Hata türü ve mesajı text'te olmalı
        assert "RuntimeError" in resp["text"]
        assert "bilerek" in resp["text"]
