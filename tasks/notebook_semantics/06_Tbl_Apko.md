---
task_id: notebook-semantics-06-tbl-apko
notebook_path: ../Telegram Bot/notebooks/Tbl_Apko.ipynb
lane: L3_manual_or_fallback
priority: P3
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
  - tasks/notebook_semantics/02_Eurobnd_Blg_V4.md
  - tasks/notebook_semantics/05_Rzrv_Blg_V7.md
evds_code_families:
  - TP.AB
  - TP.DB
  - TP.DIBSPIYDEG
  - TP.DK
  - TP.EBONDPIYDEG
  - TP.FDVY37
  - TP.HPBITABLO4
  - TP.KALANVADE
  - TP.MKNETHAR
  - TP.ODANA6
  - TP.YDOSBAYAZDEG
external_inputs:
  - excel_upload:eurobond-bbg-workbook
  - excel_local:hmb-ab-borc-stok-xls
  - pdf_table:tcmb-swap-pdf
  - web_scrape:bddk-weekly-bulletin
target_outputs:
  - generated/Tbl_Apko_ticker_report.md
  - generated/Tbl_Apko_registry_import.csv
known_blockers:
  - notebook stores no serialized serie_info mapping
  - multiple frequencies must be aligned before semantic labeling
  - EVDS and four external source blocks are merged into one macro table
---

# Tbl_Apko

## Amac

Bu notebook, APKO tablo setini olusturan en karma kaynakli akistir. Gorev, once veri kaynak bloklarini ayrismak, sonra her EVDS serisini ve dis kaynagi tek bir registry haritasina baglamak, en sonda makro tablo indicator setini kontrollu olarak tanimlamaktir.

## Mevcut Notebook Gercekleri

- Notebookta `serie_info` output'u yoktur.
- `40` benzersiz EVDS kodu vardir.
- EVDS fetch'leri frekans bazinda dort bloga ayrilmistir:
  - gunluk
  - haftalik
  - aylik
  - ceyreklik
- Dis kaynaklar:
  - kullanici yuklemeli BBG workbook
  - HMB AB borc stok XLS
  - TCMB swap PDF
  - BDDK haftalik bulletin scrape
- Notebook sonunda bir makro tablo ve birden fazla sentez kolon uretilir.

## EVDS Kod Envanteri

### Aile ozetleri

- `TP.AB`: `2`
- `TP.DB`: `15`
- `TP.DIBSPIYDEG`: `1`
- `TP.DK`: `1`
- `TP.EBONDPIYDEG`: `1`
- `TP.FDVY37`: `1`
- `TP.HPBITABLO4`: `6`
- `TP.KALANVADE`: `5`
- `TP.MKNETHAR`: `5`
- `TP.ODANA6`: `1`
- `TP.YDOSBAYAZDEG`: `2`

### Tam kod listesi

```text
TP.AB:
TP.AB.N06, TP.AB.TOPLAM

TP.DB:
TP.DB.B01, TP.DB.B02, TP.DB.B03, TP.DB.B09, TP.DB.B11, TP.DB.B14, TP.DB.B17, TP.DB.B19, TP.DB.B20, TP.DB.B21, TP.DB.B27, TP.DB.B29, TP.DB.B32, TP.DB.B35, TP.DB.B37

TP.DIBSPIYDEG:
TP.DIBSPIYDEG.ST

TP.DK:
TP.DK.USD.A.YTL

TP.EBONDPIYDEG:
TP.EBONDPIYDEG.ST

TP.FDVY37:
TP.FDVY37

TP.HPBITABLO4:
TP.HPBITABLO4.1, TP.HPBITABLO4.12, TP.HPBITABLO4.16, TP.HPBITABLO4.20, TP.HPBITABLO4.21, TP.HPBITABLO4.7

TP.KALANVADE:
TP.KALANVADE.K13, TP.KALANVADE.K20, TP.KALANVADE.K3, TP.KALANVADE.K7, TP.KALANVADE.K8

TP.MKNETHAR:
TP.MKNETHAR.M1, TP.MKNETHAR.M2, TP.MKNETHAR.M3, TP.MKNETHAR.M4, TP.MKNETHAR.M5

TP.ODANA6:
TP.ODANA6.Q01

TP.YDOSBAYAZDEG:
TP.YDOSBAYAZDEG.S11T, TP.YDOSBAYAZDEG.S122T
```

## Dis Kaynak Envanteri

- `source:tblapko-bbg-upload`
  - `source_kind=excel_upload`
  - `requiredness=required_input`
  - amac: Eurobond ihraclari/BBG tablolari

- `source:tblapko-hmb-ab-borc-xls`
  - `source_kind=excel_local`
  - `requiredness=required_input`
  - amac: Avrupa Birligi tanimli genel yonetim borc stoku tablosu

