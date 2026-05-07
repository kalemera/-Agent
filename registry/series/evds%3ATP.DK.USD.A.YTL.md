---
record_type: series
id: evds:TP.DK.USD.A.YTL
title: USD/TL Alış Kuru — Resmi TCMB Günlük Kur
status: approved
source: evds
source_version: evds2
ticker: TP.DK.USD.A.YTL
frequency: daily
unit: TL/USD
catalog_group: TCMB DÖVİZ KURLARI
description: >
  TCMB günlük resmi USD/TL alış kuru. Kaynak grubu: TCMB DÖVİZ KURLARI.
  TCMB tarafından her iş günü yayınlanan resmi kur — Türkiye'nin tüm
  resmi döviz çevirilerinde standart referans kurudur. Günlük analitik
  bilanço serilerinin (TP.AB.A02/A11/A13/A14) Bin TL → Milyar USD
  dönüşümünde kullanılır.
usage: >
  Bilanço Kalemi (Milyar USD) = (TP.AB.A_xx / 1.000.000) / TP.DK.USD.A.YTL
  Hafta sonu/tatil günlerinde null gelir → forward fill ile önceki
  iş gününün kuru kullanılır.
  Power Query: TcmbGunlukBilanco sorgusunda 5. seri.
official_url: ''
theme_ids:
- theme:reserves
- theme:banking-balance-sheet
- theme:net-reserve-estimate
indicator_ids:
- derived:tcmb-bilanco-net-doviz-pozisyonu
- derived:tcmb-bilanco-tahmini-net-rezerv
---
# USD/TL Alış Kuru — Resmi TCMB Günlük Kur

## Kaynak

**EVDS Grubu:** TCMB DÖVİZ KURLARI
**Ticker:** TP.DK.USD.A.YTL
**Frekans:** Günlük (iş günü)
**Birim:** TL/USD (Türk Lirası başına ABD Doları)

## Kullanım

TCMB'nin her iş günü saat 15:30'da Reuters Spot Türkiye sayfasından
veya alternatif yöntemle belirleyip yayımladığı resmi USD/TL alış kuru.
Türkiye'nin tüm resmi döviz işlemlerinde standart referans kuru.

## Power Query Karşılığı

`TcmbGunlukBilanco` M kodu (satır 468 + 561):

```python
Series = "TP.AB.A02-TP.AB.A11-TP.AB.A14-TP.AB.A13-TP.DK.USD.A.YTL"
# Rename: TP_DK_USD_A_YTL → "USD/TL Alış Kuru"
```

`TcmbGunlukBilanco_USD_Swap` (satır 609 + 611-619):

```python
KurCol = "USD/TL Alış Kuru"

Add_USD_1 = "Dış Varlıklar (Milyar USD)"
    each
        let k = TP.DK.USD.A.YTL,
            v = Dış Varlıklar (Milyar TL)
        in if k = null or v = null then null else v / k
```

## Tüm Bilanço Çevrimlerinde Kullanım

Beş analitik bilanço serisinin (A02, A11, A14, A13) Milyar USD'ye
dönüşümünde aynı kur kullanılır:

```
A_xx (Milyar USD) = (A_xx Bin TL / 1.000.000) / TP.DK.USD.A.YTL
```

## Hafta Sonu / Tatil Davranışı

Bu seri sadece **iş günü** yayınlanır. Hafta sonu, ulusal tatil ve dini
bayramlarda null gelir. Power Query'de TCMB analitik bilanço da o
günlerde yayınlanmadığı için pratikte boşluk sorunu yaşanmaz.

Ancak senthetik haftalık kapanış günü hesaplarında (TcmbGunlukBilanco_USD_Swap
satır 717-739) eksik tarihler için **önceki iş gününün kuru ve bilanço
değerleri** kullanılır (forward fill).

## İma Edilen Kur ile Karşılaştırma

İki farklı USD/TL kuru kullanılır:

| Kur | Tanım | Kullanım |
|---|---|---|
| **TP.DK.USD.A.YTL** | Resmi günlük | Günlük bilanço çevirimi |
| **`derived:tcmb-implied-fx-usd`** | (TP.BL001/TP.AB.C1)/1000 | Haftalık vaziyet çevirimi |

İkisi yakın değer vermeli; sapmalar TCMB'nin altın değerleme zaman
farkından kaynaklanır.

## Türetilen Indicator Kullanım

```
derived:tcmb-bilanco-net-doviz-pozisyonu
derived:tcmb-bilanco-tahmini-net-rezerv
```

Her iki indicator da bu kuru ortak kullanır.
