# Proje Durumu

> Son güncelleme: 2026-05-06 (Faz 5k–5n + 6 — Rezerv v9 tamamlandı)

## Neredeyiz?

Faz 5k (Rezerv v9 Excel haritalama — registry kısmı) tamamlandı. Devamında Faz 5l (Theme dosyaları), 5m (Notebook task spec), 5n (Pre-cutoff documentation), Faz 6 ana parçalarından **Pipeline + RezervAnalystAgent** sıfırdan inşa edildi. 81 unit test PASS.

## İki Proje

| Proje | Dizin | Durum |
|-------|-------|-------|
| EVDS Registry | `İş Kodlama/İş Agentı` | ✅ Faz 5k–5n + 6 (kısmen) bitti |
| Econ Platform | `Model/Econ` | ✅ /api/registry endpoint'leri hazır |

## Registry Sayıları (2026-05-06)

```
series:        ~274 (+37 yeni v9 + 13 mevcut güncelleme)
indicator:     ~77 (+14 yeni TCMB rezerv derived)
theme:         18 (3'ü yenilendi, 1 yeni: theme:tcmb-swap)
source_dep:    ~23 (+1 tcmb-tarafli-swap-pdf)
TOPLAM:        ~392 kayıt
```

## Faz 5k–5n (Rezerv v9) — Bu Seansta Tamamlanan

### v9 Excel'den Türetilen Yeni Kayıtlar

**Yeni Series (37):**

```
URDL alternatif (3):  TP.BL004, TP.BL008, TP.AB.N07
Net Altın yük (5):    TP.BL089, BL132, BL136, BL141, BL142
Net Döviz yük (10):   TP.BL085, BL129, BL131, BL086, BL088,
                      BL090, BL092, BL093, BL140, BL097
Diğer haftalık (5):   TP.BL099, BL117, BL118, BL012, BL098
URDL aylık (11):      TP.REZVARPD.K1 → K11
Aylık swap (3):       TP.DOVVARNC.K14, K22, K23
```

**Düzeltme:** TP.DOVVARNC.K18 başlığı "TCMB M.B. (Açık) Swap Büyüklüğü" olarak güncellendi (önceki auto-gen "2.2.1.3.Dört Ay Bir Yıl Arası" yanlış başlık).

**Mevcut Series Güncellemeleri (13):**
TP.AB.A02/A11/A13/A14, TP.DK.USD.A.YTL, TP.AB.C1/C2/TOPLAM/N06, TP.BL001/002/0021/003 — hepsi tam v9 contextine yükseltildi (description, usage, indicator_ids genişletildi).

**Yeni Derived Indicator (14):**

```
İmaEdilenUSDTL, İmaEdilenGramAltinTL, AltinTroyOns
BrutRezervTLURDL, DovizRezervTLURDL, StandbyKalintisi
BL141Etkin, BL140Etkin (3-katmanlı fallback)
NetAltinRezervi, NetDovizRezervi (pre-2018 BL085 fallback)
MBSwapToplam (K18+K22)
PDFGunlukSwapNet, PDFGunlukAltinSwapNet
SwapHaricNetAltin, SwapHaricNetDoviz
SwapHaricNetRezervGunluk, SwapHaricNetRezervURDL
BilancoNetDovizPozisyonu, BilancoTahminiNetRezerv
```

**Yeni Source Dependency:**
- `source:tcmb-tarafli-swap-pdf` — TCMB Piyasa Verileri günlük PDF scrape

**Yeni Theme:**
- `theme:tcmb-swap` — TCMB swap pozisyonları için ayrı tema (4 series + 7 indicator + 2 source)

### Documentation

| Dosya | İçerik |
|---|---|
| `docs/registry-notes/tcmb-rezerv-cutoffs.md` | Pre-2018 / pre-2021 / placeholder filtreleri / hardcoded patch — 8 bölüm + 12 test vakası |
| `docs/registry-notes/tcmb-rezerv-pipeline-design.md` | Pipeline mimari tasarım, modül yapısı, TDD sırası |
| `tasks/notebook_semantics/06_Rzrv_Blg_V9.md` | v9 notebook task spec (gelecek implementasyon referansı) |

## Faz 6 (Pipeline + Agent) — Bu Seansta Tamamlanan

### Pipeline Modülleri

```
src/evds_registry/rezerv/
├── __init__.py        ✅
├── config.py          ✅ 51 ticker + sabitler + cut-off tarihleri
├── transformers.py    ✅ Birim, BL142 backfill, BL141Etkin, BL140Etkin
├── calculators.py     ✅ Net Altın/Döviz, Standby, SH varyantları, bilanço tahmini
├── validators.py      ✅ Teyit kontrol, pre-2018 tolerans, dinamik tarih patch
├── fetchers.py        ✅ EVDS API, URDL ZIP, Taraflı Swap PDF
└── pipeline.py        ✅ run_pipeline() orchestrator + RezervSnapshot
```

### Agent

