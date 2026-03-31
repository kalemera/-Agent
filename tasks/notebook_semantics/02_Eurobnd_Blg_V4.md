---
task_id: notebook-semantics-02-eurobnd-blg-v4
notebook_path: ../Telegram Bot/notebooks/Eurobnd_Blg_V4.ipynb
lane: L2_EVDS_plus_external
priority: P2
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
  - tasks/notebook_semantics/01_DTH_Blg_V7.md
evds_code_families:
  - TP.EBONDYAZDEG
  - TP.YDOSBAYAZDEG
external_inputs:
  - excel_upload:eurobond-bbg-workbook
  - pdf_table:tcmb-vade-pdf
  - excel_local:hmb-odeme-projeksiyon-workbook
target_outputs:
  - generated/Eurobnd_Blg_V4_ticker_report.md
  - generated/Eurobnd_Blg_V4_registry_import.csv
known_blockers:
  - uploaded workbook sheet names may vary
  - TCMB vade PDF is discovered dynamically through browser automation
  - HMB workbook layout may shift month/year header rows
---

# Eurobnd_Blg_V4

## Amac

Bu notebook, eurobond stogu ve yabanci sahipligi anlatisini EVDS + upload + PDF + workbook karmasiyla kurar. Gorev, EVDS serilerini netlestirmek, EVDS disi uc zorunlu kaynagi `source_dependency` olarak kayda gecirmek ve turetilmis eurobond gostergelerini kararli sekilde tanimlamaktir.

## Mevcut Notebook Gercekleri

- Notebookta `serie_info` output'u vardir; resmi adlar oradan cozumlenebilir.
- Sadece `10` benzersiz EVDS kodu kullanir.
- Ana EVDS fetch tek bir blogdadir.
- Ek kaynaklar:
  - kullanicidan BBG Excel upload'i
  - browser automation ile TCMB vade PDF indirme
  - `tabula.read_pdf(...)` ile PDF tablo okuma
  - HMB odeme projeksiyon workbook'u uzerinden aylik borc projeksiyonu okuma
- Notebook sonrasinda tablo, yorum ve grafik uretilir.

## EVDS Kod Envanteri

### Aile ozetleri

- `TP.EBONDYAZDEG`: `2` kod
- `TP.YDOSBAYAZDEG`: `8` kod

### Tam kod listesi

```text
TP.EBONDYAZDEG:
TP.EBONDYAZDEG.S2D, TP.EBONDYAZDEG.ST

TP.YDOSBAYAZDEG:
TP.YDOSBAYAZDEG.S11T, TP.YDOSBAYAZDEG.S122T, TP.YDOSBAYAZDEG.S125T, TP.YDOSBAYAZDEG.S126T, TP.YDOSBAYAZDEG.S19, TP.YDOSBAYAZDEG.S38, TP.YDOSBAYAZDEG.S55, TP.YDOSBAYAZDEG.S76
```

## Dis Kaynak Envanteri

- `source:eurobnd-bbg-upload`
  - `source_kind=excel_upload`
  - `requiredness=required_input`
  - kullanici yuklemeli `.xlsx`
  - amac: Eurobond ihraclari ve vade dagilimi tablolari

- `source:eurobnd-tcmb-vade-pdf`
  - `source_kind=pdf_table`
  - `requiredness=required_input`
  - kaynak: TCMB web sayfasindan browser otomasyonu ile bulunan `vade.pdf`
  - amac: ozel sektor dis borc vade bilgisi

- `source:eurobnd-hmb-odeme-projeksiyonu`
  - `source_kind=excel_local`
  - `requiredness=required_input`
  - kaynak: HMB "Merkezi Yonetim Dis Borc Odeme Projeksiyonlari (Aylik)" workbook'u
  - amac: Hazine odeme projeksiyonu

## Beklenen Registry Nesneleri

### Theme

- `theme:eurobond`
- `theme:external-financing`

### Indicator

