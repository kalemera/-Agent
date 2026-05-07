"""Türev hesap fonksiyonları.

Net Altın, Net Döviz, Standby Kalıntısı, SH Net Rezerv ve günlük bilanço
tahminleri. v9 Excel M kodundaki hesap mantığının Python karşılığı.
"""

from __future__ import annotations

import datetime as _dt

import pandas as pd

from .config import YIBANK_FALLBACK_CUTOFF


# =============================================================================
# Standby Kalıntısı
# =============================================================================

def standby_kalintisi(
    n07: pd.Series,
    bl001: pd.Series,
    bl003: pd.Series,
    bl004: pd.Series,
    bl008: pd.Series,
) -> pd.Series:
    """Standby Kalıntısı = N07 - (BL001 + BL003 + BL004 + BL008).

    Birim: Bin TL. Bileşenlerden biri null ise null sayılır.
    """
    bilesen = bl001.add(bl003, fill_value=0).add(bl004, fill_value=0).add(bl008, fill_value=0)
    # En az bir bileşen yoksa null mantığı
    valid_mask = bl001.notna() | bl003.notna() | bl004.notna() | bl008.notna()
    out = n07 - bilesen
    out.loc[~valid_mask] = pd.NA
    out.loc[n07.isna()] = pd.NA
    return out


# =============================================================================
# Brüt Rezerv (URDL alternatif yolu, Milyar TL)
# =============================================================================

def brut_rezerv_tl_urdl(
    bl001: pd.Series,
    bl003: pd.Series,
    bl004: pd.Series,
    bl008: pd.Series,
) -> pd.Series:
    """Brüt Rezerv (Milyar TL) = (BL001 + BL003 + BL004 + BL008) / 1.000.000."""
    toplam = bl001.add(bl003, fill_value=0).add(bl004, fill_value=0).add(bl008, fill_value=0)
    return toplam / 1_000_000.0


def doviz_rezervi_tl_urdl(
    bl003: pd.Series,
    bl004: pd.Series,
    bl008: pd.Series,
) -> pd.Series:
    """Döviz Rezervi (Milyar TL) = (BL003 + BL004 + BL008) / 1.000.000."""
    toplam = bl003.add(bl004, fill_value=0).add(bl008, fill_value=0)
    return toplam / 1_000_000.0


# =============================================================================
# Net Altın Rezervi
# =============================================================================

def net_altin_ara_bin_tl(
    bl002: pd.Series,
    bl132: pd.Series,
    bl136: pd.Series,
    bl089: pd.Series,
    bl141_etkin: pd.Series,
) -> pd.Series:
    """Net Altın Ara (Bin TL) = BL002 - (BL132 + BL136 + BL089 + BL141Etkin).

    BL002 null ise null. Yükümlülükler null ise 0 olarak toplanır.
    """
    yuk = (
        bl132.fillna(0)
        + bl136.fillna(0)
        + bl089.fillna(0)
        + bl141_etkin.fillna(0)
    )
    out = bl002 - yuk
    out.loc[bl002.isna()] = pd.NA
    return out


def net_altin_milyar_usd(
    net_altin_ara: pd.Series,
    implied_fx: pd.Series,
) -> pd.Series:
    """Net Altın (Milyar USD) = (Ara/1.000.000) / İmaEdilenUSDTL."""
    safe_fx = implied_fx.replace(0, pd.NA)
    return (net_altin_ara / 1_000_000.0) / safe_fx


# =============================================================================
# Net Döviz Rezervi (pre-2018 fallback dahil)
# =============================================================================

