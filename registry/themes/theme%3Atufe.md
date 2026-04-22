---
record_type: theme
id: theme:tufe
title: Tuketici Fiyat Endeksi (TUFE) ve Yi-UFE
status: approved
description: Turkiye TUFE ve Yi-UFE analizi — 13 ana harcama grubu (COICOP 2018), cekirdek enflasyon (A-F), Mallar/Hizmet kirilimi, ozet tablo ve zaman serisi DB
series_ids: []
indicator_ids:
- derived:cekirdek-tufe-c
- derived:mallar-endeks
- derived:hizmet-endeks
chart_ids: []
source_dependency_ids:
- source:tufe-zaman-serisi
- source:tufe-kategoriler
- source:tufe-katkilar
- source:tufe-ozel-kapsamli
- source:tufe-endeks-sonuclari
- source:yufe-tarihsel-seri
questions:
- TUFE ne kadar arttı (aylik, yillik)?
- Cekirdek enflasyon C gostergesi ne durumda?
- Mallar ve Hizmet alt kirimlarinda durum nedir?
- Hangi kategoriler en yuksek katki yaptı?
- Yi-UFE ve TUFE arasinda ayrisma var mi?
- Enerji, gida, kira kalemleri nasil seyrediyor?
- Gecen yilin ayni ayina gore karsilastirma nasil?
---
# Tuketici Fiyat Endeksi (TUFE) ve Yi-UFE

## Aciklama

Turkiye resmi tuketici fiyat endeksi (TUFE) ve yurt ici uretici fiyat endeksi (Yi-UFE) analizi. TUIK her ayin 3'unde haber bulteni yayimlar; pipeline bu bulten dosyalarini indirip SQLite DB'ye yazar ve ozet tablo uretir.

