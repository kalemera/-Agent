# Shared Spec

Bu belge, notebook semantik haritasini genellestirecek uygulama icin karar tamamlayici ortak spesifikasyondur. Aksi belirtilmedikce tum notebook gorev dosyalari bu belgeye baglidir.

## Hedef

- Notebooktan EVDS kodlarini cikarmak.
- Kodlarin resmi adlarini, baglamli adlarini ve notebook icindeki rollerini cozumlemek.
- EVDS disi bagimliliklari kayit altina almak.
- Series, indicator, theme ve source dependency baglarini ayni registry akisina tasimak.
- Her notebook icin tekrar kullanilabilir rapor + import CSV uretebilmek.

## Ortak Analyzer Mimarisi

Genel hedef komut:

```text
registry analyze-notebook --notebook <path> --spec <slug|auto> [--report-out <path>] [--import-out <path>]
```

Kararlar:

- `--spec auto` varsayilan olmalidir.
- `auto`, notebook dosya adini `NotebookSpec.slug` ile eslestirir.
- `registry analyze-dth-notebook` korunur ve `analyze-notebook --spec dth-blg-v7` alias'i gibi davranir.
- `show-map` source dependency iliskilerini de gostermelidir.

## Dahili Tipler

### `NotebookSpec`

Minimum alanlar:

- `slug`
- `notebook_stem`
- `lane`
- `series_code_pattern`
- `series_mapping_strategies`
- `source_dependency_strategies`
- `status_rules`
- `role_rules`
- `indicator_templates`
- `theme_templates`
- `known_blockers`

### `TickerAnalysis`

Mevcut DTH yapisinin genellenmis hali:

- `ticker`
- `table_group`
- `official_series_name`
- `notebook_label`
- `context_title`
- `unit`
- `notebook_status`
- `notebook_role`
- `linked_theme_ids`
- `linked_indicator_ids`
- `linked_source_dependency_ids`
- `notes`

### `SourceDependency`

Yeni kavram. Notebookta EVDS disi ama semantik akisi etkileyen girdileri temsil eder.

Minimum alanlar:

- `id`
- `title`
- `status`
- `source_kind`
- `requiredness`
- `notebook_slug`
- `source_uri`
- `local_hint`
- `description`
- `usage`
- `linked_theme_ids`
- `linked_indicator_ids`
- `notes`

### `NotebookAnalysisResult`

- `notebook_path`
- `spec_slug`
- `analyses`
- `source_dependencies`
- `indicators`
- `themes`
- `unresolved_items`

## Registry Genisleme Hedefi

Mevcut record type'lar korunur:

- `series`
- `indicator`
- `theme`

Yeni record type eklenir:

- `source_dependency`

### `source_dependency` import satiri

Import CSV'de yeni satir tipi desteklenecek. Minimum kolonlar:

- `record_type`
- `id`
- `title`
- `description`
- `usage`
- `source_kind`
- `requiredness`
- `source_uri`
- `theme_ids`
- `indicator_ids`
- `validation_note`

Kararlar:

- `indicator.input_ids` artik sadece series degil, `source_dependency` kimliklerini de tasiyabilir.
- `theme` kaydi `series_ids`, `indicator_ids` yanina `source_dependency_ids` alacak sekilde genisletilmelidir.
- `show-map` ciktisi source dependency baglarini acikca listelemelidir.

Formula alanlari:

- `formula_expression`: mumkunse acik cebirsel ifade veya dogrudan input-id tabanli oran
- `formula_description`: expression verilemediginde notebooktan gelen metinsel formul notu

## Status Taksonomisi

### Series status

- `listed_only`: notebookta listelenir ama veri cekme veya son akis rolune girmez.
- `fetched_only`: batch icinde cekilir ama tablo/grafik/comment katmanina tasinmaz.
- `derived_input`: turetilmis hesap veya oran icin ham girdidir.
- `reported_output`: tablo, grafik veya yorum katmaninda dogrudan kullanilir.

### Source dependency requiredness

- `required_input`: notebookun mevcut akisinda zorunlu girdi.
- `supporting_input`: anlami zenginlestirir ama ana EVDS raporunu tek basina bloke etmez.
- `optional_replacement`: manuel girdinin ileride yerini almasi beklenen alternatif kaynak.
- `output_only`: notebookun urettigi ama semantik haritaya girdi olmayan artefakt.

Karar:

- `output_only` artefaktlar raporda gorunebilir, ama registry `source_dependency` kaydi olarak yazilmaz.

## Role Taksonomisi

Ortak rol ailesi, notebook dosyalarinda notebook-ozel alt etiketlerle birlikte kullanilmalidir.

- `balance_sheet_line`
- `stock_total`
- `stock_component`
- `owner_split_line`
- `currency_split_line`
- `term_split_line`
- `ratio_input`
- `ratio_output`
- `parity_effect_input`
- `manual_backfill`
- `supporting_external_input`
- `commentary_driver`
- `dormant_candidate`

Karar:

- Notebook-ozel roller bu ortak rol ailesine map edilebilmelidir.
- Rapor, notebook-ozel rolu gostermeli; shared spec, ortak aileyi tanimlamalidir.

## `context_title` Kurallari

Varsayilan kurallar:

1. Resmi seri adi top-level prefix tasiyorsa (`A.`, `B.`, `TOPLAM`) yeni `top_parent` olur.
2. Sayisal prefix (`1.`, `2.`) top-level altina yazilir ve yeni `numeric_parent_context` olur.
3. Kucuk harf prefix (`a.`, `b.`) once son sayisal parent'a, yoksa top-level parent'a baglanir.
4. Roman numeral prefix (`I.`, `II.`) top-level reset sayilmaz; notebook spec isterse ozel yorum ekleyebilir.
5. `official_series_name` korunur; `context_title` yalnizca okunabilir baglam katmanidir.
6. Notebookta acik rename mapping varsa `notebook_label` o mapping'den uretilir; `context_title` hesaplamasi bundan sonra yapilir.

