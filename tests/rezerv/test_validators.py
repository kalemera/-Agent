"""Validator modülü testleri.

Teyit kontrolü, pre-2018 tolerans, eksik tarih patch'i.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from evds_registry.rezerv import validators as val


# =============================================================================
# Teyit Kontrol
# =============================================================================

class TestTeyitFark:
    def test_basic(self):
        net_altin = pd.Series([10.0, 20.0])
        net_doviz = pd.Series([15.0, 25.0])
        nir = pd.Series([25.0, 45.0])
        result = val.teyit_fark(net_altin, net_doviz, nir)
        assert result.iloc[0] == 0.0
        assert result.iloc[1] == 0.0

    def test_with_deviation(self):
        net_altin = pd.Series([10.0])
        net_doviz = pd.Series([15.0])
        nir = pd.Series([24.5])
        result = val.teyit_fark(net_altin, net_doviz, nir)
        # 10 + 15 - 24.5 = 0.5
        assert abs(result.iloc[0] - 0.5) < 1e-9


class TestTeyitFlag:
    def test_post_2018_within_tolerance(self):
        idx = pd.DatetimeIndex(["2025-12-26"])
        fark = pd.Series([0.0005], index=idx)
        flag = val.teyit_flag(fark, idx)
        assert flag.iloc[0] is True or flag.iloc[0] == True  # noqa: E712

    def test_post_2018_outside_tolerance(self):
        idx = pd.DatetimeIndex(["2025-12-26"])
        fark = pd.Series([1.5], index=idx)
        flag = val.teyit_flag(fark, idx)
        assert flag.iloc[0] is False or flag.iloc[0] == False  # noqa: E712

    def test_pre_2018_returns_null(self):
        """Pre-2018 tarihlerde flag null döner."""
        idx = pd.DatetimeIndex(["2017-06-15"])
        fark = pd.Series([1.3], index=idx)  # büyük sapma normal
        flag = val.teyit_flag(fark, idx)
        assert flag.iloc[0] is None

    def test_null_fark_returns_null(self):
        idx = pd.DatetimeIndex(["2025-12-26"])
        fark = pd.Series([np.nan], index=idx)
        flag = val.teyit_flag(fark, idx)
        assert flag.iloc[0] is None or pd.isna(flag.iloc[0])


# =============================================================================
# Eksik Tarih Patch'i
# =============================================================================

class TestPatchMissingDates:
    def test_no_missing(self):
        """Tüm iş günleri dolu → değişiklik yok."""
        idx = pd.bdate_range("2026-04-21", "2026-04-23")
        df = pd.DataFrame({"x": [1.0, 2.0, 3.0]}, index=idx)
        patched, dates = val.patch_missing_dates(df)
        assert len(dates) == 0
        pd.testing.assert_frame_equal(patched, df)

    def test_single_missing_day(self):
        """Bir iş günü eksikse önceki günden kopyalanır."""
        idx = pd.DatetimeIndex(["2026-04-21", "2026-04-23"])  # 22 atlanmış
        df = pd.DataFrame({"x": [10.0, 30.0]}, index=idx)
        patched, dates = val.patch_missing_dates(df)
        assert len(dates) == 1
        assert pd.Timestamp("2026-04-22") in dates
        # 22 değeri 21'den kopya olmalı
        assert patched.loc["2026-04-22", "x"] == 10.0

    def test_no_prior_data_skipped(self):
        """Eksik tarih ilk günden önce ise skip edilir (önceki yok)."""
        idx = pd.DatetimeIndex(["2026-04-21"])
        df = pd.DataFrame({"x": [10.0]}, index=idx)
        patched, dates = val.patch_missing_dates(df)
        # Tek tarih → eksik tarih yok
        assert len(dates) == 0
