---
record_type: source_dependency
id: source:tcmb-tarafli-swap-pdf
title: TCMB Taraflı Swap İşlemleri (Günlük PDF)
status: approved
source_kind: web_scrape_pdf
requiredness: optional
source_uri: 'https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Piyasa+Verileri'
local_hint: ''
description: >
  TCMB'nin Piyasa Verileri sayfasında günlük olarak yayımladığı
  "TCMB Taraflı Swap İşlemleri" PDF'i. Günlük frekansta tüm swap
  kalemlerinin (FX swap, altın swap, BIST swap, geleneksel/miktar
  ihaleleri, taraflı işlemler) stok tutarlarını verir.
  TcmbTarafliSwapPdf_Table Power Query sorgusu PDF linkini
  TCMB sayfasından otomatik bulur, Pdf.Tables ile parse eder ve
  "TOPLAM-STOK Alım/Satım Yönlü" sütunlarından net swap alımı çıkarır.
usage: >
  Power Query M kodunda TcmbTarafliSwapPdf_Table sorgusu:
  1) Piyasa Verileri sayfasında 'class=pdf' + ['tcmb','taraf','swap','islem'] kelimeleri eşleşen <a> linkini bulur
  2) PDF'i indirir, magic check (%PDF) yapar
  3) Pdf.Tables ile tabloları çıkarır, en çok kolona sahip + tarih satırlı tabloları seçer
  4) Net Swap Alım = Alım Yönlü Stok - Satım Yönlü Stok (Milyar USD)
  5) Altın Swap Alım = Altın Alım Stok - Altın Satım Stok
alternative_path: >
  Aylık fallback: TP.DOVVARNC.K14 (toplam) + K23 (diğer) URDL aylık serisinden
  benzer kavramsal kategoriler türetilebilir. Ancak günlük detay sadece
  bu PDF'te bulunur — taraflı (counterparty-specific) işlemler EVDS'de yok.
validation_note: >
  PDF içinde 20.03.2026 tarihinin manifest hatası var; PDF'te sadece 19.03.2026
  yer alır. M kod bu eksikliği şu kuralla telafi eder:
  19.03.2026 satırı kopyalanır, tarih 20.03.2026 olarak yeniden etiketlenir
  (TcmbTarafliSwapPdf_Table M kodu, satır 2536-2558).
  Hardcoded patch — Python port'ta dinamik bir "missing date detection"
  mantığına çevrilmesi önerilir.
theme_ids:
- theme:reserves
- theme:tcmb-swap
indicator_ids: []
---
# TCMB Taraflı Swap İşlemleri (Günlük PDF)

## Kaynak Türü

`web_scrape_pdf` — TCMB Piyasa Verileri sayfasından günlük PDF tarama

## Zorunluluk

`optional` — günlük (PDF) erişilemezse aylık URDL fallback'i kullanılır
(TP.DOVVARNC.K14, K23). Ama günlük frekanstaki taraflı detay yalnızca bu
PDF'tedir.

## Kaynak URI

https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Piyasa+Verileri

## PDF Bulma Mantığı (M kodu, satır 2191-2210)

```python
Keywords = ["tcmb", "taraf", "swap", "islem"]

PdfSatiri = LinkleriCek.filter(
    href ends with .pdf or class contains "pdf"
    AND
    title + metin (lowercase, normalize TR) contains all of Keywords
)
```

## PDF İçeriği — Sütun Yapısı (v9)

PDF'ten çıkarılan tablo Tarih + ~25 swap kalem sütunu içerir:

| Sütun | İçerik |
|---|---|
| **Tarih (Valör)** | Günlük işlem tarihi |
| TCMB Döviz Karşılığı TL Swap Piyasası — Stok | Açık + Alım yönlü stoklar |
| BIST Swap Piyasası — Stok | BIST üzerinden swap |
| TCMB TL Karşılığı Altın Swap Piyasası | CBRT Tur işlemleri |
| TCMB Döviz Karşılığı TL Swap Geleneksel İhaleleri | (4 sütun: faiz/teklif/sonuç/stok) |
| TCMB Döviz Karşılığı TL Swap Miktar İhaleleri | Miktar bazlı |
| TCMB Altın Karşılığı TL Swap Geleneksel İhaleleri | (4 sütun) |
| TCMB Döviz Karşılığı Altın Swap Piyasası — Stok | Net alım/satım yönlü |
| **TOPLAM - STOK (Alım Yönlü)** | Tüm alım yönlü stokların toplamı |
| **TOPLAM - STOK (Satım Yönlü)** | Tüm satım yönlü stokların toplamı |

## Türetilen Sütunlar (M kodu, satır 2477-2533)

```
Tcmb Günlük Swap Net Alım (Milyar USD) =
    TOPLAM-STOK (Alım Yönlü) - TOPLAM-STOK (Satım Yönlü)

Tcmb Günlük Altın Swap Net Alım (Milyar USD) =
    Altın Alım Yönlü Stok - Altın Satım Yönlü Stok
```

Tüm rakamlar PDF'te Milyon USD, çıktıda Milyar USD'ye (÷1000) çevrilir.

## Tarih Patch (M kodu, satır 2536-2558)

```python
MissingDate  = #date(2026, 3, 20)
SourceDate   = #date(2026, 3, 19)

if 20.03.2026 zaten varsa: dokunma
elif 19.03.2026 yoksa:    dokunma (kaynak yok)
else:
    19.03.2026 satırını kopyala, tarihini 20.03.2026 yap
```

**Python port önerisi:** Bu hardcoded patch'in yerine dinamik eksik-tarih
tespiti (gün eksikse, önceki iş gününden interpolate et) konulmalı.

## Net Rezerv Formüllerinde Kullanımı

```
Swap Hariç Net Altın Rezervi:
    if PDF varsa:  NetAltin - PDFAltinSwapNet
    else (URDL):    NetAltin + DigerSwapURDL  (TP.DOVVARNC.K23 fallback)

Swap Hariç Net Döviz Rezervi:
    mbAdj = MBSwapURDL  (her zaman URDL'den, K18 + K22)
    if PDF varsa:  NetDoviz + mbAdj - PDFDovizSwapNet
    else:           NetDoviz + mbAdj + (SwapTotURDL - mbAdj)
```

İşaret kuralı (M kodu satır 1940-1944):
- **URDL**: net alım NEGATİF gösterir → toplama
- **PDF**: net alım POZİTİF gösterir → çıkarma

## Bilinen Riskler

1. **PDF format değişimi**: TCMB PDF tablosunun sütun yapısı değişirse
   `ColHasAll({"toplam","stok","alim","yonlu"})` matcher başarısız olur.
2. **Pdf.Tables bağımlılığı**: Power Query bu fonksiyon olmadan çalışmaz;
   eski Excel sürümleri ve LibreOffice desteklemiyor. Python port'ta
   `pdfplumber` veya `tabula-py` kullanılmalı.
3. **Manifest hataları**: Tarih patch'i benzeri eksiklikler tekrarlayabilir.
4. **PDF link yapısı**: TCMB sayfa şablonu değişirse `class=pdf` + keyword
   matcher yenilenmeli.