```
src/evds_registry/agent/
└── rezerv_analyst_agent.py  ✅ 8 intent, classify_intent(), RezervAnalystAgent
```

**Desteklenen Intent'ler:**
- `brut_rezerv_durum` — Brüt rezerv miktarı + haftalık değişim
- `net_rezerv_durum` — NIR + altın/döviz kırılımı
- `swap_haric_rezerv` — SH Net Altın + Döviz + Günlük + URDL
- `gunluk_tahmin` — Bilanço bazlı günlük proxy
- `altin_kompozisyon` — Brüt/Net/SH altın + ton
- `doviz_kompozisyon` — Brüt/Net/SH döviz
- `swap_breakdown` — Toplam/M.B. açık/M.B. fazla/Diğer swap
- `tarihsel_karsilastirma` — Haftalık/Aylık/YBB değişim

### Test Sonucu

```
tests/rezerv/
├── test_transformers.py    15 test  ✅
├── test_calculators.py     17 test  ✅
├── test_validators.py       9 test  ✅
├── test_fetchers.py        18 test  ✅ (mock'lu)
├── test_fetchers_integration.py  4 test  ⏭ (env'a bağlı, skip)
└── test_agent.py           18 test  ✅
TOPLAM:                     77 PASS + 4 skip in 0.51s
```

## Codemap (2026-05-07)

- `docs/CODEMAPS/INDEX.md` ✅
- `docs/CODEMAPS/rezerv-pipeline.md` ✅ — fetcher/transformer/calculator/validator/pipeline modül haritası
- `docs/CODEMAPS/agent-system.md` ✅ — BaseAnalystAgent + TUFEAnalystAgent (5 intent) + RezervAnalystAgent (8 intent) + extension rehberi

Üretim: Python `ast` (tldr CLI yok). `docs/registry-notes/` ve `docs/superpowers/plans/` dokunulmadı (tasarım/plan dokümanları, sayfa modülü değil).

## Bilinen Test Fail'leri (Pre-existing, Bu Seansla İlgili Değil)

```
tests/test_cli.py::test_indicator_approval_requires_existing_inputs    FAIL
tests/test_semantic_inference.py::test_auto_approve_detects_conflicts_and_skips_non_series    FAIL
```

Stash + tekrar koşturmayla doğrulandı — master branch'inde de fail oluyor. Bu seansta yapılan değişikliklerden bağımsız.

## Henüz Yapılmamış (Sonraki Seans)

- ⏳ Faz 7 — Mevcut chat orchestrator'a RezervAnalystAgent entegrasyonu
- ⏳ Excel cross-check (5-10 referans tarih için ±0.001 milyar USD tolerans)
- ⏳ Pre-existing 2 test fail'ini düzelt (bu seansla ilgisiz, opsiyonel)
- ✅ Codemap güncelleme — `docs/CODEMAPS/` (rezerv-pipeline + agent-system + INDEX)
- ⏳ Final commit + push

## Önemli v9 Davranış Kuralları (Pipeline'da Uyulmalı)

| Kural | Etki |
|---|---|
| **2018-08-31 cut-off** | yiBank = pre BL085 / post BL129+BL131 |
| **BL097 ≤ 100K → null** | Pre-2018 placeholder filtresi |
| **BL142 backfill** | İlk geçerli değer **sadece başlangıç** null'larına |
| **PDF: pozitif, URDL: negatif** | SH formüllerinde işaret kuralı kritik |
| **Pre-2021 PDF altın yok** | URDL II.3 (TP.DOVVARNC.K23) fallback |
| **Tarih patch: dinamik** | Hardcoded 20.03 → 19.03 yerine missing-date detection |

## Teknik Hazırlık

| Bileşen | Durum |
|---------|-------|
| EVDS Registry MCP | ✅ Hazır |
| Kayıt Agent | ✅ Hazır |
| **Rezerv Pipeline** | ✅ Hazır (fetcher + calculator + validator) |
| **RezervAnalystAgent** | ✅ Hazır (8 intent) |
| Qwen API | ✅ Çalışıyor |
| EVDS API | ✅ Key ayarlı |

## Bilinen Tuzaklar

- **YAML colon:** `title` alanında `:` varsa `"..."` içine al, yoksa YAML patlar
- **Qwen endpoint:** `dashscope-intl.aliyuncs.com` (uluslararası)
- **REGISTRY_ROOT:** `Model/Econ/.env` dosyasına eklenmeli
- **Windows encoding:** Terminal cp1254 → `✓` ve `→` UnicodeEncodeError verir, ASCII kullan
- **TÜFE press_id:** Her yeni bültende `TÜFE/tufe_config.json` güncellenmeli
- **test_kayit_agent.py:** Script doğrudan çalıştırılır
- **Pipeline EVDS API key:** `EVDS_API_KEY` env var şart, run_pipeline çağrısı öncesi kontrol et
- **PDF format değişikliği:** TCMB tablosu sütun adları değişirse `_find_col` matcher kırılabilir; düzenli kontrol et
