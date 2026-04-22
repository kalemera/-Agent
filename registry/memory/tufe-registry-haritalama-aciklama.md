# TÜFE Registry Haritalama — Detaylı Açıklama

**Tarih:** 2026-04-07
**Amaç:** TÜFE ve Yi-ÜFE veri kaynaklarının registry üzerinde nasıl organize edildiğini anlatmak. Gelecekte bir veri sorgusu geldiğinde ("TÜFE'nin alt kırılımları nerede?", "Çekirdek enflasyon B göstergesi hangi dosyadan geliyor?") bu dokümandan başlayarak tek bir zincir takip edilebilir.

---

## 1. Registry'nin Genel Mantığı

Registry, "ne nereden alınır" sorusunun **tek kaynak noktasıdır** (single source of truth). Econ platformundaki her veri serisinin, dosyasının, tablosunun ve pipeline'ının nereden geldiği ve nasıl kullanıldığı burada kayıtlıdır. MCP server `python -m src.evds_registry.mcp_server` bu dosyaları okuyarak 6 tool (`registry_search`, `registry_get`, `registry_map`, `registry_fetch`, `registry_analyze`, `registry_audit`) üzerinden sorgulanabilir yapar.

Registry klasör yapısı:
```
registry/
├── catalog/               → EVDS API serileri (evds:TP.XX.YYY formatinda, ~2000+ kayit)
├── indicators/            → Turetilen gostergeler (derived:xxx, hesaplama kurallari)
├── memory/                → Aciklama/not dosyalari (bu dosya burada!)
├── series/                → EVDS seri kayitlari (catalog ile benzer, daha detayli)
├── source_dependencies/   → Ham veri kaynaklari (XLS, PDF, API, upload)
└── themes/                → Konu basliklari — birden fazla kaynagi birlestirir
```

Kayit dosya adi formati: `{record_type}%3A{id}.md` (`%3A` = URL-encoded `:`)
- Ornek: `theme%3Atufe.md` okunur `theme:tufe`

Her kayit dosyasi:
- **YAML frontmatter**: Yapilandirilmis metadata (id, title, status, iliskiler)
- **Markdown body**: Insan-okunabilir dokumantasyon

---

## 2. TÜFE İçin Neden 7 Kayıt?

TÜFE hem TÜİK'in **ham bulten dosyalarini** (6 farkli XLS/XLSX) hem de bunlari birlestiren **tek konu basligini** (theme) icerir. Her ham dosya ayri bir `source_dependency` kaydidir; theme bunlari birbirine bagla.

```
                    theme:tufe
                    (Konu Basligi)
                         |
        +----------------+----------------+
        |                |                |
  Press 58295       Press 58295      Press 58029
  (TUFE)            (TUFE)           (Yi-UFE)
        |                |                |
  5 dosya           (devami)         1 dosya
```

### Dosya Sayisi = 7

| # | Kayit | Dosya Tipi | Rol |
|---|-------|------------|-----|
| 1 | `theme:tufe` | theme | Ana konu basligi, 6 kaynagi birlestirir |
| 2 | `source:tufe-zaman-serisi` | source_dependency | Genel endeks zaman serisi (TUFE genel %) |
| 3 | `source:tufe-kategoriler` | source_dependency | 13 kategori snapshot (son donem) |
| 4 | `source:tufe-katkilar` | source_dependency | Katki puanlari (son donem) |
| 5 | `source:tufe-ozel-kapsamli` | source_dependency | Cekirdek + Mallar + Hizmet (27 gosterge, zaman serisi) |
| 6 | `source:tufe-endeks-sonuclari` | source_dependency | COICOP 5 duzey tum kirlimlar (zaman serisi) |
| 7 | `source:yufe-tarihsel-seri` | source_dependency | Yi-UFE zaman serisi 1982+ |

---

## 3. Kaynak Dosyalarin Rolleri (Detayli)

