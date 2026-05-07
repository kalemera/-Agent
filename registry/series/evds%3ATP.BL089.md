---
record_type: series
id: evds:TP.BL089
title: Altın Zorunlu Karşılıkları (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL089
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — bankaların altın cinsi zorunlu karşılık olarak
  TCMB'de tuttukları altın stokunun TL karşılığı. Kaynak grubu:
  MERKEZ BANKASI HAFTALIK VAZİYET. TCMB Net Altın Rezervi formülünde
  altın yükümlülüklerinin bir bileşenidir.
usage: >
  TCMB Net Altın Rezervi Ara (Bin TL) =
    TP.BL002 (Varlık)
    - (TP.BL132 + TP.BL136 + TP.BL089 + TP.BL141Etkin)  (Yükümlülükler)
  TP.BL089 burada Altın ZK yükümlülüğünü temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Altın Zorunlu Karşılıkları (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL089
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Bankaların TCMB'ye altın cinsi zorunlu karşılık olarak teslim ettikleri
altın stokunun TL karşılığı. Bu kalem TCMB için bir **yükümlülüktür**
çünkü bankalar adına tutulur.

`TcmbHaftalikRezerv` sorgusunda **TCMB Net Altın Rezervi** formülünde
yükümlülük tarafında dört bileşenden biridir:

```
Net Altın Ara (Bin TL) = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + TP.BL141_Etkin)
                          ↑                ↑          ↑          ↑          ↑
                          Varlık       Teminat   Depo/ROM    AltınZK   Yurtdışı Yük
```

## v9 Notu

v7 Excel'inde ayrı `TcmbAltinZorunluKarsilik` sheet'i mevcuttu (TCMB
sayfasından scrape ediliyordu). v9'da bu sheet kaldırıldı ve ZK verisi
artık doğrudan EVDS API üzerinden TP.BL089 ile alınıyor.
