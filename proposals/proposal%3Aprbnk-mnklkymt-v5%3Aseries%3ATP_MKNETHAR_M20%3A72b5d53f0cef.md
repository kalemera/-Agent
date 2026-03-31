---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M20:72b5d53f0cef
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_MKNETHAR_M20:72b5d53f0cef
title: Semantic proposal for TP.MKNETHAR.M20
status: approved
target_type: series
target_id: evds:TP.MKNETHAR.M20
ticker: TP.MKNETHAR.M20
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 2. Net Değişim Genel Toplam
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs:
- derived:equity-plus-dibs-flow
- derived:portfolio-flow-total
candidate_formula_hint: 'derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin
  birlestirilmis net degisimi.'
confidence: 0.95
source: heuristic
evidence_fingerprint: 72b5d53f0cef0d4120c65ac8f0bd458192b16296
catalog_record_id: catalog:evds2:TP.MKNETHAR.M20
memory_rule_ids: []
evidence:
  ticker: TP.MKNETHAR.M20
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: 2. Net Değişim Genel Toplam, Net Değişim
  context_title: 2. Net Değişim Genel Toplam, Net Değişim
  frequency: weekly
  unit: milyon ABD doları
  role: stock_total
  status: derived_input
  theme_ids:
  - theme:portfolio-flows
  - theme:foreign-ownership
  - theme:swap-and-securities
  indicator_ids:
  - derived:equity-plus-dibs-flow
  - derived:portfolio-flow-total
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.MKNETHAR.M20
    title: 2. Net Değişim Genel Toplam
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_mknethar
    category: YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ
  memory_rules: []
  source_snippets:
  - '"TP.MKNETHAR.M20": [1, "NET DEĞİŞİM GENEL TOPLAM (**)"],'
  - tl_yp_menkul_kiymet_f = df_menkul_kiymet_com.loc[df_menkul_kiymet_com.index[0],
    "TP_MKNETHAR_M20"].astype(float)
  indicator_hints:
  - 'derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin birlestirilmis net degisimi.'
  - 'derived:portfolio-flow-total: Hisse, DIBS ve ilgili destek tablolarindan portfoy
    akis toplami uretilir.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.MKNETHAR.M20
promoted_memory_rule_id: memory:global-tp-mknethar-m20
notes: 'Catalog source: catalog:evds2:TP.MKNETHAR.M20'
body: "# Semantic proposal for TP.MKNETHAR.M20\n\n## Target\nseries | evds:TP.MKNETHAR.M20\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n2. Net Değişim Genel Toplam\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_total\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n- derived:equity-plus-dibs-flow\n- derived:portfolio-flow-total\n\n##\
  \ Formula Hint\nderived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin birlestirilmis\
  \ net degisimi.\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n\
  LLM requested manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.MKNETHAR.M20\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.MKNETHAR.M20\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"2. Net Değişim Genel Toplam, Net Değişim\",\n \
  \ \"context_title\": \"2. Net Değişim Genel Toplam, Net Değişim\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_total\",\n\
  \  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:portfolio-flows\"\
  ,\n    \"theme:foreign-ownership\",\n    \"theme:swap-and-securities\"\n  ],\n \
  \ \"indicator_ids\": [\n    \"derived:equity-plus-dibs-flow\",\n    \"derived:portfolio-flow-total\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:prbnk-weekly-zip\",\n    \"\
  source:prbnk-swap-pdf\"\n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.MKNETHAR.M20\"\
  ,\n    \"title\": \"2. Net Değişim Genel Toplam\",\n    \"frequency\": \"weekly\"\
  ,\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_mknethar\",\n\
  \    \"category\": \"YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ\"\n  },\n  \"\
  memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.MKNETHAR.M20\\\": [1,\
  \ \\\"NET DEĞİŞİM GENEL TOPLAM (**)\\\"],\",\n    \"tl_yp_menkul_kiymet_f = df_menkul_kiymet_com.loc[df_menkul_kiymet_com.index[0],\
  \ \\\"TP_MKNETHAR_M20\\\"].astype(float)\"\n  ],\n  \"indicator_hints\": [\n   \
  \ \"derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin birlestirilmis net\
  \ degisimi.\",\n    \"derived:portfolio-flow-total: Hisse, DIBS ve ilgili destek\
  \ tablolarindan portfoy akis toplami uretilir.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_MKNETHAR_M20%3A72b5d53f0cef.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.MKNETHAR.M20

## Target
series | evds:TP.MKNETHAR.M20

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
2. Net Değişim Genel Toplam

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_total

## Confidence
0.95

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

## Candidate Indicator Inputs
- derived:equity-plus-dibs-flow
- derived:portfolio-flow-total

## Formula Hint
derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin birlestirilmis net degisimi.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.MKNETHAR.M20

## Evidence
{
  "ticker": "TP.MKNETHAR.M20",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "2. Net Değişim Genel Toplam, Net Değişim",
  "context_title": "2. Net Değişim Genel Toplam, Net Değişim",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_total",
  "status": "derived_input",
  "theme_ids": [
    "theme:portfolio-flows",
    "theme:foreign-ownership",
    "theme:swap-and-securities"
  ],
  "indicator_ids": [
    "derived:equity-plus-dibs-flow",
    "derived:portfolio-flow-total"
  ],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.MKNETHAR.M20",
    "title": "2. Net Değişim Genel Toplam",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_mknethar",
    "category": "YURT DIŞI YERLEŞİKLER MENKUL KIYMET PORTFÖYÜ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.MKNETHAR.M20\": [1, \"NET DEĞİŞİM GENEL TOPLAM (**)\"],",
    "tl_yp_menkul_kiymet_f = df_menkul_kiymet_com.loc[df_menkul_kiymet_com.index[0], \"TP_MKNETHAR_M20\"].astype(float)"
  ],
  "indicator_hints": [
    "derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin birlestirilmis net degisimi.",
    "derived:portfolio-flow-total: Hisse, DIBS ve ilgili destek tablolarindan portfoy akis toplami uretilir."
  ],
  "notes": ""
}
