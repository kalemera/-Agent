---
record_type: proposal
id: proposal:tbl-apko:series:TP_AB_TOPLAM:6662b21a4a0c
proposal_id: proposal:tbl-apko:series:TP_AB_TOPLAM:6662b21a4a0c
title: Semantic proposal for TP.AB.TOPLAM
status: approved
target_type: series
target_id: evds:TP.AB.TOPLAM
ticker: TP.AB.TOPLAM
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: Toplam (Milyon ABD Doları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:tcmb-gross-reserves
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 6662b21a4a0c16d1defd7404d0572feb6705aeeb
catalog_record_id: catalog:evds2:TP.AB.TOPLAM
memory_rule_ids: []
evidence:
  ticker: TP.AB.TOPLAM
  notebook_slug: tbl-apko
  official_series_name: TCMB Uluslararası Brüt Rezervler
  context_title: TCMB Uluslararası Brüt Rezervler
  frequency: weekly
  unit: milyon ABD doları
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:tcmb-gross-reserves
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.AB.TOPLAM
    title: Toplam (Milyon ABD Doları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_abres2
    category: ULUSLARARASI REZERVLER (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.AB.TOPLAM": "TCMB Uluslararası Brüt Rezervler",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.AB.TOPLAM
promoted_memory_rule_id: memory:global-tp-ab-toplam
notes: 'Catalog source: catalog:evds2:TP.AB.TOPLAM'
body: "# Semantic proposal for TP.AB.TOPLAM\n\n## Target\nseries | evds:TP.AB.TOPLAM\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\nToplam (Milyon ABD Doları)\n\n##\
  \ Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nbalance_sheet_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n- derived:tcmb-gross-reserves\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nSame ticker\
  \ TP.AB.TOPLAM has a proposal with status review_pending in notebook prbnk-mnklkymt-v5,\
  \ indicating uncertainty. No approved_series or matching_memory_rules exist.\n\n\
  ## Notes\nCatalog source: catalog:evds2:TP.AB.TOPLAM\n\n## Evidence\n{\n  \"ticker\"\
  : \"TP.AB.TOPLAM\",\n  \"notebook_slug\": \"tbl-apko\",\n  \"official_series_name\"\
  : \"TCMB Uluslararası Brüt Rezervler\",\n  \"context_title\": \"TCMB Uluslararası\
  \ Brüt Rezervler\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\"\
  ,\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:tcmb-gross-reserves\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.AB.TOPLAM\",\n    \"title\": \"Toplam (Milyon ABD Doları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_abres2\",\n    \"category\": \"ULUSLARARASI REZERVLER (TCMB)\"\
  \n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.AB.TOPLAM\\\
  \": \\\"TCMB Uluslararası Brüt Rezervler\\\",\"\n  ],\n  \"indicator_hints\": [],\n\
  \  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_AB_TOPLAM%3A6662b21a4a0c.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.AB.TOPLAM

## Target
series | evds:TP.AB.TOPLAM

## Notebook
tbl-apko

## Candidate Title
Toplam (Milyon ABD Doları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

## Confidence
0.9

## Candidate Themes
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

## Candidate Indicator Inputs
- derived:tcmb-gross-reserves

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.AB.TOPLAM

## Evidence
{
  "ticker": "TP.AB.TOPLAM",
  "notebook_slug": "tbl-apko",
  "official_series_name": "TCMB Uluslararası Brüt Rezervler",
  "context_title": "TCMB Uluslararası Brüt Rezervler",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:tcmb-gross-reserves"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.AB.TOPLAM",
    "title": "Toplam (Milyon ABD Doları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_abres2",
    "category": "ULUSLARARASI REZERVLER (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.AB.TOPLAM\": \"TCMB Uluslararası Brüt Rezervler\","
  ],
  "indicator_hints": [],
  "notes": ""
}