- `derived:eurobond-total-stock`
- `derived:eurobond-foreign-stock`
- `derived:eurobond-foreign-share`
- `derived:hazine-eurobond-total`
- `derived:hazine-eurobond-foreign-stock`
- `derived:hazine-eurobond-foreign-share`
- `derived:ozel-sektor-eurobond-total`
- `derived:ozel-sektor-eurobond-foreign-stock`
- `derived:ozel-sektor-eurobond-foreign-share`

### Source dependency

- `source:eurobnd-bbg-upload`
- `source:eurobnd-tcmb-vade-pdf`
- `source:eurobnd-hmb-odeme-projeksiyonu`

## Analyzer Kurallari

- Resmi adlar birincil olarak `serie_info` output'undan okunur.
- Notebook icindeki `df_eurobond_columns` ve devamindaki rename zinciri `notebook_label` icin ikinci katmandir.
- EVDS serileri iki buyuk gruba ayrilir:
  - Hazine Eurobond
  - Ozel sektor Eurobond
- Notebookta uretilen toplamlardan dolayi indicator sayisi EVDS seri sayisindan fazladir; indicator'lar explicit template ile uretilmelidir.
- BBG upload, TCMB vade PDF ve HMB workbook source dependency olarak kayda gecer.
- Bu uc kaynaktan biri eksikse series semantigi yine uretilir; ama ilgili indicator/theme `validation_note` ile isaretlenir.

## Turetilmis Gostergeler

Notebooktan cikan ana gostergeler:

- Hazine Eurobond Toplam
- Hazine Eurobond Yabancilar
- Hazine Eurobond Yabanci Payi
- Ozel Sektor Eurobond Toplam
- Ozel Sektor Eurobond Yabancilar
- Ozel Sektor Eurobond Yabanci Payi
- Eurobond Toplam
- Eurobond Yabancilar
- Eurobond Yabanci Payi

Grafik ve yorum katmaninda ayrica:

- secimden bu yana degisim
- 19 Mart 2025 sonrasi degisim
- yilbasindan bu yana degisim

Bu tarih-bazli degisimler indicator olarak ayrismayacak; `validation_note` veya tema aciklamasina yazilacak.

## Cozumsuzler ve Fallback

Fallback sirasi:

1. `serie_info`
2. `df_eurobond_columns` / rename zinciri
3. graph/table user-facing label'lari
4. unresolved ledger

Dis kaynak fallback'leri:

- BBG upload sayfa adi bulunamazsa ilk dort sheet fallback mantigi korunur
- TCMB vade PDF sekmesi dinamik bulunamazsa source dependency unresolved notuyla raporlanir
- HMB workbook baslik satiri bulunamazsa source dependency hata notu uretilir

## Gerekli CLI/Sema Degisiklikleri

- `spec=eurobnd-blg-v4` tanimlanacak
- source dependency row'lari import CSV'ye eklenecek
- `show-map` eurobond indicator'larinda dis kaynak baglarini gosterecek

## Test Senaryolari

1. Benzersiz ticker sayisi `10` olmali.
2. Aile dagilimi `2 + 8` olmali.
3. `source:eurobnd-bbg-upload`, `source:eurobnd-tcmb-vade-pdf`, `source:eurobnd-hmb-odeme-projeksiyonu` olusmali.
4. En az `9` ana indicator uretilmeli.
5. Upload ve PDF kaynaklari yoksa seriler yine cozumlenmeli, ama raporda eksik dependency notu bulunmali.

## Acceptance Checklist

- [ ] EVDS semantigi `10` kod icin eksiksiz cikarildi.
- [ ] Uc dis kaynak source dependency olarak yazildi.
- [ ] Eurobond toplam, yabanci stok ve yabanci pay gostergeleri ayrik kaydedildi.
- [ ] Rapor, EVDS ve dis kaynak baglarini ayni dosyada gosteriyor.
- [ ] Upload/PDF workbook belirsizlikleri sessizce yutulmuyor.
