---
task_id: notebook-semantics-07-yi-yrlsk-fnsl-vrlk-v1
notebook_path: ../Telegram Bot/notebooks/Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
lane: L1_EVDS_standard
priority: P1
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
  - tasks/notebook_semantics/04_Pys_Ktlmclr_V2.md
evds_code_families:
  - TP.DIBSPIYDEG
  - TP.DK
  - TP.EBONDPIYDEG
  - TP.HPBITABLO1
  - TP.HPBITABLO2
  - TP.YDOSBAPIYDEG
  - TP.YIOSBAPIYDEG
external_inputs:
  - manual_inline:mkk-hisse-ledger
  - manual_inline:mkk-fon-ledger
  - web_scrape:vap-scrape-attempt
target_outputs:
  - generated/Yi_Yrlsk_Fnsl_Vrlk_V1_ticker_report.md
  - generated/Yi_Yrlsk_Fnsl_Vrlk_V1_registry_import.csv
known_blockers:
  - manual MKK values are embedded inline in notebook
  - VAP scrape attempt exists but is not a stable production input
---

# Yi_Yrlsk_Fnsl_Vrlk_V1

## Amac

Bu notebook, yurtici yerlesiklerin finansal varlik kompozisyonunu EVDS verileri ve manuel MKK girdileriyle birlikte kurar. Gorev, temiz EVDS semantigini kaybetmeden MKK bloklarini source dependency olarak modele eklemek ve varlik siniflari bazli gostergeleri kontrollu sekilde tanimlamaktir.

## Mevcut Notebook Gercekleri

- Notebookta `serie_info` output'u vardir.
- `84` benzersiz EVDS kodu kullanir.
- Ana EVDS fetch temizdir; aileler acik secilmistir.
- Notebookun ust kismina gomulu manuel veriler vardir:
  - `mkk_hisse_verisi`
  - `mkk_hisse_verisi_aylik`
  - `mkk_fon_verisi`
- Ayrica VAP/MKK icin Playwright tabanli bir scrape denemesi bulunur; bu guvenilir aktif kaynak degildir.

## EVDS Kod Envanteri

### Aile ozetleri

- `TP.DIBSPIYDEG`: `6`
- `TP.DK`: `1`
- `TP.EBONDPIYDEG`: `6`
- `TP.HPBITABLO1`: `3`
- `TP.HPBITABLO2`: `22`
- `TP.YDOSBAPIYDEG`: `23`
- `TP.YIOSBAPIYDEG`: `23`

### Tam kod listesi

```text
TP.DIBSPIYDEG:
TP.DIBSPIYDEG.S11, TP.DIBSPIYDEG.S12, TP.DIBSPIYDEG.S122, TP.DIBSPIYDEG.S13, TP.DIBSPIYDEG.S14, TP.DIBSPIYDEG.S15

TP.DK:
TP.DK.USD.A.YTL

TP.EBONDPIYDEG:
TP.EBONDPIYDEG.S11, TP.EBONDPIYDEG.S12, TP.EBONDPIYDEG.S122, TP.EBONDPIYDEG.S13, TP.EBONDPIYDEG.S14, TP.EBONDPIYDEG.S15

TP.HPBITABLO1:
TP.HPBITABLO1.19, TP.HPBITABLO1.20, TP.HPBITABLO1.21

TP.HPBITABLO2:
TP.HPBITABLO2.13, TP.HPBITABLO2.14, TP.HPBITABLO2.15, TP.HPBITABLO2.2, TP.HPBITABLO2.23, TP.HPBITABLO2.24, TP.HPBITABLO2.25, TP.HPBITABLO2.26, TP.HPBITABLO2.27, TP.HPBITABLO2.28, TP.HPBITABLO2.29, TP.HPBITABLO2.3, TP.HPBITABLO2.30, TP.HPBITABLO2.31, TP.HPBITABLO2.32, TP.HPBITABLO2.33, TP.HPBITABLO2.34, TP.HPBITABLO2.4, TP.HPBITABLO2.5, TP.HPBITABLO2.6, TP.HPBITABLO2.7, TP.HPBITABLO2.8

TP.YDOSBAPIYDEG:
TP.YDOSBAPIYDEG.S11, TP.YDOSBAPIYDEG.S15, TP.YDOSBAPIYDEG.S16, TP.YDOSBAPIYDEG.S2, TP.YDOSBAPIYDEG.S21, TP.YDOSBAPIYDEG.S22, TP.YDOSBAPIYDEG.S24, TP.YDOSBAPIYDEG.S3, TP.YDOSBAPIYDEG.S30, TP.YDOSBAPIYDEG.S34, TP.YDOSBAPIYDEG.S40, TP.YDOSBAPIYDEG.S41, TP.YDOSBAPIYDEG.S43, TP.YDOSBAPIYDEG.S49, TP.YDOSBAPIYDEG.S5, TP.YDOSBAPIYDEG.S53, TP.YDOSBAPIYDEG.S54, TP.YDOSBAPIYDEG.S59, TP.YDOSBAPIYDEG.S60, TP.YDOSBAPIYDEG.S62, TP.YDOSBAPIYDEG.S68, TP.YDOSBAPIYDEG.S72, TP.YDOSBAPIYDEG.S74

TP.YIOSBAPIYDEG:
TP.YIOSBAPIYDEG.S11, TP.YIOSBAPIYDEG.S15, TP.YIOSBAPIYDEG.S16, TP.YIOSBAPIYDEG.S2, TP.YIOSBAPIYDEG.S21, TP.YIOSBAPIYDEG.S22, TP.YIOSBAPIYDEG.S24, TP.YIOSBAPIYDEG.S3, TP.YIOSBAPIYDEG.S30, TP.YIOSBAPIYDEG.S34, TP.YIOSBAPIYDEG.S40, TP.YIOSBAPIYDEG.S41, TP.YIOSBAPIYDEG.S43, TP.YIOSBAPIYDEG.S49, TP.YIOSBAPIYDEG.S5, TP.YIOSBAPIYDEG.S53, TP.YIOSBAPIYDEG.S54, TP.YIOSBAPIYDEG.S59, TP.YIOSBAPIYDEG.S60, TP.YIOSBAPIYDEG.S62, TP.YIOSBAPIYDEG.S68, TP.YIOSBAPIYDEG.S72, TP.YIOSBAPIYDEG.S74
```

