---
record_type: source_dependency
id: source:tufe-kategoriler
title: TUFE Ana Harcama Gruplari Agirliklar ve Endeks (TUIK)
status: approved
source_kind: tuik_press_xls
requiredness: required
source_uri: https://veriportali.tuik.gov.tr/tr/press/58295
local_hint: TUFE/downloads/tufe/Ana-harcama-gruplarina-gore-agirliklar-tuketici-fiyat-endeksi-TUFE-ve-degisim-oranlari.xls
description: 13 COICOP 2018 ana harcama grubu icin snapshot tablo (agirlik, endeks, 5 donem degisim %)
usage: pipelines/tufe_parser.py -> parse_kategoriler() ile okunur, tufe_categories tablosuna yazilir
theme_ids:
- theme:tufe
indicator_ids: []
validation_note: 14 satir beklenir (00 TUFE genel + 01-13 kategori). Kolon sayisi >= 7.
---
# TUFE Ana Harcama Gruplari Snapshot

## Kaynak Turu
tuik_press_xls (t=r download link)

## Zorunluluk
required

## Kaynak URI
https://veriportali.tuik.gov.tr/tr/press/58295

## Local Hint
`TUFE/downloads/tufe/Ana-harcama-gruplarina-gore-agirliklar-tuketici-fiyat-endeksi-TUFE-ve-degisim-oranlari.xls`

## Dosya Yapisi
- Snapshot tablo (tek donem)
- Row 4+ veri: col0=ad, col1=agirlik, col2=endeks, col3=aylik %, col4=YTD %, col5=yillik %, col6=12A ort %
- 14 satir: code 00 (TUFE genel) + 01-13 (13 kategori)

## Kullanim
- Parser: `pipelines/tufe_parser.py::parse_kategoriler(path, year, month)`
- DB hedef: `tufe_categories` tablosu
- Kod eslesmesi COICOP 2018 standardina gore:
  - 01: Gida ve alkolsuz icecekler
  - 02: Alkollu icecekler, sigara ve tutun
  - 03: Giyim ve ayakkabi
  - 04: Konut, su, elektrik, gaz
  - 05: Ev esyasi ve bakim
  - 06: Saglik
  - 07: Ulastirma
  - 08: Bilgi ve iletisim (eski: Haberlesme)
  - 09: Eglence ve kultur
  - 10: Egitim
  - 11: Lokanta, yiyecek-icecek ve konaklama
  - 12: Sigorta ve finansal hizmetler
  - 13: Diger mal ve hizmetler

## Dogrulama Notlari
- COICOP 2018 ile 12 kategori -> 13 kategoriye gecis (2026 Ocak itibari ile)
- Base yil 2003=100 -> 2025=100 olarak guncellendi