### 3.1 `source:tufe-zaman-serisi` — Manset TUFE
**Dosya**: `Tuketici-fiyat-endeksi-ve-degisim-oranlari.xls`
**Ne iceriyor?**: Sadece TUFE **genel** endeksinin zaman serisi (2005 - bugun, aylik). Kategori kirilimi YOK.
**Ne veriyor?**: 4 metrik — endeks | aylik % | YTD % | yillik % (her biri ayri section)
**Neden gerekli?**: TUFE manset degerlerini (TUIK acikladigi %30.87 gibi) dogrulamak icin. Pre-computed % degerleri burada, biz endeks farkindan hesaplasak bile gercek TUIK degeriyle cross-check yapiliyor.
**DB hedef**: `tufe_monthly` tablosu

### 3.2 `source:tufe-kategoriler` — Snapshot (13 kategori, son donem)
**Dosya**: `Ana-harcama-gruplarina-gore-agirliklar-tuketici-fiyat-endeksi-TUFE-ve-degisim-oranlari.xls`
**Ne iceriyor?**: **Tek bir donem icin** 13 ana harcama grubunun detayi — agirlik, endeks, aylik %, YTD %, yillik %, 12 aylik ortalama
**Ne veriyor?**: Zaman serisi DEGIL, sadece son yayinlanan bultenin snapshot'i
**Neden gerekli?**: Agirliklari (weight) buradan aliyoruz. Kategoriler'in zaman serisi `source:tufe-endeks-sonuclari`'ndan gelir; bu dosya "bu ayki resmi TUIK degerleri" olarak dogrulama ve agirlik kaynagi.
**DB hedef**: `tufe_categories` tablosu (sadece son donem dolu)

### 3.3 `source:tufe-katkilar` — Katki Puanlari (snapshot)
**Dosya**: `TUFE-ana-harcama-gruplarinin-yillik-ve-aylik-degisim-oranlari-ve-genel-endeks-degisimine-katkilari.xls`
**Ne iceriyor?**: 13 kategorinin **aylik ve yillik katki puanlari** (yuzde puan). Katki = kategori agirligi × kategori % degisimi (normalizasyon ile).
**Ne veriyor?**: "Gida 8.25 yuzde puan katkida bulundu" gibi bulten ifadelerinin hammaddesi
**Neden gerekli?**: Zorunlu degil (ozet tablomuzda sutun yok), ama DB'de saklanip future brief/analiz icin hazir bekler.
**DB hedef**: `tufe_contributions` tablosu

### 3.4 `source:tufe-ozel-kapsamli` — Cekirdek + Mallar + Hizmet (KRITIK)
**Dosya**: `Ozel-Kapsamli-TUFE-Gostergeleri.xls` ⚠️ (uzanti .xls, aslinda XLSX)
**Ne iceriyor?**: 27 gosterge × 255 donem zaman serisi
- **A-F**: Cekirdek enflasyon gostergeleri (6 adet)
- **2. Mallar** + 14 alt kalem (Enerji, Gida, Taze meyve-sebze, ...)
- **3. Hizmet** + 5 alt kalem (Kira, Lokanta-oteller, Ulastirma, Haberlesme, Diger)

**Ne veriyor?**: Manset TUFE'yi **ayristirmayi** saglayan tum alt kirilimlar. Bu dosya olmadan "Mallar ne durumda?", "Hizmet enflasyonu ayrisiyor mu?" sorularina cevap veremezsin.
**Neden kritik?**: Ozet tablodaki Cekirdek (C), Mallar, Hizmet satirlari BURADAN geliyor. Bu dosya silinirse ozet tablo 3 satir eksik uretir.

**NOT**: Biz cekirdek gostergesi olarak **C** kullaniyoruz ("Enerji, gida ve alkolsuz icecekler, alkollu ickiler ile tutun urunleri ve altin haric TUFE"). TUIK haber bulteninde ozellikle B ve C one cikarilir — biz C'yi tercih ediyoruz cunku enerji + gida dahil tum gecici sok kalemleri disarida tutar (daha saf cekirdek olcut).

