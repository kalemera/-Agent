# TCMB Rezerv Pipeline — Mimari Tasarım

> **Hedef:** v9 Excel Power Query M kodunu Python paketine taşımak. `src/evds_registry/rezerv/` modülü altında, mevcut EVDSAdapter ile uyumlu.

## Yüksek Düzey Akış

```
┌─────────────────────────────────────────────────────────────┐
│                       INPUT                                  │
├─────────────────────────────────────────────────────────────┤
│  • EVDS API (51 series)                                      │
│  • TCMB URDL ZIP (tcmb-urdl-zip)                            │
│  • TCMB Taraflı Swap PDF (tcmb-tarafli-swap-pdf)             │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    FETCHERS                                  │
├─────────────────────────────────────────────────────────────┤
│  evds_fetch()      → DataFrame[51 series × dates]           │
│  urdl_zip_fetch()  → DataFrame (haftalık swap kalemleri)    │
│  pdf_fetch()       → DataFrame (günlük swap detayı)         │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                  TRANSFORMERS                                │
├─────────────────────────────────────────────────────────────┤
│  unit_convert()         → Bin TL → Milyar TL → Milyar USD    │
│  bl142_backfill()       → İlk geçerli değer öncekilere       │
│  bl141_etkin()          → BL141 ?? Türetilen (BL142×fiyat)  │
│  bl140_etkin()          → 3-katmanlı fallback                │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                  CALCULATORS                                 │
├─────────────────────────────────────────────────────────────┤
│  implied_fx_usd()           → (BL001/AB.C1)/1000             │
│  implied_gram_altin()       → (BL002×1000)/BL0021            │
│  standby_kalintisi()        → N07 - bileşen toplamı          │
│  net_altin_rezervi()        → BL002 - yükümlülükler          │
│  net_doviz_rezervi()        → varlık - yük (pre-2018 fall.)  │
│  swap_haric_net_*()         → PDF/URDL fallback              │
│  bilanco_tahmini()          → A02-A11-A14 (-A13)             │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                  VALIDATORS                                  │
├─────────────────────────────────────────────────────────────┤
│  teyit_check()        → |NetAltin+NetDoviz-NIR| ≤ 0.001      │
│  pre_2018_handler()   → BL085 fallback mantığı               │
│  date_patch()         → Eksik tarih önceki günden            │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                       OUTPUT                                 │
├─────────────────────────────────────────────────────────────┤
│  • DataFrame[~62 sütun, haftalık + günlük overlay]          │
│  • Excel "Özet" sayfası replikasyonu                        │
│  • CSV export                                                │
│  • JSON snapshot (RezervAnalystAgent için)                  │
└─────────────────────────────────────────────────────────────┘
```

## Modül Yapısı (Minimal)

```
src/evds_registry/rezerv/
├── __init__.py            # Public API
├── config.py              # Sabit listeler, tarih cut-off'ları
├── fetchers.py            # 3 fetcher (EVDS + ZIP + PDF)
├── transformers.py        # Birim, backfill, etkin değer
├── calculators.py         # Tüm hesap fonksiyonları
├── validators.py          # Teyit + cut-off mantığı
└── pipeline.py            # Orchestrator (run_full_pipeline)

tests/rezerv/
├── conftest.py            # Fixture'lar (mock data)
├── test_transformers.py
├── test_calculators.py
├── test_validators.py
└── test_pipeline.py
```

## Veri Akışı — Tip Anlaşmaları

```python
# Tüm fonksiyonlar pandas DataFrame veya Series döner
# Tarih index: pd.DatetimeIndex (UTC veya naive — tutarlı)
# Sütun adları: registry id'leri yerine kısa ad ('BL001', 'NetAltin', vb.)
# Birim: dict ile takip edilir (col → unit map)

import pandas as pd
from dataclasses import dataclass
from typing import Any

@dataclass
class RezervSnapshot:
    """Tüm pipeline çıktısı tek nesnede."""
    raw: pd.DataFrame              # Ham EVDS verisi (Bin TL/Milyon USD)
    transformed: pd.DataFrame      # Etkin değerler, backfill uygulanmış
    calculated: pd.DataFrame       # Hesaplanmış indicator'lar
    validation: pd.DataFrame       # Teyit sütunları + flagler
    metadata: dict[str, Any]       # Kaynak tarih, tahmin flag, vs.

    @property
    def latest(self) -> pd.Series:
        """En son tarih değerleri."""
        return self.calculated.iloc[-1]
```

## Kritik Mimari Kararlar

### 1) Tek "Wide" DataFrame mı, Multi-Index mi?