def yibank_with_pre2018_fallback(
    df: pd.DataFrame,
    cutoff: _dt.date = YIBANK_FALLBACK_CUTOFF,
) -> pd.Series:
    """yiBank kalemi — Pre-2018 BL085, post-2018 BL129+BL131.

    df.index pd.DatetimeIndex olmalı. Sütunlar: BL085, BL129, BL131.
    """
    cutoff_ts = pd.Timestamp(cutoff)
    pre_mask = df.index < cutoff_ts

    yibank = pd.Series(index=df.index, dtype="float64")
    # Pre-2018: BL085
    yibank.loc[pre_mask] = df.loc[pre_mask, "BL085"]
    # Post-2018: BL129 + BL131
    bl129 = df.loc[~pre_mask, "BL129"].fillna(0)
    bl131 = df.loc[~pre_mask, "BL131"].fillna(0)
    yibank.loc[~pre_mask] = bl129 + bl131
    return yibank


def net_doviz_ara_bin_tl(
    df: pd.DataFrame,
    standby_kal: pd.Series,
    bl140_etkin_val: pd.Series,
    cutoff: _dt.date = YIBANK_FALLBACK_CUTOFF,
) -> pd.Series:
    """Net Döviz Ara (Bin TL) = Varlık - Yükümlülük.

    df sütunları: BL003, BL004, BL008, BL085, BL129, BL131, BL086, BL088,
                  BL090, BL092, BL093, BL099, BL117, BL118
    """
    # Varlık
    varlik = (
        df["BL003"].fillna(0)
        + df["BL004"].fillna(0)
        + df["BL008"].fillna(0)
        + standby_kal.fillna(0)
    )

    # Yükümlülük
    yibank = yibank_with_pre2018_fallback(df, cutoff)
    yuk = (
        yibank.fillna(0)
        + df["BL086"].fillna(0)
        + df["BL088"].fillna(0)
        + df["BL090"].fillna(0)
        + df["BL092"].fillna(0)
        + df["BL093"].fillna(0)
        + bl140_etkin_val.fillna(0)
        + df["BL099"].fillna(0)
        + df["BL117"].fillna(0)
        + df["BL118"].fillna(0)
    )

    # En az bir varlık kalemi dolu olmalı
    valid_mask = (
        df["BL003"].notna() | df["BL004"].notna() | df["BL008"].notna()
    )
    out = varlik - yuk
    out.loc[~valid_mask] = pd.NA
    return out


def net_doviz_milyar_usd(
    net_doviz_ara: pd.Series,
    implied_fx: pd.Series,
) -> pd.Series:
    """Net Döviz (Milyar USD) = (Ara/1.000.000) / İmaEdilenUSDTL."""
    safe_fx = implied_fx.replace(0, pd.NA)
    return (net_doviz_ara / 1_000_000.0) / safe_fx


# =============================================================================
# Swap Hariç Net Altın
# =============================================================================

def swap_haric_net_altin(
    net_altin_usd: pd.Series,
    pdf_altin_swap: pd.Series | None,
    diger_swap_urdl: pd.Series | None,
) -> pd.Series:
    """SH Net Altın — PDF öncelikli, URDL fallback.

    İşaret kuralı:
        PDF: pozitif → çıkarma
        URDL: negatif → toplama (kavramsal olarak aynı düzeltme)
    """
    out = net_altin_usd.copy()
    if pdf_altin_swap is not None:
        # Mevcut PDF değerleri için: NetAltin - PDF
        pdf_mask = pdf_altin_swap.notna()
        out.loc[pdf_mask] = net_altin_usd.loc[pdf_mask] - pdf_altin_swap.loc[pdf_mask]
        # PDF eksik ama URDL varsa fallback
        if diger_swap_urdl is not None:
            urdl_mask = (~pdf_mask) & diger_swap_urdl.notna()
            out.loc[urdl_mask] = (
                net_altin_usd.loc[urdl_mask] + diger_swap_urdl.loc[urdl_mask]
            )
    elif diger_swap_urdl is not None:
        urdl_mask = diger_swap_urdl.notna()
        out.loc[urdl_mask] = (
            net_altin_usd.loc[urdl_mask] + diger_swap_urdl.loc[urdl_mask]
        )
    # NetAltin null olan satırlarda out null kalır
    out.loc[net_altin_usd.isna()] = pd.NA
    return out


