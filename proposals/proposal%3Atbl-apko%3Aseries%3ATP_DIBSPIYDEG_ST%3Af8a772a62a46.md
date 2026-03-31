---
record_type: proposal
id: proposal:tbl-apko:series:TP_DIBSPIYDEG_ST:f8a772a62a46
proposal_id: proposal:tbl-apko:series:TP_DIBSPIYDEG_ST:f8a772a62a46
title: Semantic proposal for TP.DIBSPIYDEG.ST
status: approved
target_type: series
target_id: evds:TP.DIBSPIYDEG.ST
ticker: TP.DIBSPIYDEG.ST
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.Toplam (S.1, S.2)
candidate_unit: milyon TL
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:foreign-dibs-stock-all-in
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: f8a772a62a46dbce641df728c4d4e1dc8b044c95
catalog_record_id: catalog:evds2:TP.DIBSPIYDEG.ST
memory_rule_ids: []
evidence:
  ticker: TP.DIBSPIYDEG.ST
  notebook_slug: tbl-apko
  official_series_name: Hazine DİBS Stoku (TL)
  context_title: Hazine DİBS Stoku (TL)
  frequency: weekly
  unit: TL
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:foreign-dibs-stock-all-in
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.DIBSPIYDEG.ST
    title: 1.Toplam (S.1, S.2)
    frequency: weekly
    unit: milyon TL
    data_group: bie_dibspiydeg
    category: DEVLET İÇ BORÇLANMA SENETLERİ
  memory_rules: []
  source_snippets:
  - '"TP.DIBSPIYDEG.ST": "Hazine DİBS Stoku (TL)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DIBSPIYDEG.ST
promoted_memory_rule_id: memory:global-tp-dibspiydeg-st
notes: 'Catalog source: catalog:evds2:TP.DIBSPIYDEG.ST'
body: "# Semantic proposal for TP.DIBSPIYDEG.ST\n\n## Target\nseries | evds:TP.DIBSPIYDEG.ST\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.Toplam (S.1, S.2)\n\n## Candidate\
  \ Unit\nmilyon TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\nstock_component\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n- theme:external-financing\n\
  - theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\n## Candidate Indicator\
  \ Inputs\n- derived:foreign-dibs-stock-all-in\n\n## Formula Hint\n-\n\n## Source\n\
  heuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nSame ticker has an existing\
  \ review_pending proposal from a different notebook (prbnk-mnklkymt-v5). No previously\
  \ approved series exist for this ticker.\n\n## Notes\nCatalog source: catalog:evds2:TP.DIBSPIYDEG.ST\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.DIBSPIYDEG.ST\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Hazine DİBS Stoku (TL)\",\n  \"context_title\"\
  : \"Hazine DİBS Stoku (TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"TL\"\
  ,\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:foreign-dibs-stock-all-in\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.DIBSPIYDEG.ST\",\n    \"title\": \"1.Toplam (S.1, S.2)\",\n\
  \    \"frequency\": \"weekly\",\n    \"unit\": \"milyon TL\",\n    \"data_group\"\
  : \"bie_dibspiydeg\",\n    \"category\": \"DEVLET İÇ BORÇLANMA SENETLERİ\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.DIBSPIYDEG.ST\\\
  \": \\\"Hazine DİBS Stoku (TL)\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_DIBSPIYDEG_ST%3Af8a772a62a46.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DIBSPIYDEG.ST

## Target
series | evds:TP.DIBSPIYDEG.ST

## Notebook
tbl-apko

## Candidate Title
1.Toplam (S.1, S.2)

## Candidate Unit
milyon TL

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
- derived:foreign-dibs-stock-all-in

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.DIBSPIYDEG.ST

## Evidence
{
  "ticker": "TP.DIBSPIYDEG.ST",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Hazine DİBS Stoku (TL)",
  "context_title": "Hazine DİBS Stoku (TL)",
  "frequency": "weekly",
  "unit": "TL",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:foreign-dibs-stock-all-in"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DIBSPIYDEG.ST",
    "title": "1.Toplam (S.1, S.2)",
    "frequency": "weekly",
    "unit": "milyon TL",
    "data_group": "bie_dibspiydeg",
    "category": "DEVLET İÇ BORÇLANMA SENETLERİ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.DIBSPIYDEG.ST\": \"Hazine DİBS Stoku (TL)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
