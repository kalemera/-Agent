---
record_type: proposal
id: proposal:tbl-apko:series:TP_MKNETHAR_M1:307d40d4f9c0
proposal_id: proposal:tbl-apko:series:TP_MKNETHAR_M1:307d40d4f9c0
title: Semantic proposal for TP.MKNETHAR.M1
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M1
ticker: TP.MKNETHAR.M1
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.1.1. Hisse Senedi
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 307d40d4f9c0bfabb0c04c020773781860614b7f
catalog_record_id: catalog:evds2:TP.MKNETHAR.M1
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M1
  notebook_slug: tbl-apko
  official_series_name: Yurtdışı Yerleşikler Hisse Senedi Stoku
  context_title: Yurtdışı Yerleşikler Hisse Senedi Stoku
  frequency: weekly
  unit: milyon ABD doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids: []
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.MKNETHAR.M1
    title: 1.1.1. Hisse Senedi
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M1": "Yurtdışı Yerleşikler Hisse Senedi Stoku",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M1
promoted_memory_rule_id: memory:global-tp-mknethar-m1
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M1'
body: "# Semantic proposal for TP.MKNETHAR.M1\n\n## Target\nseries | evds:TP.MKNETHAR.M1\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.1.1. Hisse Senedi\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  stock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nSame ticker proposal from notebook\
  \ prbnk-mnklkymt-v5 has status review_pending, introducing uncertainty about global\
  \ validation despite matching signature.\n\n## Notes\nCatalog source: catalog:evds2:TP.MKNETHAR.M1\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.MKNETHAR.M1\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Yurtdışı Yerleşikler Hisse Senedi Stoku\",\n  \"\
  context_title\": \"Yurtdışı Yerleşikler Hisse Senedi Stoku\",\n  \"frequency\":\
  \ \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_component\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:apko-summary\"\
  ,\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\",\n   \
  \ \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:tblapko-bbg-upload\",\n    \"source:tblapko-hmb-ab-borc-xls\"\
  ,\n    \"source:tblapko-swap-pdf\",\n    \"source:tblapko-bddk-weekly-bulletin\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M1\",\n\
  \    \"title\": \"1.1.1. Hisse Senedi\",\n    \"frequency\": \"weekly\",\n    \"\
  unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n    \"category\"\
  : \"YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"memory_rules\": [],\n\
  \  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M1\\\": \\\"Yurtdışı Yerleşikler\
  \ Hisse Senedi Stoku\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\
  \n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_MKNETHAR_M1%3A307d40d4f9c0.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M1

## Target
series | evds:TP.MKNETHAR.M1

## Notebook
tbl-apko

## Candidate Title
1.1.1. Hisse Senedi

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.9

## Candidate Themes
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

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
Catalog source: catalog:evds2:TP.MKNETHAR.M1

## Evidence
{
  "ticker": "TP.MKNETHAR.M1",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Yurtdışı Yerleşikler Hisse Senedi Stoku",
  "context_title": "Yurtdışı Yerleşikler Hisse Senedi Stoku",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.MKNETHAR.M1",
    "title": "1.1.1. Hisse Senedi",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M1\": \"Yurtdışı Yerleşikler Hisse Senedi Stoku\","
  ],
  "indicator_hints": [],
  "notes": ""
}