# =============================================================================
# Swap Hariç Net Döviz
# =============================================================================

def swap_haric_net_doviz(
    net_doviz_usd: pd.Series,
    mb_swap_urdl: pd.Series,
    swap_tot_urdl: pd.Series,
    pdf_fx_swap: pd.Series | None,
) -> pd.Series:
    """SH Net Döviz — M.B. her zaman URDL, non-MB PDF/URDL fallback.

    PDF varsa:  NetDoviz + mbAdj - PDF
    PDF yok:    NetDoviz + mbAdj + (SwapTot - mbAdj)   (URDL fallback)
    """
    mb_adj = mb_swap_urdl.fillna(0)
    out = net_doviz_usd + mb_adj

    if pdf_fx_swap is not None:
        pdf_mask = pdf_fx_swap.notna()
        out.loc[pdf_mask] = out.loc[pdf_mask] - pdf_fx_swap.loc[pdf_mask]
        # PDF yoksa URDL fallback
        urdl_fallback = swap_tot_urdl.fillna(0) - mb_adj
        out.loc[~pdf_mask] = out.loc[~pdf_mask] + urdl_fallback.loc[~pdf_mask]
    else:
        # Tamamı URDL fallback
        urdl_fallback = swap_tot_urdl.fillna(0) - mb_adj
        out = out + urdl_fallback

    out.loc[net_doviz_usd.isna()] = pd.NA
    return out


def swap_haric_net_rezerv_gunluk(
    sh_net_altin: pd.Series,
    sh_net_doviz: pd.Series,
) -> pd.Series:
    """SH Net Rezerv (Günlük) = SH Net Altın + SH Net Döviz."""
    out = sh_net_altin + sh_net_doviz
    return out


def swap_haric_net_rezerv_urdl(
    nir: pd.Series,
    swap_toplam_urdl: pd.Series,
    diger_swap_urdl: pd.Series,
) -> pd.Series:
    """SH Net Rezerv (URDL) = NIR + SwapToplam + DigerSwap.

    URDL işaret kuralı: tüm swap'lar negatif → toplama düzeltir.
    """
    out = nir + swap_toplam_urdl + diger_swap_urdl
    return out


# =============================================================================
# MB Swap Toplam (URDL aylık)
# =============================================================================

def mb_swap_toplam(k18: pd.Series, k22: pd.Series) -> pd.Series:
    """M.B. Swap Toplam = K18 (Açık) + K22 (Fazla)."""
    return k18.fillna(0) + k22.fillna(0)


# =============================================================================
# Günlük Bilanço Tahminleri
# =============================================================================

def bilanco_net_doviz_pozisyonu(
    a02: pd.Series,
    a11: pd.Series,
    a14: pd.Series,
    a13: pd.Series,
    fx_rate: pd.Series,
) -> pd.Series:
    """Net Döviz Pozisyonu (Milyar USD) = (A02 - A11 - A14 - A13)/1M / FX.

    Birim: Bin TL → Milyar USD.
    """
    safe_fx = fx_rate.replace(0, pd.NA)
    bin_tl = a02 - a11 - a14 - a13
    return (bin_tl / 1_000_000.0) / safe_fx


def bilanco_tahmini_net_rezerv(
    a02: pd.Series,
    a11: pd.Series,
    a14: pd.Series,
    fx_rate: pd.Series,
) -> pd.Series:
    """Tahmini Net Rezerv (Milyar USD) = (A02 - A11 - A14)/1M / FX.

    Kamu mevduat (A13) hariç; bilanço-bazlı günlük proxy.
    """
    safe_fx = fx_rate.replace(0, pd.NA)
    bin_tl = a02 - a11 - a14
    return (bin_tl / 1_000_000.0) / safe_fx
