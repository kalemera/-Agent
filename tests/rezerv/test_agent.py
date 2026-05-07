"""RezervAnalystAgent testleri."""

from __future__ import annotations

import datetime as _dt

import numpy as np
import pandas as pd
import pytest

from evds_registry.rezerv import RezervSnapshot
from evds_registry.agent.rezerv_analyst_agent import (
    RezervAnalystAgent,
    classify_intent,
)


# =============================================================================
# Intent Classification
# =============================================================================

class TestClassifyIntent:
    def test_brut_rezerv(self):
        assert classify_intent("Brüt rezerv ne kadar?") == "brut_rezerv_durum"
        assert classify_intent("brut rezerv durumu") == "brut_rezerv_durum"
        assert classify_intent("Toplam rezerv kaç?") == "brut_rezerv_durum"

    def test_net_rezerv(self):
        assert classify_intent("Net rezerv durumu nasıl?") == "net_rezerv_durum"
        assert classify_intent("NIR ne kadar?") == "net_rezerv_durum"
        assert classify_intent("Net Uluslararası Rezerv") == "net_rezerv_durum"

    def test_swap_haric_priority_over_net(self):
        """'swap hariç net rezerv' → swap_haric_rezerv (NET değil)."""
        assert classify_intent("Swap hariç net rezerv") == "swap_haric_rezerv"
        assert classify_intent("swap haric") == "swap_haric_rezerv"

    def test_gunluk_tahmin(self):
        assert classify_intent("Günlük tahmin nedir?") == "gunluk_tahmin"
        assert classify_intent("Bilanço tahmini") == "gunluk_tahmin"

    def test_altin_priority_over_brut(self):
        """'brüt altın rezerv' → altin_kompozisyon (altın daha spesifik)."""
        assert classify_intent("Altın kompozisyonu") == "altin_kompozisyon"
        assert classify_intent("Brüt altın rezerv") == "altin_kompozisyon"

    def test_doviz_kompozisyon(self):
        assert classify_intent("Döviz kompozisyon") == "doviz_kompozisyon"
        assert classify_intent("doviz rezerv") == "doviz_kompozisyon"

    def test_swap_breakdown(self):
        assert classify_intent("MB swap büyüklüğü") == "swap_breakdown"
        assert classify_intent("M.B. swap stok") == "swap_breakdown"

    def test_tarihsel(self):
        assert classify_intent("Yıl başı değişim") == "tarihsel_karsilastirma"
        assert classify_intent("Aylık değişim") == "tarihsel_karsilastirma"
        assert classify_intent("YBB nasıl?") == "tarihsel_karsilastirma"

    def test_no_match(self):
        assert classify_intent("Bana bir şiir oku") is None
        assert classify_intent("") is None


# =============================================================================
# Agent Behavior — Mock Snapshot
# =============================================================================

@pytest.fixture
def mock_snapshot() -> RezervSnapshot:
    """Sahte 5 haftalık veri içeren snapshot."""
    dates = pd.DatetimeIndex(pd.date_range("2026-04-01", periods=5, freq="W-FRI"))
    raw = pd.DataFrame(
        {
            "AB.TOPLAM": [165_000.0, 167_000.0, 168_000.0, 170_000.0, 168_900.0],  # Milyon USD
            "AB.C1": [50_000.0, 51_000.0, 51_500.0, 52_000.0, 51_800.0],
            "AB.C2": [115_000.0, 116_000.0, 116_500.0, 118_000.0, 117_100.0],
            "BL0021": [None, None, 51_000_000.0, 52_000_000.0, 51_500_000.0],
            "DOVVARNC.K14": [50.0, 51.0, 50.5, 51.5, 50.0],
            "DOVVARNC.K18": [-15.0, -15.5, -15.0, -16.0, -15.0],
            "DOVVARNC.K22": [-5.0, -5.0, -5.0, -5.5, -5.0],
            "DOVVARNC.K23": [-30.0, -30.5, -30.5, -30.0, -30.0],
        },
        index=dates,
    )
    transformed = raw.copy()
    calculated = pd.DataFrame(
        {
            "NetAltinUSD": [25.0, 25.5, 26.0, 26.5, 27.0],
            "NetDovizUSD": [22.0, 22.5, 23.0, 24.0, 23.5],
            "MBSwapToplam": [-20.0, -20.5, -20.0, -21.5, -20.0],
            "BilancoNetDovizPozisyonu": [40.0, 41.0, 42.0, 43.0, 45.9],
            "BilancoTahminiNetRezerv": [55.0, 56.0, 57.0, 58.0, 53.2],
        },
        index=dates,
    )
    return RezervSnapshot(
        raw=raw,
        transformed=transformed,
        calculated=calculated,
        validation=pd.DataFrame(index=dates),
    )


