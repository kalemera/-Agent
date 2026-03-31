# Kisa Ozet

- Notebook: `Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb`
- Spec: `yi-yrlsk-fnsl-vrlk-v1`
- Lane: `L1_EVDS_standard`
- Toplam benzersiz ticker: `84`
- Unresolved ticker: `6`

## Kod Gruplari

- `DIBSPIYDEG`: Ozel sektor tahvil stogu ve alt kirilimlari (6 seri)
- `DK`: Kur cevirim girdisi (1 seri)
- `EBONDPIYDEG`: Ozel sektor eurobond stogu ve alt kirilimlari (6 seri)
- `HPBITABLO1`: Fon ve benzeri mevduat/fon kalemleri (3 seri)
- `HPBITABLO2`: TL ve YP mevduat kirilimlari (22 seri)
- `YDOSBAPIYDEG`: Yurt disi yerlesiklerin tahvil/eurobond alt kirilimlari (23 seri)
- `YIOSBAPIYDEG`: Yurt ici yerlesiklerin tahvil/eurobond alt kirilimlari (23 seri)

## Dis Kaynaklar

- `source:yiyrlsk-mkk-hisse-manual` | MKK hisse manuel ledger | manual_inline | required_input
- `source:yiyrlsk-mkk-fon-manual` | MKK fon manuel ledger | manual_inline | required_input
- `source:yiyrlsk-vap-scrape-attempt` | VAP scrape denemesi | web_scrape | optional_replacement

## Durum Etiketleri

- `derived_input`: 84

## Rol Etiketleri

- `balance_sheet_line`: 16
- `stock_total`: 3
- `owner_split_line`: 2
- `currency_split_line`: 4
- `stock_component`: 58
- `ratio_input`: 1

## Tam Ticker Eslestirme

