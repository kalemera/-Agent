---
record_type: series
id: evds:TP.BL097
title: Yurtdışı Banka Toplam YP Yükümlülük (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL097
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtdışı bankalara karşı toplam yabancı para
  yükümlülüklerinin TL karşılığı (altın + döviz birleşik). Kaynak
  grubu: MERKEZ BANKASI HAFTALIK VAZİYET. TP.BL140 (döviz yükümlülük)
  null olduğu tarihlerde fallback baz olarak kullanılır:
  BL140Etkin = BL097 - BL141Etkin (BL097 > 100K ise).
usage: >
  TP.BL097 ≈ TP.BL140 + TP.BL141 (genel)
  Pre-2018 placeholder filtre: BL097 > 100,000 olmalı (aksi halde null sayılır)
  BL140Etkin fallback formülünde baz seri olarak yer alır.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtdışı Banka Toplam YP Yükümlülük (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL097
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

TCMB'nin yurtdışı bankalara karşı toplam yabancı para yükümlülüğü.
İçinde hem altın (TP.BL141) hem döviz (TP.BL140) bileşenleri yer alır:

```
TP.BL097 ≈ TP.BL140 + TP.BL141   (genel ilişki)
```

## TP.BL140 Etkin Fallback Formülünde Rolü

`TcmbHaftalikRezerv` sorgusunda TP.BL140 (döviz yükümlülük) null
olduğunda, TP.BL097'den türetme yapılır:

```python
BL140Etkin = (
    BL140                              if BL140 != null
    else (BL097 - BL141Etkin)          if BL097 > 100,000 and BL141Etkin != null
    else BL097                          if BL097 > 100,000
    else null
)
```

## Pre-2018 Placeholder Sorunu

Pre-2018 EVDS verilerinde TP.BL097 zaman zaman ~1.000 Bin TL gibi
**placeholder** değerler içerir (gerçek değer 100.000 üstündedir).
Bu çöp veriyi filtrelemek için `BL097 > 100,000` eşiği uygulanır:

- BL097 ≤ 100.000 → null sayılır → yük hesabında 0 gibi işlenir
- BL097 > 100.000 → gerçek veri kabul edilir, fallback formülünde kullanılır

## Net Döviz Formülünde Direkt Yeri Yoktur

TP.BL097 doğrudan Net Döviz Rezervi formülünde yer almaz; sadece
TP.BL140 verisi eksik olduğunda **dolaylı yoldan** hesaba katılır.
Doğrudan kalem TP.BL140 (Etkin) versiyonudur.
