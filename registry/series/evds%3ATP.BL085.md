---
record_type: series
id: evds:TP.BL085
title: Yurtiçi Banka Toplam YP Yükümlülük (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL085
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtiçi bankaların TCMB'ye karşı toplam yabancı
  para yükümlülüklerinin TL karşılığı (depo + teminat birleşik).
  Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. Pre-2018 dönemde
  BL129/BL131 ayrışmamış olarak bu serinin içinde geliyordu;
  TcmbHaftalikRezerv pre-2018 fallback'inde bu seri kullanılır.
usage: >
  Pre-2018 (Tarih < 2018-08-31): yiBank = TP.BL085 (toplam yurtiçi YP yükümlülük)
  Post-2018: yiBank = TP.BL129 + TP.BL131
  TCMB Net Döviz Rezervi yükümlülük tarafında yiBank kalemi olarak yer alır.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtiçi Banka Toplam YP Yükümlülük (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL085
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtiçi bankaların TCMB'ye karşı toplam yabancı para yükümlülükleri.
Bu seri, **pre-2018 dönemi için** Net Döviz Rezervi formülünde
yurtiçi banka yükümlülüklerini temsil eden tek kalemdir.

## Pre-2018 Fallback Mantığı (M kodu, satır 1503-1505)

`TcmbHaftalikRezerv` sorgusunda yurtiçi banka kalemleri tarihe göre
farklı yollarla hesaplanır:

```python
yiBank = if Tarih < #date(2018, 8, 31)
         then BL085                          # Pre-2018: toplam tek kalemde
         else BL129 + BL131                  # Post-2018: ayrışmış (depo + teminat)
```

**Sebep:** EVDS'de TP.BL129 (Yurtiçi Banka Döviz Depo) ve TP.BL131
(Yurtiçi Banka Döviz Teminat) yaklaşık 31 Ağustos 2018'den itibaren
ayrı seriler olarak yayınlanmaya başladı. Öncesinde her ikisi de
TP.BL085 toplamı içinde geliyordu.

## Net Döviz Formülünde Yeri

```
yiBank → TCMB Net Döviz Rezervi yükümlülük tarafında
Net Döviz Ara = (BL003+BL004+BL008+StandbyKalintisi) -
                (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140Etkin + SDR + BL117 + BL118)
```

## Pre-2018 Teyit Tolerance

Pre-2018 tarihlerde BL085 içinde altın teminat (BL132) da kısmen
karışık geliyordu, bu nedenle teyit sütunu (NetAltin+NetDoviz-NIR)
~1.3 milyar USD farkı normal kabul eder ve flag null döner.
