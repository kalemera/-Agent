---
record_type: proposal
id: proposal:tbl-apko:series:TP_DB_B19:58f403df3436
proposal_id: proposal:tbl-apko:series:TP_DB_B19:58f403df3436
title: Semantic proposal for TP.DB.B19
status: approved
target_type: series
target_id: evds:TP.DB.B19
ticker: TP.DB.B19
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 2.3.2.Finansal Olmayan Kuruluşlar(Borçluya Göre)
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
evidence_fingerprint: 58f403df343675f45e0fd0b0f73004c9c2d00b15
catalog_record_id: catalog:evds2:TP.DB.B19
memory_rule_ids: []
evidence:
  ticker: TP.DB.B19
  notebook_slug: tbl-apko
  official_series_name: Reel Sektör Brüt Dış Borç Stoku (2)
  context_title: Reel Sektör Brüt Dış Borç Stoku (2)
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
    id: catalog:evds2:TP.DB.B19
    title: 2.3.2.Finansal Olmayan Kuruluşlar(Borçluya Göre)
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_dbdborc
    category: TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)
  memory_rules: []
  source_snippets:
  - '"TP.DB.B19": "Reel Sektör Brüt Dış Borç Stoku (2)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DB.B19
promoted_memory_rule_id: memory:global-tp-db-b19
notes: 'Catalog source: catalog:evds2:TP.DB.B19'
body: "# Semantic proposal for TP.DB.B19\n\n## Target\nseries | evds:TP.DB.B19\n\n\
  ## Notebook\ntbl-apko\n\n## Candidate Title\n2.3.2.Finansal Olmayan Kuruluşlar(Borçluya\
  \ Göre)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\
  \n## Candidate Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n\
  - theme:apko-summary\n- theme:external-financing\n- theme:banking-balance-sheet\n\
  - theme:reserves-and-liquidity\n\n## Candidate Indicator Inputs\n-\n\n## Formula\
  \ Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n\
  No matching memory rules or approved series to confirm global safety.\n\n## Notes\n\
  Catalog source: catalog:evds2:TP.DB.B19\n\n## Evidence\n{\n  \"ticker\": \"TP.DB.B19\"\
  ,\n  \"notebook_slug\": \"tbl-apko\",\n  \"official_series_name\": \"Reel Sektör\
  \ Brüt Dış Borç Stoku (2)\",\n  \"context_title\": \"Reel Sektör Brüt Dış Borç Stoku\
  \ (2)\",\n  \"frequency\": \"quarterly\",\n  \"unit\": \"milyon ABD doları\",\n\
  \  \"role\": \"stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:tblapko-bbg-upload\",\n    \"source:tblapko-hmb-ab-borc-xls\"\
  ,\n    \"source:tblapko-swap-pdf\",\n    \"source:tblapko-bddk-weekly-bulletin\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.DB.B19\",\n    \"\
  title\": \"2.3.2.Finansal Olmayan Kuruluşlar(Borçluya Göre)\",\n    \"frequency\"\
  : \"monthly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_dbdborc\"\
  ,\n    \"category\": \"TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)\"\n  },\n  \"memory_rules\"\
  : [],\n  \"source_snippets\": [\n    \"\\\"TP.DB.B19\\\": \\\"Reel Sektör Brüt Dış\
  \ Borç Stoku (2)\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_DB_B19%3A58f403df3436.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DB.B19

## Target
series | evds:TP.DB.B19

## Notebook
tbl-apko

## Candidate Title
2.3.2.Finansal Olmayan Kuruluşlar(Borçluya Göre)

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
Catalog source: catalog:evds2:TP.DB.B19

## Evidence
{
  "ticker": "TP.DB.B19",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Reel Sektör Brüt Dış Borç Stoku (2)",
  "context_title": "Reel Sektör Brüt Dış Borç Stoku (2)",
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
    "id": "catalog:evds2:TP.DB.B19",
    "title": "2.3.2.Finansal Olmayan Kuruluşlar(Borçluya Göre)",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_dbdborc",
    "category": "TÜRKİYE BRÜT DIŞ BORÇ STOKU (HMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.DB.B19\": \"Reel Sektör Brüt Dış Borç Stoku (2)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
