"""Doğrulama: Teyit kontrolü ve cut-off mantığı.

v9 M kodundaki teyit sütunu:
    Teyit Farkı = NetAltin + NetDoviz - NIR
    Pre-2018: tolerans uygula (~1.3 mrd USD normal)
    Post-2018: |Fark| ≤ 0.001 Milyar USD
"""

from __future__ import annotations

import datetime as _dt

import pandas as pd

from .config import PRE_2018_TEYIT_TOLERANCE_DATE


def teyit_fark(
    net_altin_usd: pd.Series,
    net_doviz_usd: pd.Series,
    nir_usd: pd.Series,
    decimals: int = 6,
) -> pd.Series:
    """NetAltin + NetDoviz - NIR farkı (Milyar USD)."""
    fark = (net_altin_usd + net_doviz_usd - nir_usd).round(decimals)
    return fark


def teyit_flag(
    teyit_fark_val: pd.Series,
    index: pd.DatetimeIndex,
    tolerance: float = 0.001,
    cutoff: _dt.date = PRE_2018_TEYIT_TOLERANCE_DATE,
) -> pd.Series:
    """Teyit flag: True (doğru), False (sapma), None (pre-2018 tolerans).

    Pre-2018 için flag null döner (BL085 içinde altın teminat karışık).
    """
    cutoff_ts = pd.Timestamp(cutoff)
    flag = pd.Series(index=index, dtype="object")

    valid_mask = teyit_fark_val.notna()
    pre_mask = (index < cutoff_ts) & valid_mask
    post_mask = (index >= cutoff_ts) & valid_mask

    # Pre-2018: null
    flag.loc[pre_mask] = None
    # Post-2018: tolerans kontrolü
    flag.loc[post_mask] = teyit_fark_val.loc[post_mask].abs() <= tolerance

    return flag


def detect_missing_business_dates(
    index: pd.DatetimeIndex,
    expected_freq: str = "B",
) -> list[pd.Timestamp]:
    """Beklenen iş günü frekansındaki eksik tarihleri tespit eder.

    M kodundaki hardcoded 20.03.2026 patch'inin dinamik karşılığı.
    """
    if len(index) == 0:
        return []
    expected = pd.date_range(index.min(), index.max(), freq=expected_freq)
    missing = expected.difference(index)
    return list(missing)


def patch_missing_dates(
    df: pd.DataFrame,
    expected_freq: str = "B",
) -> tuple[pd.DataFrame, list[pd.Timestamp]]:
    """Eksik iş günlerini önceki gün verisi ile doldur.

    Returns:
        (patched_df, patched_dates_list) — uygulanan tarih listesi rapor için.
    """
    missing_dates = detect_missing_business_dates(df.index, expected_freq)
    if not missing_dates:
        return df, []

    patched_rows = []
    patched_dates = []
    for missing_date in missing_dates:
        prior_idx = df.index[df.index < missing_date]
        if len(prior_idx) == 0:
            continue
        prior_date = prior_idx.max()
        new_row = df.loc[prior_date].copy()
        new_row.name = missing_date
        patched_rows.append(new_row)
        patched_dates.append(missing_date)

    if not patched_rows:
        return df, []

    patched_df = pd.concat([df, pd.concat(patched_rows, axis=1).T])
    patched_df = patched_df.sort_index()
    return patched_df, patched_dates
