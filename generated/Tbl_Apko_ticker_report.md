# Kisa Ozet

- Notebook: `Tbl_Apko.ipynb`
- Spec: `tbl-apko`
- Lane: `L3_manual_or_fallback`
- Toplam benzersiz ticker: `40`
- Unresolved ticker: `0`

## Kod Gruplari

- `AB`: Rezerv ve likidite serileri (2 seri)
- `DB`: Ceyreklik borc stogu serileri (15 seri)
- `DIBSPIYDEG`: DIBS stok serisi (1 seri)
- `DK`: Gunluk kur girdisi (1 seri)
- `EBONDPIYDEG`: Eurobond stok serisi (1 seri)
- `FDVY37`: GSYH / oran yardimci serisi (1 seri)
- `HPBITABLO4`: Yabanci para mevduat alt kirilimlari (6 seri)
- `KALANVADE`: Kalan vade aylik serileri (5 seri)
- `MKNETHAR`: Menkul kiymet akim serileri (5 seri)
- `ODANA6`: Cari denge / odeme serisi (1 seri)
- `YDOSBAYAZDEG`: Yabanci eurobond sahipligi serileri (2 seri)

## Dis Kaynaklar

- `source:tblapko-bbg-upload` | BBG workbook upload | excel_upload | required_input
- `source:tblapko-hmb-ab-borc-xls` | HMB AB borc stok XLS | excel_local | required_input
- `source:tblapko-swap-pdf` | TCMB swap PDF | pdf_table | required_input
- `source:tblapko-bddk-weekly-bulletin` | BDDK haftalik bulten | web_scrape | required_input

## Durum Etiketleri

- `derived_input`: 40

## Rol Etiketleri

- `balance_sheet_line`: 8
- `stock_total`: 3
- `stock_component`: 21
- `ratio_input`: 2
- `term_split_line`: 5
- `commentary_driver`: 1

## Tam Ticker Eslestirme

