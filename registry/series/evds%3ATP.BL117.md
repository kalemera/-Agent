---
record_type: series
id: evds:TP.BL117
title: Akreditifler (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL117
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB nezdinde açık duran akreditifler (ithalat
  garantili döviz transfer taahhütleri) TL karşılığı. Kaynak grubu:
  MERKEZ BANKASI HAFTALIK VAZİYET. Net Döviz Rezervi formülünde
  yükümlülük tarafında dış ticaret kaynaklı sürekli yükümlülük
  niteliği taşır.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (... + TP.BL117 + TP.BL118 + ...)
  Açık duran akreditif yükümlülüklerini temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Akreditifler (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL117
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

TCMB nezdinde açık duran ithalat akreditiflerinin TL karşılığı.
Akreditif, ithalatçının bankasının TCMB'ye karşı taahhüt ettiği
döviz ödeme yükümlülüğüdür ve henüz transfer edilmemiş durumdadır.
Bu nedenle TCMB için bir nevi vadeli yükümlülük niteliği taşır.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140Etkin + SDR + TP.BL117 + BL118)
```

## TP.BL118 ile İlişki

Bu seri **TP.BL118 (Alınan Krediler)** ile birlikte dış ticaret ve
finansman kaynaklı yükümlülüklerin iki ana kalemini oluşturur. İkisi
genellikle birlikte değerlendirilir.
