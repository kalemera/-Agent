---
record_type: proposal
id: proposal:tbl-apko:series:TP_EBONDPIYDEG_ST:307ae106dda4
proposal_id: proposal:tbl-apko:series:TP_EBONDPIYDEG_ST:307ae106dda4
title: Semantic proposal for TP.EBONDPIYDEG.ST
status: approved
target_type: series
target_id: evds:TP.EBONDPIYDEG.ST
ticker: TP.EBONDPIYDEG.ST
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.Toplam (S.1, S.2)
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
evidence_fingerprint: 307ae106dda48756f5d025d57d375011e1a37721
catalog_record_id: catalog:evds2:TP.EBONDPIYDEG.ST
memory_rule_ids: []
evidence:
  ticker: TP.EBONDPIYDEG.ST
  notebook_slug: tbl-apko
  official_series_name: Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)
  context_title: Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)
  frequency: weekly
  unit: Eurobond - Yaşayan Stok
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
    id: catalog:evds2:TP.EBONDPIYDEG.ST
    title: 1.Toplam (S.1, S.2)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ebondpiydeg
    category: GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '"TP.EBONDPIYDEG.ST": "Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.EBONDPIYDEG.ST
promoted_memory_rule_id: memory:global-tp-ebondpiydeg-st
notes: 'Catalog source: catalog:evds2:TP.EBONDPIYDEG.ST'
body: "# Semantic proposal for TP.EBONDPIYDEG.ST\n\n## Target\nseries | evds:TP.EBONDPIYDEG.ST\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.Toplam (S.1, S.2)\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  stock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.EBONDPIYDEG.ST\n\n## Evidence\n{\n  \"\
  ticker\": \"TP.EBONDPIYDEG.ST\",\n  \"notebook_slug\": \"tbl-apko\",\n  \"official_series_name\"\
  : \"Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)\",\n  \"context_title\":\
  \ \"Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)\",\n  \"frequency\": \"weekly\"\
  ,\n  \"unit\": \"Eurobond - Yaşayan Stok\",\n  \"role\": \"stock_component\",\n\
  \  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:apko-summary\"\
  ,\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\",\n   \
  \ \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:tblapko-bbg-upload\",\n    \"source:tblapko-hmb-ab-borc-xls\"\
  ,\n    \"source:tblapko-swap-pdf\",\n    \"source:tblapko-bddk-weekly-bulletin\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.EBONDPIYDEG.ST\"\
  ,\n    \"title\": \"1.Toplam (S.1, S.2)\",\n    \"frequency\": \"weekly\",\n   \
  \ \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_ebondpiydeg\",\n \
  \   \"category\": \"GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.EBONDPIYDEG.ST\\\
  \": \\\"Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)\\\",\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_EBONDPIYDEG_ST%3A307ae106dda4.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.EBONDPIYDEG.ST

## Target
series | evds:TP.EBONDPIYDEG.ST

## Notebook
tbl-apko

## Candidate Title
1.Toplam (S.1, S.2)

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
Catalog source: catalog:evds2:TP.EBONDPIYDEG.ST

## Evidence
{
  "ticker": "TP.EBONDPIYDEG.ST",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)",
  "context_title": "Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)",
  "frequency": "weekly",
  "unit": "Eurobond - Yaşayan Stok",
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
    "id": "catalog:evds2:TP.EBONDPIYDEG.ST",
    "title": "1.Toplam (S.1, S.2)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ebondpiydeg",
    "category": "GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.EBONDPIYDEG.ST\": \"Kamu Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
