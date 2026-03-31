---
task_id: notebook-semantics-04-pys-ktilmclr-v2
notebook_path: ../Telegram Bot/notebooks/Pys_Ktlmclr_V2.ipynb
lane: L1_EVDS_standard
priority: P1
depends_on:
  - tasks/notebook_semantics/00_SHARED_SPEC.md
evds_code_families:
  - TP.BEK
external_inputs: []
target_outputs:
  - generated/Pys_Ktlmclr_V2_ticker_report.md
  - generated/Pys_Ktlmclr_V2_registry_import.csv
known_blockers:
  - indicator kapsaminda asiri genisleme yapilmasi gereksiz karmasiklik yaratir
---

# Pys_Ktlmclr_V2

## Amac

Bu notebook, genel analyzer mimarisini en dusuk riskle dogrulamak icin ikinci temiz baseline'dir. Gorev, beklenti anketi EVDS kodlarini aile bazinda kaydetmek ve notebookun temel beklenti gostergelerini stabil indicator setine cevirmektir.

## Mevcut Notebook Gercekleri

- Notebookta `serie_info` output'u vardir.
- Aktif source akisi `14` benzersiz EVDS kodu kullanir.
- Dis kaynak, upload veya scrape yoktur.
- Tek ana EVDS fetch blogu ve sonrasinda yorum/grafik bloglari vardir.
- Kullanici gorunumlu kolonlar acik ve net isimlendirilmistir.
- `TP.PKAUO.*` serileri yorum satirina alinmis bir blokta durur; aktif acceptance sayimina dahil edilmez.

## EVDS Kod Envanteri

### Aile ozetleri

- `TP.BEK`: `14`

### Tam kod listesi

```text
TP.BEK:
TP.BEK.S01.D.U, TP.BEK.S01.E.U, TP.BEK.S01.F.U, TP.BEK.S01.I.U, TP.BEK.S04.A.U, TP.BEK.S04.B.U, TP.BEK.S04.D.U, TP.BEK.S04.E.U, TP.BEK.S05.B.U, TP.BEK.S05.C.U, TP.BEK.S06.A.U, TP.BEK.S06.B.U, TP.BEK.S07.A.U, TP.BEK.S07.B.U

```

## Dis Kaynak Envanteri

Bu notebookta registry'ye yazilacak `source_dependency` beklenmez.

## Beklenen Registry Nesneleri

### Theme

- `theme:survey-expectations`

### Indicator

- `derived:policy-rate-expectation-current`
- `derived:policy-rate-expectation-3m`
- `derived:policy-rate-expectation-12m`
- `derived:inflation-expectation-12m`
- `derived:inflation-expectation-24m`
- `derived:usdtry-expectation-12m`
- `derived:growth-expectation`
- `derived:current-account-expectation`

## Analyzer Kurallari

- Resmi adlar `serie_info` output'undan okunur.
- `TP.BEK.*` ve `TP.PKAUO.*` aileleri ayni notebook temasi altinda tutulur; ama indikatorlar farkli alt basliklara ayrilir.
- Notebookta kullanici gorunumlu kolon isimleri `notebook_label` olarak korunur.
- Dis kaynak olmadigi icin `linked_source_dependency_ids` bos kalir.
- Burasi shared spec'in `L1` lane dogrulama alani oldugu icin fallback mantigi minimum tutulmali; gereksiz notebook-ozel istisna yazilmaz.

## Turetilmis Gostergeler

Ana anlati gruplari:

- Politika faizi beklentileri
- GSYH beklentileri
- Cari denge beklentileri
- TUFE beklentileri
- Dolar kuru beklentileri

Karar:

- Notebookta gorunen butun grafikler ayri indicator olmayacak.
- Yukaridaki bes anlatinin cekirdek driver serileri indicator olarak kaydedilecek.

## Cozumsuzler ve Fallback

- Notebookta `serie_info` mevcut oldugu icin resmi ad fallback'i beklenmez.
- Resmi ad bulunamayan kod olursa bu shared spec'e aykiri sayilir ve test kirmalidir.

## Gerekli CLI/Sema Degisiklikleri

- `spec=pys-ktilmclr-v2`
- herhangi bir `source_dependency` sema genislemesi bu notebooku etkilemez; regression test icin kullanilir

## Test Senaryolari

1. Benzersiz ticker sayisi `14` olmali.
2. Aktif aile olarak `TP.BEK` tam cikarilmali.
3. `source_dependency` listesi bos olmali.
4. En az `8` ana indicator uretilmeli.
5. Resmi adlarin buyuk cogunlugu `serie_info` mapping ile dogrudan cozumlenmeli; yorum satirindaki `TP.PKAUO` bloklari aktif sayilmamali.

## Acceptance Checklist

- [ ] Bu notebook shared spec'in temiz L1 dogrulama ornegi oldu.
- [ ] EVDS serileri eksiksiz registry draft'ina yazildi.
- [ ] Dis kaynak beklenmedigi halde source dependency uretmedi.
- [ ] Beklenti indicator seti asiri sisirilmeden kaydedildi.
