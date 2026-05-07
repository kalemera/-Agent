"""Calculator modülü testleri.

Net Altın, Net Döviz, Standby, SH varyantları, bilanço tahminleri.
"""

from __future__ import annotations

import datetime as _dt

import numpy as np
import pandas as pd
import pytest

from evds_registry.rezerv import calculators as calc


# =============================================================================
# Standby Kalıntısı
# =============================================================================

class TestStandbyKalintisi:
    def test_basic_subtraction(self):
        n07 = pd.Series([1_000_000.0])
        bl001 = pd.Series([200_000.0])
        bl003 = pd.Series([100_000.0])
        bl004 = pd.Series([300_000.0])
        bl008 = pd.Series([150_000.0])
        result = calc.standby_kalintisi(n07, bl001, bl003, bl004, bl008)
        # 1M - (200+100+300+150)K = 250K
        assert result.iloc[0] == 250_000.0

    def test_n07_null_returns_null(self):
        n07 = pd.Series([np.nan])
        bl001 = pd.Series([100.0])
        bl003 = pd.Series([100.0])
        bl004 = pd.Series([100.0])
        bl008 = pd.Series([100.0])
        result = calc.standby_kalintisi(n07, bl001, bl003, bl004, bl008)
        assert pd.isna(result.iloc[0])

    def test_all_components_null_returns_null(self):
        n07 = pd.Series([1000.0])
        all_null = pd.Series([np.nan])
        result = calc.standby_kalintisi(n07, all_null, all_null, all_null, all_null)
        assert pd.isna(result.iloc[0])


# =============================================================================
# Net Altın
# =============================================================================

class TestNetAltin:
    def test_ara_basic(self):
        """Ara = BL002 - (BL132 + BL136 + BL089 + BL141Etkin)."""
        bl002 = pd.Series([1_000_000.0])
        bl132 = pd.Series([100_000.0])
        bl136 = pd.Series([50_000.0])
        bl089 = pd.Series([200_000.0])
        bl141e = pd.Series([150_000.0])
        result = calc.net_altin_ara_bin_tl(bl002, bl132, bl136, bl089, bl141e)
        # 1M - 500K = 500K
        assert result.iloc[0] == 500_000.0

    def test_ara_bl002_null(self):
        bl002 = pd.Series([np.nan])
        bl132 = pd.Series([100.0])
        bl136 = pd.Series([100.0])
        bl089 = pd.Series([100.0])
        bl141e = pd.Series([100.0])
        result = calc.net_altin_ara_bin_tl(bl002, bl132, bl136, bl089, bl141e)
        assert pd.isna(result.iloc[0])

    def test_usd_conversion(self):
        """(Ara/1M) / İmaEdilenFX."""
        ara = pd.Series([30_000_000.0])  # Bin TL
        fx = pd.Series([30.0])           # USD/TL
        result = calc.net_altin_milyar_usd(ara, fx)
        # (30M / 1M) / 30 = 1.0 milyar USD
        assert result.iloc[0] == 1.0


# =============================================================================
# Net Döviz — Pre/Post 2018 fallback
# =============================================================================

class TestNetDovizYibank:
    def test_pre_2018_uses_bl085(self):
        """Tarih < 2018-08-31 → yiBank = BL085."""
        df = pd.DataFrame(
            {
                "BL085": [500_000.0],
                "BL129": [999_999.0],
                "BL131": [888_888.0],
            },
            index=pd.DatetimeIndex(["2017-06-15"]),
        )
        yibank = calc.yibank_with_pre2018_fallback(df)
        assert yibank.iloc[0] == 500_000.0

    def test_post_2018_uses_bl129_plus_bl131(self):
        """Tarih ≥ 2018-08-31 → yiBank = BL129 + BL131."""
        df = pd.DataFrame(
            {
                "BL085": [999_999.0],
                "BL129": [400_000.0],
                "BL131": [100_000.0],
            },
            index=pd.DatetimeIndex(["2025-12-26"]),
        )
        yibank = calc.yibank_with_pre2018_fallback(df)
        assert yibank.iloc[0] == 500_000.0

    def test_boundary_2018_08_30(self):
        """2018-08-30 hala pre-2018."""
        df = pd.DataFrame(
            {
                "BL085": [777.0],
                "BL129": [100.0],
                "BL131": [200.0],
            },
            index=pd.DatetimeIndex(["2018-08-30"]),
        )
        yibank = calc.yibank_with_pre2018_fallback(df)
        assert yibank.iloc[0] == 777.0

    def test_boundary_2018_08_31(self):
        """2018-08-31 → post-2018 (≥)."""
        df = pd.DataFrame(
            {
                "BL085": [777.0],
                "BL129": [100.0],
                "BL131": [200.0],
            },
            index=pd.DatetimeIndex(["2018-08-31"]),
        )
        yibank = calc.yibank_with_pre2018_fallback(df)
        assert yibank.iloc[0] == 300.0  # BL129 + BL131


