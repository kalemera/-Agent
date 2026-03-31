# Kisa Ozet

- Notebook: `DTH_Blg_V7.ipynb`
- Spec: `dth-blg-v7`
- Lane: `L2_EVDS_plus_external`
- Toplam benzersiz ticker: `54`
- Unresolved ticker: `2`

## Kod Gruplari

- `HPBITABLO2`: Toplam mevduat, kredi ve DTH payi hesaplarinin ana EVDS girdileri (27 seri)
- `HPBITABLO3`: Notebookta listelenen ancak aktif akisa baglanmayan TL mevduat alt kirilimlari (5 seri)
- `HPBITABLO4`: Yurt ici yerlesiklerin YP mevduat kirilimlari ve kisi turu/para cinsi ayrimlari (21 seri)
- `HPBITABLO5`: Parite etkisi ve haftalik degisim baglami (1 seri)

## Dis Kaynaklar

- `source:dth-old-series-excel` | DTH eski seri Excel backfill | excel_local | required_input

## Durum Etiketleri

- `derived_input`: 38
- `listed_only`: 5
- `fetched_only`: 10
- `reported_output`: 1

## Rol Etiketleri

- `stock_total`: 4
- `owner_split_line`: 8
- `currency_split_line`: 32
- `stock_component`: 4
- `dormant_candidate`: 5
- `parity_effect_input`: 1

## Tam Ticker Eslestirme

