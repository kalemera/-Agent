# Kisa Ozet

- Notebook: `Eurobnd_Blg_V4.ipynb`
- Spec: `eurobnd-blg-v4`
- Lane: `L2_EVDS_plus_external`
- Toplam benzersiz ticker: `10`
- Unresolved ticker: `0`

## Kod Gruplari

- `EBONDYAZDEG`: Hazine eurobond stogu ve yabanci sahipligi serileri (2 seri)
- `YDOSBAYAZDEG`: Ozel sektor eurobond stogu ve yabanci sahipligi serileri (8 seri)

## Dis Kaynaklar

- `source:eurobnd-bbg-upload` | Eurobond BBG upload | excel_upload | required_input
- `source:eurobnd-tcmb-vade-pdf` | TCMB vade PDF | pdf_table | required_input
- `source:eurobnd-hmb-odeme-projeksiyonu` | HMB odeme projeksiyonu | excel_local | required_input

## Durum Etiketleri

- `derived_input`: 10

## Rol Etiketleri

- `stock_component`: 5
- `stock_total`: 5

## Tam Ticker Eslestirme

| Ticker | Resmi Seri Adi | Baglamli Ad | Durum | Rol | Birim | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `TP.EBONDYAZDEG.S2D` | Diğer | Diğer | derived_input | stock_component | - | - |
| `TP.EBONDYAZDEG.ST` | Toplam (S.1, S.2) | Toplam (S.1, S.2) | derived_input | stock_total | - | - |
| `TP.YDOSBAYAZDEG.S11T` | Toplam (S.1, S.2) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Toplam (S.1, S.2) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_total | - | - |
| `TP.YDOSBAYAZDEG.S122T` | Toplam (S.1, S.2) (Bankalar Tarafından İhraç Edilen) | Toplam (S.1, S.2) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_total | - | - |
| `TP.YDOSBAYAZDEG.S125T` | Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_total | - | - |
| `TP.YDOSBAYAZDEG.S126T` | Toplam (S.1, S.2) (Finansal Yardımcılar Tarafından İhraç Edilen) | Toplam (S.1, S.2) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_total | - | - |
| `TP.YDOSBAYAZDEG.S19` | Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAYAZDEG.S38` | Diğer (Bankalar Tarafından İhraç Edilen) | Diğer (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAYAZDEG.S55` | Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAYAZDEG.S76` | Diğer (Finansal Yardımcılar Tarafından İhraç Edilen) | Diğer (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |

## Source Dependency Eslestirme

| ID | Baslik | Kaynak Turu | Zorunluluk | Bagli Temalar | Bagli Gostergeler | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `source:eurobnd-bbg-upload` | Eurobond BBG upload | excel_upload | required_input | theme:eurobond, theme:external-financing | - | - |
| `source:eurobnd-tcmb-vade-pdf` | TCMB vade PDF | pdf_table | required_input | theme:eurobond, theme:external-financing | - | - |
| `source:eurobnd-hmb-odeme-projeksiyonu` | HMB odeme projeksiyonu | excel_local | required_input | theme:eurobond, theme:external-financing | - | - |

## Belirsizlikler

- Upload sheet isimleri ve HMB workbook baslik satirlari degisken olabilir.
- TCMB vade PDF baglantisi notebook icinde dinamik bulunur.
-
