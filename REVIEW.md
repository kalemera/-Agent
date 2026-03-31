# EVDS Ticker Haritasi - Kapsamli Proje Review

## Proje Amaci ve Vizyon Degerlendirmesi

**Proje amaci**: Bir ekonomistin kullandigi EVDS veri setlerini toplayabilen, hangi verilerin nereden alindigi, hangi turetmelerin yapildigi ve hangi cikarimlar uretildigi bilgisini kalici olarak tutan bir agent olusturmak.

**Mevcut durum**: Proje bu amaca donuk temiz bir ilk adim atmis. CLI tabanli bir registry sistemi, draft-review-approve is akisi, Jupyter notebook analizi ve bilgi haritasi (show-map) ozellikleri calisiyor. DTH notebook'u icin referans implementasyon tamamlanmis.

---

## Genel Mimari Degerlendirmesi

### Guclu Yanlar

1. **Temiz katmanli mimari**: CLI -> Records -> Storage katmanlari birbirinden iyi ayrilmis. Her katmanin tek sorumlulugu var.

2. **Draft-Review-Approve is akisi**: Ekonomik veri kayitlarini kontrollu sekilde onaylama mekanizmasi iyi dusunulmus. Dependency validation (indicator icin input_ids kontrolu, theme icin series/indicator kontrolu) saglam.

3. **YAML frontmatter + Markdown format**: Hem insan okunabilir hem git-dostu. Dogru bir tercih.

4. **Notebook analizi**: DTH notebook icin 54 ticker'i dogru sekilde cikarma, rol/status atama, context_title hiyerarsisi ve mojibake tamiri gibi detaylar iyi ele alinmis.

5. **Test kapsami**: 9 test case ile CLI komutlari ve notebook analizi icin temel fonksiyonel testler yazilmis.

6. **Task pack yapisi**: INDEX.md -> SHARED_SPEC.md -> Notebook gorev dosyalari hiyerarsisi sistematik ve genisletilebilir.

### Zayifliklar ve Riskler

1. **Hardcoded DTH mantigi**: `notebook_analysis.py` tamamen DTH'ye ozel. TICKER_PATTERN sadece `TP.HPBITABLO[2345]` yakaliyor. `role_for()` ve `status_for()` fonksiyonlari ticker bazli if-else zinciri. Diger 6 notebook icin bu yaklasim olceklenmez.

2. **source_dependency henuz implemente degil**: SHARED_SPEC.md ve gorev dosyalari `source_dependency` record type'ini detayla tanimliyor, ama kodda bu tip yok. `records.py`'deki `normalize_import_row()` sadece series/indicator/theme kabul ediyor.

3. **Genel analyzer yok**: `analyze-notebook --spec <slug>` komutu henuz yok. Sadece `analyze-dth-notebook` var. NotebookSpec veri yapisi sadece dokumanda tanimli, kodda yok.

4. **show-map source_dependency gostermiyor**: Mevcut `show-map` sadece series/indicator/theme baglantilari gosteriyor.

5. **Source adapter'lar stub**: `StubEVDSAdapter` sadece NotImplementedError firlatiyor. Canli EVDS dogrulamasi yok.

---

## Dogru Yolda mi?

**Evet, ama gecis noktasinda.** Phase 1 (DTH baseline + registry altyapisi) basariyla tamamlanmis. Ancak Phase 2'ye gecis icin kritik karar noktalari var:

- **Genellestirme stratejisi**: DTH hardcoded mantigi 6 farkli notebook'a nasil adapte edilecek? Her notebook icin ayri `role_for()` / `status_for()` mi yazilacak yoksa veri-odakli (spec-driven) bir yaklasim mi kullanilacak?
- **source_dependency sema entegrasyonu**: Bu buyuk bir yapi degisikligi. records.py, storage.py, cli.py hepsini etkiliyor.
- **Frekans uyumu**: SHARED_SPEC.md'de frekans donusum kurallari yok. Tbl_Apko gibi coklu frekans iceren notebook'lar bunu zorunlu kiliyor.

---

## MD Dosyalarinda Tespit Edilen Sorunlar

### 1. README.md

