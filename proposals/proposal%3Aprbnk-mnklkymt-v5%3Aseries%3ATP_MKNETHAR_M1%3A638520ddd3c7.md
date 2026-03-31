---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M1:638520ddd3c7
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M1:638520ddd3c7
title: Semantic proposal for TP.MKNETHAR.M1
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M1
ticker: TP.MKNETHAR.M1
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 1.1.1. Hisse Senedi
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs:
- derived:equity-stock
- derived:equity-foreign-share
candidate_formula_hint: 'derived:equity-foreign-share: Hisse stogu ve haftalik ZIP
  tablosundan turetilen yabanci pay.'
confidence: 0.95
source: heuristic
evidence_fingerprint: 638520ddd3c74ddfe529fc0b44c6ee9079d0e746
catalog_record_id: catalog:evds2:TP.MKNETHAR.M1
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M1
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: 1.1.1. Hisse Senedi, Stok
  context_title: 1.1.1. Hisse Senedi, Stok
  frequency: weekly
  unit: milyon ABD doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:portfolio-flows
  - theme:foreign-ownership
  - theme:swap-and-securities
  indicator_ids:
  - derived:equity-stock
  - derived:equity-foreign-share
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.MKNETHAR.M1
    title: 1.1.1. Hisse Senedi
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M10": [3, "DİBS (Teminat)"],'
  - '"TP.MKNETHAR.M11": [3, "DİBS (Ödünç)"],'
  - '"TP.MKNETHAR.M12": [3, "Genel Yönetim Dışındaki Sektör İhraçları (***)"],'
  - '"TP.MKNETHAR.M1": [3, "Hisse Senedi"],'
  - '"TP.MKNETHAR.M10": [3, "DİBS (Teminat Alım) - Net Değişim"],'
  indicator_hints:
  - 'derived:equity-foreign-share: Hisse stogu ve haftalik ZIP tablosundan turetilen
    yabanci pay.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M1
promoted_memory_rule_id: memory:global-tp-mknethar-m1
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M1'
body: "# Semantic proposal for TP.MKNETHAR.M1\n\n## Target\nseries | evds:TP.MKNETHAR.M1\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n1.1.1. Hisse Senedi\n\n\
  ## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_component\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n- derived:equity-stock\n- derived:equity-foreign-share\n\n## Formula Hint\n\
  derived:equity-foreign-share: Hisse stogu ve haftalik ZIP tablosundan turetilen\
  \ yabanci pay.\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n\
  Same ticker proposal exists in different notebook with pending status\n\n## Notes\n\
  Catalog source: catalog:evds2:TP.MKNETHAR.M1\n\n## Evidence\n{\n  \"ticker\": \"\
  TP.MKNETHAR.M1\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\",\n  \"official_series_name\"\
  : \"1.1.1. Hisse Senedi, Stok\",\n  \"context_title\": \"1.1.1. Hisse Senedi, Stok\"\
  ,\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\"\
  : \"stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n \
  \   \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\",\n    \"theme:swap-and-securities\"\
  \n  ],\n  \"indicator_ids\": [\n    \"derived:equity-stock\",\n    \"derived:equity-foreign-share\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:prbnk-weekly-zip\",\n    \"\
  source:prbnk-swap-pdf\"\n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M1\"\
  ,\n    \"title\": \"1.1.1. Hisse Senedi\",\n    \"frequency\": \"weekly\",\n   \
  \ \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n    \"\
  category\": \"YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"memory_rules\"\
  : [],\n  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M10\\\": [3, \\\"DİBS (Teminat)\\\
  \"],\",\n    \"\\\"TP.MKNETHAR.M11\\\": [3, \\\"DİBS (Ödünç)\\\"],\",\n    \"\\\"\
  TP.MKNETHAR.M12\\\": [3, \\\"Genel Yönetim Dışındaki Sektör İhraçları (***)\\\"\
  ],\",\n    \"\\\"TP.MKNETHAR.M1\\\": [3, \\\"Hisse Senedi\\\"],\",\n    \"\\\"TP.MKNETHAR.M10\\\
  \": [3, \\\"DİBS (Teminat Alım) - Net Değişim\\\"],\"\n  ],\n  \"indicator_hints\"\
  : [\n    \"derived:equity-foreign-share: Hisse stogu ve haftalik ZIP tablosundan\
  \ turetilen yabanci pay.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_MKNETHAR_M1%3A638520ddd3c7.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M1

## Target
series | evds:TP.MKNETHAR.M1

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
1.1.1. Hisse Senedi

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.95

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

## Candidate Indicator Inputs
- derived:equity-stock
- derived:equity-foreign-share

## Formula Hint
derived:equity-foreign-share: Hisse stogu ve haftalik ZIP tablosundan turetilen yabanci pay.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.MKNETHAR.M1

## Evidence
{
  "ticker": "TP.MKNETHAR.M1",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "1.1.1. Hisse Senedi, Stok",
  "context_title": "1.1.1. Hisse Senedi, Stok",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:portfolio-flows",
    "theme:foreign-ownership",
    "theme:swap-and-securities"
  ],
  "indicator_ids": [
    "derived:equity-stock",
    "derived:equity-foreign-share"
  ],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.MKNETHAR.M1",
    "title": "1.1.1. Hisse Senedi",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M10\": [3, \"DİBS (Teminat)\"],",
    "\"TP.MKNETHAR.M11\": [3, \"DİBS (Ödünç)\"],",
    "\"TP.MKNETHAR.M12\": [3, \"Genel Yönetim Dışındaki Sektör İhraçları (***)\"],",
    "\"TP.MKNETHAR.M1\": [3, \"Hisse Senedi\"],",
    "\"TP.MKNETHAR.M10\": [3, \"DİBS (Teminat Alım) - Net Değişim\"],"
  ],
  "indicator_hints": [
    "derived:equity-foreign-share: Hisse stogu ve haftalik ZIP tablosundan turetilen yabanci pay."
  ],
  "notes": ""
}
