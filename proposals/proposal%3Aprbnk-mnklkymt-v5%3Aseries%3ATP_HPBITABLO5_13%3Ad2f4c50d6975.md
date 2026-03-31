---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_13:d2f4c50d6975
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_13:d2f4c50d6975
title: Semantic proposal for TP.HPBITABLO5.13
status: approved
target_type: series
target_id: evds:TP.HPBITABLO5.13
ticker: TP.HPBITABLO5.13
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 2.1.Gerçek Kişiler
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: owner_split_line
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: d2f4c50d6975d3c232d2c50a1d64a480b1c093e9
catalog_record_id: catalog:evds2:TP.HPBITABLO5.13
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO5.13
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: 1. Gerçek Kişiler (Milyon ABD Doları)
  context_title: B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1.
    Gerçek Kişiler (Milyon ABD Doları)
  frequency: weekly
  unit: Milyon ABD Doları
  role: owner_split_line
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
    id: catalog:evds2:TP.HPBITABLO5.13
    title: 2.1.Gerçek Kişiler
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo5
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO5.13'', ''TP.HPBITABLO5.14'', ''TP.HPBITABLO5.15'', ''TP.HPBITABLO5.16'','
  - '''TP_HPBITABLO5_13'': ''B1. Gerçek Kişiler'','
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO5.13
promoted_memory_rule_id: memory:global-tp-hpbitablo5-13
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO5.13'
body: "# Semantic proposal for TP.HPBITABLO5.13\n\n## Target\nseries | evds:TP.HPBITABLO5.13\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n2.1.Gerçek Kişiler\n\n##\
  \ Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nowner_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nEmpty matching_memory_rules and approved_series provide\
  \ no evidence for global safety; source is heuristic.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.HPBITABLO5.13\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO5.13\"\
  ,\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\",\n  \"official_series_name\": \"1.\
  \ Gerçek Kişiler (Milyon ABD Doları)\",\n  \"context_title\": \"B. Parite Etkisi\
  \ (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları)\"\
  ,\n  \"frequency\": \"weekly\",\n  \"unit\": \"Milyon ABD Doları\",\n  \"role\"\
  : \"owner_split_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n\
  \    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\",\n    \"theme:swap-and-securities\"\
  \n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:prbnk-weekly-zip\"\
  ,\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"catalog_record\": {\n    \"id\": \"\
  catalog:evds2:TP.HPBITABLO5.13\",\n    \"title\": \"2.1.Gerçek Kişiler\",\n    \"\
  frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_hpbitablo5\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK)\
  \ (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO5.13',\
  \ 'TP.HPBITABLO5.14', 'TP.HPBITABLO5.15', 'TP.HPBITABLO5.16',\",\n    \"'TP_HPBITABLO5_13':\
  \ 'B1. Gerçek Kişiler',\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n\
  }\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_HPBITABLO5_13%3Ad2f4c50d6975.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO5.13

## Target
series | evds:TP.HPBITABLO5.13

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
2.1.Gerçek Kişiler

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
owner_split_line

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
Catalog source: catalog:evds2:TP.HPBITABLO5.13

## Evidence
{
  "ticker": "TP.HPBITABLO5.13",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "1. Gerçek Kişiler (Milyon ABD Doları)",
  "context_title": "B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "owner_split_line",
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
    "id": "catalog:evds2:TP.HPBITABLO5.13",
    "title": "2.1.Gerçek Kişiler",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo5",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO5.13', 'TP.HPBITABLO5.14', 'TP.HPBITABLO5.15', 'TP.HPBITABLO5.16',",
    "'TP_HPBITABLO5_13': 'B1. Gerçek Kişiler',"
  ],
  "indicator_hints": [],
  "notes": ""
}
