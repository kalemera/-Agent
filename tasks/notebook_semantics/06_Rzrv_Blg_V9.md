---
task_id: notebook-semantics-06-rzrv-blg-v9
notebook_path: ../Telegram Bot/notebooks/Rzrv_Blg_V9.ipynb
lane: L2_powerquery_replication
priority: P1
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
  - tasks/notebook_semantics/05_Rzrv_Blg_V7.md
  - docs/registry-notes/tcmb-rezerv-cutoffs.md
evds_code_families:
  - TP.AB
  - TP.BL
  - TP.DK
  - TP.REZVARPD
  - TP.DOVVARNC
external_inputs:
  - source:tcmb-urdl-zip
  - source:tcmb-tarafli-swap-pdf
target_outputs:
  - generated/Rzrv_Blg_V9_ticker_report.md
  - generated/Rzrv_Blg_V9_registry_import.csv
  - src/evds_registry/rezerv/  (Python pipeline modülü)
known_blockers:
  - PDF format değişiklikleri sütun matcher'ları kırabilir
  - URDL ZIP yapı değişiklikleri II.2/II.3 satır eşleşmesini etkiler
  - Pre-2018 BL097 placeholder filtresi (>100K eşiği) gerekli
  - 20.03.2026 hardcoded patch dinamik hale getirilmeli
---

# Rzrv_Blg_V9

## Amaç

Bu notebook v7'nin yerini almak yerine **v9 Excel'in (Rezerv_Apko_queryleri_korunmus_v9.xlsm) Python karşılığı**dır. v9 Power Query M kodundan tüm rezerv hesap mantığı doğrudan replike edilir; sonuç Python pipeline modülü (`src/evds_registry/rezerv/`) için spec oluşturur.

**Kapsam farkı v7'den:**

| Konu | v7 | v9 |
|---|---|---|
| Tahmin frekansı | Haftalık | **Günlük** (analitik bilanço bazlı) |
| Altın yükümlülükler | Yok / kısmi | **5 seri tam (BL089/132/136/141/142)** |
| Döviz yükümlülükler | Yok / kısmi | **10 seri tam** |
| Standby kalıntı | Yok | **Var (TP.AB.N07 - bileşenler)** |
| BL142 backfill | Yok | **Var (ilk geçerli değer öncekilere)** |
| BL140 etkin fallback | Yok | **3-katmanlı fallback** |
| Pre-2018 BL085 fallback | Yok | **Var (Tarih < 2018-08-31)** |
| PDF altın swap | Yok | **PDF öncelikli, URDL fallback** |
| URDL aylık fallback | Yok | **TP.REZVARPD.K1-K11 + DOVVARNC.K14/22/23** |

## EVDS Kod Envanteri (v9 — 51 seri)

### Aile özetleri

- `TP.AB`: 9 (A02, A11, A13, A14, C1, C2, TOPLAM, N06, N07)
- `TP.DK`: 1 (USD.A.YTL)
- `TP.BL`: 23 (001, 002, 0021, 003, 004, 008, 012, 085, 086, 088, 089, 090, 092, 093, 097, 098, 099, 117, 118, 129, 131, 132, 136, 140, 141, 142)
- `TP.REZVARPD`: 11 (K1-K11)
- `TP.DOVVARNC`: 4 (K14, K18, K22, K23)

**Toplam: 51 seri**

### v7 → v9 yeni eklenenler (38)

```
URDL alternatif (3): TP.BL004, TP.BL008, TP.AB.N07
Net Altın yük. (5):  TP.BL089, BL132, BL136, BL141, BL142
Net Döviz yük. (10): TP.BL085, BL129, BL131, BL086, BL088, BL090, BL092, BL093, BL140, BL097
Diğer haftalık (5):  TP.BL099, BL117, BL118, BL012, BL098
URDL aylık (11):     TP.REZVARPD.K1-K11
Aylık swap (3):      TP.DOVVARNC.K14, K22, K23
```

## Beklenen Pipeline Modülleri

### `src/evds_registry/rezerv/`

```
rezerv/
├── __init__.py
├── fetchers/
│   ├── evds_fetcher.py       # 51 seri çek (chunk'lı, rate limit'li)
│   ├── urdl_zip_fetcher.py   # TCMB sayfa → ZIP scrape
│   └── tarafli_pdf_fetcher.py # Piyasa Verileri sayfa → PDF scrape
├── transformers/
│   ├── units.py              # Bin TL → Milyar TL → Milyar USD
│   ├── backfill.py           # BL142 ilk geçerli değer
│   └── etkin.py              # BL141Etkin, BL140Etkin (3-katmanlı)
├── calculators/
│   ├── implied_fx.py         # USD/TL ve gram altın TL
│   ├── standby.py            # Standby Kalıntısı
│   ├── net_altin.py          # TCMB Net Altın
│   ├── net_doviz.py          # TCMB Net Döviz (pre-2018 fallback)
│   ├── swap_haric.py         # SH Net Altın/Döviz/NUR
│   └── bilanco_tahmini.py    # Günlük analitik proxy
├── validators/
│   ├── teyit.py              # NIR teyit kontrolü
│   └── pre_2018.py           # Tarih cut-off mantığı
└── pipeline.py               # Ana orchestrator
```

