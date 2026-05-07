---
record_type: series
id: evds:TP.BL140
title: Yurtdışı Banka Döviz Yükümlülük (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL140
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtdışı bankalara karşı döviz yükümlülüklerinin
  TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. EVDS'de
  bu seri her tarih için dolu olmayabilir; TP.BL097 - TP.BL141Etkin
  fallback formülü ile "Etkin" değer hesaplanır.
usage: >
  Yurtdışı Banka Döviz Yük. Etkin (Bin TL) =
    if BL140 != null then BL140
    else if BL097 > 100,000 and BL141Etkin != null then BL097 - BL141Etkin
    else if BL097 > 100,000 then BL097
    else null   (pre-2018 placeholder filtresi)
  TCMB Net Döviz Rezervi yükümlülük tarafında yer alır.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtdışı Banka Döviz Yükümlülük (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL140
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

TCMB'nin yurtdışı bankalara karşı **döviz** cinsi yükümlülükleri.
TP.BL141 (altın yükümlülük) ile simetrik bir kalem; ikisinin toplamı
yaklaşık olarak TP.BL097 (Yurtdışı Banka Toplam YP Yükümlülük) eder.

## "Etkin" Mantığı (M kodu, satır 1470-1484)

`TcmbHaftalikRezerv` sorgusunda BL140 verisinin null olduğu tarihler
için TP.BL097 ve TP.BL141Etkin üzerinden türetme yapılır:

```python
BL140Etkin = (
    BL140                              if BL140 != null
    else (BL097 - BL141Etkin)          if BL097 > 100,000 and BL141Etkin != null
    else BL097                          if BL097 > 100,000
    else null                           # pre-2018 placeholder filtresi
)
```

**Pre-2018 Filtre:** Pre-2018 dönemde BL097 ~1.000 Bin TL gibi
placeholder değerler içeriyordu (gerçek değer 100.000 üstündedir).
`BL097 > 100.000` kontrolü bu çöp veriyi filtreler ve null döndürerek
yük hesabında 0 gibi işlenir.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140_Etkin + SDR + BL117 + BL118)
```