**Karar:** Tek wide DataFrame, sütun adları registry id'leri ile **opsiyonel** map.
- **Neden:** Excel Power Query muadili — okuyucu için tanıdık
- **Trade-off:** 60+ sütun unwieldy olabilir; ama partial test ve debug daha kolay

### 2) Tarih frekansı — Haftalık mı Günlük mü?

**Karar:** İç akışta **haftalık** (TcmbHaftalikRezerv mantığı), günlük overlay ayrı bir "view" fonksiyonu.
- **Neden:** Hesaplar haftalık kapanış üzerinde tanımlı; günlük tahmin proxy
- **Trade-off:** İki frekans karışıklık yaratabilir → açık dökümantasyon şart

### 3) Cache Stratejisi

**Karar:** EVDS adapter'da mevcut cache + fetcher seviyesinde TTL'li disk cache.
- **Neden:** EVDS rate limit + ZIP/PDF fetch maliyetli
- **TTL önerisi:** EVDS 1 gün, ZIP 1 saat, PDF 30 dk (TCMB güncellenme sıklığına göre)

### 4) Hata Yönetimi

**Karar:** Her seri için **independent fail** — bir seri null gelirse pipeline çalışmaya devam eder.
- **Neden:** Pre-2018 dönemde bazı seriler hep null; pipeline her zaman çalışmalı
- **Validation:** Bitiş öncesi kritik seriler check edilir

### 5) Tarih Patch Stratejisi

**Karar:** Hardcoded tarih (20.03.2026) **YASAK**. Dinamik missing-date detection:
- Beklenen iş günü frekansından eksik tarihler tespit edilir
- Önceki iş gününden veri kopyalanır
- Patch logu ayrı bir liste olarak validation'da raporlanır

## TDD Sırası — Test-First İmplementasyon

```
1. config.py            (sadece sabit listeler — test hızlı)
2. transformers.units   (en saf hesap)
3. transformers.backfill (BL142 backfill — sınır vakaları)
4. transformers.etkin   (BL141Etkin, BL140Etkin)
5. calculators.implied_fx
6. calculators.standby
7. calculators.net_altin
8. calculators.net_doviz   (pre-2018 fallback dahil)
9. calculators.swap_haric  (PDF/URDL işaret kuralı)
10. calculators.bilanco_tahmini
11. validators.teyit
12. fetchers (mock'lu unit, sonra integration)
13. pipeline (e2e)
```

Her modülde:
- **Önce test yaz** (RED) — bilinen Excel sonucu örneği ile
- **Implement** (GREEN) — minimal kod test'i geçirsin
- **Refactor** — kalite iyileştir, side-effect kaldır

## Excel Cross-Check Stratejisi

Excel v9'dan **5-10 örnek tarih** seçilir, bilinen output değerleri test fixture olarak kullanılır:

```python
# tests/rezerv/conftest.py
EXCEL_REFERENCE_DATA = {
    "2026-04-25": {
        "TP.BL001": 5_341_000_000,  # Bin TL
        "TP.AB.C1": 161_645,         # Milyon USD
        "İmaEdilenUSDTL": 33.034,    # TL/USD
        "NetAltin_USD": 27.432,      # Milyar USD
        "NetDoviz_USD": 25.793,
        "SH_NetRezerv_Gunluk": 35.12,
        # ...
    },
    "2018-08-30": {  # pre-2018 boundary test
        # ...
    },
    "2018-08-31": {  # post-2018 boundary test
        # ...
    },
}
```

Pipeline çıktısı bu referans değerlere ±0.001 milyar USD tolerans ile uyumlu olmalı.

## Bağımlılıklar (mevcut + yeni)

```
Mevcut:
- pandas
- requests (EVDSAdapter)
- evds (resmi TCMB lib)

Yeni:
- pdfplumber  → PDF parse (Pdf.Tables muadili)
- openpyxl    → Excel cross-check (testler için)
```

## Performans Hedefi

```
Tek pipeline run:
- EVDS 51 series fetch:    ~10-15 sn (chunked)
- ZIP fetch + parse:        ~3-5 sn
- PDF fetch + parse:        ~5-10 sn
- Transformers + Calculators: <1 sn (pandas vectorized)
- Validators + Output:      <1 sn
TOPLAM: ~20-30 sn (cache miss), <5 sn (cache hit)
```

## Versiyon Geçmişi

| Tarih | Değişiklik |
|---|---|
| 2026-05-05 | İlk versiyon — minimal modül yapısı, TDD sırası tanımlandı |
