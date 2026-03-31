---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M5:46bea1b21f9f
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M5:46bea1b21f9f
title: Semantic proposal for TP.MKNETHAR.M5
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M5
ticker: TP.MKNETHAR.M5
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 3.3. DİBS (Ödünç Alım)
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
evidence_fingerprint: 46bea1b21f9fa9a15273d7120fe167d4a9e9a02b
catalog_record_id: catalog:evds2:TP.MKNETHAR.M5
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M5
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: 1.1.5. DİBS (Ödünç Alım), Stok
  context_title: 1.1.5. DİBS (Ödünç Alım), Stok
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
    id: catalog:evds2:TP.MKNETHAR.M5
    title: 3.3. DİBS (Ödünç Alım)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M5": [3, "DİBS (Ödünç Alım)"],'
  - df_menkul_kiymet_apko_["DİBS"] = df_menkul_kiymet_apko_["TP_MKNETHAR_M2"] + df_menkul_kiymet_apko_["TP_MKNETHAR_M3"]
    + df_menkul_kiymet_apko_["TP_MKNETHAR_M4"] + df_menkul_kiymet_apko_["TP_MKNETHAR_M5"]
  - '"TP_MKNETHAR_M2", "TP_MKNETHAR_M3", "TP_MKNETHAR_M4", "TP_MKNETHAR_M5", "TP_MKNETHAR_M8",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M5
promoted_memory_rule_id: memory:global-tp-mknethar-m5
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M5'
body: "# Semantic proposal for TP.MKNETHAR.M5\n\n## Target\nseries | evds:TP.MKNETHAR.M5\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n3.3. DİBS (Ödünç Alım)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nSame ticker proposal exists from different notebook (tbl-apko)\
  \ with status review_pending\n\n## Notes\nCatalog source: catalog:evds2:TP.MKNETHAR.M5\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.MKNETHAR.M5\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"1.1.5. DİBS (Ödünç Alım), Stok\",\n  \"context_title\"\
  : \"1.1.5. DİBS (Ödünç Alım), Stok\",\n  \"frequency\": \"weekly\",\n  \"unit\"\
  : \"milyon ABD doları\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M5\",\n    \"title\"\
  : \"3.3. DİBS (Ödünç Alım)\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n    \"category\": \"\
  YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"memory_rules\": [],\n\
  \  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M5\\\": [3, \\\"DİBS (Ödünç Alım)\\\
  \"],\",\n    \"df_menkul_kiymet_apko_[\\\"DİBS\\\"] = df_menkul_kiymet_apko_[\\\"\
  TP_MKNETHAR_M2\\\"] + df_menkul_kiymet_apko_[\\\"TP_MKNETHAR_M3\\\"] + df_menkul_kiymet_apko_[\\\
  \"TP_MKNETHAR_M4\\\"] + df_menkul_kiymet_apko_[\\\"TP_MKNETHAR_M5\\\"]\",\n    \"\
  \\\"TP_MKNETHAR_M2\\\", \\\"TP_MKNETHAR_M3\\\", \\\"TP_MKNETHAR_M4\\\", \\\"TP_MKNETHAR_M5\\\
  \", \\\"TP_MKNETHAR_M8\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\
  \"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_MKNETHAR_M5%3A46bea1b21f9f.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M5

## Target
series | evds:TP.MKNETHAR.M5

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
3.3. DİBS (Ödünç Alım)

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
Catalog source: catalog:evds2:TP.MKNETHAR.M5

## Evidence
{
  "ticker": "TP.MKNETHAR.M5",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "1.1.5. DİBS (Ödünç Alım), Stok",
  "context_title": "1.1.5. DİBS (Ödünç Alım), Stok",
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
    "id": "catalog:evds2:TP.MKNETHAR.M5",
    "title": "3.3. DİBS (Ödünç Alım)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M5\": [3, \"DİBS (Ödünç Alım)\"],",
    "df_menkul_kiymet_apko_[\"DİBS\"] = df_menkul_kiymet_apko_[\"TP_MKNETHAR_M2\"] + df_menkul_kiymet_apko_[\"TP_MKNETHAR_M3\"] + df_menkul_kiymet_apko_[\"TP_MKNETHAR_M4\"] + df_menkul_kiymet_apko_[\"TP_MKNETHAR_M5\"]",
    "\"TP_MKNETHAR_M2\", \"TP_MKNETHAR_M3\", \"TP_MKNETHAR_M4\", \"TP_MKNETHAR_M5\", \"TP_MKNETHAR_M8\","
  ],
  "indicator_hints": [],
  "notes": ""
}
