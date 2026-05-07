---
record_type: series
id: evds:TP.BL131
title: Yurtiçi Banka Döviz Teminat (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL131
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtiçi bankaların TCMB'ye verdiği döviz cinsi
  teminatların TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK
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
# Yurtiçi Banka Döviz Teminat (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL131
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtiçi bankaların TCMB'ye teminat olarak verdiği döviz stokunun TL
karşılığı. Post-2018-08-31 dönemi için Net Döviz Rezervi formülünde
**yiBank** kaleminin iki bileşeninden ikincisidir (diğeri TP.BL129 —
döviz depo).

## Tarih Kırılımı

Bu seri, TP.BL129 ile birlikte 2018-08-31'den itibaren EVDS'de ayrı
yayımlanmaya başladı. Öncesinde toplam, TP.BL085 altında raporlanıyordu.

## Net Döviz Formülünde Yeri

```
yiBank = TP.BL129 + TP.BL131           # Post-2018
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140Etkin + SDR + BL117 + BL118)
```