- `source:tblapko-swap-pdf`
  - `source_kind=pdf_table`
  - `requiredness=required_input`
  - amac: TCMB tarafli swap islemleri tablosu

- `source:tblapko-bddk-weekly-bulletin`
  - `source_kind=web_scrape`
  - `requiredness=required_input`
  - amac: TL/YP krediler ve YPNG/Yasal Ozkaynak tablolari

## Beklenen Registry Nesneleri

### Theme

- `theme:apko-summary`
- `theme:external-financing`
- `theme:banking-balance-sheet`
- `theme:reserves-and-liquidity`

### Indicator

Ilk fazda en az su indicator seti beklenir:

- `derived:usdtry-buy-rate`
- `derived:bank-tl-loans`
- `derived:bank-fx-loans`
- `derived:ypng-to-equity`
- `derived:foreign-dibs-stock-all-in`
- `derived:bank-fx-deposit-precious-metals`
- `derived:12m-cumulative-current-account`
- `derived:foreign-resident-deposits-short-term`
- `derived:gross-external-debt-to-gdp`
- `derived:tcmb-gross-reserves`
- `derived:tcmb-net-reserves`

### Source dependency

- `source:tblapko-bbg-upload`
- `source:tblapko-hmb-ab-borc-xls`
- `source:tblapko-swap-pdf`
- `source:tblapko-bddk-weekly-bulletin`

## Analyzer Kurallari

- Resmi ad icin birincil kaynak `serie_names_apko_*` dict'leridir.
- `gunluk`, `haftalik`, `aylik`, `ceyreklik` bloklari farkli alt spec'ler gibi dusunulecek, ama tek notebook raporunda birlestirilecektir.
- Frequency alignment sonrasi indicator yazilacak; alignment oncesi ham seri semantigi yine registry'de korunur.
- `TP.HPBITABLO4.*` alt kumesi burada DTH notebookundaki gibi tam hiyerarsiyle degil, notebookun explicit business labels'i ile etiketlenmelidir.
- BDDK scrape sonucu gelen kolonlar `source_dependency` icinde belgelenir; EVDS series gibi id uretilmez.
- HMB ve BBG workbook'leri indicator anlamini destekledigi icin sadece not degil, gercek dependency kaydidir.

## Turetilmis Gostergeler

Notebookta gorunen ana sentez kolonlari:

- Toplam Banka Dis Finansman
- Toplam Hazine YP Borclanma Ihrac
- Yurtdisi Yerlesikler DIBS Stoku (Repo, Odunc, Teminat Dahil)
- Bankalar YP Mevduat Stoku (Kiymetli Maden)
- 12 Aylik Kumulatif Cari Denge
- Yurtdisi Yerlesikler Mevduati
- Kamu Brut Dis Borc Stoku
- TCMB Brut Dis Borc Stoku
- Reel Sektor Brut Dis Borc Stoku
- Bankalar Brut Dis Borc Stoku
- Toplam Brut Dis Borc Stoku (%, GSYH)

Karar:

- Ilk implementasyon tum tablo kolonlarini indicator yapmayacak.
- Yukaridaki sentez kolonlari ve bunlari dogrudan besleyen EVDS/dis kaynak baglari kayda gecirilecek.

## Cozumsuzler ve Fallback

Fallback sirasi:

1. `serie_names_apko_gunluk`
2. `serie_names_apko_haftalik`
3. `serie_names_apko_aylik`
4. `serie_names_apko_ceyreklik`
5. explicit derived kolon adlari
6. unresolved ledger

Ozel not:

- `serie_info` olmadigi icin bu notebook shared spec fallback zincirinin en agir testidir.

## Gerekli CLI/Sema Degisiklikleri

- `spec=tbl-apko`
- import ve show-map source dependency destekli olmali
- spec sistemi frekans alt bloklarini desteklemeli

## Test Senaryolari

1. Benzersiz ticker sayisi `40` olmali.
2. `11` EVDS ailesi dogru cikmali.
3. Dort dis kaynak dependency kaydi uretilmeli.
4. `serie_names_apko_*` dict'leri resmi ad kaynagi olarak kullanilmali.
5. Haftalik/aylik/ceyreklik bloklardan gelen indikatorlar karismamali.

## Acceptance Checklist

- [ ] Bu notebook icin source dependency modeli gercekten yeterli oldu.
- [ ] `serie_info` olmadan resmi veya baglamsal isimler acikca cikarildi.
- [ ] Disa bagimli tablo kolonlari dogru dependency'lere baglandi.
- [ ] Coklu frekans yuzunden yanlis indicator baglari uretilmedi.
