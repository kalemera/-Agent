---
record_type: series
id: evds:TP.BL086
title: Yurtdışı Banka Toplam YP Mevduat (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL086
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtdışı bankaların TCMB'de tuttuğu yabancı para
  mevduat hesaplarının TL karşılığı. Kaynak grubu: MERKEZ BANKASI
  HAFTALIK VAZİYET. TCMB Net Döviz Rezervi formülünde yükümlülük
  tarafının dış banka mevduat bileşenidir.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (yiBank + TP.BL086 + ...)
  Yurtdışı banka mevduat yükümlülüklerini temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtdışı Banka Toplam YP Mevduat (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL086
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtdışı bankaların TCMB nezdinde tuttuğu döviz mevduat hesapları.
Net Döviz Rezervi formülünde yükümlülük tarafında bağımsız bir
kalem olarak yer alır.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (BL003+BL004+BL008+StandbyKalintisi) -
                (yiBank + TP.BL086 + TP.BL088 + TP.BL090 + TP.BL092 + TP.BL093 + BL140Etkin + SDR + BL117 + BL118)
```
