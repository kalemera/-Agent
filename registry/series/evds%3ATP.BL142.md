---
record_type: series
id: evds:TP.BL142
title: Yurtdışı Banka Altın Yükümlülük (Safi Gram)
status: approved
source: evds
source_version: evds2
ticker: TP.BL142
frequency: weekly
unit: Safi Gram
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtdışı bankalara karşı altın yükümlülüklerin
  miktar (safi gram) cinsi karşılığı. Kaynak grubu: MERKEZ BANKASI
  HAFTALIK VAZİYET. TP.BL141 verisinin null olduğu tarihler için
  türetilmiş Bin TL karşılığını üretmek üzere İmaEdilenGramAltınTL ile
  çarpılır. İlk geçerli değer önceki null tarihlere backfill edilir.
usage: >
  Yurtdışı Banka Altın Yük. Türetilen (Bin TL) = TP.BL142 × İmaEdilenGramAltinTL / 1000
  Backfill: İlk non-null TP.BL142 değeri, başlangıçtaki null satırlara doldurulur.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtdışı Banka Altın Yükümlülük (Safi Gram)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL142
**Frekans:** Haftalık
**Ham Birim:** Safi Gram (gram, not Bin TL)

## Kullanım

TCMB'nin yurtdışı bankalara karşı altın yükümlülüğünün **miktar**
cinsi karşılığı. Bu seri, TP.BL141 (TL karşılık) verisinin null olduğu
tarihler için altın yükümlülüğünü türetmek üzere kullanılır.

## Türetme Formülü

```
İmaEdilenGramAltinTL = (TP.BL002 × 1000) / TP.BL0021     [TL/gram]
Türetilen (Bin TL)   = TP.BL142 × İmaEdilenGramAltinTL / 1000
```

## Backfill Mantığı (M kodu, satır 1268-1277)

`TcmbHaftalikRezerv` sorgusunda BL142 verisinin **ilk geçerli değeri**
bulunur ve serinin başındaki null satırlara backfill edilir:

```
BL142Filled: ilk non-null değer → tüm önceki null tarihlere doldurulur
```

Bu işlem time series'in başlangıcında BL142 yayını başlamadan önceki
dönemlerde de türetilmiş değer üretebilmek için yapılır. Backfill
sadece BAŞLANGIÇ yönündedir; orta veya son tarihlerdeki nulllar
karışmaz.

## Net Altın Formülüne Etkisi

BL142 → Türetilen → BL141Etkin → Net Altın yükümlülük zinciri:

```
Net Altın Ara = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + BL141_Etkin)
```
