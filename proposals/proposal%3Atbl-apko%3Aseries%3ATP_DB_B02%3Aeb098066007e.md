---
record_type: proposal
id: proposal:tbl-apko:series:TP_DB_B02:eb098066007e
proposal_id: proposal:tbl-apko:series:TP_DB_B02:eb098066007e
title: Semantic proposal for TP.DB.B02
status: approved
target_type: series
target_id: evds:TP.DB.B02
ticker: TP.DB.B02
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 2.Kısa Vadelİ Borçlar (Borçluya Göre)
candidate_unit: milyon ABD doları
candidate_frequency: monthly
candidate_role: stock_total
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:bank-fx-loans
candidate_formula_hint: 'derived:bank-fx-loans: BDDK bulteni ve EVDS ceyreklik bloklari
  ile eslenir.'
confidence: 0.95
source: heuristic
evidence_fingerprint: eb098066007e6b6033b01d213254cda995932659
catalog_record_id: catalog:evds2:TP.DB.B02
memory_rule_ids: []
evidence:
  ticker: TP.DB.B02
  notebook_slug: tbl-apko
  official_series_name: Toplam Brüt Dış Borç Stoku (Kısa Vade)
  context_title: Toplam Brüt Dış Borç Stoku (Kısa Vade)
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
  - derived:bank-fx-loans
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.DB.B02
    title: 2.Kısa Vadelİ Borçlar (Borçluya Göre)
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_dbdborc
    category: TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)
  memory_rules: []
  source_snippets:
  - '"TP.DB.B02": "Toplam Brüt Dış Borç Stoku (Kısa Vade)",'
  indicator_hints:
  - 'derived:bank-fx-loans: BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DB.B02
promoted_memory_rule_id: memory:global-tp-db-b02
notes: 'Catalog source: catalog:evds2:TP.DB.B02'
body: "# Semantic proposal for TP.DB.B02\n\n## Target\nseries | evds:TP.DB.B02\n\n\
  ## Notebook\ntbl-apko\n\n## Candidate Title\n2.Kısa Vadelİ Borçlar (Borçluya Göre)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n##\
  \ Candidate Role\nstock_total\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n- derived:bank-fx-loans\n\n## Formula Hint\nderived:bank-fx-loans:\
  \ BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nProposal source is heuristic. No matching\
  \ memory rules or approved series exist to verify global safety. Notebook slug present\
  \ suggests potential scoping. Evidence insufficient to confirm global safety without\
  \ notebook-specific scoping.\n\n## Notes\nCatalog source: catalog:evds2:TP.DB.B02\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.DB.B02\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Toplam Brüt Dış Borç Stoku (Kısa Vade)\",\n  \"\
  context_title\": \"Toplam Brüt Dış Borç Stoku (Kısa Vade)\",\n  \"frequency\": \"\
  quarterly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_total\",\n\
  \  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:apko-summary\"\
  ,\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\",\n   \
  \ \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:bank-fx-loans\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.DB.B02\",\n    \"title\": \"2.Kısa Vadelİ Borçlar (Borçluya\
  \ Göre)\",\n    \"frequency\": \"monthly\",\n    \"unit\": \"milyon ABD doları\"\
  ,\n    \"data_group\": \"bie_dbdborc\",\n    \"category\": \"TÜRKİYE BRÜT DIŞ BORÇ\
  \ STOKU (HMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\
  \\\"TP.DB.B02\\\": \\\"Toplam Brüt Dış Borç Stoku (Kısa Vade)\\\",\"\n  ],\n  \"\
  indicator_hints\": [\n    \"derived:bank-fx-loans: BDDK bulteni ve EVDS ceyreklik\
  \ bloklari ile eslenir.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_DB_B02%3Aeb098066007e.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DB.B02

## Target
series | evds:TP.DB.B02

## Notebook
tbl-apko

## Candidate Title
2.Kısa Vadelİ Borçlar (Borçluya Göre)

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
- derived:bank-fx-loans

## Formula Hint
derived:bank-fx-loans: BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.DB.B02

## Evidence
{
  "ticker": "TP.DB.B02",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Toplam Brüt Dış Borç Stoku (Kısa Vade)",
  "context_title": "Toplam Brüt Dış Borç Stoku (Kısa Vade)",
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
    "derived:bank-fx-loans"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DB.B02",
    "title": "2.Kısa Vadelİ Borçlar (Borçluya Göre)",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_dbdborc",
    "category": "TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.DB.B02\": \"Toplam Brüt Dış Borç Stoku (Kısa Vade)\","
  ],
  "indicator_hints": [
    "derived:bank-fx-loans: BDDK bulteni ve EVDS ceyreklik bloklari ile eslenir."
  ],
  "notes": ""
}
