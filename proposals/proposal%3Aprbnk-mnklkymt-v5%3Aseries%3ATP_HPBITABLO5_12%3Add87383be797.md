---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_12:dd87383be797
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_12:dd87383be797
title: Semantic proposal for TP.HPBITABLO5.12
status: approved
target_type: series
target_id: evds:TP.HPBITABLO5.12
ticker: TP.HPBITABLO5.12
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 2.Parite Etkisi (Yurt İçi Yerleşikler)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: parity_effect_input
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: dd87383be79736b9cc7c2fb05d67b9849c18797c
catalog_record_id: catalog:evds2:TP.HPBITABLO5.12
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO5.12
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları)
  context_title: B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları)
  frequency: weekly
  unit: Milyon ABD Doları
  role: parity_effect_input
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
    id: catalog:evds2:TP.HPBITABLO5.12
    title: 2.Parite Etkisi (Yurt İçi Yerleşikler)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo5
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO5.9'', ''TP.HPBITABLO5.10'', ''TP.HPBITABLO5.11'', ''TP.HPBITABLO5.12'','
  - '''TP_HPBITABLO5_12'': ''B. Parite Etkisi (Yurt İçi Yerleşikler)'','
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO5.12
promoted_memory_rule_id: memory:global-tp-hpbitablo5-12
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO5.12'
body: "# Semantic proposal for TP.HPBITABLO5.12\n\n## Target\nseries | evds:TP.HPBITABLO5.12\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n2.Parite Etkisi (Yurt İçi\
  \ Yerleşikler)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\n\
  weekly\n\n## Candidate Role\nparity_effect_input\n\n## Confidence\n0.9\n\n## Candidate\
  \ Themes\n- theme:portfolio-flows\n- theme:foreign-ownership\n- theme:swap-and-securities\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nSame ticker TP.HPBITABLO5.12 has another\
  \ proposal from notebook dth-blg-v7 with status review_pending. approved_series\
  \ is empty and matching_memory_rules is empty, indicating no prior global validation.\
  \ Heuristic source alone is insufficient for global approval without reconciling\
  \ pending conflicts.\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO5.12\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO5.12\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon\
  \ ABD Doları)\",\n  \"context_title\": \"B. Parite Etkisi (Yurt İçi Yerleşikler)\
  \ (Milyon ABD Doları)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Milyon ABD\
  \ Doları\",\n  \"role\": \"parity_effect_input\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO5.12\",\n    \"title\"\
  : \"2.Parite Etkisi (Yurt İçi Yerleşikler)\",\n    \"frequency\": \"weekly\",\n\
  \    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo5\",\n\
  \    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"\
  memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO5.9', 'TP.HPBITABLO5.10',\
  \ 'TP.HPBITABLO5.11', 'TP.HPBITABLO5.12',\",\n    \"'TP_HPBITABLO5_12': 'B. Parite\
  \ Etkisi (Yurt İçi Yerleşikler)',\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_HPBITABLO5_12%3Add87383be797.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO5.12

## Target
series | evds:TP.HPBITABLO5.12

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
2.Parite Etkisi (Yurt İçi Yerleşikler)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
parity_effect_input

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
Catalog source: catalog:evds2:TP.HPBITABLO5.12

## Evidence
{
  "ticker": "TP.HPBITABLO5.12",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları)",
  "context_title": "B. Parite Etkisi (Yurt İçi Yerleşikler) (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "parity_effect_input",
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
    "id": "catalog:evds2:TP.HPBITABLO5.12",
    "title": "2.Parite Etkisi (Yurt İçi Yerleşikler)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo5",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO5.9', 'TP.HPBITABLO5.10', 'TP.HPBITABLO5.11', 'TP.HPBITABLO5.12',",
    "'TP_HPBITABLO5_12': 'B. Parite Etkisi (Yurt İçi Yerleşikler)',"
  ],
  "indicator_hints": [],
  "notes": ""
}
