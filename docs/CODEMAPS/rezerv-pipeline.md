# Rezerv Pipeline Codemap

**Last Updated:** 2026-05-07
**Module Root:** `src/evds_registry/rezerv/`
**Public API:** `from evds_registry.rezerv import RezervSnapshot, run_pipeline`
**Extraction:** Python `ast` (tldr CLI yok)

## Amaç

TCMB rezerv pozisyonu (Brüt, Net, Swap Hariç) için v9 Excel Power Query M kodunun
Python karşılığı. Üç veri kaynağını (EVDS API, URDL Haftalık ZIP, Taraflı Swap PDF)
birleştirip standart bir `RezervSnapshot` üretir.

## Modüller

| Dosya | Rol | Bağımlılık |
|---|---|---|
| `__init__.py` | Public API re-export (`RezervSnapshot`, `run_pipeline`) | — |
| `config.py` | Sabit listeler + cut-off tarihleri (51 EVDS ticker, BL097 placeholder eşik, vs.) | — |
| `fetchers.py` | EVDS / URDL ZIP / PDF veri çekiciler | requests, evds, openpyxl, pdfplumber |
| `transformers.py` | Birim dönüşüm + backfill + etkin değer (BL142, BL141Etkin, BL140Etkin) | pandas |
| `calculators.py` | Türev hesaplar (Net Altın, Net Döviz, Standby, SH, bilanço tahmin) | pandas |
| `validators.py` | Teyit kontrolü + eksik iş günü patch | pandas |
| `pipeline.py` | Orchestrator — `run_pipeline()` zinciri + `RezervSnapshot` dataclass | calc + tx + val |

## Bağımlılık Akış Diyagramı

```
                    ┌──────────────────────────────────────┐
                    │          run_pipeline()              │
                    │            (pipeline.py)             │
                    └──────────────┬───────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        ▼                          ▼                          ▼
   raw_evds (DF)              raw_urdl (DF)             raw_pdf (DF)
   fetchers.fetch_evds_series fetchers.fetch_urdl_zip   fetchers.fetch_tarafli_swap_pdf
        │                          │                          │
        └──────────────┬───────────┴──────────────────────────┘
                       ▼
              ┌────────────────────┐
              │  validators        │
              │  patch_missing_    │   (pre-step: iş günü doldurma)
              │  dates()           │
              └─────────┬──────────┘
                        ▼
              ┌────────────────────┐
              │  transformers      │
              │  bl142_backfill    │
              │  implied_fx_usd    │
              │  bl141_etkin       │
              │  bl140_etkin       │
              └─────────┬──────────┘
                        ▼
              ┌────────────────────┐
              │  calculators       │
              │  standby_kalintisi │
              │  net_altin_*       │
              │  net_doviz_*       │
              │  swap_haric_*      │
              │  bilanco_*         │
              └─────────┬──────────┘
                        ▼
              ┌────────────────────┐
              │  validators        │
              │  teyit_fark        │   (post-step: doğrulama)
              │  teyit_flag        │
              └─────────┬──────────┘
                        ▼
              ┌────────────────────┐
              │ RezervSnapshot     │
              │  .calculated       │
              │  .latest()         │
              │  .get_indicator()  │
              └────────────────────┘
```

## Modül Detayları

### `config.py`

Sabit listeler. Kod yok, sadece `Final` literal'ler.

- `DAILY_BILANCO_TICKERS` — Günlük analitik bilanço (TP.AB.A02, ...)
- `WEEKLY_BL_TICKERS` — Haftalık BL kalemleri
- `BL097_PLACEHOLDER_THRESHOLD` — Pre-2018 filtre eşiği (≤100K)
- `CUTOFF_2018_YIBANK` — `2018-08-31` (yiBank serisi geçişi)
- `URDL_KEYWORDS_*` — URDL parsing için anahtar sözcük listeleri

### `fetchers.py`

| Fonksiyon | İmza | Açıklama |
|---|---|---|
| `fetch_evds_series` | `(tickers, start_date, end_date, api_key, frequency, chunk_size)` | EVDS API'den 51 seri çek (chunk'lı) |
| `fetch_urdl_zip` | `(url, timeout)` | TCMB sayfası → Haftalık ZIP → Excel parse |
| `urdl_extract_kalem_series` | `(urdl_df, keywords, output_name)` | URDL wide → long format çevir |
| `fetch_tarafli_swap_pdf` | `(url, timeout)` | TCMB Piyasa Verileri PDF scrape |
| `_normalize_ticker_for_evds_lib` | `(ticker)` | `TP.AB.A02` ↔ `TP_AB_A02` |
| `_normalize_date_column` | `(df)` | Tarih sütununu DatetimeIndex'e çevir |
| `_shorten_evds_column_names` | `(df)` | `TP_AB_A02` → `AB.A02` kısaltma |
| `_parse_pdf_number` | `(v)` | TR/EN format toleranslı float parse |
| `_find_col` | `(df, keywords)` | TR-normalize multi-keyword sütun arama |

### `transformers.py`

