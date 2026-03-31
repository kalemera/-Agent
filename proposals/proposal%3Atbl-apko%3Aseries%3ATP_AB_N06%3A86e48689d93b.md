---
record_type: proposal
id: proposal:tbl-apko:series:TP_AB_N06:86e48689d93b
proposal_id: proposal:tbl-apko:series:TP_AB_N06:86e48689d93b
title: Semantic proposal for TP.AB.N06
status: approved
target_type: series
target_id: evds:TP.AB.N06
ticker: TP.AB.N06
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 2A Net Uluslararası Rezervler (1+2+3)
candidate_unit: TL
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:tcmb-net-reserves
candidate_formula_hint: 'derived:tcmb-net-reserves: Net rezerv ve swap duzeltme bloklarindan
  uretilir.'
confidence: 0.85
source: hybrid
evidence_fingerprint: 86e48689d93b3e6b2726affab6657d9b350aff7f
catalog_record_id: catalog:evds2:TP.AB.N06
memory_rule_ids: []
evidence:
  ticker: TP.AB.N06
  notebook_slug: tbl-apko
  official_series_name: TCMB Uluslararası Net Rezervler (TL)
  context_title: TCMB Uluslararası Net Rezervler (TL)
  frequency: weekly
  unit: TL
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:tcmb-net-reserves
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.AB.N06
    title: 2A Net Uluslararası Rezervler (1+2+3)
    frequency: weekly
    unit: unknown
    data_group: bie_abstc2
    category: MERKEZ BANKASI HAFTALIK VAZİYET
  memory_rules: []
  source_snippets:
  - '"TP.AB.N06": "TCMB Uluslararası Net Rezervler (TL)",'
  indicator_hints:
  - 'derived:tcmb-net-reserves: Net rezerv ve swap duzeltme bloklarindan uretilir.'
  notes: ''
llm_provider: ollama_cloud
llm_model: qwen3.5:397b-cloud
promoted_record_id: ''
promoted_memory_rule_id: memory:tbl-apko-tp-ab-n06
notes: 'Catalog source: catalog:evds2:TP.AB.N06 Approved via notebook-scoped memory
  rule with TL unit.'
body: "# Semantic proposal for TP.AB.N06\n\n## Target\nseries | evds:TP.AB.N06\n\n\
  ## Notebook\ntbl-apko\n\n## Candidate Title\n2A Net Uluslararası Rezervler (1+2+3)\n\
  \n## Candidate Unit\nTL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  balance_sheet_line\n\n## Confidence\n0.85\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n- derived:tcmb-net-reserves\n\n## Formula Hint\n\
  derived:tcmb-net-reserves: Net rezerv ve swap duzeltme bloklarindan uretilir.\n\n\
  ## Source\nhybrid\n\n## Notes\nCatalog source: catalog:evds2:TP.AB.N06\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.AB.N06\",\n  \"notebook_slug\": \"tbl-apko\",\n  \"official_series_name\"\
  : \"TCMB Uluslararası Net Rezervler (TL)\",\n  \"context_title\": \"TCMB Uluslararası\
  \ Net Rezervler (TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"TL\",\n  \"\
  role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:tcmb-net-reserves\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.AB.N06\",\n    \"title\": \"2A Net Uluslararası Rezervler (1+2+3)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"unknown\",\n    \"data_group\"\
  : \"bie_abstc2\",\n    \"category\": \"MERKEZ BANKASI HAFTALIK VAZİYET\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.AB.N06\\\": \\\"\
  TCMB Uluslararası Net Rezervler (TL)\\\",\"\n  ],\n  \"indicator_hints\": [\n  \
  \  \"derived:tcmb-net-reserves: Net rezerv ve swap duzeltme bloklarindan uretilir.\"\
  \n  ],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Atbl-apko%3Aseries%3ATP_AB_N06%3A86e48689d93b.md
---
# Semantic proposal for TP.AB.N06

## Target
series | evds:TP.AB.N06

## Notebook
tbl-apko

## Candidate Title
2A Net Uluslararası Rezervler (1+2+3)

## Candidate Unit
TL

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

## Confidence
0.85

## Candidate Themes
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

## Candidate Indicator Inputs
- derived:tcmb-net-reserves

## Formula Hint
derived:tcmb-net-reserves: Net rezerv ve swap duzeltme bloklarindan uretilir.

## Source
hybrid

## Notes
Catalog source: catalog:evds2:TP.AB.N06 Approved via notebook-scoped memory rule with TL unit.

## Evidence
{
  "ticker": "TP.AB.N06",
  "notebook_slug": "tbl-apko",
  "official_series_name": "TCMB Uluslararası Net Rezervler (TL)",
  "context_title": "TCMB Uluslararası Net Rezervler (TL)",
  "frequency": "weekly",
  "unit": "TL",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:tcmb-net-reserves"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.AB.N06",
    "title": "2A Net Uluslararası Rezervler (1+2+3)",
    "frequency": "weekly",
    "unit": "unknown",
    "data_group": "bie_abstc2",
    "category": "MERKEZ BANKASI HAFTALIK VAZİYET"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.AB.N06\": \"TCMB Uluslararası Net Rezervler (TL)\","
  ],
  "indicator_hints": [
    "derived:tcmb-net-reserves: Net rezerv ve swap duzeltme bloklarindan uretilir."
  ],
  "notes": ""
}
