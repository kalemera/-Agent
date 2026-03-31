---
task_id: notebook-semantics-03-prbnk-mnklkymt-v5
notebook_path: ../Telegram Bot/notebooks/PrBnk_MnklKymt_V5.ipynb
lane: L2_EVDS_plus_external
priority: P2
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
  - tasks/notebook_semantics/01_DTH_Blg_V7.md
evds_code_families:
  - TP.AB
  - TP.DIBSPIYDEG
  - TP.DK
  - TP.HPBITABLO5
  - TP.MKNETHAR
external_inputs:
  - http_download:tcmb-weekly-zip-xlsx
  - pdf_table:tcmb-swap-pdf
target_outputs:
  - generated/PrBnk_MnklKymt_V5_ticker_report.md
  - generated/PrBnk_MnklKymt_V5_registry_import.csv
known_blockers:
  - notebook contains active and legacy/commented extraction blocks together
  - some source URLs and proxy placeholders are operational, not semantic labels
  - mixed EVDS families produce many user-facing derived series
---

# PrBnk_MnklKymt_V5

## Amac

Bu notebook, portfoy akimlari, hisse, DIBS ve swap anlatisini bir araya getirir. Gorev, EVDS ailelerini anlamli gruplara ayirmak, TCMB haftalik ZIP/XLSX ve swap PDF girdilerini source dependency olarak modellemek ve notebookun urettigi yogun turetilmis kolonlari kontrollu indicator setlerine cevirmektir.

## Mevcut Notebook Gercekleri

- Notebookta `serie_info` output'u vardir.
- `57` benzersiz EVDS kodu kullanir.
- Birden fazla EVDS fetch blogu vardir.
- Ek kaynaklar:
  - TCMB web sayfasindan haftalik ZIP/XLSX indirme blogu
  - TCMB swap PDF indirme ve `tabula.read_pdf(...)` ile ayrisma
- Notebookta eski/yorum satirina alinmis bloklar da vardir; bunlar semantik cikarimda `dormant_candidate` sayilmalidir.

## EVDS Kod Envanteri

### Aile ozetleri

- `TP.AB`: `15`
- `TP.DIBSPIYDEG`: `1`
- `TP.DK`: `1`
- `TP.HPBITABLO5`: `22`
- `TP.MKNETHAR`: `18`

### Tam kod listesi

```text
TP.AB:
TP.AB.A01, TP.AB.A02, TP.AB.A03, TP.AB.A08, TP.AB.A09, TP.AB.A11, TP.AB.A12, TP.AB.A15, TP.AB.A16, TP.AB.A17, TP.AB.A18, TP.AB.A23, TP.AB.C1, TP.AB.C2, TP.AB.TOPLAM

TP.DIBSPIYDEG:
TP.DIBSPIYDEG.ST

TP.DK:
TP.DK.USD.A.YTL

TP.HPBITABLO5:
TP.HPBITABLO5.1, TP.HPBITABLO5.10, TP.HPBITABLO5.11, TP.HPBITABLO5.12, TP.HPBITABLO5.13, TP.HPBITABLO5.14, TP.HPBITABLO5.15, TP.HPBITABLO5.16, TP.HPBITABLO5.17, TP.HPBITABLO5.18, TP.HPBITABLO5.19, TP.HPBITABLO5.2, TP.HPBITABLO5.20, TP.HPBITABLO5.21, TP.HPBITABLO5.22, TP.HPBITABLO5.3, TP.HPBITABLO5.4, TP.HPBITABLO5.5, TP.HPBITABLO5.6, TP.HPBITABLO5.7, TP.HPBITABLO5.8, TP.HPBITABLO5.9

TP.MKNETHAR:
TP.MKNETHAR.M1, TP.MKNETHAR.M10, TP.MKNETHAR.M11, TP.MKNETHAR.M12, TP.MKNETHAR.M2, TP.MKNETHAR.M20, TP.MKNETHAR.M21, TP.MKNETHAR.M22, TP.MKNETHAR.M23, TP.MKNETHAR.M24, TP.MKNETHAR.M25, TP.MKNETHAR.M26, TP.MKNETHAR.M3, TP.MKNETHAR.M4, TP.MKNETHAR.M5, TP.MKNETHAR.M7, TP.MKNETHAR.M8, TP.MKNETHAR.M9
```