| Ticker | Resmi Seri Adi | Baglamli Ad | Durum | Rol | Birim | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `TP.HPBITABLO2.1` | A. TOPLAM MEVDUAT (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) | derived_input | stock_total | Bin TL | - |
| `TP.HPBITABLO2.2` | 1. Yurt İçi Yerleşikler (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.3` | a. TL (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.4` | I. Gerçek Kişiler (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / I. Gerçek Kişiler (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.5` | II. Tüzel Kişiler (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / II. Tüzel Kişiler (Bin TL) | derived_input | stock_component | Bin TL | - |
| `TP.HPBITABLO2.6` | b. YP (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.7` | I. Gerçek Kişiler (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / I. Gerçek Kişiler (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.8` | II. Tüzel Kişiler (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / II. Tüzel Kişiler (Bin TL) | derived_input | stock_component | Bin TL | - |
| `TP.HPBITABLO2.10` | Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları) | Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları) | derived_input | stock_total | Milyon ABD Doları | - |
| `TP.HPBITABLO2.11` | Bilgi İçin: Gerçek Kişi YP Mevduatı (Milyon ABD Doları) | Bilgi İçin: Gerçek Kişi YP Mevduatı (Milyon ABD Doları) | derived_input | stock_component | Milyon ABD Doları | - |
| `TP.HPBITABLO2.12` | Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları) | Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları) | derived_input | stock_component | Milyon ABD Doları | - |
| `TP.HPBITABLO2.13` | 2. Yurt İçi Yerleşik Bankalar (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 2. Yurt İçi Yerleşik Bankalar (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.14` | a. TL (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 2. Yurt İçi Yerleşik Bankalar (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.15` | b. YP (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 2. Yurt İçi Yerleşik Bankalar (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.16` | 3. Yurt Dışı Yerleşikler (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 3. Yurt Dışı Yerleşikler (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.17` | a. TL (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 3. Yurt Dışı Yerleşikler (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.18` | b. YP (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 3. Yurt Dışı Yerleşikler (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.19` | 4. Yurt Dışı Yerleşik Bankalar (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 4. Yurt Dışı Yerleşik Bankalar (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.20` | a. TL (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 4. Yurt Dışı Yerleşik Bankalar (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.21` | b. YP (Bin TL) | A. TOPLAM MEVDUAT (Bin TL) / 4. Yurt Dışı Yerleşik Bankalar (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.22` | B. TOPLAM KREDİ (Bin TL) | B. TOPLAM KREDİ (Bin TL) | derived_input | stock_total | Bin TL | - |
| `TP.HPBITABLO2.23` | 1. Yurt İçi Yerleşikler (Bin TL) | B. TOPLAM KREDİ (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.24` | a. TL (Bin TL) | B. TOPLAM KREDİ (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.28` | b. YP (Bin TL) | B. TOPLAM KREDİ (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.32` | 2. Yurt İçi Yerleşik Finansal Kuruluşlar (Bin TL) | B. TOPLAM KREDİ (Bin TL) / 2. Yurt İçi Yerleşik Finansal Kuruluşlar (Bin TL) | derived_input | owner_split_line | Bin TL | - |
| `TP.HPBITABLO2.33` | a. TL (Bin TL) | B. TOPLAM KREDİ (Bin TL) / 2. Yurt İçi Yerleşik Finansal Kuruluşlar (Bin TL) / a. TL (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO2.34` | b. YP (Bin TL) | B. TOPLAM KREDİ (Bin TL) / 2. Yurt İçi Yerleşik Finansal Kuruluşlar (Bin TL) / b. YP (Bin TL) | derived_input | currency_split_line | Bin TL | - |
| `TP.HPBITABLO3.1` | TOPLAM TL MEVDUAT (Bin TL) | TOPLAM TL MEVDUAT (Bin TL) | listed_only | dormant_candidate | Bin TL | - |
| `TP.HPBITABLO3.2` | A. Yurt İçi Yerleşikler (Bin TL) | A. Yurt İçi Yerleşikler (Bin TL) | listed_only | dormant_candidate | Bin TL | - |
| `TP.HPBITABLO3.18` | B. Yurt İçi Yerleşik Bankalar (Bin TL) | B. Yurt İçi Yerleşik Bankalar (Bin TL) | listed_only | dormant_candidate | Bin TL | - |
| `TP.HPBITABLO3.21` | C. Yurt Dışı Yerleşikler (Bin TL) | C. Yurt Dışı Yerleşikler (Bin TL) | listed_only | dormant_candidate | Bin TL | - |
| `TP.HPBITABLO3.24` | D. Yurt Dışı Yerleşik Bankalar (Bin TL) | D. Yurt Dışı Yerleşik Bankalar (Bin TL) | listed_only | dormant_candidate | Bin TL | - |
| `TP.HPBITABLO4.1` | TOPLAM YP MEVDUAT (Milyon ABD Doları) | TOPLAM YP MEVDUAT (Milyon ABD Doları) | fetched_only | stock_total | Milyon ABD Doları | - |
| `TP.HPBITABLO4.2` | A. Yurt İçi Yerleşikler (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.3` | 1. Gerçek Kişiler (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) | derived_input | owner_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.4` | a. ABD Doları (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / a. ABD Doları (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.5` | b. Euro - ABD Doları Karşılığı (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / b. Euro - ABD Doları Karşılığı (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.6` | c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.7` | d. Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.8` | 2. Tüzel Kişiler (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) | derived_input | owner_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.9` | a. ABD Doları (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / a. ABD Doları (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.10` | b. Euro - ABD Doları Karşılığı (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / b. Euro - ABD Doları Karşılığı (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.11` | c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.12` | d. Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı (Milyon ABD Doları) | A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı (Milyon ABD Doları) | derived_input | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.13` | B. Yurt İçi Yerleşik Bankalar (Milyon ABD Doları) | B. Yurt İçi Yerleşik Bankalar (Milyon ABD Doları) | fetched_only | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.14` | unresolved_from_notebook | - | fetched_only | currency_split_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO4.15` | unresolved_from_notebook | - | fetched_only | currency_split_line | - | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. |
| `TP.HPBITABLO4.16` | C. Yurt Dışı Yerleşikler (Milyon ABD Doları) | C. Yurt Dışı Yerleşikler (Milyon ABD Doları) | fetched_only | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.17` | a. ABD Doları (Milyon ABD Doları) | C. Yurt Dışı Yerleşikler (Milyon ABD Doları) / a. ABD Doları (Milyon ABD Doları) | fetched_only | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.18` | b. Euro - ABD Doları Karşılığı (Milyon ABD Doları) | C. Yurt Dışı Yerleşikler (Milyon ABD Doları) / b. Euro - ABD Doları Karşılığı (Milyon ABD Doları) | fetched_only | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.19` | c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları) | C. Yurt Dışı Yerleşikler (Milyon ABD Doları) / c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları) | fetched_only | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.20` | d. Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı (Milyon ABD Doları) | C. Yurt Dışı Yerleşikler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı (Milyon ABD Doları) | fetched_only | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO4.21` | D. Yurt Dışı Yerleşik Bankalar (Milyon ABD Doları) | D. Yurt Dışı Yerleşik Bankalar (Milyon ABD Doları) | fetched_only | currency_split_line | Milyon ABD Doları | - |
| `TP.HPBITABLO5.12` | Yabanci para mevduatta haftalik degisim ve parite etkisi | Yabanci para mevduatta haftalik degisim ve parite etkisi | reported_output | parity_effect_input | - | - |

## Source Dependency Eslestirme

| ID | Baslik | Kaynak Turu | Zorunluluk | Bagli Temalar | Bagli Gostergeler | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `source:dth-old-series-excel` | DTH eski seri Excel backfill | excel_local | required_input | theme:dth | - | - |

## Belirsizlikler

- TP.HPBITABLO4.14 ve TP.HPBITABLO4.15 notebooktan cozumlenemiyor.
- `TP.HPBITABLO4.14`
- `TP.HPBITABLO4.15`
