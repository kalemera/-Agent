---
record_type: series
id: evds:TP.BL093
title: Uluslararası Kuruluşlar Dövizleri (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL093
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — IMF, Dünya Bankası, BIS, EBRD gibi uluslararası
  kuruluşların TCMB'de tuttuğu döviz mevduatlarının TL karşılığı.
  Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. Net Döviz Rezervi
  yükümlülük tarafında uluslararası kurum mevduat kalemini temsil eder.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (... + TP.BL093 + ...)
  Uluslararası kuruluş döviz mevduat yükümlülüklerini temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Uluslararası Kuruluşlar Dövizleri (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL093
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

IMF, Dünya Bankası, BIS, EBRD gibi uluslararası finansal kuruluşların
TCMB nezdinde tuttuğu döviz mevduatları. Bu mevduatlar TCMB için
yükümlülüktür.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + BL088 + BL090 + BL092 + TP.BL093 + BL140Etkin + SDR + BL117 + BL118)
```

## TP.BL099 (SDR Tahsisatı) ile Ayrım

Bu seri yalnızca uluslararası kuruluşların **mevduat** hesaplarını
içerir. IMF'in özel olarak tahsis ettiği SDR (Özel Çekme Hakkı)
yükümlülüğü ayrı bir seri olan **TP.BL099 (SDR Tahsisatı)** ile
takip edilir.
