"""Test fixture'ları — Excel v9 referans değerleri.

5-10 örnek tarih için bilinen pipeline çıktıları test referansı olarak
kullanılır. Pipeline değerleri ±0.001 milyar USD tolerans ile uyumlu olmalı.
"""

from __future__ import annotations

import pandas as pd
import pytest


@pytest.fixture
def sample_dates() -> pd.DatetimeIndex:
    """Test için 6 örnek tarih:
        - 2 pre-2018 (BL085 fallback testi)
        - 2 boundary (2018-08-30, 2018-08-31)
        - 2 post-2018
    """
    return pd.DatetimeIndex(
        [
            "2017-01-13",  # Pre-2018, BL085 yolu
            "2018-08-24",  # Hala pre-2018
            "2018-08-30",  # Boundary - cusp
            "2018-08-31",  # İlk post-2018
            "2025-12-26",  # Modern dönem
            "2026-04-25",  # En güncel referans
        ]
    )


@pytest.fixture
def mock_evds_raw(sample_dates: pd.DatetimeIndex) -> pd.DataFrame:
    """6 tarih × 51 ticker mock EVDS verisi.

    Gerçek değerler v9 Excel'den alınmıştır (yaklaşık).
    Pipeline sonucu ile cross-check için kullanılır.
    """
    # NOT: Gerçek Excel değerleri v9'dan çıkarıldıktan sonra burası doldurulacak.
    # Şu an placeholder — testler `pytest.skip` ile geçilir.
    df = pd.DataFrame(index=sample_dates)
    return df


@pytest.fixture
def excel_reference_values() -> dict[str, dict[str, float]]:
    """Excel v9 (TcmbHaftalikRezerv sheet) — beklenen pipeline çıktıları.

    Format: {tarih_str: {indicator_name: value}}
    Pipeline sonucu ile ±0.001 milyar USD tolerans ile uyumlu olmalı.

    Notlar:
      - 2018-08-30 → Excel'de o tarih yok, en yakın sonraki haftalık
        satır (2018-08-31, row 180) kullanıldı.
      - 2026-04-25 → Excel'de o tarih yok, en yakın önceki haftalık
        satır (2026-04-24, row 579) kullanıldı (sonraki yok).
      - Sütun haritası (sheet column → fixture key):
          AJ=BrutRezervUSD, AK=AltinRezerviUSD, AL=DovizRezerviUSD,
          AM=NetAltinUSD, AN=NetDovizUSD, AX=NIRUSD,
          AG=ImpliedFX, BF=SHNetAltin, BG=SHNetDoviz, BI=SHNetRezerv.
    """
    return {
        "2017-01-13": {
            "BrutRezervUSD": 110.559,
            "AltinRezerviUSD": 15.267,
            "DovizRezerviUSD": 95.292,
            "NetAltinUSD": 3.208718,
            "NetDovizUSD": 32.436395,
            "NIRUSD": 36.8966,
            "ImpliedFX": 3.84302,
            "SHNetAltin": 3.208718,
            "SHNetDoviz": 35.219395,
            "SHNetRezerv": 39.6796,
        },
        "2018-08-24": {
            "BrutRezervUSD": 92.691,
            "AltinRezerviUSD": 19.767,
            "DovizRezerviUSD": 72.924,
            "NetAltinUSD": 8.136649,
            "NetDovizUSD": 19.27387,
            "NIRUSD": 28.556665,
            "ImpliedFX": 5.994674,
            "SHNetAltin": 8.136649,
            "SHNetDoviz": 18.46787,
            "SHNetRezerv": 27.750665,
        },
        "2018-08-30": {
            # Nearest-next: 2018-08-31 satırı kullanıldı (row 180)
            "BrutRezervUSD": 88.848,
            "AltinRezerviUSD": 18.435,
            "DovizRezerviUSD": 70.413,
            "NetAltinUSD": 8.276209,
            "NetDovizUSD": 18.444805,
            "NIRUSD": 26.721013,
            "ImpliedFX": 6.406372,
            "SHNetAltin": 8.276209,
            "SHNetDoviz": 17.638805,
            "SHNetRezerv": 25.915013,
        },
        "2018-08-31": {
            "BrutRezervUSD": 88.848,
            "AltinRezerviUSD": 18.435,
            "DovizRezerviUSD": 70.413,
            "NetAltinUSD": 8.276209,
            "NetDovizUSD": 18.444805,
            "NIRUSD": 26.721013,
            "ImpliedFX": 6.406372,
            "SHNetAltin": 8.276209,
            "SHNetDoviz": 17.638805,
            "SHNetRezerv": 25.915013,
        },
        "2025-12-26": {
            "BrutRezervUSD": 193.87187,
            "AltinRezerviUSD": 116.893832,
            "DovizRezerviUSD": 76.978038,
            "NetAltinUSD": 83.418652,
            "NetDovizUSD": -3.645147,
            "NIRUSD": 79.773506,
            "ImpliedFX": 42.7641,
            "SHNetAltin": 88.322652,
            "SHNetDoviz": -20.737147,
            "SHNetRezerv": 67.038506,
        },
        "2026-04-25": {
            # Nearest-prev: 2026-04-24 satırı kullanıldı (row 579, son satır)
            "BrutRezervUSD": 171.051581,
            "AltinRezerviUSD": 110.100868,
            "DovizRezerviUSD": 60.950712,
            "NetAltinUSD": 72.03934,
            "NetDovizUSD": -17.809369,
            "NIRUSD": 54.229972,
            "ImpliedFX": 44.8132,
            "SHNetAltin": 74.12034,
            "SHNetDoviz": -37.727369,
            "SHNetRezerv": 36.390972,
        },
    }
