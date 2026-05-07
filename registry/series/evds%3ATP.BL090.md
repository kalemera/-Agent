---
record_type: series
id: evds:TP.BL090
title: Diğer Döviz Mevduat (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL090
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB'de tutulan diğer (banka dışı, kamu/şirket
  vb.) döviz mevduat hesaplarının TL karşılığı. Kaynak grubu: MERKEZ
  BANKASI HAFTALIK VAZİYET. Net Döviz Rezervi yükümlülük tarafında
  bağımsız bir kalemdir.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (... + TP.BL090 + ...)
  Banka dışı döviz mevduatlarını temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Diğer Döviz Mevduat (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL090
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

TCMB'de tutulan banka dışı kuruluşların (kamu kurumları, hazine,
şirketler vb.) döviz mevduatları. Net Döviz Rezervi formülünde
yükümlülük tarafındaki "diğer" kalemini temsil eder.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + BL088 + TP.BL090 + BL092 + BL093 + BL140Etkin + SDR + BL117 + BL118)
```
