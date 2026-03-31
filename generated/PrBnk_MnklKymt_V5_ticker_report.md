# Kisa Ozet

- Notebook: `PrBnk_MnklKymt_V5.ipynb`
- Spec: `prbnk-mnklkymt-v5`
- Lane: `L2_EVDS_plus_external`
- Toplam benzersiz ticker: `57`
- Unresolved ticker: `0`

## Kod Gruplari

- `AB`: Rezerv/swap ve destekleyici analitik bilanco serileri (15 seri)
- `DIBSPIYDEG`: DIBS stogu ve yabanci sahipligi (1 seri)
- `DK`: Kur cevirim girdisi (1 seri)
- `HPBITABLO5`: Mevduat ve parite yardimci serileri (22 seri)
- `MKNETHAR`: Menkul kiymet stok ve net hareket serileri (18 seri)

## Dis Kaynaklar

- `source:prbnk-weekly-zip` | TCMB haftalik ZIP/XLSX | http_download | required_input
- `source:prbnk-swap-pdf` | TCMB swap PDF | pdf_table | required_input

## Durum Etiketleri

- `derived_input`: 57

## Rol Etiketleri

- `currency_split_line`: 17
- `owner_split_line`: 4
- `parity_effect_input`: 1
- `balance_sheet_line`: 15
- `stock_component`: 16
- `ratio_input`: 1
- `stock_total`: 3

## Tam Ticker Eslestirme