# =============================================================================
# Swap Hariç Net Altın — PDF/URDL Fallback
# =============================================================================

class TestSwapHaricNetAltin:
    def test_pdf_priority(self):
        """PDF varsa: NetAltin - PDF (PDF pozitif → çıkarma)."""
        net_altin = pd.Series([100.0])
        pdf_swap = pd.Series([10.0])
        urdl = pd.Series([-5.0])
        result = calc.swap_haric_net_altin(net_altin, pdf_swap, urdl)
        assert result.iloc[0] == 90.0  # 100 - 10

    def test_urdl_fallback(self):
        """PDF yok, URDL fallback: NetAltin + URDL (URDL negatif → toplama)."""
        net_altin = pd.Series([100.0])
        pdf_swap = pd.Series([np.nan])
        urdl = pd.Series([-15.0])
        result = calc.swap_haric_net_altin(net_altin, pdf_swap, urdl)
        assert result.iloc[0] == 85.0  # 100 + (-15)

    def test_neither_returns_net_altin(self):
        """Her ikisi yoksa NetAltin değişmeden döner."""
        net_altin = pd.Series([100.0])
        result = calc.swap_haric_net_altin(net_altin, None, None)
        assert result.iloc[0] == 100.0


# =============================================================================
# Bilanço Tahminleri
# =============================================================================

class TestBilancoTahmini:
    def test_net_doviz_pozisyonu(self):
        """A02 - A11 - A14 - A13, USD'ye çevir."""
        a02 = pd.Series([200_000_000.0])  # 200B Bin TL
        a11 = pd.Series([50_000_000.0])
        a14 = pd.Series([30_000_000.0])
        a13 = pd.Series([20_000_000.0])
        fx = pd.Series([30.0])
        result = calc.bilanco_net_doviz_pozisyonu(a02, a11, a14, a13, fx)
        # (200-50-30-20)B / 1M / 30 = 100B/1M/30 = 100/30 ≈ 3.33
        assert abs(result.iloc[0] - (100_000_000.0 / 1_000_000.0 / 30.0)) < 1e-9

    def test_tahmini_net_rezerv(self):
        """A02 - A11 - A14 (A13 hariç)."""
        a02 = pd.Series([200_000_000.0])
        a11 = pd.Series([50_000_000.0])
        a14 = pd.Series([30_000_000.0])
        fx = pd.Series([30.0])
        result = calc.bilanco_tahmini_net_rezerv(a02, a11, a14, fx)
        # (200-50-30)B / 1M / 30 = 120/30 = 4.0
        assert abs(result.iloc[0] - 4.0) < 1e-9


# =============================================================================
# MB Swap Toplam
# =============================================================================

class TestMBSwapToplam:
    def test_basic(self):
        k18 = pd.Series([10.0, 20.0])
        k22 = pd.Series([5.0, 15.0])
        result = calc.mb_swap_toplam(k18, k22)
        assert result.iloc[0] == 15.0
        assert result.iloc[1] == 35.0

    def test_null_treated_as_zero(self):
        k18 = pd.Series([10.0, np.nan])
        k22 = pd.Series([np.nan, 15.0])
        result = calc.mb_swap_toplam(k18, k22)
        assert result.iloc[0] == 10.0
        assert result.iloc[1] == 15.0