## Test Vakaları (Python Pipeline için)

`docs/registry-notes/tcmb-rezerv-cutoffs.md` Bölüm 8'deki 12 test vakası **mutlaka** kontrol edilmeli:

1. Pre-2018 BL085 fallback
2. Post-2018 BL129+BL131
3-4. Cut-off boundary (2018-08-30 / 2018-08-31)
5-6. BL097 placeholder filtresi
7-8. BL142 backfill (sadece başlangıç)
9. Pre-2021 PDF altın swap fallback
10. Post-2021 PDF altın swap kullanım
11. 20.03.2026 hardcoded patch
12. Resmi tatil sentetik bilanço satırı

## Beklenen Registry Nesneleri

### Theme

- `theme:reserves`
- `theme:net-reserve-estimate`
- `theme:tcmb-swap`

### Indicator (19 yeni — daha önce eklendi)

```
derived:tcmb-implied-fx-usd
derived:tcmb-implied-gram-altin-fiyat
derived:tcmb-altin-troy-ons
derived:tcmb-brut-rezerv-tl-urdl
derived:tcmb-doviz-rezervi-tl-urdl
derived:tcmb-standby-kalintisi
derived:tcmb-bl141-etkin
derived:tcmb-bl140-etkin
derived:tcmb-net-altin-rezervi
derived:tcmb-net-doviz-rezervi
derived:tcmb-mb-swap-toplam
derived:tcmb-pdf-gunluk-swap-net
derived:tcmb-pdf-gunluk-altin-swap-net
derived:tcmb-swap-haric-net-altin
derived:tcmb-swap-haric-net-doviz
derived:tcmb-swap-haric-net-rezerv-gunluk
derived:tcmb-swap-haric-net-rezerv-urdl
derived:tcmb-bilanco-net-doviz-pozisyonu
derived:tcmb-bilanco-tahmini-net-rezerv
```

### Source dependency

- `source:tcmb-urdl-zip` (haftalık ZIP scrape)
- `source:tcmb-tarafli-swap-pdf` (günlük PDF scrape)

## Acceptance Checklist (Pipeline)

- [ ] 51 EVDS series çekme başarılı (chunk'lı)
- [ ] Birim dönüşümleri doğru (Bin TL → Milyar USD)
- [ ] BL142 backfill sadece başlangıç (orta null'lar dokunulmamış)
- [ ] BL141Etkin + BL140Etkin 3-katmanlı fallback'ler doğru
- [ ] Standby Kalıntısı = N07 - bileşen toplamı
- [ ] Net Altın hesabı v9 Excel sonucuna ±0.001 milyar USD
- [ ] Net Döviz hesabı pre/post-2018 doğru kırılım
- [ ] SH Net Altın PDF/URDL fallback işaret kuralı doğru
- [ ] SH Net Döviz mbAdj kuralı doğru
- [ ] Teyit sütunu post-2018 ≤ 0.001, pre-2018 null
- [ ] PDF tarih patch dinamik (hardcoded değil)
- [ ] URDL ZIP scrape FATA / 404 dayanıklı

## Çözümsüzler ve Risk Notları

- **TCMB sayfa şablonu değişikliği** → URDL ZIP linki bulunamayabilir
- **PDF format değişikliği** → "TOPLAM-STOK Alım/Satım Yönlü" matcher fail
- **Pdf.Tables Python karşılığı** → `pdfplumber` veya `tabula-py` ile replike
- **EVDS rate limit** → Chunk size + retry-with-backoff
- **Encoding sorunları** → ZIP/PDF UTF-8 vs Windows-1254 fallback

## Gerekli CLI/Şema Değişiklikleri

- `spec=rzrv-blg-v9`
- v7 ile **paralel** çalışacak (v7 deprecated değil, eski analiz için)
- `show-map` v9 indicator/source dependency akışını gösterecek

## Versiyon Geçmişi

| Tarih | Değişiklik |
|---|---|
| 2026-05-05 | İlk versiyon — registry kayıtları tamamlanmıştır, pipeline implementasyonu bekliyor |
