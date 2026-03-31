---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO4_6:50007c1c4f43
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO4_6:50007c1c4f43
title: Semantic proposal for TP.HPBITABLO4.6
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.6
ticker: TP.HPBITABLO4.6
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.1.1.c.Diğer - ABD Doları Karşılığı
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 50007c1c4f43febe3716f97bf93b28b731b60c60
catalog_record_id: catalog:evds2:TP.HPBITABLO4.6
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.6
  notebook_slug: dth-blg-v7
  official_series_name: c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)
  context_title: A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon
    ABD Doları) / c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)
  frequency: weekly
  unit: Milyon ABD Doları
  role: currency_split_line
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids: []
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO4.6
    title: 1.1.1.c.Diğer - ABD Doları Karşılığı
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO4.5'', ''TP.HPBITABLO4.6'', ''TP.HPBITABLO4.7'', ''TP.HPBITABLO4.8'','
  - '''TP_HPBITABLO4_6'': ''A.1.c. Diğer'','
  - df_mevduat["Diğer"] = df_mevduat["TP_HPBITABLO4_6"] + df_mevduat["TP_HPBITABLO4_11"]
  - df_mevduat["Diğer (Gerçek Kişiler)"] = df_mevduat["TP_HPBITABLO4_6"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.6
promoted_memory_rule_id: memory:global-tp-hpbitablo4-6
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.6'
body: "# Semantic proposal for TP.HPBITABLO4.6\n\n## Target\nseries | evds:TP.HPBITABLO4.6\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.1.c.Diğer - ABD Doları Karşılığı\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\ncurrency_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nInsufficient evidence for global safety:\
  \ matching_memory_rules and approved_series are empty\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.HPBITABLO4.6\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO4.6\"\
  ,\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\": \"c. Diğer\
  \ - ABD Doları Karşılığı (Milyon ABD Doları)\",\n  \"context_title\": \"A. Yurt\
  \ İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) /\
  \ c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)\",\n  \"frequency\": \"weekly\"\
  ,\n  \"unit\": \"Milyon ABD Doları\",\n  \"role\": \"currency_split_line\",\n  \"\
  status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n  \"\
  indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO4.6\",\n\
  \    \"title\": \"1.1.1.c.Diğer - ABD Doları Karşılığı\",\n    \"frequency\": \"\
  weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo4\"\
  ,\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO4.5', 'TP.HPBITABLO4.6',\
  \ 'TP.HPBITABLO4.7', 'TP.HPBITABLO4.8',\",\n    \"'TP_HPBITABLO4_6': 'A.1.c. Diğer',\"\
  ,\n    \"df_mevduat[\\\"Diğer\\\"] = df_mevduat[\\\"TP_HPBITABLO4_6\\\"] + df_mevduat[\\\
  \"TP_HPBITABLO4_11\\\"]\",\n    \"df_mevduat[\\\"Diğer (Gerçek Kişiler)\\\"] = df_mevduat[\\\
  \"TP_HPBITABLO4_6\\\"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n\
  }\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO4_6%3A50007c1c4f43.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.6

## Target
series | evds:TP.HPBITABLO4.6

## Notebook
dth-blg-v7

## Candidate Title
1.1.1.c.Diğer - ABD Doları Karşılığı

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
currency_split_line

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
Catalog source: catalog:evds2:TP.HPBITABLO4.6

## Evidence
{
  "ticker": "TP.HPBITABLO4.6",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)",
  "context_title": "A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "currency_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO4.6",
    "title": "1.1.1.c.Diğer - ABD Doları Karşılığı",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO4.5', 'TP.HPBITABLO4.6', 'TP.HPBITABLO4.7', 'TP.HPBITABLO4.8',",
    "'TP_HPBITABLO4_6': 'A.1.c. Diğer',",
    "df_mevduat[\"Diğer\"] = df_mevduat[\"TP_HPBITABLO4_6\"] + df_mevduat[\"TP_HPBITABLO4_11\"]",
    "df_mevduat[\"Diğer (Gerçek Kişiler)\"] = df_mevduat[\"TP_HPBITABLO4_6\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
