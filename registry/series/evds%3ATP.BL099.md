---
record_type: series
id: evds:TP.BL099
title: SDR Tahsisatı (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL099
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — IMF tarafından Türkiye'ye tahsis edilen Özel
  Çekme Hakkı (SDR) yükümlülüğünün TL karşılığı. Kaynak grubu:
  MERKEZ BANKASI HAFTALIK VAZİYET. SDR tahsisatı bir nevi IMF'ye
  karşı sürekli yükümlülük niteliği taşır ve Net Döviz Rezervi
  formülünde yükümlülük tarafında yer alır.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (... + TP.BL099 + ...)
  SDR'lar (Milyar USD) raporu = TP.BL099 / 1,000,000 / İmaEdilenUSDTL
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# SDR Tahsisatı (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL099
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

IMF'in üye ülkelere periyodik olarak tahsis ettiği Özel Çekme Hakkı
(SDR) tutarı. Tahsisat, bir nevi IMF'ye karşı **sürekli yükümlülük**
sayılır (kullanılmadığı sürece duran bir yükümlülük) ve Net Döviz
Rezervi formülünde yükümlülük tarafında yer alır.

## İki Kullanım Alanı

1. **Net Döviz formülünde yükümlülük olarak:**
   ```
   Net Döviz Ara = (Varlıklar) - (... + TP.BL099 + ...)
   ```

2. **SDR'lar (Milyar USD) raporu olarak:**
   ```
   SDR'lar (Milyar USD) = (TP.BL099 / 1,000,000) / İmaEdilenUSDTL
   ```
   Bu rapor URDL aylık fallback'teki **TP.REZVARPD.K9 (SDR'lar)**
   kalemiyle eşdeğerdir.

## 2021 SDR Tahsisatı

IMF 2021 Ağustos'ta tarihsel en büyük SDR tahsisatını gerçekleştirmiştir
(~650 milyar USD küresel, Türkiye payı ~6.4 milyar USD). Bu tarihten
sonra TP.BL099 değerinde belirgin bir sıçrama görülür.