| Fonksiyon | İmza | Açıklama |
|---|---|---|
| `bin_tl_to_milyar_tl` | `(value)` | ÷ 1.000.000 |
| `milyon_usd_to_milyar_usd` | `(value)` | ÷ 1000 |
| `gram_to_troy_ons` | `(gram)` | ÷ 31.1034768 |
| `bin_tl_with_fx_to_milyar_usd` | `(bin_tl, fx_rate)` | (BinTL/1M) / FX |
| `bl142_backfill` | `(bl142_series)` | İlk geçerli değer **sadece başlangıç** null'larına |
| `bl141_turetilen` | `(bl142_filled, implied_gram_altin_tl)` | BL142 × ImaEdilenGram / 1000 |
| `bl141_etkin` | `(bl141_real, bl141_turetilen_val)` | Gerçek öncelikli; null ise türetilen |
| `bl140_etkin` | `(bl140, bl097, bl141_etkin_val, placeholder_threshold)` | 3 katmanlı fallback (M kod 1470-1484) |
| `implied_fx_usd` | `(bl001_bin_tl, ab_c1_milyon_usd)` | (BL001/AB.C1) / 1000 |
| `implied_gram_altin_tl` | `(bl002_bin_tl, bl0021_safi_gram)` | (BL002 × 1000) / BL0021 |

### `calculators.py`

| Fonksiyon | Çıktı | Birim |
|---|---|---|
| `standby_kalintisi` | N07 - (BL001+BL003+BL004+BL008) | Bin TL |
| `brut_rezerv_tl_urdl` | (BL001+BL003+BL004+BL008) / 1M | Milyar TL |
| `doviz_rezervi_tl_urdl` | (BL003+BL004+BL008) / 1M | Milyar TL |
| `net_altin_ara_bin_tl` | BL002 - (BL132+BL136+BL089+BL141Etkin) | Bin TL |
| `net_altin_milyar_usd` | (Ara/1M) / İmaEdilenUSDTL | Milyar USD |
| `yibank_with_pre2018_fallback` | Pre-2018 BL085, post-2018 BL129+BL131 | — |
| `net_doviz_ara_bin_tl` | Varlık - Yükümlülük (cut-off duyarlı) | Bin TL |
| `net_doviz_milyar_usd` | (Ara/1M) / İmaEdilenUSDTL | Milyar USD |
| `swap_haric_net_altin` | NetAltinUSD - PDFAltinSwap (URDL fallback) | Milyar USD |
| `swap_haric_net_doviz` | NetDovizUSD - MBSwapURDL - PDFNonMB | Milyar USD |
| `swap_haric_net_rezerv_gunluk` | SHNetAltin + SHNetDoviz | Milyar USD |
| `swap_haric_net_rezerv_urdl` | NIR + SwapToplam + DigerSwap | Milyar USD |
| `mb_swap_toplam` | K18 (Açık) + K22 (Fazla) | — |
| `bilanco_net_doviz_pozisyonu` | (A02-A11-A14-A13)/1M / FX | Milyar USD |
| `bilanco_tahmini_net_rezerv` | (A02-A11-A14)/1M / FX | Milyar USD |

### `validators.py`

| Fonksiyon | İmza | Açıklama |
|---|---|---|
| `teyit_fark` | `(net_altin_usd, net_doviz_usd, nir_usd, decimals)` | NetAltin + NetDoviz - NIR (Milyar USD) |
| `teyit_flag` | `(teyit_fark_val, index, tolerance, cutoff)` | True/False/None — pre-2018 tolerans, post-2018 tight |
| `detect_missing_business_dates` | `(index, expected_freq)` | Eksik iş günleri tespit |
| `patch_missing_dates` | `(df, expected_freq)` | Önceki gün verisi ile doldur |

### `pipeline.py`

| Sembol | Tip | Açıklama |
|---|---|---|
| `RezervSnapshot` | dataclass | `raw`, `calculated`, `meta` alanları + `.latest()` + `.get_indicator(name)` |
| `run_pipeline` | func | `(raw_evds, raw_urdl, raw_pdf) → RezervSnapshot` |
| `_empty_series` | helper | Index'e uyumlu dtype=float64 boş seri |
| `_has_cols` | helper | Tüm sütunlar mevcut mu? |
| `_align_optional` | helper | Opsiyonel kaynaklardan seri çıkar + hizala |
| `_extract_pdf_series` | helper | PDF wide → FX/Altın swap kalemleri |

## Önemli v9 Davranış Kuralları (Pipeline'da Uyulmalı)

| Kural | Modül | Etki |
|---|---|---|
| 2018-08-31 cut-off | calculators | yiBank = pre BL085 / post BL129+BL131 |
| BL097 ≤ 100K → null | transformers | Pre-2018 placeholder filtresi (`bl140_etkin`) |
| BL142 backfill | transformers | İlk geçerli değer **sadece başlangıç** null'larına |
| PDF: pozitif, URDL: negatif | calculators | SH formüllerinde işaret kuralı kritik |
| Pre-2021 PDF altın yok | calculators | URDL II.3 fallback |
| Tarih patch: dinamik | validators | Hardcoded değil, missing-date detection |

## Test Dosyaları

| Test | Konu | Sayı |
|---|---|---|
| `tests/rezerv/test_transformers.py` | Birim dönüşüm + backfill | 15 |
| `tests/rezerv/test_calculators.py` | Türev hesaplar | 17 |
| `tests/rezerv/test_validators.py` | Teyit + tarih patch | 9 |
| `tests/rezerv/test_fetchers.py` | Mock fetcher davranışı | 18 |
| `tests/rezerv/test_fetchers_integration.py` | Live API (env-bağımlı, skip) | 4 |

## İlgili Dokümanlar

- `docs/registry-notes/tcmb-rezerv-cutoffs.md` — Cut-off tarih listesi
- `docs/registry-notes/tcmb-rezerv-pipeline-design.md` — Tasarım kararları
- `docs/CODEMAPS/agent-system.md` — Snapshot'u tüketen agent'lar
