# Notebook Semantics Task Pack

Bu klasor, `../Telegram Bot/notebooks` altindaki notebooklari ortak bir semantik harita ve registry akisina tasimak icin hazirlanmis gorev paketidir. Hedef, tekil sohbet baglamina bagli kalmadan bir notebookun EVDS serilerini, turetilmis gostergelerini, dis kaynak bagimliliklarini ve belirsizliklerini yeniden insa edebilmektir.

## Nasil Okunmali

1. Ilk olarak `tasks/notebook_semantics/00_SHARED_SPEC.md` okunur.
2. Ardindan lane sirasina gore ilgili notebook gorev dosyasi okunur.
3. Uygulamaya gecilecegi zaman ayni lane icindeki notebooklar paralel degil, sirali ele alinir.
4. Bir notebook gorev dosyasi tek basina uygulanabilir olacak sekilde yazilmistir; sohbet gecmisi zorunlu degildir.

## Lane Matrisi

Lane yorum kurali:

- `L1_EVDS_standard`: ana extraction akisi temiz EVDS uzerindedir; yardimci manuel veya web girdileri olabilir ama primer semantik omurga EVDS'dir.
- `L2_EVDS_plus_external`: EVDS ile birlikte en az bir zorunlu veya belirgin `source_dependency` vardir.
- `L3_manual_or_fallback`: `serie_info` yoktur veya fallback/manual ledger mantigi birinci sinif hale gelir.

| Notebook | Lane | EVDS aileleri | Dis kaynaklar | Ana blokajlar |
| --- | --- | --- | --- | --- |
| `DTH_Blg_V7.ipynb` | `L2_EVDS_plus_external` | `TP.HPBITABLO2`, `TP.HPBITABLO3`, `TP.HPBITABLO4`, `TP.HPBITABLO5` | Yerel eski seri Excel dosyasi | `TP.HPBITABLO4.14` ve `.15` notebooktan cozumlenemiyor |
| `Eurobnd_Blg_V4.ipynb` | `L2_EVDS_plus_external` | `TP.EBONDYAZDEG`, `TP.YDOSBAYAZDEG` | BBG Excel upload, TCMB vade PDF indirme, HMB odeme projeksiyon workbook'u | Upload ve PDF akislarinin sayfa/sekme adlari degisken |
| `PrBnk_MnklKymt_V5.ipynb` | `L2_EVDS_plus_external` | `TP.AB`, `TP.DIBSPIYDEG`, `TP.DK`, `TP.HPBITABLO5`, `TP.MKNETHAR` | TCMB haftalik ZIP/XLSX, TCMB swap PDF | Karisik kaynakli ve kismi yorum satirina alinmis bloklar var |
| `Pys_Ktlmclr_V2.ipynb` | `L1_EVDS_standard` | `TP.BEK` | Yok | `TP.PKAUO` serileri yorum satirinda; aktif akis `TP.BEK` ile sinirli |
| `Rzrv_Blg_V7.ipynb` | `L3_manual_or_fallback` | `TP.AB`, `TP.DK`, `TP.DOVVARNC` | TCMB swap PDF, manuel inline swap tablosu | `SERIE_NAME` izi print output fallback'iyle geliyor; `TP.DOVVARNC.K18` aktif akis disinda |
| `Tbl_Apko.ipynb` | `L3_manual_or_fallback` | `TP.AB`, `TP.DB`, `TP.DIBSPIYDEG`, `TP.DK`, `TP.EBONDPIYDEG`, `TP.FDVY37`, `TP.HPBITABLO4`, `TP.KALANVADE`, `TP.MKNETHAR`, `TP.ODANA6`, `TP.YDOSBAYAZDEG` | BBG Excel upload, HMB AB borc XLS, TCMB swap PDF, BDDK haftalik bulletin scrape | `serie_info` yok, coklu frekans ve coklu kaynak ayni tabloda birlesiyor |
| `Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb` | `L1_EVDS_standard` | `TP.DIBSPIYDEG`, `TP.DK`, `TP.EBONDPIYDEG`, `TP.HPBITABLO1`, `TP.HPBITABLO2`, `TP.YDOSBAPIYDEG`, `TP.YIOSBAPIYDEG` | Manuel MKK inline verileri, opsiyonel VAP scrape denemesi | EVDS temiz olsa da MKK verisi notebook icinde manuel tutuluyor |

## Completion Matrisi

