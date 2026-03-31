---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_DK_USD_A_YTL:efe9bae13718
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_DK_USD_A_YTL:efe9bae13718
title: Semantic proposal for TP.DK.USD.A.YTL
status: approved
target_type: series
target_id: evds:TP.DK.USD.A.YTL
ticker: TP.DK.USD.A.YTL
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: (USD)  ABD  Doları  (Döviz  Alış)
candidate_unit: Türk lirası
candidate_frequency: daily
candidate_role: ratio_input
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: efe9bae1371859a9c4c108343ef326a1e9631dac
catalog_record_id: catalog:evds2:TP.DK.USD.A.YTL
memory_rule_ids: []
evidence:
  ticker: TP.DK.USD.A.YTL
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: USD/TL (Alış Kuru)
  context_title: USD/TL (Alış Kuru)
  frequency: weekly
  unit: Türk lirası
  role: ratio_input
  status: derived_input
  theme_ids:
  - theme:portfolio-flows
  - theme:foreign-ownership
  - theme:swap-and-securities
  indicator_ids: []
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.DK.USD.A.YTL
    title: (USD)  ABD  Doları  (Döviz  Alış)
    frequency: daily
    unit: Türk lirası
    data_group: bie_dkdovytl
    category: TCMB DÖVİZ KURLARI
  memory_rules: []
  source_snippets:
  - '"TP.DK.USD.A.YTL": [3, "USD/TL (Alış Kuru)"],'
  - df_menkul_kiymet_apko_["DİBS (Tüm Stok, USD)"] = df_menkul_kiymet_apko_["TP_DIBSPIYDEG_ST"]
    / df_menkul_kiymet_apko_["TP_DK_USD_A_YTL"]
  - '"TP_MKNETHAR_M9", "TP_MKNETHAR_M10", "TP_MKNETHAR_M11", "TP_DIBSPIYDEG_ST", "TP_DK_USD_A_YTL"'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DK.USD.A.YTL
promoted_memory_rule_id: memory:global-tp-dk-usd-a-ytl
notes: 'Catalog source: catalog:evds2:TP.DK.USD.A.YTL'
body: "# Semantic proposal for TP.DK.USD.A.YTL\n\n## Target\nseries | evds:TP.DK.USD.A.YTL\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n(USD)  ABD  Doları  (Döviz\
  \  Alış)\n\n## Candidate Unit\nTürk lirası\n\n## Candidate Frequency\ndaily\n\n\
  ## Candidate Role\nratio_input\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nMultiple same-ticker proposals exist with review_pending\
  \ status\n\n## Notes\nCatalog source: catalog:evds2:TP.DK.USD.A.YTL\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.DK.USD.A.YTL\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"USD/TL (Alış Kuru)\",\n  \"context_title\": \"\
  USD/TL (Alış Kuru)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Türk lirası\"\
  ,\n  \"role\": \"ratio_input\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\",\n    \"theme:swap-and-securities\"\
  \n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:prbnk-weekly-zip\"\
  ,\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"catalog_record\": {\n    \"id\": \"\
  catalog:evds2:TP.DK.USD.A.YTL\",\n    \"title\": \"(USD)  ABD  Doları  (Döviz  Alış)\"\
  ,\n    \"frequency\": \"daily\",\n    \"unit\": \"Türk lirası\",\n    \"data_group\"\
  : \"bie_dkdovytl\",\n    \"category\": \"TCMB DÖVİZ KURLARI\"\n  },\n  \"memory_rules\"\
  : [],\n  \"source_snippets\": [\n    \"\\\"TP.DK.USD.A.YTL\\\": [3, \\\"USD/TL (Alış\
  \ Kuru)\\\"],\",\n    \"df_menkul_kiymet_apko_[\\\"DİBS (Tüm Stok, USD)\\\"] = df_menkul_kiymet_apko_[\\\
  \"TP_DIBSPIYDEG_ST\\\"] / df_menkul_kiymet_apko_[\\\"TP_DK_USD_A_YTL\\\"]\",\n \
  \   \"\\\"TP_MKNETHAR_M9\\\", \\\"TP_MKNETHAR_M10\\\", \\\"TP_MKNETHAR_M11\\\",\
  \ \\\"TP_DIBSPIYDEG_ST\\\", \\\"TP_DK_USD_A_YTL\\\"\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_DK_USD_A_YTL%3Aefe9bae13718.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DK.USD.A.YTL

## Target
series | evds:TP.DK.USD.A.YTL

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
(USD)  ABD  Doları  (Döviz  Alış)

## Candidate Unit
Türk lirası

## Candidate Frequency
daily

## Candidate Role
ratio_input

## Confidence
0.9

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

## Candidate Indicator Inputs
-

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.DK.USD.A.YTL

## Evidence
{
  "ticker": "TP.DK.USD.A.YTL",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "USD/TL (Alış Kuru)",
  "context_title": "USD/TL (Alış Kuru)",
  "frequency": "weekly",
  "unit": "Türk lirası",
  "role": "ratio_input",
  "status": "derived_input",
  "theme_ids": [
    "theme:portfolio-flows",
    "theme:foreign-ownership",
    "theme:swap-and-securities"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DK.USD.A.YTL",
    "title": "(USD)  ABD  Doları  (Döviz  Alış)",
    "frequency": "daily",
    "unit": "Türk lirası",
    "data_group": "bie_dkdovytl",
    "category": "TCMB DÖVİZ KURLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.DK.USD.A.YTL\": [3, \"USD/TL (Alış Kuru)\"],",
    "df_menkul_kiymet_apko_[\"DİBS (Tüm Stok, USD)\"] = df_menkul_kiymet_apko_[\"TP_DIBSPIYDEG_ST\"] / df_menkul_kiymet_apko_[\"TP_DK_USD_A_YTL\"]",
    "\"TP_MKNETHAR_M9\", \"TP_MKNETHAR_M10\", \"TP_MKNETHAR_M11\", \"TP_DIBSPIYDEG_ST\", \"TP_DK_USD_A_YTL\""
  ],
  "indicator_hints": [],
  "notes": ""
}
