---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M22:5f5663fef3eb
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M22:5f5663fef3eb
title: Semantic proposal for TP.MKNETHAR.M22
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M22
ticker: TP.MKNETHAR.M22
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 2.2. Yurt Dışı Piyasa Toplam
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 5f5663fef3eb607efe9d55982bec325a3dfefffb
catalog_record_id: catalog:evds2:TP.MKNETHAR.M22
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M22
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: 2.2. Yurt Dışı Piyasa Toplam, Net Değişim
  context_title: 2.2. Yurt Dışı Piyasa Toplam, Net Değişim
  frequency: weekly
  unit: milyon ABD doları
  role: stock_total
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
    id: catalog:evds2:TP.MKNETHAR.M22
    title: 2.2. Yurt Dışı Piyasa Toplam
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M22": [2, "B.2. Yurt Dışı Piyasa Toplam"],'
  - yp_menkul_kiymet_f = df_menkul_kiymet_com.loc[df_menkul_kiymet_com.index[0], "TP_MKNETHAR_M22"].astype(float)
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M22
promoted_memory_rule_id: memory:global-tp-mknethar-m22
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M22'
body: "# Semantic proposal for TP.MKNETHAR.M22\n\n## Target\nseries | evds:TP.MKNETHAR.M22\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n2.2. Yurt Dışı Piyasa Toplam\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_total\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.MKNETHAR.M22\n\n## Evidence\n{\n  \"ticker\": \"TP.MKNETHAR.M22\"\
  ,\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\",\n  \"official_series_name\": \"2.2.\
  \ Yurt Dışı Piyasa Toplam, Net Değişim\",\n  \"context_title\": \"2.2. Yurt Dışı\
  \ Piyasa Toplam, Net Değişim\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon\
  \ ABD doları\",\n  \"role\": \"stock_total\",\n  \"status\": \"derived_input\",\n\
  \  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M22\",\n    \"title\"\
  : \"2.2. Yurt Dışı Piyasa Toplam\",\n    \"frequency\": \"weekly\",\n    \"unit\"\
  : \"milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n    \"category\"\
  : \"YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"memory_rules\": [],\n\
  \  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M22\\\": [2, \\\"B.2. Yurt Dışı\
  \ Piyasa Toplam\\\"],\",\n    \"yp_menkul_kiymet_f = df_menkul_kiymet_com.loc[df_menkul_kiymet_com.index[0],\
  \ \\\"TP_MKNETHAR_M22\\\"].astype(float)\"\n  ],\n  \"indicator_hints\": [],\n \
  \ \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_MKNETHAR_M22%3A5f5663fef3eb.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M22

## Target
series | evds:TP.MKNETHAR.M22

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
2.2. Yurt Dışı Piyasa Toplam

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_total

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
Catalog source: catalog:evds2:TP.MKNETHAR.M22

## Evidence
{
  "ticker": "TP.MKNETHAR.M22",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "2.2. Yurt Dışı Piyasa Toplam, Net Değişim",
  "context_title": "2.2. Yurt Dışı Piyasa Toplam, Net Değişim",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_total",
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
    "id": "catalog:evds2:TP.MKNETHAR.M22",
    "title": "2.2. Yurt Dışı Piyasa Toplam",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M22\": [2, \"B.2. Yurt Dışı Piyasa Toplam\"],",
    "yp_menkul_kiymet_f = df_menkul_kiymet_com.loc[df_menkul_kiymet_com.index[0], \"TP_MKNETHAR_M22\"].astype(float)"
  ],
  "indicator_hints": [],
  "notes": ""
}
