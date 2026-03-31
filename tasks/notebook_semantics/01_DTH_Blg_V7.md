---
task_id: notebook-semantics-01-dth-blg-v7
notebook_path: ../Telegram Bot/notebooks/DTH_Blg_V7.ipynb
lane: L2_EVDS_plus_external
priority: P1
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
  - src/evds_registry/notebook_analysis.py
evds_code_families:
  - TP.HPBITABLO2
  - TP.HPBITABLO3
  - TP.HPBITABLO4
  - TP.HPBITABLO5
external_inputs:
  - excel_local:dth_old_series_19022025.xlsx
target_outputs:
  - generated/DTH_Blg_V7_ticker_report.md
  - generated/DTH_Blg_V7_registry_import.csv
known_blockers:
  - TP.HPBITABLO4.14 and TP.HPBITABLO4.15 unresolved_from_notebook
  - old Excel columns use legacy/mojibake labels and require explicit normalization
---

# DTH_Blg_V7

## Amac

Bu notebook, genel analyzer mimarisi icin referans baseline'dir. Buradaki gorev, mevcut DTH implementasyonunu bozmadan ortak kurallari ayrismak, eski seri Excel backfill'ini `source_dependency` olarak modellemek ve DTH semantigini genel `NotebookSpec` yapisina tasimaktir.

## Mevcut Notebook Gercekleri

- Notebookta seriallesmis `serie_info` output'u vardir; resmi seri adlari buradan okunabilir.
- Uc EVDS fetch blogu vardir:
  - ana DTH/mevduat blogu
  - ek tablo blogu
  - `TP.HPBITABLO5.12` parite etkisi blogu
- Bir adet yerel Excel girdisi vardir: `'/content/drive/MyDrive/DataFiles/dth_old_series_19022025.xlsx'`
- PDF birlestirme blogu vardir ancak bu bir cikti artefaktidir; `source_dependency` degildir.
- Mevcut projede bu notebook icin calisan analyzer ve testler bulunmaktadir; bunlar baseline kabul edilir.

## EVDS Kod Envanteri

### Aile ozetleri

- `TP.HPBITABLO2`: `27` kod
- `TP.HPBITABLO3`: `5` kod
- `TP.HPBITABLO4`: `21` kod
- `TP.HPBITABLO5`: `1` kod

### Tam kod listesi

```text
TP.HPBITABLO2:
TP.HPBITABLO2.1, TP.HPBITABLO2.10, TP.HPBITABLO2.11, TP.HPBITABLO2.12, TP.HPBITABLO2.13, TP.HPBITABLO2.14, TP.HPBITABLO2.15, TP.HPBITABLO2.16, TP.HPBITABLO2.17, TP.HPBITABLO2.18, TP.HPBITABLO2.19, TP.HPBITABLO2.2, TP.HPBITABLO2.20, TP.HPBITABLO2.21, TP.HPBITABLO2.22, TP.HPBITABLO2.23, TP.HPBITABLO2.24, TP.HPBITABLO2.28, TP.HPBITABLO2.3, TP.HPBITABLO2.32, TP.HPBITABLO2.33, TP.HPBITABLO2.34, TP.HPBITABLO2.4, TP.HPBITABLO2.5, TP.HPBITABLO2.6, TP.HPBITABLO2.7, TP.HPBITABLO2.8

TP.HPBITABLO3:
TP.HPBITABLO3.1, TP.HPBITABLO3.18, TP.HPBITABLO3.2, TP.HPBITABLO3.21, TP.HPBITABLO3.24

TP.HPBITABLO4:
TP.HPBITABLO4.1, TP.HPBITABLO4.10, TP.HPBITABLO4.11, TP.HPBITABLO4.12, TP.HPBITABLO4.13, TP.HPBITABLO4.14, TP.HPBITABLO4.15, TP.HPBITABLO4.16, TP.HPBITABLO4.17, TP.HPBITABLO4.18, TP.HPBITABLO4.19, TP.HPBITABLO4.2, TP.HPBITABLO4.20, TP.HPBITABLO4.21, TP.HPBITABLO4.3, TP.HPBITABLO4.4, TP.HPBITABLO4.5, TP.HPBITABLO4.6, TP.HPBITABLO4.7, TP.HPBITABLO4.8, TP.HPBITABLO4.9

TP.HPBITABLO5:
TP.HPBITABLO5.12
```

## Dis Kaynak Envanteri

### Kayda alinacak source dependency'ler