| Ticker | Resmi Seri Adi | Baglamli Ad | Durum | Rol | Birim | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `TP.HPBITABLO5.1` | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.2` | 1. Gerçek Kişiler (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) | derived_input | owner_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.3` | a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.4` | b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.5` | c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.6` | d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.7` | 2. Tüzel Kişiler (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) | derived_input | owner_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.8` | a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.9` | b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.10` | c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.11` | d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.12` | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) | derived_input | parity_effect_input | Milyon ABD Doları | - |
| `TP.HPBITABLO5.13` | 1. Gerçek Kişiler (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) | derived_input | owner_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.14` | a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.15` | b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.16` | c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.17` | d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.18` | 2. Tüzel Kişiler (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) | derived_input | owner_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.19` | a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / a. ABD Doları Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.20` | b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / b. Euro Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.21` | c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.22` | d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.AB.A01` | A.AKTİF(Bin TL) | A.AKTİF(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A02` | A.1_DIŞ VARLIKLAR(Bin TL) | A.1_DIŞ VARLIKLAR(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A03` | A.2_İÇ VARLIKLAR(Bin TL) | A.2_İÇ VARLIKLAR(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A08` | A.3_DEĞERLEME HESABI(BİN TL) | A.3_DEĞERLEME HESABI(BİN TL) | derived_input | balance_sheet_line | BİN TL | - |
| `TP.AB.A09` | P.PASİF(Bin TL) | P.PASİF(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A11` | P.1a_Dış Yükümlülükler(Bin TL) | P.1a_Dış Yükümlülükler(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A12` | P.1b_İç Yükümlülükler(Bin TL) | P.1b_İç Yükümlülükler(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A15` | P.2_MERKEZ BANKASI PARASI(Bin TL) | P.2_MERKEZ BANKASI PARASI(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A16` | P.2A_Rezerv Para(Bin TL) | P.2A_Rezerv Para(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A17` | P.2Aa_Emisyon(Bin TL) | P.2Aa_Emisyon(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A18` | P.2Ab_Bankalar Mevduatı(Bin TL) | P.2Ab_Bankalar Mevduatı(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A23` | P.2B_Diğer Merkez Bankası Parası(Bin TL) | P.2B_Diğer Merkez Bankası Parası(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.C1` | I-Altın | I-Altın | derived_input | balance_sheet_line | - | - |
| `TP.AB.C2` | II-Döviz | II-Döviz | derived_input | balance_sheet_line | - | - |
| `TP.AB.TOPLAM` | MERKEZ BANKASI REZERVLERİ (Milyon usd) (**) | MERKEZ BANKASI REZERVLERİ (Milyon usd) (**) | derived_input | balance_sheet_line | Milyon usd | - |
| `TP.DIBSPIYDEG.ST` | DİBS (Tüm Stok, Piyasa Değeri) | DİBS (Tüm Stok, Piyasa Değeri) | derived_input | stock_component | - | - |
| `TP.DK.USD.A.YTL` | USD/TL (Alış Kuru) | USD/TL (Alış Kuru) | derived_input | ratio_input | - | - |
| `TP.MKNETHAR.M1` | 1.1.1. Hisse Senedi, Stok | 1.1.1. Hisse Senedi, Stok | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M10` | 2.1.4. DİBS (Teminat Alım), Net Değişim | 2.1.4. DİBS (Teminat Alım), Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M11` | 2.1.5. DİBS (Ödünç Alım), Net Değişim | 2.1.5. DİBS (Ödünç Alım), Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M12` | 2.1.6. Genel Yönetim Dışındaki Sektörlerce İhraç Edilen Borçlanma Senetleri, Net Değişim | 2.1.6. Genel Yönetim Dışındaki Sektörlerce İhraç Edilen Borçlanma Senetleri, Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M2` | 1.1.2. DİBS (Kesin Alım), Stok | 1.1.2. DİBS (Kesin Alım), Stok | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M20` | 2. Net Değişim Genel Toplam, Net Değişim | 2. Net Değişim Genel Toplam, Net Değişim | derived_input | stock_total | - | - |
| `TP.MKNETHAR.M21` | 2.1. Yurt İçi Piyasa Toplam, Net Değişim | 2.1. Yurt İçi Piyasa Toplam, Net Değişim | derived_input | stock_total | - | - |
| `TP.MKNETHAR.M22` | 2.2. Yurt Dışı Piyasa Toplam, Net Değişim | 2.2. Yurt Dışı Piyasa Toplam, Net Değişim | derived_input | stock_total | - | - |
| `TP.MKNETHAR.M23` | 2.2.1. Genel Yönetim İhraçları, Net Değişim | 2.2.1. Genel Yönetim İhraçları, Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M24` | 2.2.2. Finansal Olmayan Kuruluş İhraçları, Net Değişim | 2.2.2. Finansal Olmayan Kuruluş İhraçları, Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M25` | 2.2.3. Banka İhraçları, Net Değişim | 2.2.3. Banka İhraçları, Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M26` | 2.2.4. Diğer Finansal Kuruluş İhraçları, Net Değişim | 2.2.4. Diğer Finansal Kuruluş İhraçları, Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M3` | 1.1.3. DİBS (Ters Repo), Stok | 1.1.3. DİBS (Ters Repo), Stok | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M4` | 1.1.4. DİBS (Teminat Alım), Stok | 1.1.4. DİBS (Teminat Alım), Stok | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M5` | 1.1.5. DİBS (Ödünç Alım), Stok | 1.1.5. DİBS (Ödünç Alım), Stok | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M7` | 2.1.1. Hisse Senedi, Net Değişim | 2.1.1. Hisse Senedi, Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M8` | 2.1.2. DİBS (Kesin Alım), Net Değişim | 2.1.2. DİBS (Kesin Alım), Net Değişim | derived_input | stock_component | - | - |
| `TP.MKNETHAR.M9` | 2.1.3. DİBS (Ters Repo), Net Değişim | 2.1.3. DİBS (Ters Repo), Net Değişim | derived_input | stock_component | - | - |

## Source Dependency Eslestirme

| ID | Baslik | Kaynak Turu | Zorunluluk | Bagli Temalar | Bagli Gostergeler | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `source:prbnk-weekly-zip` | TCMB haftalik ZIP/XLSX | http_download | required_input | theme:portfolio-flows, theme:foreign-ownership | - | - |
| `source:prbnk-swap-pdf` | TCMB swap PDF | pdf_table | required_input | theme:swap-and-securities | - | - |

## Belirsizlikler

- Notebookta aktif ve legacy/commented extraction bloklari birlikte duruyor; dormant adaylar aktif akisla karistirilmamali.
-
