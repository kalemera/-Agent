"""TCMB Rezerv Pipeline — Ana orchestrator.

run_pipeline() — fetcher → transformer → calculator → validator zincirini
çalıştırır ve RezervSnapshot döner.

Akış:
    1) Validator pre-step: patch_missing_dates (günlük bilanço için)
    2) Transformer: BL142 backfill, ImpliedFX/Altın, BL141Etkin, BL140Etkin
    3) Calculator: Standby, Brüt URDL, NetAltın/Döviz, Swap, SH, Bilanço
    4) Validator: TeyitFark, TeyitFlag
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd

from . import calculators as calc
from . import transformers as tx
from . import validators as val

PIPELINE_VERSION = "v9.1.0"


@dataclass
class RezervSnapshot:
    """Pipeline çıktısı — tüm akış aşamaları tek nesnede."""

    raw: pd.DataFrame
    """Ham EVDS verisi (Bin TL / Milyon USD birimleri)."""

    transformed: pd.DataFrame
    """Etkin değerler, backfill uygulanmış, kur dönüşümleri yapılmış."""

    calculated: pd.DataFrame
    """Hesaplanmış indicator'lar — Net Altın, Net Döviz, SH NUR, vb."""

    validation: pd.DataFrame
    """Teyit sütunları, flagler, hata kayıtları."""

    metadata: dict[str, Any] = field(default_factory=dict)
    """Snapshot metadata: kaynak tarih, patched dates, pipeline version, vs."""

    @property
    def latest(self) -> pd.Series:
        """En son tarih değerleri (calculated frame'in son satırı)."""
        if self.calculated.empty:
            return pd.Series(dtype="float64")
        return self.calculated.iloc[-1]

    def get_indicator(self, name: str) -> pd.Series:
        """Hesaplanmış bir indicator'u getir (örn 'NetAltinUSD', 'SHNetRezervGunluk')."""
        if name not in self.calculated.columns:
            raise KeyError(f"Indicator '{name}' bulunamadı.")
        return self.calculated[name]


# =============================================================================
# Yardımcılar
# =============================================================================

def _empty_series(index: pd.Index) -> pd.Series:
    """Index'e uyumlu, dtype=float64 boş seri."""
    return pd.Series(index=index, dtype="float64")


def _has_cols(df: pd.DataFrame, cols: list[str]) -> bool:
    """Tüm sütunlar mevcut mu?"""
    return all(c in df.columns for c in cols)


def _align_optional(
    raw_optional: pd.DataFrame | None,
    target_index: pd.DatetimeIndex,
    column_keywords_map: dict[str, list[str]],
    extractor,
) -> dict[str, pd.Series]:
    """Opsiyonel kaynaklardan (URDL/PDF) seri çıkar ve target index'e hizala.

    Args:
        raw_optional: opsiyonel ham veri (None olabilir)
        target_index: hedeflenen index (calculated frame'in indexi)
        column_keywords_map: {output_name: [keyword1, ...]}
        extractor: çıkarıcı fonksiyon (urdl için urdl_extract_kalem_series gibi)

    Returns:
        {output_name: pd.Series (target_index'e reindex edilmiş)} — yoksa None
    """
    out: dict[str, pd.Series] = {}
    if raw_optional is None or raw_optional.empty:
        return out
    for name, keywords in column_keywords_map.items():
        try:
            df_extracted = extractor(raw_optional, keywords, output_name=name)
        except Exception:
            continue
        if df_extracted.empty or name not in df_extracted.columns:
            continue
        # Target index'e reindex (forward fill — haftalık/aylık veri günlük index'e)
        series = df_extracted[name].reindex(target_index, method="ffill")
        out[name] = series
    return out