- `source:dth-old-series-excel`
  - `source_kind=excel_local`
  - `requiredness=required_input`
  - amac: eski DTH serilerini bugunku kolon adlariyla birlestirmek
  - ana risk: kolon adlari notebookta legacy ve mojibake formlar tasiyor

### Kayda alinmayacak artefaktlar

- `Functions.html_tables_to_pdfs(...)`
- `Functions.merge_pdfs(...)`

Bu bloklar rapor ciktisi uretir; semantik haritaya girdi degildir.

## Beklenen Registry Nesneleri

### Theme

- `theme:dth`

### Indicator

- `derived:dth-share-in-total-deposits`
- `derived:dth-share-in-resident-deposits`
- `derived:resident-deposit-share-in-total-deposits`

### Source dependency

- `source:dth-old-series-excel`

### Series notlari

- Tum `TP.HPBITABLO2.*`, `TP.HPBITABLO3.*`, `TP.HPBITABLO4.*`, `TP.HPBITABLO5.12` kayitlari series olarak uretilir.
- `TP.HPBITABLO4.14` ve `TP.HPBITABLO4.15` resmi ad yoksa `unresolved_from_notebook` olarak kalir.

## Analyzer Kurallari

- DTH mevcut implementasyonu baseline kabul edilir; semantik davranis korunur.
- `official_series_name` icin birincil kaynak notebook output'undaki `serie_info` dict'idir.
- `context_title` ortak shared spec kurallariyla hesaplanir.
- `HPBITABLO3` serileri `listed_only` kalir.
- `TP.HPBITABLO4.1`, `.13`, `.14`, `.15`, `.16`, `.17`, `.18`, `.19`, `.20`, `.21` `fetched_only` olur.
- `TP.HPBITABLO5.12` `reported_output` kalir ve `parity_effect_input` rolunu korur.
- Excel backfill blogu series olarak degil, `source_dependency` olarak modellenir.
- PDF export akisi source dependency degildir.

## Turetilmis Gostergeler

Notebookun mevcut anlati omurgasi su gruplardan olusur:

- Toplam mevduat icinde DTH payi
- Yurtici yerlesiklerin mevduati icinde DTH payi
- Toplam mevduat icinde yurtici yerlesiklerin payi
- DTH stok
- DTH bakiyesi
- DTH payi
- DTH icinde pay
- Parite etkisi arindirilmis yorum

Karar:

- Registry'ye ilk fazda sadece mevcut uc ana oran indicator olarak yazilir.
- Grafik ve tablo adlari raporda not olarak korunur, otomatik indicator patlamasi yaratmaz.

## Cozumsuzler ve Fallback

- `TP.HPBITABLO4.14`
- `TP.HPBITABLO4.15`

Bu iki kod:

- batch icinde fetch edilir
- downstream akista kullanilmaz
- notebook icindeki kayitli resmi seri adinda gorunmez
- varsayimsal isim verilmez

Eski Excel icin fallback:

1. notebook icindeki explicit rename dict
2. legacy kolonlardan bugunku isme map
3. hala eslesmeyen kolonlar `source_dependency` notuna yazilir

## Gerekli CLI/Sema Degisiklikleri

- `registry analyze-dth-notebook` alias olarak kalmali
- genel implementasyon `registry analyze-notebook --spec dth-blg-v7` ile ayni semantics'i vermeli
- import CSV `source_dependency` satiri tasiyabilmeli
- `show-map` serinin bagli `source:dth-old-series-excel` girdisini gosterebilmeli

## Test Senaryolari

1. Benzersiz ticker sayisi `54` olmali.
2. `TP.HPBITABLO3.1`, `.2`, `.18`, `.21`, `.24` `listed_only` olmali.
3. `TP.HPBITABLO4.14` ve `.15` `fetched_only` olmali.
4. `context_title` ambigu satirlarda dolu olmali.
5. `TP.HPBITABLO5.12` `reported_output` kalmali.
6. `source:dth-old-series-excel` import CSV'de yazilmali.
7. DTH mevcut report/import ciktisi anlamsal regresyon yasamamali.

## Acceptance Checklist

- [ ] DTH mevcut testleri kirmadan genel spec'e tasindi.
- [ ] Rapor `Baglamli Ad` ve `Dis Kaynaklar` bolumlerini iceriyor.
- [ ] Import CSV series + indicator + theme + source_dependency satirlari uretiyor.
- [ ] `TP.HPBITABLO4.14` ve `.15` acik belirsizlik olarak raporlanmis durumda.
- [ ] Eski seri Excel girdisi source dependency olarak kayda gecti.