class TestRezervAnalystAgent:
    def test_handle_unknown_intent_returns_help(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        text = agent.handle("Bana şiir oku")
        assert "anlayamadım" in text.lower() or "yardımcı olabilirim" in text.lower()

    def test_brut_rezerv_response(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("Brüt rezerv ne kadar?")
        assert resp.intent == "brut_rezerv_durum"
        # 168_900 / 1000 = 168.9 milyar USD
        assert "168" in resp.text
        assert resp.data["brut_rezerv_milyar_usd"] == pytest.approx(168.9, rel=0.01)
        # Haftalık değişim: 168.9 - 170 = -1.1
        assert resp.data["haftalik_degisim"] == pytest.approx(-1.1, abs=0.01)

    def test_net_rezerv_response(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("Net Uluslararası Rezerv durumu")
        assert resp.intent == "net_rezerv_durum"
        # NetAltin (27) + NetDoviz (23.5) = 50.5
        assert resp.data["net_altin_milyar_usd"] == pytest.approx(27.0)
        assert resp.data["net_doviz_milyar_usd"] == pytest.approx(23.5)
        assert resp.data["nir_milyar_usd"] == pytest.approx(50.5)

    def test_gunluk_tahmin_response(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("Günlük bilanço tahmini")
        assert resp.intent == "gunluk_tahmin"
        assert resp.data["net_doviz_pozisyonu_milyar_usd"] == pytest.approx(45.9)
        assert resp.data["tahmini_net_rezerv_milyar_usd"] == pytest.approx(53.2)

    def test_altin_kompozisyon_response(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("Altın kompozisyonu")
        assert resp.intent == "altin_kompozisyon"
        # Brüt altın 51.8 milyar USD
        assert resp.data["brut_altin_milyar_usd"] == pytest.approx(51.8)
        assert resp.data["net_altin_milyar_usd"] == pytest.approx(27.0)
        # Ton: 51_500_000 / 1_000_000 = 51.5
        assert resp.data["altin_ton"] == pytest.approx(51.5)

    def test_swap_breakdown_response(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("MB swap büyüklüğü")
        assert resp.intent == "swap_breakdown"
        assert resp.data["mb_acik_swap"] == pytest.approx(-15.0)
        assert resp.data["mb_fazla_swap"] == pytest.approx(-5.0)
        # MBSwapToplam from calculated frame
        assert resp.data["mb_swap_toplam"] == pytest.approx(-20.0)

    def test_tarihsel_karsilastirma_response(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("Aylık değişim nasıl?")
        assert resp.intent == "tarihsel_karsilastirma"
        # Haftalık: 168.9 - 170 = -1.1
        assert resp.data["haftalik_degisim"] == pytest.approx(-1.1, abs=0.01)
        # Aylık (4 dönem öncesi): 168.9 - 165 = +3.9
        assert resp.data["aylik_degisim"] == pytest.approx(3.9, abs=0.01)

    def test_swap_haric_response_empty_data(self, mock_snapshot):
        """SH sütunları yoksa null değer döner ama crash etmez."""
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("Swap hariç net rezerv")
        assert resp.intent == "swap_haric_rezerv"
        # Mock'ta SH sütunları yok → veri yok mesajları
        assert "swap hariç" in resp.text.lower() or "Swap" in resp.text

    def test_snapshot_date_set(self, mock_snapshot):
        agent = RezervAnalystAgent(mock_snapshot)
        resp = agent.response("Brüt rezerv")
        # 2026-04-01 + 4 hafta = 2026-05-01 cuma
        assert resp.snapshot_date == _dt.date(2026, 5, 1)