def _extract_pdf_series(
    raw_pdf: pd.DataFrame,
    target_index: pd.DatetimeIndex,
) -> dict[str, pd.Series]:
    """PDF wide DataFrame'den FX/Altın swap kalemlerini çıkar."""
    out: dict[str, pd.Series] = {}
    if raw_pdf is None or raw_pdf.empty:
        return out

    # PDF index'i Tarih datetime olmalı (fetch_tarafli_swap_pdf böyle döner)
    candidates = {
        "PDFFXSwap": "Tcmb Günlük Döviz Swap Net Alım (Milyar USD)",
        "PDFAltinSwap": "Tcmb Günlük Altın Swap Net Alım (Milyar USD)",
    }
    for out_name, col_name in candidates.items():
        if col_name in raw_pdf.columns:
            series = raw_pdf[col_name]
            if not isinstance(series.index, pd.DatetimeIndex):
                continue
            # Günlük index'e reindex (ffill — PDF gün-içi yayın atlar)
            out[out_name] = series.reindex(target_index, method="ffill")
    return out


# =============================================================================
# Ana Pipeline
# =============================================================================

def run_pipeline(
    raw_evds: pd.DataFrame,
    raw_urdl: pd.DataFrame | None = None,
    raw_pdf: pd.DataFrame | None = None,
) -> RezervSnapshot:
    """Tüm rezerv pipeline'ını çalıştır.

    Args:
        raw_evds: EVDS API'den çekilmiş seriler (51 sütun, sütun adları kısa form)
        raw_urdl: URDL ZIP'ten haftalık swap kalemleri (opsiyonel, wide format)
        raw_pdf: PDF'ten günlük swap detayı (opsiyonel, Tarih index'li)

    Returns:
        RezervSnapshot — tüm akış aşamalarının çıktısı
    """
    metadata: dict[str, Any] = {
        "pipeline_version": PIPELINE_VERSION,
        "urdl_used": raw_urdl is not None and not (raw_urdl.empty if isinstance(raw_urdl, pd.DataFrame) else True),
        "pdf_used": raw_pdf is not None and not (raw_pdf.empty if isinstance(raw_pdf, pd.DataFrame) else True),
        "patched_dates": [],
    }

    # =====================================================================
    # 0) PRE-VALIDATE — Eksik iş günü patch'i (sentetik bilanço için)
    # =====================================================================
    # Günlük bilanço sütunları varsa (AB.A02 gibi), eksik iş günlerini doldur
    daily_cols = [c for c in ["AB.A02", "AB.A11", "AB.A14", "AB.A13"] if c in raw_evds.columns]
    if daily_cols and isinstance(raw_evds.index, pd.DatetimeIndex):
        try:
            patched_df, patched_dates = val.patch_missing_dates(raw_evds, expected_freq="B")
            if patched_dates:
                raw_evds = patched_df
                metadata["patched_dates"] = [pd.Timestamp(d).strftime("%Y-%m-%d") for d in patched_dates]
        except Exception:
            # Patch fail → orijinalle devam (defensive)
            pass

    # =====================================================================
    # 1) TRANSFORM
    # =====================================================================
    transformed = raw_evds.copy()

    # BL142 backfill
    if "BL142" in transformed.columns:
        transformed = transformed.assign(
            BL142_filled=tx.bl142_backfill(transformed["BL142"])
        )

    # İma Edilen kurlar (BL001 ve AB.C1 yoksa null seri)
    if _has_cols(transformed, ["BL001", "AB.C1"]):
        implied_fx = tx.implied_fx_usd(transformed["BL001"], transformed["AB.C1"])
    else:
        implied_fx = _empty_series(transformed.index)
    transformed = transformed.assign(ImpliedFX=implied_fx)

    if _has_cols(transformed, ["BL002", "BL0021"]):
        implied_gram_altin = tx.implied_gram_altin_tl(
            transformed["BL002"], transformed["BL0021"]
        )
    else:
        implied_gram_altin = _empty_series(transformed.index)
    transformed = transformed.assign(ImpliedGramAltinTL=implied_gram_altin)

    # BL141 etkin
    if _has_cols(transformed, ["BL141", "BL142_filled"]):
        bl141_t = tx.bl141_turetilen(
            transformed["BL142_filled"], transformed["ImpliedGramAltinTL"]
        )
        transformed = transformed.assign(
            BL141_Etkin=tx.bl141_etkin(transformed["BL141"], bl141_t)
        )
    else:
        transformed = transformed.assign(BL141_Etkin=_empty_series(transformed.index))

    # BL140 etkin (3-katmanlı)
    if _has_cols(transformed, ["BL140", "BL097"]):
        transformed = transformed.assign(
            BL140_Etkin=tx.bl140_etkin(
                transformed["BL140"],
                transformed["BL097"],
                transformed["BL141_Etkin"],
            )
        )
    else:
        transformed = transformed.assign(BL140_Etkin=_empty_series(transformed.index))

    # =====================================================================
    # 2) CALCULATE
    # =====================================================================
    calculated = pd.DataFrame(index=transformed.index)
    idx = transformed.index

    # ---- Standby Kalıntısı ----
    if _has_cols(transformed, ["AB.N07", "BL001", "BL003", "BL004", "BL008"]):
        calculated["StandbyKalintisi"] = calc.standby_kalintisi(
            transformed["AB.N07"],
            transformed["BL001"],
            transformed["BL003"],
            transformed["BL004"],
            transformed["BL008"],
        )
    else:
        calculated["StandbyKalintisi"] = _empty_series(idx)

    # ---- Brüt Rezerv URDL ----
    if _has_cols(transformed, ["BL001", "BL003", "BL004", "BL008"]):
        calculated["BrutRezervTL_URDL"] = calc.brut_rezerv_tl_urdl(
            transformed["BL001"],
            transformed["BL003"],
            transformed["BL004"],
            transformed["BL008"],
        )
    else:
        calculated["BrutRezervTL_URDL"] = _empty_series(idx)

    # ---- Döviz Rezerv URDL ----
    if _has_cols(transformed, ["BL003", "BL004", "BL008"]):
        calculated["DovizRezervTL_URDL"] = calc.doviz_rezervi_tl_urdl(
            transformed["BL003"],
            transformed["BL004"],
            transformed["BL008"],
        )
    else:
        calculated["DovizRezervTL_URDL"] = _empty_series(idx)

    # ---- Net Altın ----
    if _has_cols(transformed, ["BL002", "BL132", "BL136", "BL089", "BL141_Etkin"]):
        calculated["NetAltinAra_BinTL"] = calc.net_altin_ara_bin_tl(
            transformed["BL002"],
            transformed["BL132"],
            transformed["BL136"],
            transformed["BL089"],
            transformed["BL141_Etkin"],
        )
        calculated["NetAltinUSD"] = calc.net_altin_milyar_usd(
            calculated["NetAltinAra_BinTL"], transformed["ImpliedFX"]
        )
    else:
        calculated["NetAltinAra_BinTL"] = _empty_series(idx)
        calculated["NetAltinUSD"] = _empty_series(idx)

    # ---- Net Döviz ----
    net_doviz_required = [
        "BL003", "BL004", "BL008", "BL085", "BL129", "BL131",
        "BL086", "BL088", "BL090", "BL092", "BL093", "BL099", "BL117", "BL118",
    ]
    if _has_cols(transformed, net_doviz_required) and isinstance(idx, pd.DatetimeIndex):
        calculated["NetDovizAra_BinTL"] = calc.net_doviz_ara_bin_tl(
            transformed,
            calculated["StandbyKalintisi"],
            transformed["BL140_Etkin"],
        )
        calculated["NetDovizUSD"] = calc.net_doviz_milyar_usd(
            calculated["NetDovizAra_BinTL"], transformed["ImpliedFX"]
        )
    else:
        calculated["NetDovizAra_BinTL"] = _empty_series(idx)
        calculated["NetDovizUSD"] = _empty_series(idx)

    # ---- NIR (Milyar USD) — AB.N06 (Bin TL) / 1M / FX ----
    if "AB.N06" in transformed.columns and "ImpliedFX" in transformed.columns:
        safe_fx = transformed["ImpliedFX"].replace(0, pd.NA)
        calculated["NIRUSD"] = (transformed["AB.N06"] / 1_000_000.0) / safe_fx
    else:
        calculated["NIRUSD"] = _empty_series(idx)

    # ---- MB Swap Toplam (raw_evds K18 + K22) ----
    if _has_cols(transformed, ["DOVVARNC.K18", "DOVVARNC.K22"]):
        calculated["MBSwapToplam"] = calc.mb_swap_toplam(
            transformed["DOVVARNC.K18"],
            transformed["DOVVARNC.K22"],
        )
    else:
        calculated["MBSwapToplam"] = _empty_series(idx)

    # ---- URDL Swap Kalemleri (raw_urdl varsa) ----
    # Excel M kodu (TcmbHaftalikRezerv satır 1707-1755) ile birebir uyumlu:
    #   MBSwap   = II.2.a.iii (Açık, 4ay-1yıl)   + II.2.b.iii (Fazla, 4ay-1yıl)
    #   SwapTot  = II.2 (Forward future swap toplam) — exact match prefer
    #   DigerSwap = II.3 ana satır (Diğer)
    urdl_series: dict[str, pd.Series] = {}
    if raw_urdl is not None and not raw_urdl.empty:
        try:
            from .fetchers import urdl_extract_kalem_series, urdl_extract_kalem_sum

            # MBSwapURDL — II.2.a.iii + II.2.b.iii toplamı (M kod satır 1707-1712)
            mb_df = urdl_extract_kalem_sum(
                raw_urdl,
                [["II.2.a.iii"], ["II.2.b.iii"]],
                output_name="MBSwapURDL",
            )
            if not mb_df.empty:
                urdl_series["MBSwapURDL"] = (
                    mb_df["MBSwapURDL"].reindex(idx, method="ffill")
                )

            # SwapTotURDL — "II.2." satırı (toplam forward/future/swap)
            tot_df = urdl_extract_kalem_series(
                raw_urdl, ["II.2."], output_name="SwapTotURDL"
            )
            if not tot_df.empty:
                urdl_series["SwapTotURDL"] = (
                    tot_df["SwapTotURDL"].reindex(idx, method="ffill")
                )

            # DigerSwapURDL — "II.3" ana satırı (Diğer)
            diger_df = urdl_extract_kalem_series(
                raw_urdl, ["II.3 "], output_name="DigerSwapURDL"
            )
            if not diger_df.empty:
                urdl_series["DigerSwapURDL"] = (
                    diger_df["DigerSwapURDL"].reindex(idx, method="ffill")
                )
        except Exception:
            urdl_series = {}
    calculated["MBSwapURDL"] = urdl_series.get("MBSwapURDL", _empty_series(idx))
    calculated["DigerSwapURDL"] = urdl_series.get("DigerSwapURDL", _empty_series(idx))
    calculated["SwapTotURDL"] = urdl_series.get("SwapTotURDL", _empty_series(idx))

    # ---- PDF Swap Kalemleri (raw_pdf varsa) ----
    pdf_series: dict[str, pd.Series] = {}
    if raw_pdf is not None and not raw_pdf.empty:
        pdf_series = _extract_pdf_series(raw_pdf, idx)
    calculated["PDFFXSwap"] = pdf_series.get("PDFFXSwap", _empty_series(idx))
    calculated["PDFAltinSwap"] = pdf_series.get("PDFAltinSwap", _empty_series(idx))

    # ---- Swap Hariç Net Altın (PDF öncelikli, URDL fallback) ----
    pdf_altin_input = calculated["PDFAltinSwap"] if pdf_series else None
    urdl_diger_input = calculated["DigerSwapURDL"] if urdl_series else None
    calculated["SHNetAltin"] = calc.swap_haric_net_altin(
        calculated["NetAltinUSD"],
        pdf_altin_input,
        urdl_diger_input,
    )

    # ---- Swap Hariç Net Döviz ----
    pdf_fx_input = calculated["PDFFXSwap"] if pdf_series else None
    if urdl_series:
        calculated["SHNetDoviz"] = calc.swap_haric_net_doviz(
            calculated["NetDovizUSD"],
            calculated["MBSwapURDL"],
            calculated["SwapTotURDL"],
            pdf_fx_input,
        )
    else:
        # URDL yoksa: NetDoviz - PDF (PDF varsa), yoksa NetDoviz
        if pdf_fx_input is not None:
            shd = calculated["NetDovizUSD"] - pdf_fx_input.fillna(0)
            shd.loc[calculated["NetDovizUSD"].isna()] = pd.NA
            calculated["SHNetDoviz"] = shd
        else:
            calculated["SHNetDoviz"] = calculated["NetDovizUSD"].copy()

    # ---- SH Net Rezerv (Günlük) = SHNetAltin + SHNetDoviz ----
    calculated["SHNetRezervGunluk"] = calc.swap_haric_net_rezerv_gunluk(
        calculated["SHNetAltin"],
        calculated["SHNetDoviz"],
    )

    # ---- SH Net Rezerv (URDL) = NIR + SwapTot + Diger ----
    if urdl_series and not calculated["NIRUSD"].isna().all():
        calculated["SHNetRezervURDL"] = calc.swap_haric_net_rezerv_urdl(
            calculated["NIRUSD"],
            calculated["SwapTotURDL"].fillna(0),
            calculated["DigerSwapURDL"].fillna(0),
        )
    else:
        calculated["SHNetRezervURDL"] = _empty_series(idx)

    # ---- Bilanço Net Döviz Pozisyonu (günlük, A02 - A11 - A14 - A13) ----
    bilanco_required = ["AB.A02", "AB.A11", "AB.A14", "AB.A13", "DK.USD.A.YTL"]
    if _has_cols(transformed, bilanco_required):
        calculated["BilancoNetDovizPozisyonu"] = calc.bilanco_net_doviz_pozisyonu(
            transformed["AB.A02"],
            transformed["AB.A11"],
            transformed["AB.A14"],
            transformed["AB.A13"],
            transformed["DK.USD.A.YTL"],
        )
    else:
        calculated["BilancoNetDovizPozisyonu"] = _empty_series(idx)

    # ---- Bilanço Tahmini Net Rezerv (A13 hariç) ----
    if _has_cols(transformed, ["AB.A02", "AB.A11", "AB.A14", "DK.USD.A.YTL"]):
        calculated["BilancoTahminiNetRezerv"] = calc.bilanco_tahmini_net_rezerv(
            transformed["AB.A02"],
            transformed["AB.A11"],
            transformed["AB.A14"],
            transformed["DK.USD.A.YTL"],
        )
    else:
        calculated["BilancoTahminiNetRezerv"] = _empty_series(idx)

    # =====================================================================
    # 3) VALIDATE
    # =====================================================================
    validation = pd.DataFrame(index=transformed.index)

    if not calculated["NIRUSD"].isna().all():
        validation["TeyitFark"] = val.teyit_fark(
            calculated["NetAltinUSD"],
            calculated["NetDovizUSD"],
            calculated["NIRUSD"],
        )
        if isinstance(transformed.index, pd.DatetimeIndex):
            validation["TeyitFlag"] = val.teyit_flag(
                validation["TeyitFark"], transformed.index
            )
        else:
            validation["TeyitFlag"] = pd.Series(index=transformed.index, dtype="object")

    # Anchor sütun(lar) — NetAltinUSD veya NetDovizUSD dolu olan satırlar
    # "gerçek haftalık vaziyet verisi" olduğunu gösterir. patch_missing_dates()
    # sentetik tarihlerinde bunlar NaN — calculated'dan elenmesi gerek ki
    # agent latest='son anlamlı tarih' olsun.
    anchor_cols = [c for c in ("NetAltinUSD", "NetDovizUSD") if c in calculated.columns]
    if anchor_cols and not calculated.empty:
        valid_mask = calculated[anchor_cols].notna().any(axis=1)
        calculated = calculated[valid_mask]
    if not validation.empty:
        validation = validation.loc[validation.index.intersection(calculated.index)]

    return RezervSnapshot(
        raw=raw_evds,
        transformed=transformed,
        calculated=calculated,
        validation=validation,
        metadata=metadata,
    )
