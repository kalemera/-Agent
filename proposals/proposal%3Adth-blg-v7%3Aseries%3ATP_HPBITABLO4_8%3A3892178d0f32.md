---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO4_8:3892178d0f32
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO4_8:3892178d0f32
title: Semantic proposal for TP.HPBITABLO4.8
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.8
ticker: TP.HPBITABLO4.8
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.1.2.Tüzel Kişiler
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: owner_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 3892178d0f328dc414ef4be52fb183c1dbe1457f
catalog_record_id: catalog:evds2:TP.HPBITABLO4.8
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.8
  notebook_slug: dth-blg-v7
  official_series_name: 2. Tüzel Kişiler (Milyon ABD Doları)
  context_title: A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon
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
    id: catalog:evds2:TP.HPBITABLO4.8
    title: 1.1.2.Tüzel Kişiler
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO4.5'', ''TP.HPBITABLO4.6'', ''TP.HPBITABLO4.7'', ''TP.HPBITABLO4.8'','
  - '''TP_HPBITABLO4_8'': ''A.2. Tüzel Kişiler'','
  - df_mevduat["Tüzel Kişiler"] = df_mevduat["TP_HPBITABLO4_8"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.8
promoted_memory_rule_id: memory:global-tp-hpbitablo4-8
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.8'
body: "# Semantic proposal for TP.HPBITABLO4.8\n\n## Target\nseries | evds:TP.HPBITABLO4.8\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.2.Tüzel Kişiler\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  owner_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\n##\
  \ Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n\
  ## Approval Mode\n-\n\n## Approval Reason\nNo matching memory rules or approved\
  \ series found to confirm global safety; source is heuristic.\n\n## Notes\nCatalog\
  \ source: catalog:evds2:TP.HPBITABLO4.8\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO4.8\"\
  ,\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\": \"2. Tüzel\
  \ Kişiler (Milyon ABD Doları)\",\n  \"context_title\": \"A. Yurt İçi Yerleşikler\
  \ (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Milyon ABD Doları\",\n  \"role\": \"owner_split_line\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n\
  \  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO4.8\",\n\
  \    \"title\": \"1.1.2.Tüzel Kişiler\",\n    \"frequency\": \"weekly\",\n    \"\
  unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo4\",\n    \"\
  category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\"\
  : [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO4.5', 'TP.HPBITABLO4.6', 'TP.HPBITABLO4.7',\
  \ 'TP.HPBITABLO4.8',\",\n    \"'TP_HPBITABLO4_8': 'A.2. Tüzel Kişiler',\",\n   \
  \ \"df_mevduat[\\\"Tüzel Kişiler\\\"] = df_mevduat[\\\"TP_HPBITABLO4_8\\\"]\"\n\
  \  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO4_8%3A3892178d0f32.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.8

## Target
series | evds:TP.HPBITABLO4.8

## Notebook
dth-blg-v7

## Candidate Title
1.1.2.Tüzel Kişiler

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
Catalog source: catalog:evds2:TP.HPBITABLO4.8

## Evidence
{
  "ticker": "TP.HPBITABLO4.8",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "2. Tüzel Kişiler (Milyon ABD Doları)",
  "context_title": "A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları)",
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
    "id": "catalog:evds2:TP.HPBITABLO4.8",
    "title": "1.1.2.Tüzel Kişiler",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO4.5', 'TP.HPBITABLO4.6', 'TP.HPBITABLO4.7', 'TP.HPBITABLO4.8',",
    "'TP_HPBITABLO4_8': 'A.2. Tüzel Kişiler',",
    "df_mevduat[\"Tüzel Kişiler\"] = df_mevduat[\"TP_HPBITABLO4_8\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
