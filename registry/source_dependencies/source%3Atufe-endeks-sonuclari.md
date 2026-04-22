---
record_type: source_dependency
id: source:tufe-endeks-sonuclari
title: Harcama Gruplarina Gore Endeks Sonuclari XLSX (TUIK)
status: approved
source_kind: tuik_press_xlsx
requiredness: required
source_uri: https://veriportali.tuik.gov.tr/tr/press/58295
local_hint: TUFE/downloads/tufe/Harcama-gruplarina-gore-endeks-sonuclari.xlsx
description: COICOP 2018 5 duzey kirilim - Duzey 2 (14), Duzey 3 (44), Duzey 4 (111), Duzey 5 (178) kategori endeksleri zaman serisi
usage: pipelines/tufe_parser.py -> parse_endeks_sonuclari() ile okunur, tufe_endeks tablosuna yazilir
theme_ids:
- theme:tufe
indicator_ids: []
validation_note: 4 sheet (Duzey 2/3/4/5). 267 satir x 19-178 sutun. 2005-bugun aylik. Code '0' (TUFE genel) sadece Duzey 2'de kaydedilir (PK collision).
---
# Harcama Gruplarina Gore Endeks Sonuclari

## Kaynak Turu
tuik_press_xlsx (t=i download link, native XLSX)

## Zorunluluk
required (Duzey 2 ozet tablo icin kritik)

## Kaynak URI
https://veriportali.tuik.gov.tr/tr/press/58295

## Local Hint
`TUFE/downloads/tufe/Harcama-gruplarina-gore-endeks-sonuclari.xlsx`

## Dosya Yapisi
4 sheet, her biri ayni layout:
- **Duzey 2**: 14 sutun (TUFE genel + 13 ana harcama grubu) — 2-haneli COICOP kodlari
- **Duzey 3**: 44 sutun (TUFE + alt kirilimlar) — 3-haneli kodlar (011, 012, ...)
- **Duzey 4**: 111 sutun — 4-haneli kodlar
- **Duzey 5**: 178 sutun — 5-haneli kodlar (COICOP 2018 5'li duzey)

Satir yapisi (her sheet ayni):
- R1-R3: Baslik + base yil
- R5: COICOP kodlari
- R6: Turkce kategori adlari
- R7: Baslik (Yil / Aylar / Months)
- R8+: Yil | Ay(TR) | Ay(EN) | endeks degerleri (col3+)

## COICOP 2018 Duzeyler
- Duzey 1: Tek kategori (TUFE genel)
- Duzey 2: 13 ana harcama grubu (01-13) — CLASS
- Duzey 3: Alt gruplar (011, 012, 013...)
- Duzey 4: Alt-alt gruplar (0111, 0112...)
- Duzey 5: 174 alt sinif (COICOP 2018 5'li sinif)

## Kullanim
- Parser: `pipelines/tufe_parser.py::parse_endeks_sonuclari()`
- DB hedef: `tufe_endeks` tablosu (year, month, coicop_code, coicop_level, category_name, index_value)
- ~77.764 satir (tum duzeyler × 255 donem)
- Aylik/yillik % endeks farkindan hesaplanir (pipelines/tufe_rapport.py)

## PK Cakismasi Notu
Code `0` (TUFE genel) her 4 sheet'te de var. PK = (year, month, coicop_code) oldugu icin parser sadece Duzey 2'de kayd eder; Duzey 3-5'te code `0` satirlari atlanir.

## Avantaj
Bu tek dosya 2005'ten bugune kadar TUM donemlerin TUM kirimlarinin endekslerini icerir. Aylik/yillik degisim bundan hesaplanabilir; TUIK'in ayri "aylik degisim" ve "yillik degisim" dosyalarina ihtiyac kalmaz.

## Dogrulama Notlari
- Son donem 2026-03 TUFE endeks = 121.47 (2025=100)
- TUIK resmi 30.87% yillik ile esler: (121.47 / 92.82 - 1) * 100 = 30.87%