## Dis Kaynak Envanteri

- `source:prbnk-weekly-zip`
  - `source_kind=http_download`
  - `requiredness=required_input`
  - amac: TCMB haftalik para ve banka istatistiklerinden ek XLSX tablo almak

- `source:prbnk-swap-pdf`
  - `source_kind=pdf_table`
  - `requiredness=required_input`
  - amac: TCMB swap stokunun tablo seviyesinde ayrisimi

Kayit disi tutulacaklar:

- proxy placeholder URL'leri
- font ve gorunum asset'leri

## Beklenen Registry Nesneleri

### Theme

- `theme:portfolio-flows`
- `theme:foreign-ownership`
- `theme:swap-and-securities`

### Indicator

Ilk fazda en az su indicator seti cikarilacak:

- `derived:equity-stock`
- `derived:equity-foreign-share`
- `derived:dibs-stock`
- `derived:dibs-foreign-share`
- `derived:equity-plus-dibs-flow`
- `derived:swap-stock`
- `derived:swap-net-change`
- `derived:portfolio-flow-total`

### Source dependency

- `source:prbnk-weekly-zip`
- `source:prbnk-swap-pdf`

## Analyzer Kurallari

- Resmi adlar `serie_info` output'undan okunur.
- `TP.MKNETHAR.*` ailesi menkul kiymet stogu ve akimlarini besler.
- `TP.HPBITABLO5.*` ailesi mevduat/parite tarafinda yardimci blogdur; notebookta rolune gore bilesen veya yorum girdisi olarak isaretlenmelidir.
- `TP.AB.*` ve `TP.DK.USD.A.YTL` rezerv/swap ve kur cevirimleri icin destekleyici roldedir.
- Comment satirina alinmis veya triple-quoted eski bloklar `dormant_candidate` olarak belgelenmeli; aktif indicator'a donusturulmemelidir.
- PDF ve ZIP kaynaklari indicator input'u olabilir, fakat resmi EVDS series gibi davranilmaz.

## Turetilmis Gostergeler

Notebookun gorunen anlatisi su ailelerden olusur:

- Portfoy akimlari
- Hisse stogu
- Hisse yabanci orani
- DIBS stogu
- DIBS yabanci orani
- Swap stogu
- Yabanci swap net degisimi
- Hisse Senedi + DIBS net degisimi

Karar:

- Ilk fazda grafik basina ayri indicator yerine anlati omurgasi indicatorlari kaydedilir.
- Kolon sayisi cok oldugu icin her non-TP kolon indicator'a donusturulmez.

## Cozumsuzler ve Fallback

Fallback sirasi:

1. `serie_info`
2. active rename/columns mapping'leri
3. non-TP derived kolon atamalari
4. unresolved ledger

Ozel not:

- Comment icindeki eski ZIP extraction blogu sadece semantik delil olarak okunur; aktif source dependency sayilmasi icin notebookun fiili akisini besledigine bakilir.

## Gerekli CLI/Sema Degisiklikleri

- `spec=prbnk-mnklkymt-v5`
- source dependency destekli import row'lari
- `show-map` indicator -> source dependency baglarini gostermeli

## Test Senaryolari

1. Benzersiz ticker sayisi `57` olmali.
2. `5` aile aynen cikmali.
3. `source:prbnk-weekly-zip` ve `source:prbnk-swap-pdf` olusmali.
4. En az `8` ana indicator uretilmeli.
5. Comment icindeki eski bloklar aktif series veya indicator olarak sayilmamali.

## Acceptance Checklist

- [ ] `57` EVDS kodunun aile dagilimi dogru cikti.
- [ ] Portfoy akimlari / swap / menkul kiymet indicator seti kaydedildi.
- [ ] ZIP ve PDF girdileri source dependency oldu.
- [ ] Legacy/commented bloklar aktif akisla karistirilmadi.
- [ ] Rapor, unresolved veya dormant adaylari acikca ayiriyor.
