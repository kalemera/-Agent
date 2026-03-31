# EVDS Ticker Haritasi

Bu proje, EVDS ile baslayarak kullandiginiz ham serileri, bunlardan turetilen gostergeleri, temalari ve notebook disi veri bagimliliklarini kalici bir bilgi haritasinda tutar.

## Kurulum

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e .[dev]
```

## Klasor Yapisi

- `drafts/`: onay bekleyen kayitlar
- `registry/series/`: onayli ham seri kayitlari
- `registry/indicators/`: onayli turetilmis gosterge kayitlari
- `registry/themes/`: onayli tema kayitlari
- `registry/source_dependencies/`: onayli dis kaynak bagimliliklari
- `registry/catalog/`: EVDS metadata katalog cache'i
- `registry/memory/`: onayli semantik hafiza kurallari
- `proposals/`: review queue'ya dusen semantic proposal kayitlari

## CLI

```bash
registry add-series-draft --ticker TP.FE.OKG01 --description "TUFE endeksi" --usage "Enflasyon izlemede kullanirim" --source-version evds2
registry add-indicator-draft --title "TUFE yillik degisim" --input-id evds:TP.FE.OKG01 --formula-expression "(x_t / x_t-12 - 1) * 100"
registry add-theme-draft --title "Enflasyon" --description "Enflasyon temasi" --series-id evds:TP.FE.OKG01 --indicator-id derived:cpi-yoy
registry import-drafts --file examples/import_template.csv
registry review-drafts
registry approve-draft evds:TP.FE.OKG01
registry show-map TP.FE.OKG01
registry analyze-notebook --notebook "C:/path/to/DTH_Blg_V7.ipynb" --spec auto
registry analyze-dth-notebook --notebook "C:/path/to/DTH_Blg_V7.ipynb"
registry sync-evds-catalog --source-version evds2 --scope group:bie_yssk
registry infer-notebook-semantics --notebook "C:/path/to/DTH_Blg_V7.ipynb" --spec auto
registry review-proposals
registry auto-approve-proposals --min-confidence 0.90
registry promote-proposal proposal:dth-blg-v7:series:TP_HPBITABLO4_14:abcd1234
registry reject-proposal proposal:dth-blg-v7:series:TP_HPBITABLO4_15:abcd5678
```

## `add-series-draft`

Zorunlu alanlar:

- `--ticker`
- `--description`
- `--usage`

Opsiyonel alanlar:

- `--title`
- `--source-version` (`evds2` veya `evds3`)
- `--frequency`
- `--unit`
- `--official-url`
- `--theme-id` tekrarli
- `--indicator-id` tekrarli

## `add-indicator-draft`

Zorunlu alanlar:

- `--title`

Opsiyonel alanlar:

- `--id`
- `--input-id` tekrarli
- `--formula-expression`
- `--formula-description`
- `--output-frequency`
- `--output-unit`
- `--economic-meaning`
- `--validation-note`
- `--theme-id` tekrarli

## `add-theme-draft`

Zorunlu alanlar:

- `--title`
- `--description`

Opsiyonel alanlar:

- `--id`
- `--series-id` tekrarli
- `--indicator-id` tekrarli
- `--source-dependency-id` tekrarli
- `--question` tekrarli

## `import-drafts`

CSV satirlari asagidaki kolonlari kullanir. Liste alanlari `|` ile ayrilir.

Ortak alanlar:

- `record_type`: `series`, `indicator`, `theme`, `source_dependency`, `catalog`, `memory_rule`, `proposal`
- `id`
- `title`

`series` alanlari:

- `ticker`
- `source_version`
- `frequency`
- `unit`
- `description`
- `usage`
- `official_url`
- `theme_ids`
- `indicator_ids`

`indicator` alanlari:

- `input_ids`
- `formula_expression`
- `formula_description`
- `output_frequency`
- `output_unit`
- `economic_meaning`
- `validation_note`
- `theme_ids`

`theme` alanlari:

- `description`
- `series_ids`
- `indicator_ids`
- `source_dependency_ids`
- `questions`

`source_dependency` alanlari:

- `description`
- `usage`
- `source_kind`
- `requiredness`
- `source_uri`
- `local_hint`
- `theme_ids`
- `indicator_ids`
- `validation_note`

`catalog` alanlari:

- `ticker`
- `source_version`
- `frequency`
- `unit`
- `category`
- `data_group`
- `official_url`

`memory_rule` alanlari:

- `scope`
- `match_pattern`
- `target_type`
- `notebook_slug`
- `resolved_title`
- `resolved_unit`
- `resolved_frequency`
- `resolved_role`
- `resolved_theme_ids`
- `resolved_formula_hint`
- `evidence_source`
- `approved_by`
- `approved_at`
- `notes`

`proposal` alanlari:

- `target_type`
- `target_id`
- `ticker`
- `notebook_slug`
- `candidate_title`
- `candidate_unit`
- `candidate_frequency`
- `candidate_role`
- `candidate_theme_ids`
- `candidate_indicator_inputs`
- `candidate_formula_hint`
- `confidence`
- `status`
- `evidence_fingerprint`
- `catalog_record_id`
- `memory_rule_ids`

Alan ayrimi:

- `formula_expression`: mumkunse dogrudan cebirsel ifade veya acik input-id tabanli oran tanimi
- `formula_description`: notebookta formulu sadece metinsel olarak biliyorsaniz kullanilan aciklama

## `analyze-notebook`

Bu komut notebooku tarar, spec secimine gore ticker anlamlarini cozumler ve iki dosya uretir:

- `generated/<notebook_stem>_ticker_report.md`
- `generated/<notebook_stem>_registry_import.csv`

Argumanlar:

- `--notebook`: analiz edilecek `.ipynb` yolu
- `--spec`: `auto` veya bilinen spec slug'i
- `--report-out`: opsiyonel rapor cikti yolu
- `--import-out`: opsiyonel import CSV cikti yolu

Desteklenen spec slug'lari:

- `dth-blg-v7`
- `eurobnd-blg-v4`
- `prbnk-mnklkymt-v5`
- `pys-ktilmclr-v2`
- `rzrv-blg-v7`
- `tbl-apko`
- `yi-yrlsk-fnsl-vrlk-v1`

`analyze-notebook`, varsa `registry/catalog/` ve `registry/memory/` kayitlarini uygulayarak raporu zenginlestirir.

Ornek:

```bash
registry analyze-notebook --notebook "C:/Users/bthkr/OneDrive/Masaustu/Is Kodlama/Telegram Bot/notebooks/DTH_Blg_V7.ipynb" --spec auto
```

Varsayilan cikti yollarini ezmek icin:

```bash
registry analyze-notebook \
  --notebook "C:/path/to/DTH_Blg_V7.ipynb" \
  --spec dth-blg-v7 \
  --report-out "generated/dth_report.md" \
  --import-out "generated/dth_import.csv"
