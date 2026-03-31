---
record_type: proposal
id: proposal:eurobnd-blg-v4:series:TP_EBONDYAZDEG_S2D:8b74e6221a65
proposal_id: proposal:eurobnd-blg-v4:series:TP_EBONDYAZDEG_S2D:8b74e6221a65
title: Semantic proposal for TP.EBONDYAZDEG.S2D
status: approved
target_type: series
target_id: evds:TP.EBONDYAZDEG.S2D
ticker: TP.EBONDYAZDEG.S2D
notebook_slug: eurobnd-blg-v4
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Eurobnd_Blg_V4.ipynb
candidate_title: 1.2.2.Diğer
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:eurobond
- theme:external-financing
candidate_indicator_inputs:
- derived:eurobond-foreign-stock
- derived:eurobond-foreign-share
- derived:hazine-eurobond-foreign-stock
- derived:hazine-eurobond-foreign-share
candidate_formula_hint: 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci
  stoklarinin toplam stoga orani.'
confidence: 0.95
source: heuristic
evidence_fingerprint: 8b74e6221a65f45eb047fc85bdf753e97cf99643
catalog_record_id: catalog:evds2:TP.EBONDYAZDEG.S2D
memory_rule_ids: []
evidence:
  ticker: TP.EBONDYAZDEG.S2D
  notebook_slug: eurobnd-blg-v4
  official_series_name: Diğer
  context_title: Diğer
  frequency: weekly
  unit: milyon ABD doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:eurobond
  - theme:external-financing
  indicator_ids:
  - derived:eurobond-foreign-stock
  - derived:eurobond-foreign-share
  - derived:hazine-eurobond-foreign-stock
  - derived:hazine-eurobond-foreign-share
  source_dependency_ids:
  - source:eurobnd-bbg-upload
  - source:eurobnd-tcmb-vade-pdf
  - source:eurobnd-hmb-odeme-projeksiyonu
  catalog_record:
    id: catalog:evds2:TP.EBONDYAZDEG.S2D
    title: 1.2.2.Diğer
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ebondyazdeg
    category: GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.EBONDYAZDEG.S2D'', ''TP.YDOSBAYAZDEG.S19'', ''TP.YDOSBAYAZDEG.S38'', ''TP.YDOSBAYAZDEG.S55'','
  - df_eurobond["Hazine Eurobond Yabancılar"] = df_eurobond["TP_EBONDYAZDEG_S2D"]
  indicator_hints:
  - 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam
    stoga orani.'
  - 'derived:hazine-eurobond-foreign-share: evds:TP.EBONDYAZDEG.S2D / evds:TP.EBONDYAZDEG.ST'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.EBONDYAZDEG.S2D
