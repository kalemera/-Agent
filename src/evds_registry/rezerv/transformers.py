"""Birim dönüşümleri, backfill ve etkin değer hesapları.

v9 Power Query M kodundaki transformer adımları:
- BL142 backfill (M kod satır 1268-1277)
- BL141Etkin (M kod satır 1310-1331)
- BL140Etkin 3-katmanlı fallback (M kod satır 1470-1484)
"""

from __future__ import annotations

import pandas as pd

from .config import (
    BIN_TL_TO_MILYAR_TL,
    BL097_PLACEHOLDER_THRESHOLD,
    GRAM_PER_TROY_OZ,
    MILYON_USD_TO_MILYAR_USD,
)


# =============================================================================
# Birim Dönüşümleri
# =============================================================================

def bin_tl_to_milyar_tl(value: float | pd.Series) -> float | pd.Series:
    """Bin TL → Milyar TL dönüşümü (÷1.000.000)."""
    return value / BIN_TL_TO_MILYAR_TL


def milyon_usd_to_milyar_usd(value: float | pd.Series) -> float | pd.Series:
    """Milyon USD → Milyar USD dönüşümü (÷1000)."""
    return value / MILYON_USD_TO_MILYAR_USD


def gram_to_troy_ons(gram: float | pd.Series) -> float | pd.Series:
    """Safi gram → Troy ons (÷31.1034768)."""
    return gram / GRAM_PER_TROY_OZ


def bin_tl_with_fx_to_milyar_usd(
    bin_tl: pd.Series,
    fx_rate: pd.Series,
) -> pd.Series:
    """Bin TL → Milyar USD = (Bin TL / 1.000.000) / USD/TL.

    fx_rate null veya 0 ise NaN döner (M kod davranışı).
    """
    safe_fx = fx_rate.replace(0, pd.NA)
    return (bin_tl / BIN_TL_TO_MILYAR_TL) / safe_fx


# =============================================================================
# BL142 Backfill — sadece BAŞLANGIÇ yönünde
# =============================================================================

def bl142_backfill(bl142_series: pd.Series) -> pd.Series:
    """BL142'nin ilk geçerli değerini başlangıçtaki null tarihlere yay.

    M kod satır 1268-1277 — yalnızca SERINI BAŞINDAKİ null'lar doldurulur.
    Orta ve son null'lar **dokunulmaz**.
    """
    out = bl142_series.copy()
    first_valid_idx = out.first_valid_index()
    if first_valid_idx is None:
        return out
    first_valid_value = out.loc[first_valid_idx]
    # Sadece başlangıç → first_valid_idx arası null'lar doldurulur
    mask_before = out.index < first_valid_idx
    out.loc[mask_before & out.isna()] = first_valid_value
    return out


# =============================================================================
# BL141 Etkin — Türetilen Fallback
# =============================================================================

def bl141_turetilen(
    bl142_filled: pd.Series,
    implied_gram_altin_tl: pd.Series,
) -> pd.Series:
    """Türetilen BL141 = BL142 (gram) × İmaEdilenGramAltinTL / 1000.

    Birim: Bin TL.
    """
    return (bl142_filled * implied_gram_altin_tl) / 1000.0


def bl141_etkin(bl141_real: pd.Series, bl141_turetilen_val: pd.Series) -> pd.Series:
    """Gerçek BL141 öncelikli; null ise türetilen kullanılır."""
    return bl141_real.fillna(bl141_turetilen_val)


# =============================================================================
# BL140 Etkin — 3-Katmanlı Fallback
# =============================================================================

def bl140_etkin(
    bl140: pd.Series,
    bl097: pd.Series,
    bl141_etkin_val: pd.Series,
    placeholder_threshold: float = BL097_PLACEHOLDER_THRESHOLD,
) -> pd.Series:
    """BL140 etkin değer — 3 katmanlı fallback (M kod 1470-1484).

    Öncelik:
        1. BL140 dolu → BL140
        2. BL097 > eşik AND BL141Etkin var → BL097 - BL141Etkin
        3. BL097 > eşik → BL097
        4. Aksi → null (pre-2018 placeholder filtre)
    """
    out = bl140.copy().astype("float64")

    bl097_ok = bl097.notna() & (bl097 > placeholder_threshold)
    bl141e_ok = bl141_etkin_val.notna()

    # Katman 1: BL140 dolu — out zaten BL140
    layer1_mask = bl140.notna()

    # Katman 2: BL140 null + BL097_ok + BL141Etkin var
    layer2_mask = (~layer1_mask) & bl097_ok & bl141e_ok
    out.loc[layer2_mask] = bl097.loc[layer2_mask] - bl141_etkin_val.loc[layer2_mask]

    # Katman 3: BL140 null + BL097_ok + BL141Etkin null
    layer3_mask = (~layer1_mask) & bl097_ok & (~bl141e_ok)
    out.loc[layer3_mask] = bl097.loc[layer3_mask]

    # Katman 4: pre-2018 placeholder veya hepsi null → NaN (zaten NaN)

    return out


# =============================================================================
# İma Edilen Kurlar (transformer/calculator sınırında — burada tutuyoruz)
# =============================================================================

def implied_fx_usd(bl001_bin_tl: pd.Series, ab_c1_milyon_usd: pd.Series) -> pd.Series:
    """İma Edilen USD/TL = (BL001 / AB.C1) / 1000.

    Birim mantığı: (Bin TL × 1000) / (Milyon USD × 1.000.000) → TL/USD.
    AB.C1 = 0 ise NaN.
    """
    safe_c1 = ab_c1_milyon_usd.replace(0, pd.NA)
    return (bl001_bin_tl / safe_c1) / 1000.0


def implied_gram_altin_tl(
    bl002_bin_tl: pd.Series,
    bl0021_safi_gram: pd.Series,
) -> pd.Series:
    """İma Edilen Gram Altın TL = (BL002 × 1000) / BL0021.

    Birim: TL/gram. BL0021 = 0 → NaN.
    """
    safe_gram = bl0021_safi_gram.replace(0, pd.NA)
    return (bl002_bin_tl * 1000.0) / safe_gram
