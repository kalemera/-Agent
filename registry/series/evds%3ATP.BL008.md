---
record_type: series
id: evds:TP.BL008
title: Döviz Menkul Kıymetler (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL008
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB'nin sahip olduğu yabancı para cinsi menkul
  kıymetler (tahvil/bono portföyü) TL cinsinden. Kaynak grubu:
  MERKEZ BANKASI HAFTALIK VAZİYET. Brüt döviz rezervinin "menkul kıymet"
  bileşeni; aylık URDL aylık fallback'inde TP.REZVARPD.K3 ile eşleşir.
usage: >
  Brüt Rezerv (Milyar TL, URDL) = (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008) / 1,000,000
  Döviz Rezervi (Milyar TL) = (TP.BL003 + TP.BL004 + TP.BL008) / 1,000,000
  Menkul Kıymetler (Milyar USD) = (TP.BL008 ham olmayan; ayrı seri TP.BL012'den)
  TCMB Net Döviz Rezervi varlık tarafının üçüncü bileşeni.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Döviz Menkul Kıymetler (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL008
**Frekans:** Haftalık
**Ham Birim:** Bin TL → ÷1,000,000 → Milyar TL

## Kullanım

TCMB döviz cinsi menkul kıymet portföyü (yabancı devlet tahvilleri vb.).
Power Query `TcmbHaftalikRezerv` sorgusunda **Brüt Rezerv (URDL
alternatif yolu)** üçlü formülünün üçüncü bileşeni:

```
Brüt Rezerv = TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008
```

## TP.BL012 ile İlişki

Excel'de ayrıca **TP.BL012** ("Menkul Kıymetler Ham") ayrı bir kalem
olarak çekilir ve İma Edilen USD/TL kuruyla Milyar USD'ye çevrilir
("Menkul Kıymetler (Milyar USD)" raporu). TP.BL008 brüt rezerv
formülünde yer alırken, TP.BL012 raporlama tarafında portföy değerini
gösterir — iki seri farklı amaçlar için kullanılır.

## URDL Aylık Eşleşmesi

Aylık fallback'te (TP.REZVARPD serisi) bu kalem **TP.REZVARPD.K3
"Menkul Kıymetler (Milyar USD)"** ile aynı kavramı temsil eder.