## Extraction Pipeline

Her notebook icin asagidaki sira sabittir:

1. Notebook JSON yuklenir.
2. Tum source hucrelerinden EVDS kodlari regex ile cikarilir.
3. Kodlar aile bazinda gruplanir.
4. Resmi ad icin ordered fallback uygulanir.
5. Dis kaynaklar `SourceDependency` olarak cikarilir.
6. Notebook-ozel role/status kurallari uygulanir.
7. Indicator ve theme kayitlari spec template'lerinden uretilir.
8. Rapor ve import CSV yazilir.

### Resmi ad fallback sirasi

1. Hucre output'unda seriallesmis `serie_info` veya `SERIE_CODE/SERIE_NAME` dict'i
2. Source kodundaki `serie_names_*` mapping dict'leri
3. `evds.get_series(...)` sonucunun output'unda bulunan `SERIE_CODE`, `SERIE_NAME`
4. Fetch sonrasi `rename(...)` veya `columns = {...}` mapping'leri
5. Turetilmis kolon atamalari icindeki kullanici gorunumlu kolon adlari
6. `unresolved_from_notebook`

### `serie_info` olmayan notebook fallback'i

Bu sira degistirilmeyecek:

1. Explicit rename dict
2. DataFrame column rename/assignment zinciri
3. Manuel inline ledger veya dictionary
4. Notebook task dosyasinda tutulan unresolved ledger
5. Sonraki fazda canli EVDS dogrulama

## Mixed-Source Modelleme Kurallari

Bir dis kaynagin `source_dependency` olmasi icin su kosullardan biri saglanmali:

- Notebook analizinde kullanilan tabloyu veya hesaplamayi besliyor olmasi
- EVDS serisinin anlamini tek basina tasimaya yetmedigi yerde baglamsal zorunlu girdi olmasi
- Manuel veri backfill, upload veya scrape yoluyla getiriliyor olmasi

Asagidaki durumlar `source_dependency` degildir:

- Salt PDF export veya HTML export gibi cikti artefaktlari
- Font URL'leri ve stil asset'leri
- Notebook icinde yalniz gorunum amacli yardimci linkler

### `source_kind` enum'u

- `excel_upload`
- `excel_local`
- `http_download`
- `pdf_table`
- `web_scrape`
- `manual_inline`
- `manual_file`

## Frekans Hizalama

Varsayilan frekans kararlar:

- Haftalik seriler native haftalik frekansta tutulur; task dosyasi acik istemedikce ayliga zorlanmaz.
- Aylik seriler ay sonu referansi ile korunur.
- Ceyreklik seriler ceyrek sonu referansi ile korunur.
- Gunluk seriler haftalik veya aylik bir gostergeye girecekse task dosyasi acik resample kuralini belirtmelidir.
- Daha dusuk frekansli seri daha yuksek frekansli seriye otomatik forward-fill edilmez; notebook gorevi bunu acikca izin verirse uygulanir.
- Bir indicator farkli frekansli girdiler kullaniyorsa hizalama karari notebook gorev dosyasinda yazili degilse testte belirsizlik olarak raporlanir.

## Rapor Sozlesmesi

Her `generated/<stem>_ticker_report.md` dosyasi su bolumleri icermelidir:

- Kisa Ozet
- Kod Gruplari
- Dis Kaynaklar
- Durum Etiketleri
- Rol Etiketleri
- Tam Ticker Eslestirme
- Source Dependency Eslestirme
- Belirsizlikler

Ticker eslestirme tablosunda minimum kolonlar:

- `Ticker`
- `Resmi Seri Adi`
- `Baglamli Ad`
- `Durum`
- `Rol`
- `Birim`
- `Notlar`

Source dependency tablosunda minimum kolonlar:

- `ID`
- `Baslik`
- `Kaynak Turu`
- `Zorunluluk`
- `Bagli Temalar`
- `Bagli Gostergeler`
- `Notlar`

## Import CSV Sozlesmesi

Her notebook import CSV'si asagidaki row tiplerini desteklemelidir:

- `series`
- `indicator`
- `theme`
- `source_dependency`

Karar:

- Notebook analiz ciktisi tek CSV uretmeye devam eder.
- CSV icindeki satir sirasi: `series`, `indicator`, `theme`, `source_dependency` olmak zorunda degildir; fakat okuma mantigi buna bagli yazilmayacaktir.

## Test ve Acceptance Sablonu

Her notebook gorevinde asagidaki testler birebir uygulanir:

1. Notebooktaki benzersiz EVDS kod sayisi dogru cikmali.
2. Kod aileleri task dosyasindaki envanterle ayni olmali.
3. `serie_info` varsa resmi adlar oradan alinmali; yoksa fallback sirasi calismali.
4. `source_dependency` listesi task dosyasindaki dis kaynak envanterini kapsamalidir.
5. Cozumsuz kodlar sessizce yanlis adlandirilmamalidir.
6. `generated/<stem>_registry_import.csv` import akisini gecmeli.

Ek zorunlu testler:

- DTH baseline testi korunacak.
- `auto` spec secimi notebook stem'i ile dogru eslesecek.
- `show-map` bir series sorgusunda indicator/theme/source dependency baglarini gosterecek.

## Varsayimlar

- Task dosyalari Turkce ama ASCII yazilir.
- Canli EVDS dogrulamasi task yazimi asamasinda zorunlu degildir.
- `source_dependency` semasi uygulanana kadar mixed-source notebooklar tam import onayi alamayabilir; bu beklenen gecis durumudur.
