---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO5_12:30fc288bad0f
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO5_12:30fc288bad0f
title: Semantic proposal for TP.HPBITABLO5.12
status: approved
target_type: series
target_id: evds:TP.HPBITABLO5.12
ticker: TP.HPBITABLO5.12
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 2.Parite Etkisi (Yurt İçi Yerleşikler)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: parity_effect_input
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 30fc288bad0f7fb5dfa874961263597ff92f2ef6
catalog_record_id: catalog:evds2:TP.HPBITABLO5.12
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO5.12
  notebook_slug: dth-blg-v7
  official_series_name: Yabanci para mevduatta haftalik degisim ve parite etkisi
  context_title: Yabanci para mevduatta haftalik degisim ve parite etkisi
  frequency: weekly
  unit: milyon ABD doları
  role: parity_effect_input
  status: reported_output
  theme_ids:
  - theme:dth
  indicator_ids: []
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO5.12
    title: 2.Parite Etkisi (Yurt İçi Yerleşikler)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo5
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '["TP.HPBITABLO5.12"],'
  - 'dth_parite_etkisi.rename(columns={''TP_HPBITABLO5_12'': ''B. Parite Etkisi (Yurt
    İçi Yerleşikler)''}, inplace=True)'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO5.12
promoted_memory_rule_id: memory:global-tp-hpbitablo5-12
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO5.12'
body: "# Semantic proposal for TP.HPBITABLO5.12\n\n## Target\nseries | evds:TP.HPBITABLO5.12\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n2.Parite Etkisi (Yurt İçi Yerleşikler)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nparity_effect_input\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nSame ticker proposal exists in review_pending\
  \ status from different notebook; approved_series is empty.\n\n## Notes\nCatalog\
  \ source: catalog:evds2:TP.HPBITABLO5.12\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO5.12\"\
  ,\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\": \"Yabanci para\
  \ mevduatta haftalik degisim ve parite etkisi\",\n  \"context_title\": \"Yabanci\
  \ para mevduatta haftalik degisim ve parite etkisi\",\n  \"frequency\": \"weekly\"\
  ,\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"parity_effect_input\",\n  \"\
  status\": \"reported_output\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n  \"\
  indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO5.12\"\
  ,\n    \"title\": \"2.Parite Etkisi (Yurt İçi Yerleşikler)\",\n    \"frequency\"\
  : \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo5\"\
  ,\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"[\\\"TP.HPBITABLO5.12\\\
  \"],\",\n    \"dth_parite_etkisi.rename(columns={'TP_HPBITABLO5_12': 'B. Parite\
  \ Etkisi (Yurt İçi Yerleşikler)'}, inplace=True)\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO5_12%3A30fc288bad0f.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO5.12

## Target
series | evds:TP.HPBITABLO5.12

## Notebook
dth-blg-v7

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
- theme:dth

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
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "Yabanci para mevduatta haftalik degisim ve parite etkisi",
  "context_title": "Yabanci para mevduatta haftalik degisim ve parite etkisi",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "parity_effect_input",
  "status": "reported_output",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
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
    "[\"TP.HPBITABLO5.12\"],",
    "dth_parite_etkisi.rename(columns={'TP_HPBITABLO5_12': 'B. Parite Etkisi (Yurt İçi Yerleşikler)'}, inplace=True)"
  ],
  "indicator_hints": [],
  "notes": ""
}
