---
record_type: series
id: evds:TP.BL092
title: İşçi Dövizleri (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL092
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtdışında çalışan Türk işçilerinin TCMB'de
  tuttuğu döviz hesapları (Kredi Mektuplu Döviz Tevdiat Hesabı —
  KMDTH ve benzeri) TL karşılığı. Kaynak grubu: MERKEZ BANKASI
  HAFTALIK VAZİYET. Net Döviz Rezervi yükümlülük tarafında özel
  amaçlı bir kalem.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (... + TP.BL092 + ...)
  İşçi dövizleri özel hesap yükümlülüklerini temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# İşçi Dövizleri (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL092
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtdışında çalışan Türk işçilerinin TCMB'de açabildiği özel döviz
hesapları. Tarihsel olarak Kredi Mektuplu Döviz Tevdiat Hesabı (KMDTH)
gibi araçlar bu kalemde toplanmıştır. Bu mevduatlar TCMB için
yükümlülüktür ve Net Döviz Rezervi formülünde yükümlülük tarafında
yer alır.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + BL088 + BL090 + TP.BL092 + BL093 + BL140Etkin + SDR + BL117 + BL118)
```

## Tarihsel Önem

İşçi Dövizleri kalemi 1970'lerden itibaren Türkiye'nin döviz akışında
önemli bir role sahip olmuştur. Modern dönemde tutarı görece düşük
kalsa da rezerv hesabında tarihsel süreklilik için izlenir.
