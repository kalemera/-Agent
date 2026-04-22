---
record_type: source_dependency
id: source:tufe-zaman-serisi
title: TUFE Zaman Serisi XLS (TUIK)
status: approved
source_kind: tuik_press_xls
requiredness: required
source_uri: https://veriportali.tuik.gov.tr/tr/press/58295
local_hint: TUFE/downloads/tufe/Tuketici-fiyat-endeksi-ve-degisim-oranlari.xls
description: TUIK TUFE haber bulteni ekindeki genel endeks zaman serisi dosyasi (2005-bugun aylik)
usage: pipelines/tufe_parser.py -> parse_zaman_serisi() ile okunur, tufe_monthly tablosuna yazilir
theme_ids:
- theme:tufe
indicator_ids: []
validation_note: 4 bolumlu (endeks, aylik %, YTD %, yillik %). Pattern tabanli section detection. Min 20 satir beklenir.
---
# TUFE Zaman Serisi XLS

## Kaynak Turu
tuik_press_xls (t=i download link)

## Zorunluluk
required

## Kaynak URI
https://veriportali.tuik.gov.tr/tr/press/58295

## Indirme Yolu
Playwright ile press sayfasindan "Tuketici fiyat endeksi ve degisim oranlari" link'i bulunup indirilir.
Sync wrapper: `pipelines/tufe_fetcher.py::fetch_tufe_files()`

## Local Hint
`TUFE/downloads/tufe/Tuketici-fiyat-endeksi-ve-degisim-oranlari.xls`

## Dosya Yapisi
- 4 bolumlu wide XLS (255+ satir, 13 sutun)
- Bolumler: endeks degerleri | bir onceki aya gore % | YTD % | yillik %
- Her bolumde Yil | Ocak..Aralik layout
- Parser pattern tabanli (SECTION_PATTERNS regex)

## Kullanim
- Parser: `pipelines/tufe_parser.py::parse_zaman_serisi()`
- DB hedef: `tufe_monthly` tablosu (year, month, index_value, monthly_pct, ytd_pct, annual_pct, avg_12m_pct)
- Pipeline: `pipelines/tufe_pipeline.py::run_pipeline()`

## Dogrulama Notlari
- CP#3: Magic bytes (XLS = D0CF11E0)
- CP#4: Min 20 satir
- CP#5: Son donem max 60 gun eski olmali
- CP#7: SHA-256 checksum uniqueness

## Press ID
58295 (kalici seri id'si, her ay yeni bulten ayni ID altinda)
