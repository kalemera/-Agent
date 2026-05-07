"""Transformer modülü testleri.

TDD sırasındaki ilk modül — birim dönüşümleri ve backfill mantığı.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from evds_registry.rezerv import transformers as tx


# =============================================================================
# Birim Dönüşümleri
# =============================================================================

class TestUnitConversions:
    def test_bin_tl_to_milyar_tl(self):
        assert tx.bin_tl_to_milyar_tl(1_000_000.0) == 1.0
        assert tx.bin_tl_to_milyar_tl(5_341_000_000) == 5341.0

    def test_milyon_usd_to_milyar_usd(self):
        assert tx.milyon_usd_to_milyar_usd(161_645) == 161.645

    def test_gram_to_troy_ons(self):
        # 31.1034768 gram = 1 troy ons
        assert abs(tx.gram_to_troy_ons(31.1034768) - 1.0) < 1e-9


# =============================================================================
# BL142 Backfill — Sadece Başlangıç
# =============================================================================

class TestBL142Backfill:
    def test_only_leading_nulls_filled(self):
        """Başlangıçtaki null'lar doldurulur, ortadaki/sondaki dokunulmaz."""
        s = pd.Series(
            [np.nan, np.nan, 100.0, 110.0, np.nan, 120.0, np.nan],
            index=pd.RangeIndex(7),
        )
        result = tx.bl142_backfill(s)

        # İlk iki null → 100 (ilk geçerli değer)
        assert result.iloc[0] == 100.0
        assert result.iloc[1] == 100.0
        # Mevcut değerler değişmemeli
        assert result.iloc[2] == 100.0
        assert result.iloc[3] == 110.0
        # Ortadaki null DOKUNULMAMALI
        assert pd.isna(result.iloc[4])
        # Sondaki null DOKUNULMAMALI
        assert pd.isna(result.iloc[6])

    def test_all_null_returns_all_null(self):
        s = pd.Series([np.nan] * 5)
        result = tx.bl142_backfill(s)
        assert result.isna().all()

    def test_no_leading_nulls(self):
        """Hiç başlangıç null'u yoksa seri değişmeden döner."""
        s = pd.Series([100.0, 110.0, 120.0])
        result = tx.bl142_backfill(s)
        pd.testing.assert_series_equal(result, s)


# =============================================================================
# BL141 Etkin
# =============================================================================

class TestBL141Etkin:
    def test_real_value_preferred(self):
        """Gerçek BL141 dolu ise türetilen göz ardı edilir."""
        real = pd.Series([100.0, 110.0, np.nan, np.nan])
        turetilen = pd.Series([200.0, 220.0, 230.0, np.nan])
        result = tx.bl141_etkin(real, turetilen)
        assert result.iloc[0] == 100.0
        assert result.iloc[1] == 110.0
        assert result.iloc[2] == 230.0  # gerçek null → türetilen
        assert pd.isna(result.iloc[3])  # her ikisi null

    def test_turetilen_calculation(self):
        """BL142×fiyat/1000 formülü."""
        bl142 = pd.Series([1000.0, 2000.0])
        fiyat = pd.Series([200.0, 250.0])  # TL/gram
        result = tx.bl141_turetilen(bl142, fiyat)
        # 1000 × 200 / 1000 = 200
        assert result.iloc[0] == 200.0
        # 2000 × 250 / 1000 = 500
        assert result.iloc[1] == 500.0


# =============================================================================
# BL140 Etkin (3-katmanlı)
# =============================================================================

class TestBL140Etkin:
    def test_layer1_real_value(self):
        """Katman 1: BL140 dolu → BL140 kullanılır."""
        bl140 = pd.Series([100.0, 200.0])
        bl097 = pd.Series([500.0, 600.0])
        bl141e = pd.Series([50.0, 75.0])
        result = tx.bl140_etkin(bl140, bl097, bl141e)
        assert result.iloc[0] == 100.0
        assert result.iloc[1] == 200.0

    def test_layer2_bl097_minus_bl141etkin(self):
        """Katman 2: BL140 null + BL097 > 100K + BL141Etkin var."""
        bl140 = pd.Series([np.nan])
        bl097 = pd.Series([500_000.0])  # > 100K threshold
        bl141e = pd.Series([200_000.0])
        result = tx.bl140_etkin(bl140, bl097, bl141e)
        assert result.iloc[0] == 300_000.0  # 500K - 200K

    def test_layer3_bl097_only(self):
        """Katman 3: BL140 null + BL097 > 100K + BL141Etkin null."""
        bl140 = pd.Series([np.nan])
        bl097 = pd.Series([500_000.0])
        bl141e = pd.Series([np.nan])
        result = tx.bl140_etkin(bl140, bl097, bl141e)
        assert result.iloc[0] == 500_000.0

    def test_layer4_pre2018_placeholder_filtered(self):
        """Katman 4: BL097 ≤ 100K (pre-2018 çöp) → null."""
        bl140 = pd.Series([np.nan])
        bl097 = pd.Series([1_000.0])  # placeholder
        bl141e = pd.Series([np.nan])
        result = tx.bl140_etkin(bl140, bl097, bl141e)
        assert pd.isna(result.iloc[0])


# =============================================================================
# İma Edilen Kurlar
# =============================================================================

class TestImpliedFX:
    def test_implied_fx_usd(self):
        """İma Edilen USD/TL = (BL001 / AB.C1) / 1000."""
        bl001 = pd.Series([5_000_000_000.0])  # Bin TL
        ab_c1 = pd.Series([150_000.0])         # Milyon USD
        result = tx.implied_fx_usd(bl001, ab_c1)
        # (5e9 / 150_000) / 1000 = 33.333
        assert abs(result.iloc[0] - 33.333) < 0.01

    def test_implied_gram_altin_tl(self):
        """İma Edilen Gram Altın TL = (BL002 × 1000) / BL0021."""
        bl002 = pd.Series([100_000.0])        # Bin TL
        bl0021 = pd.Series([50_000.0])         # Safi Gram
        result = tx.implied_gram_altin_tl(bl002, bl0021)
        # (100_000 × 1000) / 50_000 = 2000
        assert result.iloc[0] == 2000.0

    def test_zero_denominator_returns_nan(self):
        """0 paydası → NaN."""
        bl001 = pd.Series([5e9])
        ab_c1 = pd.Series([0.0])
        result = tx.implied_fx_usd(bl001, ab_c1)
        assert pd.isna(result.iloc[0])