| Ticker | Resmi Seri Adi | Baglamli Ad | Durum | Rol | Birim | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `TP.HPBITABLO4.1` | Bankalar YP Mevduat Stoku | Bankalar YP Mevduat Stoku | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO4.7` | Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Gerçek Kişi, Kıymetli Maden) | Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Gerçek Kişi, Kıymetli Maden) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO4.12` | Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli Maden) | Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli Maden) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO4.16` | Bankalar YP Mevduat Stoku (Yurtdışı Yerleşikler) | Bankalar YP Mevduat Stoku (Yurtdışı Yerleşikler) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO4.20` | Bankalar YP Mevduat Stoku (Yurtdışı Yerleşikler, Kıymetli Maden) | Bankalar YP Mevduat Stoku (Yurtdışı Yerleşikler, Kıymetli Maden) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO4.21` | Bankalar YP Mevduat Stoku (Yurtdışı Yerleşik Bankalar) | Bankalar YP Mevduat Stoku (Yurtdışı Yerleşik Bankalar) | derived_input | balance_sheet_line | - | - |
| `TP.AB.N06` | TCMB Uluslararası Net Rezervler (TL) | TCMB Uluslararası Net Rezervler (TL) | derived_input | balance_sheet_line | TL | - |
| `TP.AB.TOPLAM` | TCMB Uluslararası Brüt Rezervler | TCMB Uluslararası Brüt Rezervler | derived_input | balance_sheet_line | - | - |
| `TP.DB.B01` | Toplam Brüt Dış Borç Stoku | Toplam Brüt Dış Borç Stoku | derived_input | stock_total | - | - |
| `TP.DB.B02` | Toplam Brüt Dış Borç Stoku (Kısa Vade) | Toplam Brüt Dış Borç Stoku (Kısa Vade) | derived_input | stock_total | - | - |
| `TP.DB.B03` | Kamu Brüt Dış Borç Stoku (Kısa Vade) | Kamu Brüt Dış Borç Stoku (Kısa Vade) | derived_input | stock_component | - | - |
| `TP.DB.B09` | Bankalar Brüt Dış Borç Stoku (1) | Bankalar Brüt Dış Borç Stoku (1) | derived_input | stock_component | - | - |
| `TP.DB.B11` | Reel Sektör Brüt Dış Borç Stoku (1) | Reel Sektör Brüt Dış Borç Stoku (1) | derived_input | stock_component | - | - |
| `TP.DB.B14` | TCMB Brüt Dış Borç Stoku (Kısa Vade) | TCMB Brüt Dış Borç Stoku (Kısa Vade) | derived_input | stock_component | - | - |
| `TP.DB.B17` | Bankalar Brüt Dış Borç Stoku (3) | Bankalar Brüt Dış Borç Stoku (3) | derived_input | stock_component | - | - |
| `TP.DB.B19` | Reel Sektör Brüt Dış Borç Stoku (2) | Reel Sektör Brüt Dış Borç Stoku (2) | derived_input | stock_component | - | - |
| `TP.DB.B20` | Toplam Brüt Dış Borç Stoku (Uzun Vade) | Toplam Brüt Dış Borç Stoku (Uzun Vade) | derived_input | stock_total | - | - |
| `TP.DB.B21` | Kamu Brüt Dış Borç Stoku (Uzun Vade) | Kamu Brüt Dış Borç Stoku (Uzun Vade) | derived_input | stock_component | - | - |
| `TP.DB.B27` | Bankalar Brüt Dış Borç Stoku (2) | Bankalar Brüt Dış Borç Stoku (2) | derived_input | stock_component | - | - |
| `TP.DB.B29` | Reel Sektör Brüt Dış Borç Stoku (3) | Reel Sektör Brüt Dış Borç Stoku (3) | derived_input | stock_component | - | - |
| `TP.DB.B32` | TCMB Brüt Dış Borç Stoku (Uzun Vade) | TCMB Brüt Dış Borç Stoku (Uzun Vade) | derived_input | stock_component | - | - |
| `TP.DB.B35` | Bankalar Brüt Dış Borç Stoku (4) | Bankalar Brüt Dış Borç Stoku (4) | derived_input | stock_component | - | - |
| `TP.DB.B37` | Reel Sektör Brüt Dış Borç Stoku (4) | Reel Sektör Brüt Dış Borç Stoku (4) | derived_input | stock_component | - | - |
| `TP.DIBSPIYDEG.ST` | Hazine DİBS Stoku (TL) | Hazine DİBS Stoku (TL) | derived_input | stock_component | TL | - |
| `TP.DK.USD.A.YTL` | USD/TL (Alış Kuru) | USD/TL (Alış Kuru) | derived_input | ratio_input | - | - |
| `TP.EBONDPIYDEG.ST` | Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok) | Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok) | derived_input | stock_component | Eurobond - Yaşayan Stok | - |
| `TP.FDVY37` | Reel Sektör Net Döviz Pozisyonu | Reel Sektör Net Döviz Pozisyonu | derived_input | ratio_input | - | - |
| `TP.KALANVADE.K13` | Vadesine 1 Yıldan Az Kalan Dış Borç (Ticari Krediler) | Vadesine 1 Yıldan Az Kalan Dış Borç (Ticari Krediler) | derived_input | term_split_line | - | - |
| `TP.KALANVADE.K20` | Vadesine 1 Yıldan Az Kalan Dış Borç | Vadesine 1 Yıldan Az Kalan Dış Borç | derived_input | term_split_line | - | - |
| `TP.KALANVADE.K3` | Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, DTH) | Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, DTH) | derived_input | term_split_line | - | - |
| `TP.KALANVADE.K7` | Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, Banka Mevduatı) | Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, Banka Mevduatı) | derived_input | term_split_line | - | - |
| `TP.KALANVADE.K8` | Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat) | Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat) | derived_input | term_split_line | - | - |
| `TP.MKNETHAR.M1` | Yurtdışı Yerleşikler Hisse Senedi Stoku | Yurtdışı Yerleşikler Hisse Senedi Stoku | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M2` | Yurtdışı Yerleşikler DİBS Stoku (Kesin Alım) | Yurtdışı Yerleşikler DİBS Stoku (Kesin Alım) | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M3` | Yurtdışı Yerleşikler DİBS Stoku (Ters Repo) | Yurtdışı Yerleşikler DİBS Stoku (Ters Repo) | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M4` | Yurtdışı Yerleşikler DİBS Stoku (Teminat Alım) | Yurtdışı Yerleşikler DİBS Stoku (Teminat Alım) | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M5` | Yurtdışı Yerleşikler DİBS Stoku (Ödünç Alım) | Yurtdışı Yerleşikler DİBS Stoku (Ödünç Alım) | derived_input | stock_component | - | - |
| `TP.ODANA6.Q01` | Cari Denge | Cari Denge | derived_input | commentary_driver | - | - |
| `TP.YDOSBAYAZDEG.S11T` | Reel Sektör Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok) | Reel Sektör Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok) | derived_input | stock_component | Eurobond - Yaşayan Stok | - |
| `TP.YDOSBAYAZDEG.S122T` | Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok) | Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok) | derived_input | stock_component | Eurobond - Yaşayan Stok | - |

## Source Dependency Eslestirme

| ID | Baslik | Kaynak Turu | Zorunluluk | Bagli Temalar | Bagli Gostergeler | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `source:tblapko-bbg-upload` | BBG workbook upload | excel_upload | required_input | theme:apko-summary, theme:external-financing | - | - |
| `source:tblapko-hmb-ab-borc-xls` | HMB AB borc stok XLS | excel_local | required_input | theme:external-financing | - | - |
| `source:tblapko-swap-pdf` | TCMB swap PDF | pdf_table | required_input | theme:reserves-and-liquidity | - | - |
| `source:tblapko-bddk-weekly-bulletin` | BDDK haftalik bulten | web_scrape | required_input | theme:banking-balance-sheet | - | - |

## Belirsizlikler

- Notebookta serie_info output'u yok; resmi adlar source dict ve fallback zincirinden cozumlenir.
- Coklu frekans bloklari ayni makro tabloda birlesir.
-
