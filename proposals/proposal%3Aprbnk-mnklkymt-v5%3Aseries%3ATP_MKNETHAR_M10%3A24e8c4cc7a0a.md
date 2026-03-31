---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M10:24e8c4cc7a0a
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M10:24e8c4cc7a0a
title: Semantic proposal for TP.MKNETHAR.M10
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M10
ticker: TP.MKNETHAR.M10
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 4.2. DİBS (Teminat Alım)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 24e8c4cc7a0abcdcfd915db2a54a80f8da99ba96
catalog_record_id: catalog:evds2:TP.MKNETHAR.M10
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M10
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: 2.1.4. DİBS (Teminat Alım), Net Değişim
  context_title: 2.1.4. DİBS (Teminat Alım), Net Değişim
  frequency: weekly
  unit: milyon ABD doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:portfolio-flows
  - theme:foreign-ownership
  - theme:swap-and-securities
  indicator_ids: []
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.MKNETHAR.M10
    title: 4.2. DİBS (Teminat Alım)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M10": [3, "DİBS (Teminat)"],'
  - '"TP.MKNETHAR.M10": [3, "DİBS (Teminat Alım) - Net Değişim"],'
  - df_menkul_kiymet_apko_["DİBS - Net Değişim"] = df_menkul_kiymet_apko_["TP_MKNETHAR_M8"]
    + df_menkul_kiymet_apko_["TP_MKNETHAR_M9"] + df_menkul_kiymet_apko_["TP_MKNETHAR_M10"]
    + df_menkul_kiymet_apko_["TP_MKNETHAR_M11"]
  - '"TP_MKNETHAR_M9", "TP_MKNETHAR_M10", "TP_MKNETHAR_M11", "TP_DIBSPIYDEG_ST", "TP_DK_USD_A_YTL"'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M10
promoted_memory_rule_id: memory:global-tp-mknethar-m10
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M10'
body: "# Semantic proposal for TP.MKNETHAR.M10\n\n## Target\nseries | evds:TP.MKNETHAR.M10\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n4.2. DİBS (Teminat Alım)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nEmpty approved_series and matching_memory_rules prevent\
  \ verification of global safety; notebook_slug indicates specific context.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.MKNETHAR.M10\n\n## Evidence\n{\n  \"ticker\"\
  : \"TP.MKNETHAR.M10\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\",\n  \"official_series_name\"\
  : \"2.1.4. DİBS (Teminat Alım), Net Değişim\",\n  \"context_title\": \"2.1.4. DİBS\
  \ (Teminat Alım), Net Değişim\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon\
  \ ABD doları\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M10\",\n    \"title\"\
  : \"4.2. DİBS (Teminat Alım)\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n    \"category\": \"\
  YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"memory_rules\": [],\n\
  \  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M10\\\": [3, \\\"DİBS (Teminat)\\\
  \"],\",\n    \"\\\"TP.MKNETHAR.M10\\\": [3, \\\"DİBS (Teminat Alım) - Net Değişim\\\
  \"],\",\n    \"df_menkul_kiymet_apko_[\\\"DİBS - Net Değişim\\\"] = df_menkul_kiymet_apko_[\\\
  \"TP_MKNETHAR_M8\\\"] + df_menkul_kiymet_apko_[\\\"TP_MKNETHAR_M9\\\"] + df_menkul_kiymet_apko_[\\\
  \"TP_MKNETHAR_M10\\\"] + df_menkul_kiymet_apko_[\\\"TP_MKNETHAR_M11\\\"]\",\n  \
  \  \"\\\"TP_MKNETHAR_M9\\\", \\\"TP_MKNETHAR_M10\\\", \\\"TP_MKNETHAR_M11\\\", \\\
  \"TP_DIBSPIYDEG_ST\\\", \\\"TP_DK_USD_A_YTL\\\"\"\n  ],\n  \"indicator_hints\":\
  \ [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_MKNETHAR_M10%3A24e8c4cc7a0a.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M10

## Target
series | evds:TP.MKNETHAR.M10

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
4.2. DİBS (Teminat Alım)

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
Catalog source: catalog:evds2:TP.MKNETHAR.M10

## Evidence
{
  "ticker": "TP.MKNETHAR.M10",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "2.1.4. DİBS (Teminat Alım), Net Değişim",
  "context_title": "2.1.4. DİBS (Teminat Alım), Net Değişim",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:portfolio-flows",
    "theme:foreign-ownership",
    "theme:swap-and-securities"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.MKNETHAR.M10",
    "title": "4.2. DİBS (Teminat Alım)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M10\": [3, \"DİBS (Teminat)\"],",
    "\"TP.MKNETHAR.M10\": [3, \"DİBS (Teminat Alım) - Net Değişim\"],",
    "df_menkul_kiymet_apko_[\"DİBS - Net Değişim\"] = df_menkul_kiymet_apko_[\"TP_MKNETHAR_M8\"] + df_menkul_kiymet_apko_[\"TP_MKNETHAR_M9\"] + df_menkul_kiymet_apko_[\"TP_MKNETHAR_M10\"] + df_menkul_kiymet_apko_[\"TP_MKNETHAR_M11\"]",
    "\"TP_MKNETHAR_M9\", \"TP_MKNETHAR_M10\", \"TP_MKNETHAR_M11\", \"TP_DIBSPIYDEG_ST\", \"TP_DK_USD_A_YTL\""
  ],
  "indicator_hints": [],
  "notes": ""
}