| Notebook | Spec | Durum | Unresolved | Not |
| --- | --- | --- | --- | --- |
| `DTH_Blg_V7.ipynb` | `dth-blg-v7` | `done` | `2` | `TP.HPBITABLO4.14` ve `.15` notebooktan cozumlenemiyor |
| `Eurobnd_Blg_V4.ipynb` | `eurobnd-blg-v4` | `done` | `0` | Uc source dependency ile rapor ve import CSV uretiliyor |
| `PrBnk_MnklKymt_V5.ipynb` | `prbnk-mnklkymt-v5` | `done` | `0` | Legacy/commented bloklar aktif akisla karistirilmiyor |
| `Pys_Ktlmclr_V2.ipynb` | `pys-ktilmclr-v2` | `done` | `0` | Aktif akista yalniz `TP.BEK` ailesi var |
| `Rzrv_Blg_V7.ipynb` | `rzrv-blg-v7` | `done` | `0` | `TP.DOVVARNC.K18` dormant candidate olarak korunuyor |
| `Tbl_Apko.ipynb` | `tbl-apko` | `done` | `0` | Coklu frekans ve 4 source dependency ayni raporda birlesiyor |
| `Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb` | `yi-yrlsk-fnsl-vrlk-v1` | `done_with_unresolved` | `6` | `TP.HPBITABLO2.25-27` ve `.29-.31` notebooktan net cozumlenemiyor |

## Onerilen Uygulama Sirasi

1. `00_SHARED_SPEC.md`
2. `04_Pys_Ktlmclr_V2.md`
3. `07_Yi_Yrlsk_Fnsl_Vrlk_V1.md`
4. `01_DTH_Blg_V7.md`
5. `02_Eurobnd_Blg_V4.md`
6. `03_PrBnk_MnklKymt_V5.md`
7. `05_Rzrv_Blg_V7.md`
8. `06_Tbl_Apko.md`

Bu sira bilincli secilmistir:

- `L1` lane ortak spec'i en az riskle dogrular.
- `DTH` mevcut implementasyon nedeniyle referans baseline'dir.
- `L2` lane source dependency modelini zenginlestirir.
- `L3` lane fallback ve manuel ledger mantigini zorlar.

## Bagimliliklar

- Tum notebook gorevleri `00_SHARED_SPEC.md` uzerine kuruludur.
- `01_DTH_Blg_V7.md` mevcut DTH baseline koduna ve genel analyzer gecisine referanstir.
- `02_Eurobnd_Blg_V4.md` uygulama sirasinda `01_DTH_Blg_V7.md` sonrasina baglidir.
- `05_Rzrv_Blg_V7.md` fallback mantigi icin `01_DTH_Blg_V7.md` referansini kullanir.
- `06_Tbl_Apko.md` karma kaynak ve fallback yapisi nedeniyle `05_Rzrv_Blg_V7.md` sonrasina baglidir.
- `07_Yi_Yrlsk_Fnsl_Vrlk_V1.md` temiz EVDS extraction ornegi olarak `04_Pys_Ktlmclr_V2.md` sonrasina baglidir.
- `L2` ve `L3` notebooklarinda `source_dependency` record type zorunludur.
- `show-map` hedefi series + indicator + theme + source_dependency iliskilerini gosterecek sekilde dusunulmelidir.
- DTH mevcut ciktilari geriye donuk uyumluluk icin referans kabul edilir.

## Acik Blokajlar

- `Rzrv_Blg_V7.ipynb` ve `Tbl_Apko.ipynb` notebooklarinda seriallesmis `serie_info` yok.
- `Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb` EVDS tarafi temiz olmasina ragmen MKK verisi manuel dictionary olarak gomulu.
- `Eurobnd_Blg_V4.ipynb` ve `Tbl_Apko.ipynb` upload edilen dosya sekme adlarina bagimli.
- `PrBnk_MnklKymt_V5.ipynb` icinde hem EVDS hem yorum satirina alinmis eski extraction bloklari bir arada.

## Hangi Dosyayla Baslanmali

- Ortak tasarim veya CLI hedefini degistirecek biri once `00_SHARED_SPEC.md` okumali.
- Tek notebook gorevini uygulayacak biri ilgili notebook dosyasini dogrudan okuyabilir.
- `L3` lane calisani, gorev dosyasindan once mutlaka `00_SHARED_SPEC.md` fallback sirasini okumali.
- DTH regressionsiz ilerlemek isteyen biri `01_DTH_Blg_V7.md` dosyasini baseline olarak kullanmali.

## Cikti Sozlesmesi

Her notebook gorevinde hedef ciktinin isimlendirmesi aynidir:

- `generated/<notebook_stem>_ticker_report.md`
- `generated/<notebook_stem>_registry_import.csv`

Genel CLI hedefi ileride:

```text
registry analyze-notebook --notebook <path> --spec <slug|auto>
```

Mevcut `registry analyze-dth-notebook` komutu, genel yapinin icinde geriye donuk alias olarak korunmalidir.
