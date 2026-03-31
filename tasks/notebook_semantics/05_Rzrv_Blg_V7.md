---
task_id: notebook-semantics-05-rzrv-blg-v7
notebook_path: ../Telegram Bot/notebooks/Rzrv_Blg_V7.ipynb
lane: L3_manual_or_fallback
priority: P2
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
  - tasks/notebook_semantics/01_DTH_Blg_V7.md
evds_code_families:
  - TP.AB
  - TP.DK
  - TP.DOVVARNC
external_inputs:
  - pdf_table:tcmb-swap-pdf
  - manual_inline:swap-amount-ledger
target_outputs:
  - generated/Rzrv_Blg_V7_ticker_report.md
  - generated/Rzrv_Blg_V7_registry_import.csv
known_blockers:
  - notebook stores no serialized serie_info dict, only get_series print output fallback
  - TP.DOVVARNC.K18 appears only in dormant/commented block
  - reserve semantics depend on both EVDS and manual swap values
---

# Rzrv_Blg_V7

## Amac

Bu notebook, rezerv anlatisini EVDS verileri ile swap PDF ve manuel swap tablosunu birlestirerek kurar. Gorev, `serie_info` olmayan notebooklar icin fallback sirasini sabitlemek, rezerv semantigini bozmadan source dependency modeline tasimak ve dormant kodlari aktif akisla karistirmamaktir.

## Mevcut Notebook Gercekleri

- Notebookta seriallesmis `serie_info` output'u yoktur.
- Ancak `evds.get_series(...)` cagrilarinin print output'unda `SERIE_CODE` / `SERIE_NAME` fallback izi vardir.
- `10` benzersiz EVDS kodu vardir.
- `evds.get_sub_categories(...)` ve `evds.get_series(...)` cagrilari bilgi hucrelerinde vardir; bu cagrilar resmi ad fallback'inde kullanilabilir.
- Ana hesaplama iki EVDS blogu ve bir swap PDF/blogu etrafinda kurulur.
- `TP.DOVVARNC.K18` iceren aylik swap blogu triple-quoted ve aktif akis disindadir.

## EVDS Kod Envanteri

### Aile ozetleri

- `TP.AB`: `8`
- `TP.DK`: `1`
- `TP.DOVVARNC`: `1`

### Tam kod listesi

```text
TP.AB:
TP.AB.A02, TP.AB.A10, TP.AB.A11, TP.AB.A13, TP.AB.A14, TP.AB.C1, TP.AB.C2, TP.AB.N06

TP.DK:
TP.DK.USD.A.YTL

TP.DOVVARNC:
TP.DOVVARNC.K18
```

## Dis Kaynak Envanteri

- `source:rzrv-swap-pdf`
  - `source_kind=pdf_table`
  - `requiredness=required_input`
  - kaynak: TCMB swap PDF
  - amac: alis/satis/depoya donen swap tablosu

- `source:rzrv-manual-swap-ledger`
  - `source_kind=manual_inline`
  - `requiredness=required_input`
  - kaynak: notebook icinde manuel girilen swap tutari tablosu
  - amac: tahmini net rezerv hesabinda "Diger Ulke MB Swap" kalemini beslemek

Kayda alinmayacak destek linkleri:

- TradingView haber linki
- rezerv aciklama PDF linkleri

Bunlar semantik girdiden cok referans dokuman niteligindedir.

## Beklenen Registry Nesneleri

### Theme

- `theme:reserves`
- `theme:net-reserve-estimate`

### Indicator

- `derived:reserve-total`
- `derived:reserve-gold`
- `derived:reserve-fx`
- `derived:net-reserve-standby`
- `derived:estimated-net-reserve`
- `derived:swap-adjusted-net-reserve`
- `derived:gold-share-in-reserves`

### Source dependency

- `source:rzrv-swap-pdf`
- `source:rzrv-manual-swap-ledger`

## Analyzer Kurallari

- Resmi ad fallback'i su sirada calisir:
  1. `evds.get_series(...)` sonucunun output'u
  2. explicit rename/columns atamalari
  3. turetilmis user-facing kolonlar
  4. unresolved ledger
- `TP.AB.A02`, `.A10`, `.A11`, `.A13`, `.A14`, `TP.DK.USD.A.YTL` tahmini net rezerv blogunun ana girdileridir.
- `TP.AB.C1`, `TP.AB.C2`, `TP.AB.N06`, `TP.DK.USD.A.YTL` rezerv toplami ve stand-by net rezerv blogunu besler.
- `TP.DOVVARNC.K18` yalniz dormant/commented block icindeyse `dormant_candidate` olarak raporlanir; aktif indicator girdi sayilmaz.
- Manuel swap ledger source dependency olmadan `estimated-net-reserve` indikatoru tamam sayilmaz.

## Turetilmis Gostergeler

Notebooktan cikan ana anlati:

- Rezerv Toplam
- Rezerv Altin
- Rezerv Doviz
- Net Rezerv Stand-By
- Tahmini Net Rezerv
- Swap Haric Net Rezerv
- Rezerv Altin Payi
- Tahmin sapmasi / tahmin-gercek farki

Karar:

- Tahmin sapmasi ve fark kolonlari indicator degil, `validation_note` icinde yardimci kalite metrigidir.
- Ana registry indicator seti yukaridaki yedi kalemle sinirli tutulur.

## Cozumsuzler ve Fallback

- `TP.DOVVARNC.K18` aktif akis disindadir; raporda `dormant_candidate` notu ile yer alir.
- `serie_info` olmadigi icin resmi adlarin bir kismi notebooktan tam cozumlenemeyebilir.
- Bu durumda varsayimsal EVDS adi atanmayacak; explicit `unresolved_from_notebook` notu kullanilacak.

## Gerekli CLI/Sema Degisiklikleri

- `spec=rzrv-blg-v7`
- fallback chain shared spec'teki sirayla birebir uygulanacak
- `show-map` indikator -> source dependency iliskilerini gosterecek

## Test Senaryolari

1. Benzersiz ticker sayisi `10` olmali.
2. `TP.AB`, `TP.DK`, `TP.DOVVARNC` aileleri dogru cikmali.
3. `source:rzrv-swap-pdf` ve `source:rzrv-manual-swap-ledger` olusmali.
4. `TP.DOVVARNC.K18` aktif indicator girdisi olmamali.
5. Resmi adlar seriallesmis `serie_info` olmadan print output + rename fallback'iyle cozumlenebildigi kadar cozumlenmeli.

## Acceptance Checklist

- [ ] `serie_info` olmayan notebook fallback'i gercekten calisiyor.
- [ ] Manuel swap girdisi source dependency olarak kayda gecti.
- [ ] Dormant swap serisi aktif akisla karistirilmadi.
- [ ] Rezerv anlatisi indicator seti net ve sinirli tutuldu.
