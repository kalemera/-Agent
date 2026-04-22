---
record_type: source_dependency
id: source:yufe-tarihsel-seri
title: Yi-UFE Tarihsel Seri XLS (TUIK)
status: approved
source_kind: tuik_press_xls
requiredness: required
source_uri: https://veriportali.tuik.gov.tr/tr/press/58029
local_hint: TUFE/downloads/yufe/Yurt-Ici-Uretici-Fiyat-Endeksi-ve-Degisim-Oranlari-Tarihsel-Seri.xls
description: Yurt Ici Uretici Fiyat Endeksi zaman serisi 1982-bugun aylik (5 section wide format)
usage: pipelines/tufe_parser.py -> parse_yufe() ile okunur, yufe_monthly tablosuna yazilir
theme_ids:
- theme:tufe
indicator_ids: []
validation_note: Wide format, 5 section (Endeks, Aylik %, YTD %, Yillik %, 12A Ortalama). 267 satir x 13 sutun.
---
# Yi-UFE Tarihsel Seri

## Kaynak Turu
tuik_press_xls (t=i download link)

## Zorunluluk
required

## Kaynak URI
https://veriportali.tuik.gov.tr/tr/press/58029

## Local Hint
`TUFE/downloads/yufe/Yurt-Ici-Uretici-Fiyat-Endeksi-ve-Degisim-Oranlari-Tarihsel-Seri.xls`

## Dosya Yapisi (267 satir x 13 sutun, wide format)

### 5 Section (ayni layout)
1. **R3-R54**: "Endeks Degerleri" — endeks degerleri
2. **R55-R105**: "Bir onceki Aya Gore Degisim Orani (%)" — aylik %
3. **R106-R156**: "Bir onceki Yilin Aralik Ayina Gore Degisim Orani (%)" — YTD %
4. **R157-R207**: "Yillik Degisim (Bir onceki yilin ayni ayina gore)" — yillik %
5. **R208-R257**: "On Iki Aylik Ortalamalara Gore Degisim Orani (%)" — 12A ortalama

Her section'da:
- Baslik satiri (TR + EN)
- Header: Yil | Ocak | Subat | ... | Aralik
- Veri: Yil (1982-2026) | 12 ay degerleri
- Eski yil suffixleri: 1982(1), 1991(2), 1996(3), 2006(4) — farkli base yil TEFE/UFE donemlerini gosterir

## Press ID
**58029** (kalici seri id'si — TCMB TUFE'nin 58295 ile beraber ayni portalda)

## Kullanim
- Parser: `pipelines/tufe_parser.py::parse_yufe()`
- DB hedef: `yufe_monthly` tablosu (year, month, index_value, monthly_pct, ytd_pct, annual_pct, avg_12m_pct)
- 531 satir (1982-01 -> 2026-03)

## Base Yil
2003=100 — Yi-UFE'nin base yili TUFE'den (2025=100) farklidir. Seviye karsilastirmasi yaparken dikkat.

## Dogrulama Notlari
- Son donem 2026-03 Yi-UFE: endeks=5145.36, yillik=%28.08, aylik=%2.30
- TUIK resmi haber bulteni verileriyle eslesmelidir
- Year regex: `r"^(\d{4})"` — yil suffix'ini (1), (2), (3), (4) atla
