---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO4_3:f7bb0f2a4b90
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO4_3:f7bb0f2a4b90
title: Semantic proposal for TP.HPBITABLO4.3
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.3
ticker: TP.HPBITABLO4.3
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.1.1.Gerçek Kişiler
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: owner_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: f7bb0f2a4b90cf75e9fdf45bdb673fd009a8dda5
catalog_record_id: catalog:evds2:TP.HPBITABLO4.3
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.3
  notebook_slug: dth-blg-v7
  official_series_name: 1. Gerçek Kişiler (Milyon ABD Doları)
  context_title: A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon
    ABD Doları)
  frequency: weekly
  unit: Milyon ABD Doları
  role: owner_split_line
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids: []
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO4.3
    title: 1.1.1.Gerçek Kişiler
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO4.1'', ''TP.HPBITABLO4.2'', ''TP.HPBITABLO4.3'', ''TP.HPBITABLO4.4'','
  - '''TP_HPBITABLO4_3'': ''A.1. Gerçek Kişiler'','
  - df_mevduat["Gerçek Kişiler"] = df_mevduat["TP_HPBITABLO4_3"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.3
promoted_memory_rule_id: memory:global-tp-hpbitablo4-3
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.3'
body: "# Semantic proposal for TP.HPBITABLO4.3\n\n## Target\nseries | evds:TP.HPBITABLO4.3\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.1.Gerçek Kişiler\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  owner_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\n##\
  \ Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n\
  ## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO4.3\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO4.3\",\n  \"notebook_slug\": \"dth-blg-v7\"\
  ,\n  \"official_series_name\": \"1. Gerçek Kişiler (Milyon ABD Doları)\",\n  \"\
  context_title\": \"A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler\
  \ (Milyon ABD Doları)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Milyon ABD\
  \ Doları\",\n  \"role\": \"owner_split_line\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:dth-old-series-excel\"\n  ],\n  \"catalog_record\": {\n    \"\
  id\": \"catalog:evds2:TP.HPBITABLO4.3\",\n    \"title\": \"1.1.1.Gerçek Kişiler\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_hpbitablo4\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ\
  \ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n\
  \    \"'TP.HPBITABLO4.1', 'TP.HPBITABLO4.2', 'TP.HPBITABLO4.3', 'TP.HPBITABLO4.4',\"\
  ,\n    \"'TP_HPBITABLO4_3': 'A.1. Gerçek Kişiler',\",\n    \"df_mevduat[\\\"Gerçek\
  \ Kişiler\\\"] = df_mevduat[\\\"TP_HPBITABLO4_3\\\"]\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO4_3%3Af7bb0f2a4b90.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.3

## Target
series | evds:TP.HPBITABLO4.3

## Notebook
dth-blg-v7

## Candidate Title
1.1.1.Gerçek Kişiler

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
owner_split_line

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
Catalog source: catalog:evds2:TP.HPBITABLO4.3

## Evidence
{
  "ticker": "TP.HPBITABLO4.3",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "1. Gerçek Kişiler (Milyon ABD Doları)",
  "context_title": "A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "owner_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO4.3",
    "title": "1.1.1.Gerçek Kişiler",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO4.1', 'TP.HPBITABLO4.2', 'TP.HPBITABLO4.3', 'TP.HPBITABLO4.4',",
    "'TP_HPBITABLO4_3': 'A.1. Gerçek Kişiler',",
    "df_mevduat[\"Gerçek Kişiler\"] = df_mevduat[\"TP_HPBITABLO4_3\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