**KRITIK GOTCHA**: Dosya `.xls` uzantili ama gercekte **XLSX** formatinda. `xlrd` kutuphanesi acamaz (`XLRDError: Excel xlsx file; not supported`). Cozum:
```python
shutil.copy(path, tmp_path_xlsx)  # .xls -> .xlsx olarak kopyala
wb = openpyxl.load_workbook(tmp_path_xlsx, data_only=True)
# read_only=True KULLANMA — Windows'ta WinError 32 (temp file locked)
try:
    # ... parse ...
finally:
    wb.close()
    tmp_path_xlsx.unlink()
```

**Indicator kodlama semasi**:
- `A`, `B`, `C`, `D`, `E`, `F` — cekirdek (orijinal TUIK harfleri)
- `M_TOTAL` — Mallar aggregate (yeni kod, TUIK'de "2. Mallar" satiri)
- `M_01` ... `M_14` — Mallar alt kalemler (sirali: Enerji, Gida, ..., Alkollu icecekler-tutun-altin)
- `H_TOTAL` — Hizmet aggregate
- `H_01` ... `H_05` — Hizmet alt kalemler (Kira, Lokanta, Ulastirma, Haberlesme, Diger)

**DB hedef**: `tufe_core` tablosu

### 3.5 `source:tufe-endeks-sonuclari` — COICOP 5 Duzey Zaman Serisi
**Dosya**: `Harcama-gruplarina-gore-endeks-sonuclari.xlsx` (native xlsx)
**Ne iceriyor?**: 4 sheet (Duzey 2, 3, 4, 5), her biri TUIK COICOP 2018 agacinin farkli bir derinligini gosterir:
- **Duzey 2**: 14 kolon (TUFE genel + 13 ana harcama grubu) — 2-haneli COICOP kodlari (01, 02, ..., 13)
- **Duzey 3**: 44 kolon — 3-haneli kodlar (011, 012, 021, ...)
- **Duzey 4**: 111 kolon — 4-haneli kodlar (0111, 0112, ...)
- **Duzey 5**: 178 kolon — 5-haneli kodlar (01111, 01112, ...), TUIK'in en ince detayi (174 alt sinif)

**Ne veriyor?**: Her duzeyde TUM donemlerin (2005-01 → bugun, aylik) **sadece endeks** degerleri. Yuzde hesaplari YOK.
**Neden kritik?**: Bu tek dosya, **kategori bazli zaman serisi**nin tek kaynagi. Mesela "Gida ve alkolsuz icecekler 2025 Mart'ta ne kadar artti?" sorusunu cevaplamak icin bu dosyadaki 2025-03 ile 2024-03 endeksleri arasinda hesap yapariz.

**COICOP 2018 hiyerarsisi ornegi**:
```
01 Gida ve alkolsuz icecekler (Duzey 2)
├── 011 Gida (Duzey 3)
│   ├── 0111 Ekmek ve tahillar (Duzey 4)
│   │   ├── 01111 Pirinc (Duzey 5)
│   │   ├── 01112 Un ve diger tahillar
│   │   └── ...
│   ├── 0112 Et (Duzey 4)
│   └── ...
└── 012 Alkolsuz icecekler (Duzey 3)
```

**DB hedef**: `tufe_endeks` tablosu — `(year, month, coicop_code, coicop_level, category_name, index_value)`
- Yaklasik **77.764 satir** (tum duzeyler × 255 donem)

**PK Cakismasi Gotchasi**: Code `'0'` (TUFE genel) her 4 sheet'te de var. `PRIMARY KEY (year, month, coicop_code)` oldugundan INSERT OR REPLACE ile en son yazilan (Duzey 5) onceki duzeyleri siler. **Cozum**: Parser'da `if code == '0' and level > 2: continue` — code '0' sadece Duzey 2'de kaydedilir (kendi dogal yerinde).

### 3.6 `source:yufe-tarihsel-seri` — Yi-UFE (Yurt Ici Uretici Fiyat Endeksi)
**Dosya**: `Yurt-Ici-Uretici-Fiyat-Endeksi-ve-Degisim-Oranlari-Tarihsel-Seri.xls`
**Press ID**: **58029** (TUFE'nin 58295'inden farkli!)
**Ne iceriyor?**: Yi-UFE zaman serisi **1982 - bugun** (43+ yil!). Wide format, 5 section:
1. Endeks degerleri
2. Bir onceki aya gore degisim %
3. Bir onceki yilin Aralik ayina gore degisim % (YTD)
4. Yillik degisim %
5. On iki aylik ortalamalara gore degisim %

**Ne veriyor?**: Uretici tarafindan (fabrika cikisi) fiyat baskisi gostergesi. TUFE manset'ten farkli bir olcut — TUFE tuketiciye ulasan fiyatlari, Yi-UFE ureticiden cikan fiyatlari olcer.
**Neden onemli?**: TUFE ve Yi-UFE arasindaki **ayrisma** analitik sinyaldir. Yi-UFE yuksekse fakat TUFE dusukse, baskinin tuketiciye henuz yansimadigini gosterir (ileride TUFE'nin artmasi beklenir).

**Yil suffix gotchasi**: Yi-UFE dosyasi 1982'den baslayip farkli base yillara gore (1981 TEFE, 1987 TEFE, 1994 TEFE, 2003 Yi-UFE) birlestirilmis zincir serisidir. Yil satirlarinda parantezli numara var: `1982(1)`, `1991(2)`, `1996(3)`, `2006(4)`. Parser `re.match(r"^(\d{4})", cell)` ile sadece yili cikar, suffix'i atar.

**Base yil**: 2003=100 (TUFE'nin 2025=100'unden FARKLI). Seviye karsilastirmasinda dikkat — endeks degerleri 5000+ olabilir (Yi-UFE = 5145.36 @ 2026-03).

**DB hedef**: `yufe_monthly` tablosu (531 satir)

---

## 4. Pipeline -> DB -> Rapor Zinciri

```
                    TUIK Portal
                    (veriportali.tuik.gov.tr)
                         |
              +----------+----------+
              |                     |
         Press 58295          Press 58029
         (TUFE, 5 dosya)      (Yi-UFE, 1 dosya)
              |                     |
              v                     v
         Playwright Fetcher (pipelines/tufe_fetcher.py)
              |                     |
              v                     v
         TUFE/downloads/tufe/   TUFE/downloads/yufe/
              |                     |
              +----------+----------+
                         |
                         v
              Parser Katmani (pipelines/tufe_parser.py)
              ├── parse_zaman_serisi()      → tufe_monthly
              ├── parse_kategoriler()       → tufe_categories
              ├── parse_contributions()     → tufe_contributions
              ├── parse_ozel_kapsamli()     → tufe_core
              ├── parse_endeks_sonuclari()  → tufe_endeks
              └── parse_yufe()              → yufe_monthly
                         |
                         v
              Validator (pipelines/tufe_validator.py)
              ├── CP#3: Magic bytes (XLS/XLSX tespiti)
              ├── CP#4: Satir sayisi (min 20)
              ├── CP#5: Tarih araligi (max 60 gun eski)
              ├── CP#6: Cift kayit kontrolu
              └── CP#7: SHA-256 checksum (duplicate)
                         |
                         v
              DB Upsert (pipelines/tufe_db.py)
              TUFE/tufe.db (SQLite, WAL mode)
                         |
                         v
              Rapor Uretici (pipelines/tufe_rapport.py)
              └── TUFE/outputs/tufe_ozet.html
                   └── wkhtmltopdf → tufe_ozet.pdf
                   └── poppler → tufe_ozet.png
                         |
                         v
              Email (pipelines/tufe_email.py)
              Gmail SMTP + attachments
```

---

## 5. Ozet Tablonun Hesaplama Mantigi

Ozet tablodaki **her satirin** kaynagi farkli — bu yuzden registry sart:

| Satir | Kaynak Tablo | COICOP / Kod | Hesaplama |
|-------|--------------|--------------|-----------|
| TUFE | tufe_endeks (Duzey 2) | code='0' | (cur_idx / prev_idx - 1) × 100 |
| 13 Kategori | tufe_endeks (Duzey 2) | code='01'...'13' | Ayni formul |
| Cekirdek TUFE (C) | tufe_core | indicator_code='C' | Ayni formul |
| Mallar | tufe_core | indicator_code='M_TOTAL' | Ayni formul |
| Hizmet | tufe_core | indicator_code='H_TOTAL' | Ayni formul |
| Yurt Ici UFE | yufe_monthly | — | Ayni formul (index_value) |

**4 sutun hesabi** (dinamik, her ay otomatik kayar):
```python
# current period (Mart 2026) ve onceki ay (Subat 2026) ve gecen yil ayni ay (Mart 2025) + (Subat 2025)
monthly_cur  = (idx[Mart 2026] / idx[Subat 2026] - 1) * 100
monthly_prev = (idx[Mart 2025] / idx[Subat 2025] - 1) * 100
annual_cur   = (idx[Mart 2026] / idx[Mart 2025]  - 1) * 100
annual_prev  = (idx[Mart 2025] / idx[Mart 2024]  - 1) * 100
```

Nisan 2026 geldiginde TUM formuller otomatik "Nisan 2026 / Mart 2026" ve "Nisan 2025 / Nisan 2024" olarak kayar. Donem stringleri `MONTH_NAMES_TR[mo] + yr` ile dinamik.

---

## 6. Gelecekte Neyi Nerede Ararim?

### Senaryo 1: "TUFE'nin altındaki Giyim ve ayakkabi kategorisinde son 5 yilin verisi lazim"
1. Registry: `theme:tufe` → soruyla ilgili tabloyu bul
2. Theme body: "Kategori kirilimlari tufe_endeks tablosunda (COICOP 2-5 duzey)"
3. Source: `source:tufe-endeks-sonuclari` → parser referansi → `parse_endeks_sonuclari()`
4. DB sorgu:
   ```sql
   SELECT year, month, index_value FROM tufe_endeks
   WHERE coicop_code='03' AND coicop_level=2
   ORDER BY year DESC, month DESC LIMIT 60;
   ```

### Senaryo 2: "Hizmet altında Kira endeksi nasıl seyrediyor?"
1. Registry: `theme:tufe` → "Hizmet alt kalemleri tufe_core'da H_01-H_05"
2. Source: `source:tufe-ozel-kapsamli` → parser → `parse_ozel_kapsamli()`
3. DB sorgu:
   ```sql
   SELECT year, month, index_value FROM tufe_core
   WHERE indicator_code='H_01'  -- Kira
   ORDER BY year, month;
   ```

### Senaryo 3: "Yi-UFE ve TUFE arasindaki ayrismayi goster"
1. Registry: `theme:tufe` → "TUFE = tufe_monthly, Yi-UFE = yufe_monthly"
2. Source: `source:tufe-zaman-serisi` + `source:yufe-tarihsel-seri`
3. DB sorgu:
   ```sql
   SELECT t.year, t.month, t.annual_pct AS tufe, y.annual_pct AS yufe
   FROM tufe_monthly t
   LEFT JOIN yufe_monthly y ON t.year=y.year AND t.month=y.month
   WHERE t.year >= 2020 ORDER BY t.year, t.month;
   ```

### Senaryo 4: "Yeni bir TUFE bulteni yayimlandi, pipeline'i tekrar calistirmak istiyorum"
1. `source:tufe-zaman-serisi` body'sinde: "Pipeline: pipelines/tufe_pipeline.py::run_pipeline()"
2. Pipeline dosya adlarini `_find_file()` ile tespit eder — dosya adinda "degisim" / "agirlik" / "katki" / "kapsaml" / "endeks-sonuclari" gecenleri bulur
3. Web trigger: `POST /api/tufe-resmi/run` (streaming output)
4. Manuel mode: `python -m pipelines.tufe_pipeline --from-uploads`

---

## 7. Bilinen Gotcha'lar (Ozet Liste)

| # | Gotcha | Nerede Yer Aliyor? | Cozum |
|---|--------|---------------------|-------|
| 1 | Ozel Kapsamli .xls aslinda XLSX | `source:tufe-ozel-kapsamli` | shutil.copy → .xlsx → openpyxl |
| 2 | openpyxl read_only WinError 32 | parse_ozel_kapsamli | read_only=False, data_only=True, try/finally close |
| 3 | COICOP code '0' cakismasi | parse_endeks_sonuclari | Sadece Duzey 2'de kaydet |
| 4 | Yi-UFE yil suffix (1982(1)) | parse_yufe | `re.match(r"^(\d{4})")` |
| 5 | Email .env yuklenmiyor | tufe_pipeline.py | `load_dotenv(BASE / ".env")` |
| 6 | Turkce dizin adi (TUFE/) | Tum path'ler | unicode escape `T\u00DCFE` veya direct UTF-8 |
| 7 | TUIK COICOP 12 → 13 gecisi | source:tufe-kategoriler | Eski "Haberlesme" → yeni "Bilgi ve iletisim" |
| 8 | Base yil 2003=100 → 2025=100 | Tum TUFE | 2026 Ocak'tan itibaren yeni base |
| 9 | Press ID degisebilir mi? | source_uri | 58295/58029 kalici gorunuyor, config.json'da tutuluyor |
| 10 | f-string CSS conflict | tufe_rapport.py | Plain string + `.replace()` |

---

## 8. Dosya Listesi ve Hizli Erisim

```
registry/themes/
└── theme%3Atufe.md                              # Ana konu basligi

registry/source_dependencies/
├── source%3Atufe-zaman-serisi.md                # 1. Manset TUFE zaman serisi
├── source%3Atufe-kategoriler.md                 # 2. 13 kategori snapshot
├── source%3Atufe-katkilar.md                    # 3. Katki puanlari
├── source%3Atufe-ozel-kapsamli.md               # 4. Cekirdek + Mallar + Hizmet (27 gosterge)
├── source%3Atufe-endeks-sonuclari.md            # 5. COICOP 5 duzey zaman serisi
└── source%3Ayufe-tarihsel-seri.md               # 6. Yi-UFE (Press 58029)

registry/memory/
└── tufe-registry-haritalama-aciklama.md         # Bu dosya (detaylı aciklama)
```

---

## 9. DB Tablolarinin Satir Sayilari (Mart 2026 itibari ile)

| Tablo | Satir | Kaynak |
|-------|-------|--------|
| tufe_monthly | 255 | source:tufe-zaman-serisi |
| tufe_categories | 14 | source:tufe-kategoriler (sadece son donem) |
| tufe_contributions | 14 | source:tufe-katkilar (sadece son donem) |
| tufe_core | 6.885 | source:tufe-ozel-kapsamli (27 × 255) |
| tufe_endeks | 77.764 | source:tufe-endeks-sonuclari (Duzey 2-5 × 255) |
| yufe_monthly | 531 | source:yufe-tarihsel-seri (1982-2026) |

**Toplam TÜFE verisi**: ~85.463 satir, ~6 MB SQLite DB.

---

## 10. Sonuc: Bu Dosya Neden Var?

Bu doküman, registry'nin "neden 7 dosya?" sorusunu tek bakışta cevaplıyor:
- **theme:tufe** = kapsayıcı (nerede ne var?)
- **6 source_dependency** = her biri farklı bir XLS dosyası, farklı bir DB tablosu, farklı bir parse fonksiyonu

Gelecekte TÜFE ile ilgili herhangi bir soru geldiğinde:
1. Bu dosyayı aç
2. İlgili senaryoyu (bölüm 6) bul
3. Source dependency'ye git → parser ve DB tablosu bilgisi orada
4. Theme dosyasına git → pipeline akışı ve gotchas orada

**Registry'nin büyüme kuralı**: Yeni bir TÜİK dosyası (ör. mevsim etkisinden arındırılmış TÜFE) eklenirse:
1. Yeni bir `source:tufe-xxx.md` yarat
2. `theme:tufe.md`'nin `source_dependency_ids` listesine ekle
3. Bu dokümana ekle (bölüm 3'e yeni alt-bölüm, bölüm 9'a yeni satır)
