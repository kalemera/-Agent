---
record_type: proposal
id: proposal:tbl-apko:series:TP_ODANA6_Q01:eec4ec7569c8
proposal_id: proposal:tbl-apko:series:TP_ODANA6_Q01:eec4ec7569c8
title: Semantic proposal for TP.ODANA6.Q01
status: approved
target_type: series
target_id: evds:TP.ODANA6.Q01
ticker: TP.ODANA6.Q01
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.Cari İşlemler Hesabı
candidate_unit: milyon ABD doları
candidate_frequency: monthly
candidate_role: commentary_driver
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:12m-cumulative-current-account
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: eec4ec7569c81f9cdcfbcc15ac147109a6b328b8
catalog_record_id: catalog:evds2:TP.ODANA6.Q01
memory_rule_ids: []
evidence:
  ticker: TP.ODANA6.Q01
  notebook_slug: tbl-apko
  official_series_name: Cari Denge
  context_title: Cari Denge
  frequency: monthly
  unit: milyon ABD doları
  role: commentary_driver
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:12m-cumulative-current-account
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.ODANA6.Q01
    title: 1.Cari İşlemler Hesabı
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_odana6
    category: ÖDEMELER DENGESİ İSTATİSTİKLERİ (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.ODANA6.Q01": "Cari Denge",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.ODANA6.Q01
promoted_memory_rule_id: memory:global-tp-odana6-q01
notes: 'Catalog source: catalog:evds2:TP.ODANA6.Q01'
body: "# Semantic proposal for TP.ODANA6.Q01\n\n## Target\nseries | evds:TP.ODANA6.Q01\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.Cari İşlemler Hesabı\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n## Candidate Role\n\
  commentary_driver\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n- derived:12m-cumulative-current-account\n\n##\
  \ Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval\
  \ Reason\nLLM requested manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.ODANA6.Q01\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.ODANA6.Q01\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Cari Denge\",\n  \"context_title\": \"Cari Denge\"\
  ,\n  \"frequency\": \"monthly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\"\
  : \"commentary_driver\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n\
  \    \"theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:12m-cumulative-current-account\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.ODANA6.Q01\",\n    \"title\": \"1.Cari İşlemler Hesabı\",\n\
  \    \"frequency\": \"monthly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_odana6\",\n    \"category\": \"ÖDEMELER DENGESİ İSTATİSTİKLERİ (TCMB)\"\n\
  \  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.ODANA6.Q01\\\
  \": \\\"Cari Denge\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n\
  }\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_ODANA6_Q01%3Aeec4ec7569c8.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.ODANA6.Q01

## Target
series | evds:TP.ODANA6.Q01

## Notebook
tbl-apko

## Candidate Title
1.Cari İşlemler Hesabı

## Candidate Unit
milyon ABD doları

## Candidate Frequency
monthly

## Candidate Role
commentary_driver

## Confidence
0.9

## Candidate Themes
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

## Candidate Indicator Inputs
- derived:12m-cumulative-current-account

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.ODANA6.Q01

## Evidence
{
  "ticker": "TP.ODANA6.Q01",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Cari Denge",
  "context_title": "Cari Denge",
  "frequency": "monthly",
  "unit": "milyon ABD doları",
  "role": "commentary_driver",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:12m-cumulative-current-account"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.ODANA6.Q01",
    "title": "1.Cari İşlemler Hesabı",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_odana6",
    "category": "ÖDEMELER DENGESİ İSTATİSTİKLERİ (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.ODANA6.Q01\": \"Cari Denge\","
  ],
  "indicator_hints": [],
  "notes": ""
}
