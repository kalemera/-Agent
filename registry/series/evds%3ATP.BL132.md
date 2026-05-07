---
record_type: series
id: evds:TP.BL132
title: Yurtiçi Banka Altın Teminat (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL132
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtiçi bankaların TCMB'ye teslim ettiği altın
  teminatlarının TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK
  VAZİYET. TCMB Net Altın Rezervi formülünde altın yükümlülüklerinin
  ilk bileşenidir.
usage: >
  TCMB Net Altın Rezervi Ara (Bin TL) =
    TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + TP.BL141Etkin)
  Yurtiçi banka kaynaklı altın teminatlarını temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtiçi Banka Altın Teminat (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL132
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtiçinde faaliyet gösteren bankaların TCMB'ye teminat olarak
yatırdıkları altın stokunun TL karşılığı. TCMB için yükümlülük
niteliğindedir.

`TcmbHaftalikRezerv` sorgusunda **TCMB Net Altın Rezervi** formülünde
yükümlülük tarafında ilk kalemdir:

```
Net Altın Ara = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + TP.BL141Etkin)
```

## Pre-2018 Tarihleri Önemli Not

`TcmbHaftalikRezerv` M kodunda, **Tarih < 2018-08-31** için BL132 ve
BL129/BL131 (döviz teminat) gibi kalemler ayrışmamış olarak BL085 toplamı
içinde geliyordu. Bu nedenle pre-2018 dönemde teyit sütunu (NetAltin +
NetDoviz - NIR) için ~1.3 milyar USD farkı normal kabul edilir; flag
değeri null döner.
