---
record_type: source_dependency
id: source:tufe-ozel-kapsamli
title: Ozel Kapsamli TUFE Gostergeleri XLSX (TUIK)
status: approved
source_kind: tuik_press_xlsx_masked_as_xls
requiredness: required
source_uri: https://veriportali.tuik.gov.tr/tr/press/58295
local_hint: TUFE/downloads/tufe/Ozel-Kapsamli-TUFE-Gostergeleri.xls
description: Cekirdek enflasyon gostergeleri (A-F) + Mallar/Hizmet alt kirilimlari (27 gosterge, zaman serisi)
usage: pipelines/tufe_parser.py -> parse_ozel_kapsamli() ile okunur, tufe_core tablosuna yazilir
theme_ids:
- theme:tufe
indicator_ids:
- derived:cekirdek-tufe-c
- derived:cekirdek-tufe-b
- derived:mallar-endeks
- derived:hizmet-endeks
validation_note: Dosya .xls uzantili ama gercekte XLSX. shutil.copy + openpyxl ile acilir. 183 satir x 258 sutun.
---
# Ozel Kapsamli TUFE Gostergeleri (Cekirdek + Mallar + Hizmet)

## Kaynak Turu
tuik_press_xlsx_masked_as_xls (t=i download link)

## KRITIK GOTCHA
Dosya `.xls` uzantili ama gercekte **XLSX** formatinda. `xlrd` ile acilmaz:
- `shutil.copy` ile gecici `.xlsx` dosyaya kopyala
- `openpyxl.load_workbook(data_only=True)` ile ac
- `read_only=False` (read_only=True Windows'ta WinError 32 verir — temp file locked)
- Try/finally ile `wb.close()` ve temp file cleanup

## Zorunluluk
required

## Kaynak URI
https://veriportali.tuik.gov.tr/tr/press/58295

## Local Hint
`TUFE/downloads/tufe/Ozel-Kapsamli-TUFE-Gostergeleri.xls`

## Dosya Yapisi (183 satir x 258 sutun)
- **R6**: Yil satiri (col4+ = 2005, 2005, 2005, ..., 2026, 2026, 2026)
- **R7**: Ay adlari Turkce (col4+ = Ocak, Subat, Mart, ..., Aralik)
- **R8**: Ay adlari Ingilizce (skip)
- **R9**: Section header "1. Ozel kapsamli TUFE gostergeleri"
- **R10-R15**: A, B, C, D, E, F cekirdek gostergeler (col1=kod, col2=TR ad, col3=EN ad, col4+=endeks)
- **R16**: "2. Mallar" header + aggregate endeks
- **R17-R30**: Mallar alt kirilimlari (14 satir: Enerji, Gida, Islenmemis gida, Taze meyve-sebze, Diger islenmemis, Islenmis gida, Ekmek-tahillar, Diger islenmis, Enerji ve gida disi mallar, Temel mallar, Giyim-ayakkabi, Dayanikli mallar (altin haric), Diger temel, Alkol-tutun-altin)
- **R31**: "3. Hizmet" header + aggregate endeks
- **R32-R36**: Hizmet alt kirilimlari (5 satir: Kira, Lokanta-oteller, Ulastirma hizmetleri, Haberlesme hizmetleri, Diger hizmetler)
- **R38+**: Ek bolumler (Aylik degisim %, YTD %, Yillik %, 12A ortalama) — pipeline kullanmiyor, endeksten hesapliyoruz

## Indicator Code Scheme
- `A` - `F`: Cekirdek gostergeler (A-F)
- `M_TOTAL`: Mallar aggregate
- `M_01` - `M_14`: Mallar alt kirilimlari
- `H_TOTAL`: Hizmet aggregate
- `H_01` - `H_05`: Hizmet alt kirilimlari

## Kullanim
- Parser: `pipelines/tufe_parser.py::parse_ozel_kapsamli()`
- DB hedef: `tufe_core` tablosu
- 27 gosterge x 255 donem = ~6885 satir
- Aylik/yillik % endeks farkindan rapportta hesaplanir

## Dogrulama Notlari
- Base yil 2025=100
- **Cekirdek C** (KULLANDIGIMIZ): "Enerji, gida ve alkolsuz icecekler, alkollu ickiler ile tutun urunleri ve altin haric TUFE" — rapport ve ozet tabloda bu gosterge
- Cekirdek B: "Islenmemis gida urunleri, enerji, alkollu ickiler ve tutun ile altin haric TUFE" (alternatif olcut)
