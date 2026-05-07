"""Sabit listeler ve tarih cut-off'ları.

v9 Excel Power Query M kodundaki tüm sabitlerin merkezi yer tutucu.
"""

from __future__ import annotations

import datetime as _dt
from typing import Final

# =============================================================================
# EVDS Series — 51 ticker
# =============================================================================

# Günlük analitik bilanço (TcmbGunlukBilanco)
DAILY_BILANCO_TICKERS: Final[list[str]] = [
    "TP.AB.A02",          # Dış Varlıklar
    "TP.AB.A11",          # Dış Yükümlülükler
    "TP.AB.A14",          # Bankalar Döviz Mevduatı
    "TP.AB.A13",          # Kamu ve Diğer Döviz Mevduatı
    "TP.DK.USD.A.YTL",    # USD/TL Alış Kuru
]

# Haftalık vaziyet (TcmbHaftalikRezerv) — 31 ticker
WEEKLY_VAZIYET_TICKERS: Final[list[str]] = [
    # Resmi rezerv özet
    "TP.AB.TOPLAM",       # Brüt Rezerv (Milyon USD)
    "TP.AB.C1",           # Brüt Altın (Milyon USD)
    "TP.AB.C2",           # Brüt Döviz (Milyon USD)
    "TP.AB.N06",          # NIR (Bin TL)
    "TP.AB.N07",          # Brüt Rezerv Standby (Bin TL)
    # Altın — varlık + yükümlülük
    "TP.BL001",           # Altın Rezervi (Bin TL)
    "TP.BL002",           # Uluslararası Standartta Altın (Bin TL)
    "TP.BL0021",          # Uluslararası Standartta Altın (Safi Gram)
    "TP.BL089",           # Altın ZK
    "TP.BL132",           # Yurtiçi Banka Altın Teminat
    "TP.BL136",           # Yurtiçi Banka Altın Depo/ROM
    "TP.BL141",           # Yurtdışı Banka Altın Yükümlülük (Bin TL)
    "TP.BL142",           # Yurtdışı Banka Altın Yükümlülük (Safi Gram)
    # Döviz — varlık
    "TP.BL003",           # Yabancı Para Banknotlar
    "TP.BL004",           # Yurtdışı Banka Toplam YP Varlık
    "TP.BL008",           # Döviz Menkul Kıymetler
    "TP.BL012",           # Toplam Menkul Kıymetler
    "TP.BL098",           # IMF Rezerv Pozisyonu
    # Döviz — yükümlülük
    "TP.BL085",           # Yurtiçi Banka Toplam YP Yük (pre-2018)
    "TP.BL129",           # Yurtiçi Banka Döviz Depo
    "TP.BL131",           # Yurtiçi Banka Döviz Teminat
    "TP.BL086",           # Yurtdışı Banka YP Mevduat
    "TP.BL088",           # Döviz ZK
    "TP.BL090",           # Diğer Döviz Mevduat
    "TP.BL092",           # İşçi Dövizleri
    "TP.BL093",           # Uluslararası Kuruluşlar
    "TP.BL097",           # Yurtdışı Banka Toplam YP Yük (BL140 baz)
    "TP.BL140",           # Yurtdışı Banka Döviz Yükümlülük
    "TP.BL099",           # SDR Tahsisatı
    "TP.BL117",           # Akreditifler
    "TP.BL118",           # Alınan Krediler
]

# Aylık URDL fallback (TcmbAylikRezerv_Altin_Swap)
MONTHLY_URDL_TICKERS: Final[list[str]] = [
    "TP.REZVARPD.K1",     # Resmi Rezerv Varlıkları
    "TP.REZVARPD.K2",     # Döviz Varlıkları
    "TP.REZVARPD.K3",     # Menkul Kıymetler
    "TP.REZVARPD.K4",     # Toplam Nakit ve Mevduatlar
    "TP.REZVARPD.K5",     # Diğer MB, BIS, IMF
    "TP.REZVARPD.K6",     # Yurtiçi Bankalar
    "TP.REZVARPD.K7",     # Yurtdışı Bankalar
    "TP.REZVARPD.K8",     # IMF Rezerv Pozisyonu
    "TP.REZVARPD.K9",     # SDR'lar
    "TP.REZVARPD.K10",    # Resmi Altın Rezervleri
    "TP.REZVARPD.K11",    # Saf Altın
    "TP.DOVVARNC.K14",    # TCMB Toplam Swap
    "TP.DOVVARNC.K18",    # M.B. Açık Swap
    "TP.DOVVARNC.K22",    # M.B. Fazla Swap
    "TP.DOVVARNC.K23",    # Diğer Swap
]

ALL_TICKERS: Final[list[str]] = (
    DAILY_BILANCO_TICKERS + WEEKLY_VAZIYET_TICKERS + MONTHLY_URDL_TICKERS
)

# =============================================================================
# Birim Sabitleri
# =============================================================================

BIN_TL_TO_MILYAR_TL: Final[float] = 1_000_000.0    # ÷
MILYON_USD_TO_MILYAR_USD: Final[float] = 1000.0    # ÷
GRAM_PER_TROY_OZ: Final[float] = 31.1034768

# =============================================================================
# Tarih Cut-off'ları (docs/registry-notes/tcmb-rezerv-cutoffs.md)
# =============================================================================

YIBANK_FALLBACK_CUTOFF: Final[_dt.date] = _dt.date(2018, 8, 31)
"""Pre-2018: yiBank = BL085 toplam. Post-2018: yiBank = BL129 + BL131."""

PRE_2018_TEYIT_TOLERANCE_DATE: Final[_dt.date] = _dt.date(2018, 8, 31)
"""Pre-2018 tarihlerde teyit flag null döner (~1.3 mrd USD sapma normal)."""

BL097_PLACEHOLDER_THRESHOLD: Final[float] = 100_000.0
"""BL097 < 100K Bin TL → null sayılır (pre-2018 placeholder filtre)."""

# =============================================================================
# Source URI'leri
# =============================================================================

URDL_PAGE_URL: Final[str] = (
    "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/"
    "Istatistikler/Odemeler+Dengesi+ve+Ilgili+Istatistikler/"
    "Uluslararasi+Rezervler+ve+Doviz+Likiditesi/"
)

PIYASA_VERILERI_URL: Final[str] = (
    "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/"
    "Istatistikler/Piyasa+Verileri"
)

PDF_KEYWORDS: Final[list[str]] = ["tcmb", "taraf", "swap", "islem"]
URDL_ZIP_TITLE_PREFIX: Final[str] = "Haftalık Uluslararası Rezervler"
