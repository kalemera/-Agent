"""Gerçek API'leri çağıran entegrasyon testleri.

Bu testler ENV'da EVDS_API_KEY varsa çalışır; yoksa skip edilir.
Network bağımlı olduğu için CI'da opsiyonel tutulmalı.
"""

from __future__ import annotations

import os

import pandas as pd
import pytest

from evds_registry.rezerv import fetchers


_HAS_API_KEY = bool(os.getenv("EVDS_API_KEY") or os.getenv("EVDS_KEY"))


@pytest.mark.skipif(not _HAS_API_KEY, reason="EVDS_API_KEY env var yok — entegrasyon testi skip")
class TestEvdsLive:
    def test_fetch_three_tickers(self):
        """Küçük ticker setiyle gerçek EVDS çağrısı."""
        df = fetchers.fetch_evds_series(
            tickers=["TP.AB.TOPLAM", "TP.AB.C1", "TP.DK.USD.A.YTL"],
            start_date="01-01-2024",
            end_date="31-12-2024",
        )
        assert not df.empty
        assert isinstance(df.index, pd.DatetimeIndex)
        # Sütun adlarının kısaltıldığını doğrula
        assert "AB.TOPLAM" in df.columns or "AB.C1" in df.columns

    def test_full_ticker_set(self):
        """51 ticker'ın hepsi çekilebilmeli (chunk'lı)."""
        df = fetchers.fetch_evds_series(
            start_date="01-01-2025",
            end_date="31-01-2025",
        )
        assert not df.empty
        # En az 30 sütun bekleyebilirsek kapsam yeterli
        assert df.shape[1] >= 30


@pytest.mark.skipif(
    not os.getenv("RUN_NETWORK_TESTS"),
    reason="RUN_NETWORK_TESTS env yok — network testleri skip",
)
class TestUrdlZipLive:
    def test_fetch_real_zip(self):
        """Gerçek TCMB sayfasından ZIP indir + parse."""
        df = fetchers.fetch_urdl_zip()
        assert not df.empty
        assert "Kalem" in df.columns
        # En az birkaç tarih sütunu olmalı
        date_cols = [c for c in df.columns if isinstance(c, pd.Timestamp)]
        assert len(date_cols) >= 3


@pytest.mark.skipif(
    not os.getenv("RUN_NETWORK_TESTS"),
    reason="RUN_NETWORK_TESTS env yok — network testleri skip",
)
class TestPdfLive:
    def test_fetch_real_pdf(self):
        """Gerçek TCMB Piyasa Verileri PDF'i indir + parse."""
        df = fetchers.fetch_tarafli_swap_pdf()
        assert not df.empty
        assert isinstance(df.index, pd.DatetimeIndex)
        # Net swap sütunu hesaplanmış olmalı
        assert "Tcmb Günlük Swap Net Alım (Milyar USD)" in df.columns
