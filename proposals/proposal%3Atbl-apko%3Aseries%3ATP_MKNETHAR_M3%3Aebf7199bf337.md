---
record_type: proposal
id: proposal:tbl-apko:series:TP_MKNETHAR_M3:ebf7199bf337
proposal_id: proposal:tbl-apko:series:TP_MKNETHAR_M3:ebf7199bf337
title: Semantic proposal for TP.MKNETHAR.M3
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M3
ticker: TP.MKNETHAR.M3
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 3.1. DİBS (Ters Repo)
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
evidence_fingerprint: ebf7199bf337ec11f8001dd7d644cca186577fd0
catalog_record_id: catalog:evds2:TP.MKNETHAR.M3
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M3
  notebook_slug: tbl-apko
  official_series_name: Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)
  context_title: Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)
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
    id: catalog:evds2:TP.MKNETHAR.M3
    title: 3.1. DİBS (Ters Repo)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M3": "Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M3
promoted_memory_rule_id: memory:global-tp-mknethar-m3
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M3'
body: "# Semantic proposal for TP.MKNETHAR.M3\n\n## Target\nseries | evds:TP.MKNETHAR.M3\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n3.1. DİBS (Ters Repo)\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  stock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nAnother proposal for the same ticker\
  \ TP.MKNETHAR.M3 exists from notebook prbnk-mnklkymt-v5 with status review_pending,\
  \ creating uncertainty for global approval.\n\n## Notes\nCatalog source: catalog:evds2:TP.MKNETHAR.M3\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.MKNETHAR.M3\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)\",\n\
  \  \"context_title\": \"Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_component\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:apko-summary\"\
  ,\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\",\n   \
  \ \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:tblapko-bbg-upload\",\n    \"source:tblapko-hmb-ab-borc-xls\"\
  ,\n    \"source:tblapko-swap-pdf\",\n    \"source:tblapko-bddk-weekly-bulletin\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M3\",\n\
  \    \"title\": \"3.1. DİBS (Ters Repo)\",\n    \"frequency\": \"weekly\",\n   \
  \ \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n    \"\
  category\": \"YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"memory_rules\"\
  : [],\n  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M3\\\": \\\"Yurtdışı Yerleşikler\
  \ DİBS Stoku (Ters Repo)\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\":\
  \ \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_MKNETHAR_M3%3Aebf7199bf337.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M3

## Target
series | evds:TP.MKNETHAR.M3

## Notebook
tbl-apko

## Candidate Title
3.1. DİBS (Ters Repo)

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
Catalog source: catalog:evds2:TP.MKNETHAR.M3

## Evidence
{
  "ticker": "TP.MKNETHAR.M3",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)",
  "context_title": "Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)",
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
    "id": "catalog:evds2:TP.MKNETHAR.M3",
    "title": "3.1. DİBS (Ters Repo)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M3\": \"Yurtdışı Yerleşikler DİBS Stoku (Ters Repo)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