**Sorun 1 - Tutarsiz path ayiraclari (satir 28 vs 105-108)**:
- Satir 28: `"C:\path\to\DTH_Blg_V7.ipynb"` (backslash)
- Satir 105-108: `"C:\path\DTH_Blg_V7.ipynb"` ama `--report-out generated\dth_report.md` (backslash devam ediyor ama `\` continuation char olarak okunabilir shell'de)
- **Oneri**: README'deki orneklerde tutarli bir sekilde Windows path'leri kullanilmali veya tum ornekler forward slash ile yazilmali.

**Sorun 2 - analyze-dth-notebook dokumantasyonu eksik**:
- README'de `--report-out` ve `--import-out` opsiyonel parametreleri aciklanmamis, sadece ornekte gosterilmis.

**Sorun 3 - source_dependency henuz dokumante edilmemis**:
- README sadece series/indicator/theme record type'larini anlatiyor. SHARED_SPEC.md'de tanimlanan `source_dependency` README'ye henuz yansitilmamis. Bu beklenen bir gecis durumu olabilir ama not dusulmelidir.

### 2. INDEX.md

**Sorun 4 - Lane matrisi ile gorev dosyasi tutarsizligi (Yi_Yrlsk)**:
- INDEX.md satir 22: `Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb` icin lane `L1_EVDS_standard` ve dis kaynaklar siralanmis: "Manuel MKK inline verileri, opsiyonel VAP scrape denemesi"
- `07_Yi_Yrlsk_Fnsl_Vrlk_V1.md` satir 133: "Bu notebook L1 lane'de kalsa da source dependency yok sayilmaz"
- **Sorun**: L1_EVDS_standard tanimi "temiz EVDS" anlamina geliyor ama bu notebook manuel MKK dictionary'leri ve VAP scrape iceriyor. Lane taniminin ya genisletilmesi ya da bu notebook'un L2'ye tasinmasi gerekir. Mevcut hali kafa karistirici.

**Sorun 5 - Bagimlilik dokumantasyonu eksik**:
- INDEX.md satir 44: "Tum notebook gorevleri 00_SHARED_SPEC.md uzerine kuruludur" diyor.
- Ancak gorev dosyalarinda capraz bagimliliklar var (ornegin 02 -> 01, 05 -> 01, 06 -> 05) ve bunlar INDEX.md'de explicit listelenmiyor.

### 3. 00_SHARED_SPEC.md

**Sorun 6 - context_title kurallari ile mevcut kod uyumsuzlugu**:
- SHARED_SPEC.md satir 170-179: `context_title` kurallari 6 madde olarak tanimli.
- `notebook_analysis.py` satir 312-342: `derive_context_title()` fonksiyonu bu kurallari uyguluyor ama kural 4 (Roman numeral) ve kural 6 (rename mapping) icin explicit islem yok. Roman numeral sadece "top-level reset sayilmaz" olarak handle ediliyor ama baska bir sey yapilmiyor.

**Sorun 7 - Rapor sozlesmesinde "Dis Kaynaklar" bolumu eksik**:
- SHARED_SPEC.md satir 239-248: Rapor sozlesmesi "Dis Kaynaklar" ve "Source Dependency Eslestirme" bolumlerini gerektiriyor.
- Mevcut `render_markdown_report()` (notebook_analysis.py satir 375-450) bu bolumleri uretmiyor. Sadece Kisa Ozet, Kod Gruplari, Durum/Rol Etiketleri, Tam Ticker Eslestirme ve Belirsizlikler var.

**Sorun 8 - Frekans semantigi tanimlanmamis**:
- SHARED_SPEC.md'de frekans hizalama (alignment) kurallari yok.
- `06_Tbl_Apko.md` icindeki gunluk/haftalik/aylik/ceyreklik frekans bloklari icin ortak bir donusum veya hizalama rehberi eksik.
- Bu, indicator hesaplamalarinin dogru yapilabilmesi icin kritik bir bosluk.

### 4. 01_DTH_Blg_V7.md

**Sorun 9 - depends_on referansi belirsiz**:
- Satir 8: `existing DTH baseline in src/evds_registry/notebook_analysis.py`
- Bu bir dosya yolu degil, semantik bir referans. Diger gorev dosyalarindaki `depends_on` formatindan farkli ve standart degil.

**Sorun 10 - Acceptance checklist tamamlanma durumu**:
- DTH icin `generated/DTH_Blg_V7_ticker_report.md` ve `generated/DTH_Blg_V7_registry_import.csv` zaten uretilmis durumda.
- Ancak acceptance checklist tamamen bos (tum kutucuklar `[ ]`).
- Mevcut DTH implementasyonu bazi maddeleri kismen karsilamasina ragmen (ticker extraction, report generation) hicbiri isaretlenmemis. Bu ya checklist'in Phase 2 hedeflerini olctugu icin (source_dependency henuz yok) ya da guncellenmemis oldugu icin boyle.

### 5. 07_Yi_Yrlsk_Fnsl_Vrlk_V1.md

**Sorun 11 - Lane siniflandirmasi ile icerik uyumsuzlugu** (INDEX.md ile de baglantili):
- Satir 3: `lane: L1_EVDS_standard`
- Satir 17-20: 3 adet external_input listeleniyor (manual_inline x2, web_scrape x1)
- Satir 133: "Bu notebook L1 lane'de kalsa da source dependency yok sayilmaz"
- **Sorun**: L1 tanimi "EVDS temiz" notebooklar icin. 3 dis kaynak varken L1 demek tanim ile celisiyor. Bu bilincli bir karar olabilir ama belgede yeterince gerekcelendirilmemis.

### 6. Genel MD Tutarliligi

**Sorun 12 - formula_expression vs formula_description uyumsuzlugu**:
- SHARED_SPEC.md ve README.md'de `formula_expression` bir alan olarak tanimli.
- `notebook_analysis.py` satir 513: indicator import satirlarinda `formula_expression` bos birakiliyor, icerik `formula_description`'a yaziliyor.
- `records.py` satir 134: Validation sadece ikisinden birinin dolu olmasini istiyor (`if not record.get("formula_expression") and not record.get("formula_description")`).
- Pratikte `formula_expression` hicbir zaman doldurulmuyor. Alanlarin farki/amaci belirsiz.

**Sorun 13 - Tum gorev dosyalarinda acceptance checklist bos**:
- 01 den 07'ye kadar tum gorev dosyalarindaki acceptance checklist'ler tamamen isaretlenmemis.
- Eger DTH baseline calisiyor durumda ise en azindan 01'deki bazi maddeler isaretlenebilirdi.

**Sorun 14 - generated/ klasorundeki rapor SHARED_SPEC sozlesmesini karsilamiyor**:
- `generated/DTH_Blg_V7_ticker_report.md` raporu mevcut ama SHARED_SPEC.md'deki rapor sozlesmesindeki "Dis Kaynaklar" ve "Source Dependency Eslestirme" bolumlerini icermiyor (cunku source_dependency henuz implemente degil).

---

## Kod Seviyesi Gozlemler

### notebook_analysis.py - Olceklenme Riski

- `TICKER_PATTERN = re.compile(r"TP\.HPBITABLO[2345]\.\d+")` sadece HPBITABLO ailesi icin calisiyor.
- Diger notebook'lar `TP.BEK`, `TP.PKAUO`, `TP.AB`, `TP.DK`, `TP.DIBSPIYDEG`, `TP.EBONDPIYDEG` gibi tamamen farkli aileler kullaniyor.
- `role_for()` fonksiyonu 30+ satirlik if-else zinciri. Her yeni notebook benzer bir zincir gerektirecek.
- **Oneri**: NotebookSpec veri yapisi icerisinde `series_code_pattern`, `role_rules`, `status_rules` alanlarinin veri-odakli tanimlanmasi Phase 2 icin kritik.

### records.py - source_dependency Eksikligi

- `normalize_import_row()` sadece 3 record type kabul ediyor: series, indicator, theme.
- SHARED_SPEC.md 4. bir tip tanimliyor: `source_dependency`.
- Bu eklenmeden L2/L3 notebook'lar tam import akisina giremez.

### cli.py - Genel Analyzer Komutu Eksik

- Sadece `analyze-dth-notebook` subcommand'i var.
- SHARED_SPEC.md ve INDEX.md `analyze-notebook --spec <slug|auto>` komutunu hedef olarak tanimliyor ama henuz yok.

---

## Sonuc ve Oneriler

### Projenin Durumu: Saglam Phase 1, Phase 2 Esiginde

Proje, hedefledigi ilk amaca (DTH notebook'u icin veri haritasi) ulasmis durumda. Mimari temiz, testler var, is akisi calisiyor. Ancak 7 notebook'a genislemek icin su adimlar gerekiyor:

### Oncelik Sirali Oneriler

1. **YUKSEK - source_dependency record type'ini implemente et**: records.py, storage.py, cli.py'ye source_dependency destegi ekle. Bu olmadan L2/L3 notebook'lar tamamlanamaz.

2. **YUKSEK - NotebookSpec veri yapisini kodla**: SHARED_SPEC.md'deki tanimdan yola cikarak spec-driven analyzer mimarisi kur. DTH mevcut hardcoded mantigi bu yapinin ilk ornegi olarak refactor edilebilir.

3. **YUKSEK - analyze-notebook genel komutunu ekle**: `--spec auto` ile notebook dosya adini eslestiren genel komutu implement et. `analyze-dth-notebook` alias olarak koru.

4. **ORTA - Lane tanimi netlestirilmeli**: L1 icinde dis kaynak iceren notebook'lar icin ya lane tanimini genislet ya da Yi_Yrlsk'yi L2'ye tasi. INDEX.md ve gorev dosyalari arasindaki tutarsizligi gider.

5. **ORTA - Frekans hizalama semantigini SHARED_SPEC'e ekle**: Ozellikle Tbl_Apko gibi coklu frekans notebook'lar icin ortak kurallar tanimla.

6. **ORTA - Rapor sozlesmesini kodda uygula**: render_markdown_report() icine "Dis Kaynaklar" ve "Source Dependency Eslestirme" bolumlerini ekle.

7. **DUSUK - MD dosyalarindaki tutarsizliklari gider**: README path ayiraclari, acceptance checklist guncellemeleri, formula_expression/description anlam ayrimi netlestirilmeli.

8. **DUSUK - show-map'i source_dependency icin genislet**: source_dependency eklendikten sonra show-map ciktisina source dependency baglarini ekle.
