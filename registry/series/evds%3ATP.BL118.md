---
record_type: series
id: evds:TP.BL118
title: Alınan Krediler (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL118
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB'nin yurtdışından aldığı kredilerin TL
  karşılığı (BIS, IMF olağan dışı, swap line vb.). Kaynak grubu:
  MERKEZ BANKASI HAFTALIK VAZİYET. Net Döviz Rezervi formülünde
  yükümlülük tarafında dış kredi kalemini temsil eder.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (... + TP.BL117 + TP.BL118 + ...)
  Yurtdışından alınan kredi yükümlülüklerini temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Alınan Krediler (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL118
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

TCMB'nin yurtdışı finansal kuruluşlardan (BIS, IMF, diğer merkez
bankaları) aldığı kredilerin TL karşılığı. Swap line kullanımları
(Çin Halk Bankası, Katar Merkez Bankası vb. ile imzalanan) bu
kalemde takip edilebilir.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140Etkin + SDR + BL117 + TP.BL118)
```

## Swap Line Kullanımıyla İlişki

Türkiye'nin Çin (CNY-TRY swap, 2019), BAE (AED-TRY swap, 2023),
Katar (QAR-TRY swap, 2018) gibi merkez bankalarıyla imzaladığı
swap anlaşmalarının kullanılan kısımları bu kalemde yansır. Bu
yüzden seri politik/diplomatik döviz desteği akışlarına duyarlıdır.
