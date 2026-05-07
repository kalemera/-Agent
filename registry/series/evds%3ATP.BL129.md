---
record_type: series
id: evds:TP.BL129
title: Yurtiçi Banka Döviz Depo (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL129
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtiçi bankaların TCMB'de tuttuğu döviz depo
  hesaplarının TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK
  VAZİYET. 2018-08-31 sonrası ayrışmış kalem; öncesinde TP.BL085
  toplamı içinde geliyordu.
usage: >
  Post-2018-08-31: yiBank = TP.BL129 + TP.BL131
  TCMB Net Döviz Rezervi yükümlülük tarafında yer alır.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtiçi Banka Döviz Depo (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL129
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtiçi bankaların TCMB'de tuttuğu döviz cinsi depo hesapları.
Post-2018-08-31 dönemi için Net Döviz Rezervi formülünde **yiBank**
kaleminin iki bileşeninden birincisidir (diğeri TP.BL131 — döviz
teminat).

## Tarih Kırılımı

```python
yiBank = if Tarih < #date(2018, 8, 31)
         then TP.BL085                       # Pre-2018: toplam
         else TP.BL129 + TP.BL131            # Post-2018: ayrışmış
```

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (BL003+BL004+BL008+StandbyKalintisi) -
                (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140Etkin + SDR + BL117 + BL118)
```