```

## `analyze-dth-notebook`

Bu komut geriye donuk alias'tir ve su davranisa denktir:

```text
registry analyze-notebook --spec dth-blg-v7
```

## `show-map`

`show-map` su kayit tipleri icin cift yonlu baglari gosterir:

- `series`
- `indicator`
- `theme`
- `source_dependency`

Bir `series` sorgusunda indikator, tema ve ilgili `source_dependency` baglari birlikte gorunur.

Ek olarak `show-map`, varsa bagli proposal ve memory rule provenance bilgisini de gosterir.

## `sync-evds-catalog`

Bu komut EVDS metadata katalog kayitlarini `registry/catalog/` altina yazar.

Argumanlar:

- `--source-version`: `evds2` veya `evds3`
- `--scope`: `all`, `category:<id>`, `group:<code>`, `ticker:<code>`

Varsayilan ortam degiskenleri:

- `EVDS_API_KEY` veya `EVDS_KEY`
- `EVDS_BASE_URL` (varsayilan: `https://evds3.tcmb.gov.tr/igmevdsms-dis/`)

## `infer-notebook-semantics`

Bu komut notebook analizi, katalog metadata ve semantik hafiza kurallarini birlestirip review queue icin proposal uretir.

Ciktilar:

- `generated/<notebook_stem>_semantic_inference_report.md`
- `generated/<notebook_stem>_semantic_proposals.json`
- `generated/<notebook_stem>_semantic_draft_candidates.csv`
- `proposals/*.md`

LLM ortam degiskenleri:

- `LLM_PROVIDER=ollama`
- `OLLAMA_API_KEY` veya `OLLAMA_CLOUD_API_KEY`
- `OLLAMA_MODEL`
- `OLLAMA_BASE_URL` veya `OLLAMA_CLOUD_BASE_URL`

LLM tanimli degilse komut heuristic-only calisir; mevcut analiz akisi bozulmaz.

## `review-proposals`

Bu komut proposal kuyruğunu status, notebook, target type ve confidence filtreleriyle listeler.

## `auto-approve-proposals`

Bu komut yalniz `series` proposal'lari icin LLM destekli ikinci bir guvenlik kapisi calistirir.

Varsayilan davranis:

- sadece `review_pending` proposal'lara bakar
- `confidence >= 0.90` altindaki series'leri `manual_review` yapar
- `source=hybrid` veya conflict iceren series'leri `manual_review` yapar
- guvenli series'leri dogrudan canonical registry'ye yazar
- canonical `series.title` icin notebook baglami degil, EVDS resmi seri adi kullanilir
- notebook baglami ve kullanim alani `description`/`usage` alanlarinda korunur

Argumanlar:

- `--notebook`
- `--min-confidence`
- `--limit`

Notlar:

- LLM kapaliysa komut hata vererek durur
- `indicator` ve `theme` proposal'lari bu komut tarafindan otomatik onaylanmaz
- sonuc ozeti `approved / manual_review / skipped` olarak yazdirilir

Filtreler:

- `--status`
- `--notebook`
- `--target-type`
- `--min-confidence`

## `promote-proposal` / `reject-proposal`

- `promote-proposal`, proposal'dan draft kayit ve memory rule uretir.
- `reject-proposal`, ayni evidence fingerprint'e sahip proposal tekrar uretilse bile reddedilmis durumda kalmasini saglar.

## Kayit Kurallari

- EVDS serileri `evds:<ticker>` kimligiyle tutulur.
- Gosterge kimlikleri `derived:<slug>`, tema kimlikleri `theme:<slug>`, dis kaynaklar `source:<slug>` seklindedir.
- EVDS serilerinde `source_version` onay sirasinda zorunludur.
- Turetilmis gosterge onayi icin tum `input_ids` kayitli olmalidir.
- Tema onayi icin bagli seri, gosterge ve `source_dependency` kimlikleri kayitli olmalidir.
- `source_dependency` onayi icin kaynak turu, zorunluluk, aciklama ve kullanim alani dolu olmalidir.
- `catalog` kayitlari approved registry akisindan ayridir; `sync-evds-catalog` ile guncellenir.
- `memory_rule` kayitlari semantic inference tarafinda otomatik uygulanir.
