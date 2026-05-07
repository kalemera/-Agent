---
record_type: series
id: evds:TP.DOVVARNC.K14
title: TCMB Swap Büyüklüğü (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.DOVVARNC.K14
frequency: monthly
unit: Milyar USD
catalog_group: DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
description: >
  TCMB'nin tüm swap stoklarının aylık toplam Milyar USD karşılığı.
  Kaynak grubu: DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU. Bu seri TCMB'nin
  bankalarla, BIST'le ve karşı taraflarla gerçekleştirdiği tüm
  swap işlemlerinin (FX swap + altın swap + diğer) toplam stokunu
  gösterir. Aylık fallback olarak haftalık ZIP scrape başarısız
  olduğunda kullanılır.
usage: >
  TCMB toplam swap stoku (aylık). Diğer DOVVARNC swap kalemleri
  (K18 + K22 + K23) bu üst toplamın alt bileşenleridir.
official_url: ''
theme_ids:
- theme:reserves
- theme:tcmb-swap
indicator_ids: []
---
# TCMB Swap Büyüklüğü (Milyar USD)

## Kaynak

**EVDS Grubu:** DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
**Ticker:** TP.DOVVARNC.K14
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

TCMB'nin tüm swap işlem stoklarının aylık toplam değeri. URDL aylık
fallback'inde "TCMB Swap Büyüklüğü" sütunu olarak kullanılır.

## Alt Bileşenler

```
TP.DOVVARNC.K14 (Toplam Swap)
    ├── TP.DOVVARNC.K18 → TCMB M.B. (Açık) Swap
    ├── TP.DOVVARNC.K22 → TCMB M.B. (Fazla) Swap
    └── TP.DOVVARNC.K23 → TCMB Diğer Swaplar
```

`TcmbAylıkRezerv_Altin_Swap` sorgusunda bu üç alt kalem (K18 + K22 + K23)
ile K14 üst toplamı tutarlılık için karşılaştırılır.

## Haftalık ZIP ile İlişki

Haftalık URDL ZIP yayınında "yurtiçi para döviz forward future kısa
fazla pozisyon büyüklük" anahtar kelimelerini içeren satır TP.DOVVARNC.K14
ile aynı kavramı temsil eder; aylık seri haftalık verinin geçmişe dönük
sürekli izlenmesini sağlar.