**Portal**: veriportali.tuik.gov.tr (eski data.tuik.gov.tr'dan tasindi)
**TUFE Press ID**: 58295 (kalici)
**Yi-UFE Press ID**: 58029 (kalici)
**Base Yillar**: TUFE 2025=100 (2026 Ocak'tan itibaren), Yi-UFE 2003=100
**COICOP**: 2018 5'li duzey (13 ana harcama grubu, 174 alt sinif)

## Veri Kaynaklari

### TUFE (Press 58295) — 5 dosya
1. **source:tufe-zaman-serisi** — Genel endeks zaman serisi (t=i)
2. **source:tufe-kategoriler** — 13 kategori snapshot agirlik+endeks+5 degisim (t=r)
3. **source:tufe-katkilar** — 13 kategori aylik/yillik katki puanlari (t=r)
4. **source:tufe-ozel-kapsamli** — Cekirdek A-F + Mallar/Hizmet kirilimi (27 gosterge zaman serisi, t=i, xlsx-masked-as-xls)
5. **source:tufe-endeks-sonuclari** — COICOP 5 duzey kirilim endeksleri (t=i, native xlsx, 4 sheet)

### Yi-UFE (Press 58029) — 1 dosya
6. **source:yufe-tarihsel-seri** — Zaman serisi 1982-bugun (t=i, 5 section wide format)

## Database Tablolari (TUFE/tufe.db)

### Ana Zaman Serileri
- **tufe_monthly** — TUFE genel endeks ve degisim oranlari (year, month, index_value, monthly_pct, ytd_pct, annual_pct, avg_12m_pct)
- **yufe_monthly** — Yi-UFE zaman serisi (ayni schema)

### Kategori Kirinlimlari
- **tufe_categories** — 13 ana harcama grubu snapshot (year, month, category_code 00-13, name, weight, index, 4 degisim)
- **tufe_contributions** — Kategori bazli aylik/yillik katki puanlari
- **tufe_endeks** — COICOP 5 duzey tum kirilimlar zaman serisi (year, month, coicop_code, coicop_level 2-5, category_name, index_value) ~77.764 satir

### Cekirdek ve Alt Kirilimlar
- **tufe_core** — Ozel kapsamli gostergeler (27 kod × 255 donem):
  - `A`-`F`: Cekirdek enflasyon gostergeleri
  - `M_TOTAL`, `M_01`-`M_14`: Mallar aggregate + 14 alt kalem
  - `H_TOTAL`, `H_01`-`H_05`: Hizmet aggregate + 5 alt kalem

### Yardimci
- **yufe_sectors** — Yi-UFE sektor kirilimi (henuz doldurulmadi)
- **pipeline_runs** — Pipeline calistirma audit log
- **uploads** — Manuel yuklenen dosyalar (checksum, file_type)

## Ozet Tablo Yapisi

`pipelines/tufe_rapport.py::generate_html_table()` cikisi:
`TUFE/outputs/tufe_ozet.html` + `.pdf` + `.png`

### Sutunlar (dinamik, her ay otomatik kayar)
- **Aylik (%)**: {donem_cur} | {donem_prev}
- **Yillik (%)**: {donem_cur} | {donem_prev}
- donem_cur = en son TUFE donemi (ornek: "Mart 2026")
- donem_prev = gecen yilin ayni ayi (ornek: "Mart 2025")

### Satirlar (18 adet)
1. **TUFE** (genel endeks, tufe_endeks'ten coicop_code='0')
2-14. **13 Ana Harcama Grubu** (Duzey 2, code 01-13)
15. **Cekirdek TUFE (C)** (tufe_core'dan, indicator_code='C' — Enerji, gida ve alkolsuz icecekler, alkollu ickiler ile tutun urunleri ve altin haric TUFE)
16. **Mallar** (tufe_core'dan, indicator_code='M_TOTAL')
17. **Hizmet** (tufe_core'dan, indicator_code='H_TOTAL')
18. **Yurt Ici UFE** (yufe_monthly endeks)

Tum degisim oranlari **endeks degerlerinden hesaplanir** (pre-computed % kullanilmaz).

## Pipeline Akisi

```
pipelines/tufe_pipeline.py::run_pipeline()
  |
  ├── 1. Dosya temini
  |   ├── fetch_tufe_files()  → TUFE press 58295 (Playwright)
  |   └── fetch_yufe_files()  → Yi-UFE press 58029 (Playwright)
  |
  ├── 2. Parse
  |   ├── parse_zaman_serisi()      → tufe_monthly
  |   ├── parse_kategoriler()       → tufe_categories
  |   ├── parse_contributions()     → tufe_contributions
  |   ├── parse_ozel_kapsamli()     → tufe_core (27 kod)
  |   ├── parse_endeks_sonuclari()  → tufe_endeks (COICOP 2-5)
  |   └── parse_yufe()              → yufe_monthly
  |
  ├── 3. Validate (CP#3-7)
  |   ├── Magic bytes kontrolu
  |   ├── Satir sayisi
  |   ├── Tarih araligi (max 60 gun)
  |   ├── Cift donem kontrolu
  |   └── SHA-256 checksum duplicate
  |
  ├── 4. DB upsert (INSERT OR REPLACE)
  |
  ├── 5. Rapor uret (tufe_rapport.py)
  |   └── HTML + PDF + PNG ozet tablo
  |
  └── 6. Email gonder (tufe_email.py)
```

## FastAPI Endpoints (routers/tufe_resmi.py)

- `GET /api/tufe-resmi/data` — Son donem ozet
- `GET /api/tufe-resmi/time-series?limit=120` — TUFE zaman serisi
- `GET /api/tufe-resmi/categories?months=12` — Kategori kirilimi
- `GET /api/tufe-resmi/core?limit=240` — Cekirdek/Mallar/Hizmet gostergeleri
- `GET /api/tufe-resmi/yufe?limit=120` — Yi-UFE
- `GET /api/tufe-resmi/last-run` — Son pipeline calistirma
- `GET /api/tufe-resmi/brief` — Kisa metin ozeti
- `POST /api/tufe-resmi/run` — Pipeline tetikle (admin)
- `POST /api/tufe-resmi/upload` — Manuel XLS yukle (admin)

## Kritik Gotchalar

- **Ozel Kapsamli dosyasi**: `.xls` uzantili ama gercekte XLSX — `shutil.copy` + `openpyxl` gerekir
- **read_only=True kullanma**: openpyxl read_only mode Windows'ta `WinError 32` verir (temp file locked)
- **COICOP code '0' cakismasi**: Endeks sonuclari dosyasinda code '0' her 4 sheet'te var — sadece Duzey 2'de kaydet
- **Yi-UFE year suffix**: (1), (2), (3), (4) → regex `^(\d{4})` ile yil cikar
- **Turkce karakter dizin adi**: `TÜFE/` (buyuk U umlaut) — Windows'ta path olarak calisir ama print() encoding sorunu yapabilir
- **Email .env yukleme**: `pipelines/tufe_pipeline.py` icinde `load_dotenv(BASE / ".env")` sart
- **Kategori mapping**: Eski COICOP 12 -> yeni COICOP 2018 13 kategori gecisi. Eski "Haberlesme" -> yeni "Bilgi ve iletisim"

## Analiz Sorulari

- TUFE yillik enflasyon ne durumda? (tufe_monthly.annual_pct son donem)
- Hangi kategori en yuksek yillik artis? (tufe_categories order by annual_pct desc)
- Cekirdek TUFE C gostergesi manset TUFE'den nasil ayrisiyor? (tufe_core C vs tufe_monthly)
- Mallar/Hizmet enflasyonu ayrismasi nedir? (M_TOTAL vs H_TOTAL)
- Yi-UFE TUFE'den yuksek mi? (uretici tarafinda baski sinyali)
- Gecen yilin ayni ayina gore bu ay daha mi hizli artis? (dinamik ozet tablo)
- Enerji, gida, kira kalemleri nasil seyrediyor? (tufe_core M_01, M_02, H_01)