promoted_memory_rule_id: memory:global-tp-ebondyazdeg-s2d
notes: 'Catalog source: catalog:evds2:TP.EBONDYAZDEG.S2D'
body: "# Semantic proposal for TP.EBONDYAZDEG.S2D\n\n## Target\nseries | evds:TP.EBONDYAZDEG.S2D\n\
  \n## Notebook\neurobnd-blg-v4\n\n## Candidate Title\n1.2.2.Diğer\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  stock_component\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:eurobond\n\
  - theme:external-financing\n\n## Candidate Indicator Inputs\n- derived:eurobond-foreign-stock\n\
  - derived:eurobond-foreign-share\n- derived:hazine-eurobond-foreign-stock\n- derived:hazine-eurobond-foreign-share\n\
  \n## Formula Hint\nderived:eurobond-foreign-share: Hazine ve ozel sektor yabanci\
  \ stoklarinin toplam stoga orani.\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.EBONDYAZDEG.S2D\n\n## Evidence\n{\n  \"ticker\": \"TP.EBONDYAZDEG.S2D\"\
  ,\n  \"notebook_slug\": \"eurobnd-blg-v4\",\n  \"official_series_name\": \"Diğer\"\
  ,\n  \"context_title\": \"Diğer\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"\
  milyon ABD doları\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:eurobond\",\n    \"theme:external-financing\"\
  \n  ],\n  \"indicator_ids\": [\n    \"derived:eurobond-foreign-stock\",\n    \"\
  derived:eurobond-foreign-share\",\n    \"derived:hazine-eurobond-foreign-stock\"\
  ,\n    \"derived:hazine-eurobond-foreign-share\"\n  ],\n  \"source_dependency_ids\"\
  : [\n    \"source:eurobnd-bbg-upload\",\n    \"source:eurobnd-tcmb-vade-pdf\",\n\
  \    \"source:eurobnd-hmb-odeme-projeksiyonu\"\n  ],\n  \"catalog_record\": {\n\
  \    \"id\": \"catalog:evds2:TP.EBONDYAZDEG.S2D\",\n    \"title\": \"1.2.2.Diğer\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_ebondyazdeg\",\n    \"category\": \"GENEL YÖNETİM YURT DIŞI\
  \ BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.EBONDYAZDEG.S2D', 'TP.YDOSBAYAZDEG.S19', 'TP.YDOSBAYAZDEG.S38', 'TP.YDOSBAYAZDEG.S55',\"\
  ,\n    \"df_eurobond[\\\"Hazine Eurobond Yabancılar\\\"] = df_eurobond[\\\"TP_EBONDYAZDEG_S2D\\\
  \"]\"\n  ],\n  \"indicator_hints\": [\n    \"derived:eurobond-foreign-share: Hazine\
  \ ve ozel sektor yabanci stoklarinin toplam stoga orani.\",\n    \"derived:hazine-eurobond-foreign-share:\
  \ evds:TP.EBONDYAZDEG.S2D / evds:TP.EBONDYAZDEG.ST\"\n  ],\n  \"notes\": \"\"\n\
  }\n"
path: proposals\proposal%3Aeurobnd-blg-v4%3Aseries%3ATP_EBONDYAZDEG_S2D%3A8b74e6221a65.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.EBONDYAZDEG.S2D

## Target
series | evds:TP.EBONDYAZDEG.S2D

## Notebook
eurobnd-blg-v4

## Candidate Title
1.2.2.Diğer

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.95

## Candidate Themes
- theme:eurobond
- theme:external-financing

## Candidate Indicator Inputs
- derived:eurobond-foreign-stock
- derived:eurobond-foreign-share
- derived:hazine-eurobond-foreign-stock
- derived:hazine-eurobond-foreign-share

## Formula Hint
derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.EBONDYAZDEG.S2D

## Evidence
{
  "ticker": "TP.EBONDYAZDEG.S2D",
  "notebook_slug": "eurobnd-blg-v4",
  "official_series_name": "Diğer",
  "context_title": "Diğer",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:eurobond",
    "theme:external-financing"
  ],
  "indicator_ids": [
    "derived:eurobond-foreign-stock",
    "derived:eurobond-foreign-share",
    "derived:hazine-eurobond-foreign-stock",
    "derived:hazine-eurobond-foreign-share"
  ],
  "source_dependency_ids": [
    "source:eurobnd-bbg-upload",
    "source:eurobnd-tcmb-vade-pdf",
    "source:eurobnd-hmb-odeme-projeksiyonu"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.EBONDYAZDEG.S2D",
    "title": "1.2.2.Diğer",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ebondyazdeg",
    "category": "GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.EBONDYAZDEG.S2D', 'TP.YDOSBAYAZDEG.S19', 'TP.YDOSBAYAZDEG.S38', 'TP.YDOSBAYAZDEG.S55',",
    "df_eurobond[\"Hazine Eurobond Yabancılar\"] = df_eurobond[\"TP_EBONDYAZDEG_S2D\"]"
  ],
  "indicator_hints": [
    "derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.",
    "derived:hazine-eurobond-foreign-share: evds:TP.EBONDYAZDEG.S2D / evds:TP.EBONDYAZDEG.ST"
  ],
  "notes": ""
}
