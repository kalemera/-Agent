"""Fetcher unit testleri.

Network çağrılar mock'lanır. Asıl entegrasyon testleri ayrı dosyada
(test_fetchers_integration.py) — gerçek API çağrısı içerir, ENV'a bağlı.
"""

from __future__ import annotations

import io
import zipfile
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from evds_registry.rezerv import fetchers


# =============================================================================
# Yardımcı fonksiyonlar
# =============================================================================

class TestParsePdfNumber:
    def test_tr_format_with_dot_comma(self):
        # 1.246,50 → 1246.5
        assert fetchers._parse_pdf_number("1.246,50") == 1246.5

    def test_en_format_with_comma_dot(self):
        # 1,246.50 → 1246.5
        assert fetchers._parse_pdf_number("1,246.50") == 1246.5

    def test_only_dot_thousand(self):
        # 1.246 (3 hane sonra) → 1246 (TR binlik)
        assert fetchers._parse_pdf_number("1.246") == 1246.0

    def test_only_dot_decimal(self):
        # 1.25 (2 hane) → 1.25 (EN ondalık)
        assert fetchers._parse_pdf_number("1.25") == 1.25

    def test_only_comma_thousand(self):
        # 1,246 (3 hane) → 1246 (EN binlik)
        assert fetchers._parse_pdf_number("1,246") == 1246.0

    def test_only_comma_decimal(self):
        # 1,25 (2 hane) → 1.25 (TR ondalık)
        assert fetchers._parse_pdf_number("1,25") == 1.25

    def test_negative(self):
        assert fetchers._parse_pdf_number("-100") == -100.0

    def test_empty_or_none(self):
        assert fetchers._parse_pdf_number(None) is None
        assert fetchers._parse_pdf_number("") is None
        assert fetchers._parse_pdf_number("  ") is None

    def test_invalid_chars(self):
        # Sadece harfler
        assert fetchers._parse_pdf_number("abc") is None


class TestFindCol:
    def test_finds_all_keywords(self):
        df = pd.DataFrame(columns=["Toplam Stok Alım Yönlü", "Diğer", "Tarih"])
        result = fetchers._find_col(df, ["toplam", "stok", "alim", "yonlu"])
        assert result == "Toplam Stok Alım Yönlü"

    def test_tr_normalize(self):
        df = pd.DataFrame(columns=["Altın TL Alım Yönlü Stok", "X"])
        result = fetchers._find_col(df, ["altin", "tl", "alim", "yonlu", "stok"])
        assert result == "Altın TL Alım Yönlü Stok"

    def test_no_match(self):
        df = pd.DataFrame(columns=["a", "b"])
        assert fetchers._find_col(df, ["xyz"]) is None


# =============================================================================
# EVDS Fetcher (mock'lu)
# =============================================================================

class TestFetchEvdsSeries:
    def test_no_api_key_raises(self, monkeypatch):
        monkeypatch.delenv("EVDS_API_KEY", raising=False)
        monkeypatch.delenv("EVDS_KEY", raising=False)
        with pytest.raises(ValueError, match="EVDS API key gereklidir"):
            fetchers.fetch_evds_series(["TP.AB.A02"])

    def test_chunked_call(self, monkeypatch):
        """50 ticker → 2 chunk (chunk_size=25)."""
        monkeypatch.setenv("EVDS_API_KEY", "test_key")

        # Mock evds.evdsAPI
        mock_df1 = pd.DataFrame(
            {
                "Tarih": ["01-01-2024", "02-01-2024"],
                "TP_AB_A02": [100.0, 110.0],
            }
        )
        mock_df2 = pd.DataFrame(
            {
                "Tarih": ["01-01-2024", "02-01-2024"],
                "TP_BL001": [200.0, 220.0],
            }
        )

        call_count = [0]

        class MockEvds:
            def __init__(self, *args, **kwargs):
                pass

            def get_data(self, tickers, **kwargs):
                call_count[0] += 1
                return mock_df1 if call_count[0] == 1 else mock_df2

        with patch.dict("sys.modules", {"evds": MagicMock(evdsAPI=MockEvds)}):
            tickers = [f"TP.X.K{i}" for i in range(40)]
            result = fetchers.fetch_evds_series(tickers, chunk_size=25)

        assert call_count[0] == 2  # 40 ticker → 2 chunk
        assert "AB.A02" in result.columns
        assert "BL001" in result.columns
        assert isinstance(result.index, pd.DatetimeIndex)


class TestNormalizeAndShorten:
    def test_normalize_date_column_tarih_dd_mm_yyyy(self):
        df = pd.DataFrame(
            {"Tarih": ["01-01-2024", "02-01-2024"], "x": [1.0, 2.0]}
        )
        result = fetchers._normalize_date_column(df)
        assert isinstance(result.index, pd.DatetimeIndex)
        assert result.index[0] == pd.Timestamp("2024-01-01")

    def test_shorten_evds_column_names(self):
        df = pd.DataFrame(
            {"TP_AB_A02": [1], "TP_BL001": [2], "TP_DK_USD_A_YTL": [3]}
        )
        result = fetchers._shorten_evds_column_names(df)
        assert "AB.A02" in result.columns
        assert "BL001" in result.columns
        assert "DK.USD.A.YTL" in result.columns


# =============================================================================
# URDL ZIP Fetcher Helper
# =============================================================================

class TestUrdlExtractKalemSeries:
    def test_extract_kalem_with_keywords(self):
        # Mock URDL wide DataFrame
        df = pd.DataFrame(
            {
                "Kalem": [
                    "I.A. Resmi rezerv varlıkları",
                    "II.2.a.iii Forward future swap",
                    "Diğer",
                ],
                pd.Timestamp("2026-04-25"): [150.0, -10.0, 5.0],
                pd.Timestamp("2026-05-02"): [155.0, -12.0, 6.0],
            }
        )
        result = fetchers.urdl_extract_kalem_series(
            df, keywords=["II.2.a.iii"], output_name="MB_Open"
        )
        assert "MB_Open" in result.columns
        assert len(result) == 2
        assert result.loc["2026-04-25", "MB_Open"] == -10.0

    def test_no_match_returns_empty(self):
        df = pd.DataFrame(
            {
                "Kalem": ["A", "B"],
                pd.Timestamp("2026-04-25"): [1.0, 2.0],
            }
        )
        result = fetchers.urdl_extract_kalem_series(
            df, keywords=["XYZ"], output_name="x"
        )
        assert result.empty
