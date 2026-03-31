---
record_type: proposal
id: proposal:tbl-apko:series:TP_DK_USD_A_YTL:f47ce47a50be
proposal_id: proposal:tbl-apko:series:TP_DK_USD_A_YTL:f47ce47a50be
title: Semantic proposal for TP.DK.USD.A.YTL
status: approved
target_type: series
target_id: evds:TP.DK.USD.A.YTL
ticker: TP.DK.USD.A.YTL
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: (USD)  ABD  Doları  (Döviz  Alış)
candidate_unit: Türk lirası
candidate_frequency: daily
candidate_role: ratio_input
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:usdtry-buy-rate
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: f47ce47a50be3d360d6e65a45646c48cc0e7f199
catalog_record_id: catalog:evds2:TP.DK.USD.A.YTL
memory_rule_ids: []
evidence:
  ticker: TP.DK.USD.A.YTL
  notebook_slug: tbl-apko
  official_series_name: USD/TL (Alış Kuru)
  context_title: USD/TL (Alış Kuru)
  frequency: daily
  unit: Türk lirası
  role: ratio_input
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:usdtry-buy-rate
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
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
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DK.USD.A.YTL
promoted_memory_rule_id: memory:global-tp-dk-usd-a-ytl
notes: 'Catalog source: catalog:evds2:TP.DK.USD.A.YTL'
body: "# Semantic proposal for TP.DK.USD.A.YTL\n\n## Target\nseries | evds:TP.DK.USD.A.YTL\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n(USD)  ABD  Doları  (Döviz  Alış)\n\
  \n## Candidate Unit\nTürk lirası\n\n## Candidate Frequency\ndaily\n\n## Candidate\
  \ Role\nratio_input\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n- derived:usdtry-buy-rate\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nThree other\
  \ proposals for the same ticker are currently pending review, and there are no existing\
  \ approved series or matching memory rules to confirm global safety without notebook-specific\
  \ scoping.\n\n## Notes\nCatalog source: catalog:evds2:TP.DK.USD.A.YTL\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.DK.USD.A.YTL\",\n  \"notebook_slug\": \"tbl-apko\",\n  \"\
  official_series_name\": \"USD/TL (Alış Kuru)\",\n  \"context_title\": \"USD/TL (Alış\
  \ Kuru)\",\n  \"frequency\": \"daily\",\n  \"unit\": \"Türk lirası\",\n  \"role\"\
  : \"ratio_input\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"\
  theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:usdtry-buy-rate\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.DK.USD.A.YTL\",\n    \"title\": \"(USD)  ABD  Doları  (Döviz\
  \  Alış)\",\n    \"frequency\": \"daily\",\n    \"unit\": \"Türk lirası\",\n   \
  \ \"data_group\": \"bie_dkdovytl\",\n    \"category\": \"TCMB DÖVİZ KURLARI\"\n\
  \  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.DK.USD.A.YTL\\\
  \": [3, \\\"USD/TL (Alış Kuru)\\\"],\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_DK_USD_A_YTL%3Af47ce47a50be.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DK.USD.A.YTL

## Target
series | evds:TP.DK.USD.A.YTL

## Notebook
tbl-apko

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
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

## Candidate Indicator Inputs
- derived:usdtry-buy-rate

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
  "notebook_slug": "tbl-apko",
  "official_series_name": "USD/TL (Alış Kuru)",
  "context_title": "USD/TL (Alış Kuru)",
  "frequency": "daily",
  "unit": "Türk lirası",
  "role": "ratio_input",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:usdtry-buy-rate"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
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
    "\"TP.DK.USD.A.YTL\": [3, \"USD/TL (Alış Kuru)\"],"
  ],
  "indicator_hints": [],
  "notes": ""
}
