---
record_type: source_dependency
id: source:tufe-katkilar
title: TUFE Ana Harcama Gruplari Katki Puanlari (TUIK)
status: approved
source_kind: tuik_press_xls
requiredness: optional
source_uri: https://veriportali.tuik.gov.tr/tr/press/58295
local_hint: TUFE/downloads/tufe/TUFE-ana-harcama-gruplarinin-yillik-ve-aylik-degisim-oranlari-ve-genel-endeks-degisimine-katkilari.xls
description: 13 kategorinin TUFE genel endekse aylik ve yillik katki puanlari (yuzde puan)
usage: pipelines/tufe_parser.py -> parse_contributions() ile okunur, tufe_contributions tablosuna yazilir
theme_ids:
- theme:tufe
indicator_ids: []
validation_note: 14 satir beklenir. Aggregate satir (code 00) ve 13 kategori.
---
# TUFE Katki Puanlari

## Kaynak Turu
tuik_press_xls (t=r download link)

## Zorunluluk
optional (ozet tabloda yok, ama pipeline DB'ye yaziyor)

## Kaynak URI
https://veriportali.tuik.gov.tr/tr/press/58295

## Local Hint
`TUFE/downloads/tufe/TUFE-ana-harcama-gruplarinin-yillik-ve-aylik-degisim-oranlari-ve-genel-endeks-degisimine-katkilari.xls`

## Dosya Yapisi
- Snapshot tablo (tek donem)
- Row 4+ veri: col0=ad, col1=agirlik, col2=aylik katki puan, col3=yillik katki puan
- 14 satir (00 + 01-13)

## Kullanim
- Parser: `pipelines/tufe_parser.py::parse_contributions(path, year, month)`
- DB hedef: `tufe_contributions` tablosu
- Katkilar TUFE genel endeksteki degisimin hangi kategorilerden geldiini gosterir
- TUIK haber bulteninde "en yuksek katki..." gibi ifadeler bu dosyadan gelir

## Dogrulama Notlari
- Aylik katkilarin toplami yaklasik aylik TUFE % ile eslesmelidir
- Yillik katkilarin toplami yaklasik yillik TUFE % ile eslesmelidir