| Ticker | Resmi Seri Adi | Baglamli Ad | Durum | Rol | Birim | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `TP.HPBITABLO1.19` | Repo (Bin TL) | Repo (Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.HPBITABLO1.20` | Para Piyasası Fonları (Bin TL) | Para Piyasası Fonları (Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.HPBITABLO1.21` | İhraç Edilen Menkul Kıymetler (Bin TL) | İhraç Edilen Menkul Kıymetler (Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.HPBITABLO2.2` | TL+YP Mevduat (Toplam, Bankalar Hariç) | TL+YP Mevduat (Toplam, Bankalar Hariç) | derived_input | stock_total | - | - |
| `TP.HPBITABLO2.3` | TL Mevduat (Toplam, Bankalar Hariç) | TL Mevduat (Toplam, Bankalar Hariç) | derived_input | stock_total | - | - |
| `TP.HPBITABLO2.4` | TL Mevduat (Gerçek Kişi) | TL Mevduat (Gerçek Kişi) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO2.5` | TL Mevduat (Tüzel Kişi) | TL Mevduat (Tüzel Kişi) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO2.6` | YP Mevduat (Toplam, Bankalar Hariç) | YP Mevduat (Toplam, Bankalar Hariç) | derived_input | stock_total | - | - |
| `TP.HPBITABLO2.7` | YP Mevduat (Gerçek Kişi) | YP Mevduat (Gerçek Kişi) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO2.8` | YP Mevduat (Tüzel Kişi) | YP Mevduat (Tüzel Kişi) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO2.13` | TL+YP Mevduat (Bankalar) | TL+YP Mevduat (Bankalar) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO2.14` | TL Mevduat (Bankalar) | TL Mevduat (Bankalar) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO2.15` | YP Mevduat (Bankalar) | YP Mevduat (Bankalar) | derived_input | balance_sheet_line | - | - |
| `TP.HPBITABLO2.23` | 1. Yurt Ici Yerlesikler (Bin TL) | 1. Yurt Ici Yerlesikler (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.24` | a. TL (Bin TL) | 1. Yurt Ici Yerlesikler (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.25` | unresolved_from_notebook | - | derived_input | balance_sheet_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO2.26` | unresolved_from_notebook | - | derived_input | balance_sheet_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO2.27` | unresolved_from_notebook | - | derived_input | balance_sheet_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO2.28` | b. YP (Bin TL) | 1. Yurt Ici Yerlesikler (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.29` | unresolved_from_notebook | - | derived_input | balance_sheet_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO2.30` | unresolved_from_notebook | - | derived_input | balance_sheet_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO2.31` | unresolved_from_notebook | - | derived_input | balance_sheet_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO2.32` | 2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL) | 2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.33` | a. TL (Bin TL) | 2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.34` | b. YP (Bin TL) | 2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.DIBSPIYDEG.S11` | Finansal Olmayan Kuruluşlar (S.11) | Finansal Olmayan Kuruluşlar (S.11) | derived_input | stock_component | - | - |
| `TP.DIBSPIYDEG.S12` | Finansal Kuruluşlar (S.12) | Finansal Kuruluşlar (S.12) | derived_input | stock_component | - | - |
| `TP.DIBSPIYDEG.S122` | Bankalar (S.122) | Bankalar (S.122) | derived_input | stock_component | - | - |
| `TP.DIBSPIYDEG.S13` | Genel Yönetim (S.13) | Genel Yönetim (S.13) | derived_input | stock_component | - | - |
| `TP.DIBSPIYDEG.S14` | Hanehalkı (S.14) | Hanehalkı (S.14) | derived_input | stock_component | - | - |
| `TP.DIBSPIYDEG.S15` | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) | derived_input | stock_component | - | - |
| `TP.DK.USD.A.YTL` | USD/TL (Alis Kuru) | USD/TL (Alis Kuru) | derived_input | ratio_input | - | - |
| `TP.EBONDPIYDEG.S11` | Finansal Olmayan Kuruluşlar (S.11) | Finansal Olmayan Kuruluşlar (S.11) | derived_input | stock_component | - | - |
| `TP.EBONDPIYDEG.S12` | Finansal Kuruluşlar (S.12) | Finansal Kuruluşlar (S.12) | derived_input | stock_component | - | - |
| `TP.EBONDPIYDEG.S122` | Bankalar (S.122) | Bankalar (S.122) | derived_input | stock_component | - | - |
| `TP.EBONDPIYDEG.S13` | Genel Yönetim (S.13) | Genel Yönetim (S.13) | derived_input | stock_component | - | - |
| `TP.EBONDPIYDEG.S14` | Hanehalkı (S.14) | Hanehalkı (S.14) | derived_input | stock_component | Milyon ABD Dolari | Notebookta USD/TL ile carpilarak 'Eurobond (Gercek Kisi)' TL karsiligina cevriliyor. |
| `TP.EBONDPIYDEG.S15` | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S11` | Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S15` | Hanehalkı (S.14) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Hanehalkı (S.14) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | Milyon ABD Dolari | Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor. |
| `TP.YDOSBAPIYDEG.S16` | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S2` | Finansal Olmayan Kuruluşlar (S.11) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S21` | Finansal Olmayan Kuruluşlar (S.11) (Bankalar Tarafından İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S22` | Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen) | Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S24` | Bankalar (S.122) (Bankalar Tarafından İhraç Edilen) | Bankalar (S.122) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S3` | Finansal Kuruluşlar (S.12) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Finansal Kuruluşlar (S.12) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S30` | Genel Yönetim (S.13) (Bankalar Tarafından İhraç Edilen) | Genel Yönetim (S.13) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S34` | Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen) | Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | Milyon ABD Dolari | Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor. |
| `TP.YDOSBAPIYDEG.S40` | Finansal Olmayan Kuruluşlar (S.11) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S41` | Finansal Kuruluşlar (S.12) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Finansal Kuruluşlar (S.12) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S43` | Bankalar (S.122) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Bankalar (S.122) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S49` | Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S5` | Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S53` | Hanehalkı (S.14) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Hanehalkı (S.14) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | Milyon ABD Dolari | Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor. |
| `TP.YDOSBAPIYDEG.S54` | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S59` | Finansal Olmayan Kuruluşlar (S.11) (Finansal Yardımcılar Tarafından İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S60` | Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç Edilen) | Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S62` | Bankalar (S.122) (Finansal Yardımcılar Tarafından İhraç Edilen) | Bankalar (S.122) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S68` | Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen) | Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YDOSBAPIYDEG.S72` | Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen) | Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | Milyon ABD Dolari | Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor. |
| `TP.YDOSBAPIYDEG.S74` | Dünyanın Geri Kalanı (S.2) (Finansal Yardımcılar Tarafından İhraç Edilen) | Dünyanın Geri Kalanı (S.2) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S11` | Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S15` | Hanehalkı (S.14) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Hanehalkı (S.14) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S16` | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S2` | Finansal Olmayan Kuruluşlar (S.11) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S21` | Finansal Olmayan Kuruluşlar (S.11) (Bankalar Tarafından İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S22` | Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen) | Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S24` | Bankalar (S.122) (Bankalar Tarafından İhraç Edilen) | Bankalar (S.122) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S3` | Finansal Kuruluşlar (S.12) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Finansal Kuruluşlar (S.12) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S30` | Genel Yönetim (S.13) (Bankalar Tarafından İhraç Edilen) | Genel Yönetim (S.13) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S34` | Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen) | Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S40` | Finansal Olmayan Kuruluşlar (S.11) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S41` | Finansal Kuruluşlar (S.12) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Finansal Kuruluşlar (S.12) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S43` | Bankalar (S.122) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Bankalar (S.122) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S49` | Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S5` | Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S53` | Hanehalkı (S.14) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Hanehalkı (S.14) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S54` | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Diğer Finansal Aracılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S59` | Finansal Olmayan Kuruluşlar (S.11) (Finansal Yardımcılar Tarafından İhraç Edilen) | Finansal Olmayan Kuruluşlar (S.11) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S60` | Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç Edilen) | Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S62` | Bankalar (S.122) (Finansal Yardımcılar Tarafından İhraç Edilen) | Bankalar (S.122) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S68` | Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen) | Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S72` | Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen) | Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |
| `TP.YIOSBAPIYDEG.S74` | Dünyanın Geri Kalanı (S.2) (Finansal Yardımcılar Tarafından İhraç Edilen) | Dünyanın Geri Kalanı (S.2) (Finansal Yardımcılar Tarafından İhraç Edilen) | derived_input | stock_component | - | - |

## Source Dependency Eslestirme

| ID | Baslik | Kaynak Turu | Zorunluluk | Bagli Temalar | Bagli Gostergeler | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `source:yiyrlsk-mkk-hisse-manual` | MKK hisse manuel ledger | manual_inline | required_input | theme:resident-financial-assets, theme:resident-securities | - | - |
| `source:yiyrlsk-mkk-fon-manual` | MKK fon manuel ledger | manual_inline | required_input | theme:resident-financial-assets, theme:resident-securities | - | - |
| `source:yiyrlsk-vap-scrape-attempt` | VAP scrape denemesi | web_scrape | optional_replacement | theme:resident-securities | - | - |

## Belirsizlikler

- MKK manuel ledger bloklari notebook icinde gomulu oldugundan source dependency olarak izlenmelidir.
- VAP scrape denemesi aktif bir veri kaynagi degildir.
- `TP.HPBITABLO2.25`
- `TP.HPBITABLO2.26`
- `TP.HPBITABLO2.27`
- `TP.HPBITABLO2.29`
- `TP.HPBITABLO2.30`
- `TP.HPBITABLO2.31`
