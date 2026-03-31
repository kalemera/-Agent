---
record_type: proposal
id: proposal:tbl-apko:series:TP_DB_B01:f43b4104ea92
proposal_id: proposal:tbl-apko:series:TP_DB_B01:f43b4104ea92
title: Semantic proposal for TP.DB.B01
status: approved
target_type: series
target_id: evds:TP.DB.B01
ticker: TP.DB.B01
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.Türkiye Brüt Dış Borç Stoku
candidate_unit: milyon ABD doları
candidate_frequency: monthly
candidate_role: stock_total
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:bank-tl-loans
candidate_formula_hint: 'derived:bank-tl-loans: BDDK bulteni ve EVDS ceyreklik bloklari
  ile eslenir.'
confidence: 0.95
source: heuristic
evidence_fingerprint: f43b4104ea92bba47541f11e099c904d8dfc6c0d
catalog_record_id: catalog:evds2:TP.DB.B01
memory_rule_ids: []
evidence:
  ticker: TP.DB.B01
  notebook_slug: tbl-apko
  official_series_name: Toplam Brüt Dış Borç Stoku
  context_title: Toplam Brüt Dış Borç Stoku
  frequency: quarterly
  unit: milyon ABD doları
  role: stock_total
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:bank-tl-loans
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.DB.B01
    title: 1.Türkiye Brüt Dış Borç Stoku
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_dbdborc
    category: TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)
  memory_rules: []
  source_snippets:
  - '"TP.DB.B01": "Toplam Brüt Dış Borç Stoku",'
  indicator_hints:
  - 'derived:bank-tl-loans: BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DB.B01
promoted_memory_rule_id: memory:global-tp-db-b01
notes: 'Catalog source: catalog:evds2:TP.DB.B01'
body: "# Semantic proposal for TP.DB.B01\n\n## Target\nseries | evds:TP.DB.B01\n\n\
  ## Notebook\ntbl-apko\n\n## Candidate Title\n1.Türkiye Brüt Dış Borç Stoku\n\n##\
  \ Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n## Candidate\
  \ Role\nstock_total\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n- derived:bank-tl-loans\n\n## Formula Hint\nderived:bank-tl-loans:\
  \ BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nnotebook_slug present, source is heuristic,\
  \ matching_memory_rules empty, approved_series empty\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.DB.B01\n\n## Evidence\n{\n  \"ticker\": \"TP.DB.B01\",\n  \"\
  notebook_slug\": \"tbl-apko\",\n  \"official_series_name\": \"Toplam Brüt Dış Borç\
  \ Stoku\",\n  \"context_title\": \"Toplam Brüt Dış Borç Stoku\",\n  \"frequency\"\
  : \"quarterly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_total\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:apko-summary\"\
  ,\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\",\n   \
  \ \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:bank-tl-loans\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.DB.B01\",\n    \"title\": \"1.Türkiye Brüt Dış Borç Stoku\"\
  ,\n    \"frequency\": \"monthly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_dbdborc\",\n    \"category\": \"TÜRKİYE BRÜT DIŞ BORÇ STOKU\
  \ (HMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.DB.B01\\\
  \": \\\"Toplam Brüt Dış Borç Stoku\\\",\"\n  ],\n  \"indicator_hints\": [\n    \"\
  derived:bank-tl-loans: BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.\"\n\
  \  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_DB_B01%3Af43b4104ea92.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DB.B01

## Target
series | evds:TP.DB.B01

## Notebook
tbl-apko

## Candidate Title
1.Türkiye Brüt Dış Borç Stoku

## Candidate Unit
milyon ABD doları

## Candidate Frequency
monthly

## Candidate Role
stock_total

## Confidence
0.95

## Candidate Themes
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

## Candidate Indicator Inputs
- derived:bank-tl-loans

## Formula Hint
derived:bank-tl-loans: BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.DB.B01

## Evidence
{
  "ticker": "TP.DB.B01",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Toplam Brüt Dış Borç Stoku",
  "context_title": "Toplam Brüt Dış Borç Stoku",
  "frequency": "quarterly",
  "unit": "milyon ABD doları",
  "role": "stock_total",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:bank-tl-loans"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DB.B01",
    "title": "1.Türkiye Brüt Dış Borç Stoku",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_dbdborc",
    "category": "TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.DB.B01\": \"Toplam Brüt Dış Borç Stoku\","
  ],
  "indicator_hints": [
    "derived:bank-tl-loans: BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir."
  ],
  "notes": ""
}
