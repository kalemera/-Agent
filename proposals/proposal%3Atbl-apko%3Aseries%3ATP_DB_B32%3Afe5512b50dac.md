---
record_type: proposal
id: proposal:tbl-apko:series:TP_DB_B32:fe5512b50dac
proposal_id: proposal:tbl-apko:series:TP_DB_B32:fe5512b50dac
title: Semantic proposal for TP.DB.B32
status: approved
target_type: series
target_id: evds:TP.DB.B32
ticker: TP.DB.B32
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 3.2.TCMB (Borçluya Göre)
candidate_unit: milyon ABD doları
candidate_frequency: monthly
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
evidence_fingerprint: fe5512b50dac64982e887c497d5a8fec9f30f604
catalog_record_id: catalog:evds2:TP.DB.B32
memory_rule_ids: []
evidence:
  ticker: TP.DB.B32
  notebook_slug: tbl-apko
  official_series_name: TCMB Brüt Dış Borç Stoku (Uzun Vade)
  context_title: TCMB Brüt Dış Borç Stoku (Uzun Vade)
  frequency: quarterly
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
    id: catalog:evds2:TP.DB.B32
    title: 3.2.TCMB (Borçluya Göre)
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_dbdborc
    category: TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)
  memory_rules: []
  source_snippets:
  - '"TP.DB.B32": "TCMB Brüt Dış Borç Stoku (Uzun Vade)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DB.B32
promoted_memory_rule_id: memory:global-tp-db-b32
notes: 'Catalog source: catalog:evds2:TP.DB.B32'
body: "# Semantic proposal for TP.DB.B32\n\n## Target\nseries | evds:TP.DB.B32\n\n\
  ## Notebook\ntbl-apko\n\n## Candidate Title\n3.2.TCMB (Borçluya Göre)\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n## Candidate Role\n\
  stock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nNo matching memory rules or approved\
  \ series exist to confirm global safety; proposal source is heuristic and includes\
  \ notebook slug.\n\n## Notes\nCatalog source: catalog:evds2:TP.DB.B32\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.DB.B32\",\n  \"notebook_slug\": \"tbl-apko\",\n  \"official_series_name\"\
  : \"TCMB Brüt Dış Borç Stoku (Uzun Vade)\",\n  \"context_title\": \"TCMB Brüt Dış\
  \ Borç Stoku (Uzun Vade)\",\n  \"frequency\": \"quarterly\",\n  \"unit\": \"milyon\
  \ ABD doları\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:apko-summary\",\n    \"theme:external-financing\"\
  ,\n    \"theme:banking-balance-sheet\",\n    \"theme:reserves-and-liquidity\"\n\
  \  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\"\
  ,\n    \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n \
  \   \"source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n   \
  \ \"id\": \"catalog:evds2:TP.DB.B32\",\n    \"title\": \"3.2.TCMB (Borçluya Göre)\"\
  ,\n    \"frequency\": \"monthly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_dbdborc\",\n    \"category\": \"TÜRKİYE BRÜT DIŞ BORÇ STOKU\
  \ (HMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.DB.B32\\\
  \": \\\"TCMB Brüt Dış Borç Stoku (Uzun Vade)\\\",\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_DB_B32%3Afe5512b50dac.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DB.B32

## Target
series | evds:TP.DB.B32

## Notebook
tbl-apko

## Candidate Title
3.2.TCMB (Borçluya Göre)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
monthly

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
Catalog source: catalog:evds2:TP.DB.B32

## Evidence
{
  "ticker": "TP.DB.B32",
  "notebook_slug": "tbl-apko",
  "official_series_name": "TCMB Brüt Dış Borç Stoku (Uzun Vade)",
  "context_title": "TCMB Brüt Dış Borç Stoku (Uzun Vade)",
  "frequency": "quarterly",
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
    "id": "catalog:evds2:TP.DB.B32",
    "title": "3.2.TCMB (Borçluya Göre)",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_dbdborc",
    "category": "TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.DB.B32\": \"TCMB Brüt Dış Borç Stoku (Uzun Vade)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