## Dis Kaynak Envanteri

- `source:yiyrlsk-mkk-hisse-manual`
  - `source_kind=manual_inline`
  - `requiredness=required_input`
  - kaynak: `mkk_hisse_verisi` ve `mkk_hisse_verisi_aylik`
  - amac: yerli hisse portfoy degeri ve gercek kisi kirilimi

- `source:yiyrlsk-mkk-fon-manual`
  - `source_kind=manual_inline`
  - `requiredness=required_input`
  - kaynak: `mkk_fon_verisi`
  - amac: yatirim fonu portfoy degeri ve gercek kisi kirilimi

- `source:yiyrlsk-vap-scrape-attempt`
  - `source_kind=web_scrape`
  - `requiredness=optional_replacement`
  - kaynak: VAP/MKK iframe scrape denemesi
  - not: mevcut durumda stabil aktif girdi degildir; manuel ledger yerine gelecek aday kaynak gibi ele alinir

## Beklenen Registry Nesneleri

### Theme

- `theme:resident-financial-assets`
- `theme:resident-securities`
- `theme:resident-deposits`

### Indicator

Ilk fazda en az su indicator seti beklenir:

- `derived:private-sector-bond-total`
- `derived:private-sector-eurobond-total`
- `derived:tl-deposit-total`
- `derived:fx-deposit-total`
- `derived:local-equity-total`
- `derived:local-fund-total`
- `derived:resident-financial-assets-total`
- `derived:real-person-share`

### Source dependency

- `source:yiyrlsk-mkk-hisse-manual`
- `source:yiyrlsk-mkk-fon-manual`
- `source:yiyrlsk-vap-scrape-attempt`

## Analyzer Kurallari

- Resmi EVDS adlari `serie_info` output'undan okunur.
- Bu notebook L1 lane'de kalir; burada L1 "hic dis kaynak yok" degil, "primer extraction omurgasi temiz EVDS" anlamindadir.
- MKK ve VAP girdileri yine source dependency olarak kayda gecirilir.
- MKK inline dictionary'leri series gibi degil source dependency gibi ele alinir.
- `source:yiyrlsk-vap-scrape-attempt` aktif veri kaynagi degil, alternatif/gelecek kaynak olarak isaretlenir.
- `TP.HPBITABLO1` ve `TP.HPBITABLO2` aileleri mevduat ve fon semantigini, `TP.DIBSPIYDEG` ve `TP.EBONDPIYDEG` aileleri menkul kiymet semantigini, `TP.YDOSBAPIYDEG` ve `TP.YIOSBAPIYDEG` aileleri yerli/yabanci tasnifini besler.

## Turetilmis Gostergeler

Notebooktan gorunen ana user-facing kolon gruplari:

- Ozel sektor tahvil (gercek kisi, tuzel kisi, bankalar, toplam)
- Ozel sektor eurobond (gercek kisi, tuzel kisi, bankalar, toplam)
- TL mevduat
- YP mevduat
- Yatirim fonu
- Hisse senedi
- DIBS
- Eurobond
- Yerli finansal varlik toplami

Karar:

- Tum alt kolonlar tek tek indicator olmayacak.
- Varlik sinifi bazli toplamlar ve ana kirilim driver'lari indicator olarak yazilacak.

## Cozumsuzler ve Fallback

- MKK manuel verileri resmi EVDS adi gibi davranmaz.
- VAP scrape denemesi stabil olmadigi icin source dependency notunda "replacement candidate" olarak gecmelidir.
- EVDS tarafinda `serie_info` bulundugu icin unresolved oraninin dusuk olmasi beklenir; yuksek unresolved durum test hatasi sayilmalidir.

## Gerekli CLI/Sema Degisiklikleri

- `spec=yi-yrlsk-fnsl-vrlk-v1`
- source dependency destekli import ve show-map
- L1 lane regression testlerinde bu notebook, MKK kaynaklariyla birlikte yine de temiz EVDS extraction ornegi sayilacak

## Test Senaryolari

1. Benzersiz ticker sayisi `84` olmali.
2. `7` EVDS ailesi dogru cikmali.
3. `source:yiyrlsk-mkk-hisse-manual`, `source:yiyrlsk-mkk-fon-manual`, `source:yiyrlsk-vap-scrape-attempt` olusmali.
4. En az `8` ana indicator uretilmeli.
5. `serie_info` kaynakli resmi adlar baskin olmali; manual MKK kaynaklari series gibi sayilmamali.

## Acceptance Checklist

- [ ] Buyuk EVDS aileleri eksiksiz cozumlendi.
- [ ] MKK manuel verisi source dependency olarak kaydedildi.
- [ ] VAP scrape denemesi opsiyonel replacement olarak dogru etiketlendi.
- [ ] Varlik sinifi bazli indicator seti gereksiz sisirme olmadan yazildi.
