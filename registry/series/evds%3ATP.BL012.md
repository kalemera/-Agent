---
record_type: series
id: evds:TP.BL012
title: Menkul Kıymetler (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL012
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB'nin sahip olduğu toplam menkul kıymet
  portföyünün TL karşılığı (yurtiçi + yurtdışı). Kaynak grubu:
  MERKEZ BANKASI HAFTALIK VAZİYET. TP.BL008 (Döviz Menkul Kıymetler)
  bu serinin döviz cinsi alt kümesidir; TP.BL012 daha geniş kapsam
  içerir ve raporlama amaçlı kullanılır.
usage: >
  Menkul Kıymetler (Milyar USD) = (TP.BL012 / 1,000,000) / İmaEdilenUSDTL
  Brüt Rezerv kompozisyonu raporunda Milyar USD cinsinden gösterilir.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Menkul Kıymetler (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL012
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

TCMB'nin sahip olduğu toplam menkul kıymet portföyü (TL + döviz, hem
yurtiçi devlet tahvilleri hem de yabancı tahviller). Bu seri
raporlama amaçlı **Milyar USD** cinsinden hesaplanır:

```
Menkul Kıymetler (Milyar USD) = (TP.BL012 / 1,000,000) / İmaEdilenUSDTL
```

## TP.BL008 ile Ayrım

Bu iki seri **farklı amaçlar** için kullanılır:

| Seri | Kapsam | Amaç |
|---|---|---|
| **TP.BL008** | Sadece döviz menkul kıymetler | Brüt rezerv formülü içinde varlık kalemi |
| **TP.BL012** | Toplam (TL + döviz) | Raporlama, USD karşılık gösterimi |

`TcmbHaftalikRezerv` M kodunda BL012, "Menkul Kıymetler Ham" olarak
çekilir, sonra İmaEdilenUSDTL üzerinden Milyar USD'ye çevrilir.

## URDL Aylık Eşleşmesi

Bu seri yaklaşık olarak URDL aylık fallback'teki **TP.REZVARPD.K3
"Menkul Kıymetler"** kalemiyle aynı kavramı temsil eder.
