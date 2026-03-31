---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M2:4bbc49370faa
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M2:4bbc49370faa
title: Semantic proposal for TP.MKNETHAR.M2
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M2
ticker: TP.MKNETHAR.M2
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 1.1.2. DİBS (Kesin Alım)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs:
- derived:equity-stock
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 4bbc49370faa34704e2073c4a07c7768ef854250
catalog_record_id: catalog:evds2:TP.MKNETHAR.M2
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M2
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: 1.1.2. DİBS (Kesin Alım), Stok
  context_title: 1.1.2. DİBS (Kesin Alım), Stok
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
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.MKNETHAR.M2
    title: 1.1.2. DİBS (Kesin Alım)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M20": [1, "NET DEĞİŞİM GENEL TOPLAM (**)"],'
  - '"TP.MKNETHAR.M21": [2, "B.1. Yurt İçi Piyasa Toplam (**)"],'
  - '"TP.MKNETHAR.M22": [2, "B.2. Yurt Dışı Piyasa Toplam"],'
  - '"TP.MKNETHAR.M23": [3, "Genel Yönetim İhraçları"],'
  - '"TP.MKNETHAR.M24": [3, "Finansal Olmayan Kuruluş İhraçları"],'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M2
promoted_memory_rule_id: memory:global-tp-mknethar-m2
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M2'
body: "# Semantic proposal for TP.MKNETHAR.M2\n\n## Target\nseries | evds:TP.MKNETHAR.M2\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n1.1.2. DİBS (Kesin Alım)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n- derived:equity-stock\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.MKNETHAR.M2\n\n## Evidence\n{\n  \"ticker\"\
  : \"TP.MKNETHAR.M2\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\",\n  \"official_series_name\"\
  : \"1.1.2. DİBS (Kesin Alım), Stok\",\n  \"context_title\": \"1.1.2. DİBS (Kesin\
  \ Alım), Stok\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\"\
  ,\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\",\n    \"theme:swap-and-securities\"\
  \n  ],\n  \"indicator_ids\": [\n    \"derived:equity-stock\"\n  ],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M2\",\n    \"title\"\
  : \"1.1.2. DİBS (Kesin Alım)\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n    \"category\": \"\
  YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"memory_rules\": [],\n\
  \  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M20\\\": [1, \\\"NET DEĞİŞİM GENEL\
  \ TOPLAM (**)\\\"],\",\n    \"\\\"TP.MKNETHAR.M21\\\": [2, \\\"B.1. Yurt İçi Piyasa\
  \ Toplam (**)\\\"],\",\n    \"\\\"TP.MKNETHAR.M22\\\": [2, \\\"B.2. Yurt Dışı Piyasa\
  \ Toplam\\\"],\",\n    \"\\\"TP.MKNETHAR.M23\\\": [3, \\\"Genel Yönetim İhraçları\\\
  \"],\",\n    \"\\\"TP.MKNETHAR.M24\\\": [3, \\\"Finansal Olmayan Kuruluş İhraçları\\\
  \"],\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_MKNETHAR_M2%3A4bbc49370faa.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M2

## Target
series | evds:TP.MKNETHAR.M2

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
1.1.2. DİBS (Kesin Alım)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.9

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

## Candidate Indicator Inputs
- derived:equity-stock

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.MKNETHAR.M2

## Evidence
{
  "ticker": "TP.MKNETHAR.M2",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "1.1.2. DİBS (Kesin Alım), Stok",
  "context_title": "1.1.2. DİBS (Kesin Alım), Stok",
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
    "derived:equity-stock"
  ],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.MKNETHAR.M2",
    "title": "1.1.2. DİBS (Kesin Alım)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M20\": [1, \"NET DEĞİŞİM GENEL TOPLAM (**)\"],",
    "\"TP.MKNETHAR.M21\": [2, \"B.1. Yurt İçi Piyasa Toplam (**)\"],",
    "\"TP.MKNETHAR.M22\": [2, \"B.2. Yurt Dışı Piyasa Toplam\"],",
    "\"TP.MKNETHAR.M23\": [3, \"Genel Yönetim İhraçları\"],",
    "\"TP.MKNETHAR.M24\": [3, \"Finansal Olmayan Kuruluş İhraçları\"],"
  ],
  "indicator_hints": [],
  "notes": ""
}
