---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO4_9:b2880e08f339
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO4_9:b2880e08f339
title: Semantic proposal for TP.HPBITABLO4.9
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.9
ticker: TP.HPBITABLO4.9
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.1.2.a.ABD Doları
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: b2880e08f339b07bb921fc86d01d44df91a70e3f
catalog_record_id: catalog:evds2:TP.HPBITABLO4.9
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.9
  notebook_slug: dth-blg-v7
  official_series_name: a. ABD Doları (Milyon ABD Doları)
  context_title: A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon
    ABD Doları) / a. ABD Doları (Milyon ABD Doları)
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
    id: catalog:evds2:TP.HPBITABLO4.9
    title: 1.1.2.a.ABD Doları
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO4.9'', ''TP.HPBITABLO4.10'', ''TP.HPBITABLO4.11'', ''TP.HPBITABLO4.12'','
  - '''TP_HPBITABLO4_9'': ''A.2.a. ABD Doları'','
  - df_mevduat["Dolar"] = df_mevduat["TP_HPBITABLO4_4"] + df_mevduat["TP_HPBITABLO4_9"]
  - df_mevduat["Dolar (Tüzel Kişiler)"] = df_mevduat["TP_HPBITABLO4_9"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.9
promoted_memory_rule_id: memory:global-tp-hpbitablo4-9
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.9'
body: "# Semantic proposal for TP.HPBITABLO4.9\n\n## Target\nseries | evds:TP.HPBITABLO4.9\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.2.a.ABD Doları\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  currency_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\n\
  ## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\napproved_series and matching_memory_rules\
  \ are empty, providing insufficient evidence for global safety.\n\n## Notes\nCatalog\
  \ source: catalog:evds2:TP.HPBITABLO4.9\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO4.9\"\
  ,\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\": \"a. ABD Doları\
  \ (Milyon ABD Doları)\",\n  \"context_title\": \"A. Yurt İçi Yerleşikler (Milyon\
  \ ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / a. ABD Doları (Milyon ABD\
  \ Doları)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Milyon ABD Doları\",\n\
  \  \"role\": \"currency_split_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:dth\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:dth-old-series-excel\"\n  ],\n  \"catalog_record\": {\n    \"\
  id\": \"catalog:evds2:TP.HPBITABLO4.9\",\n    \"title\": \"1.1.2.a.ABD Doları\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_hpbitablo4\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ\
  \ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n\
  \    \"'TP.HPBITABLO4.9', 'TP.HPBITABLO4.10', 'TP.HPBITABLO4.11', 'TP.HPBITABLO4.12',\"\
  ,\n    \"'TP_HPBITABLO4_9': 'A.2.a. ABD Doları',\",\n    \"df_mevduat[\\\"Dolar\\\
  \"] = df_mevduat[\\\"TP_HPBITABLO4_4\\\"] + df_mevduat[\\\"TP_HPBITABLO4_9\\\"]\"\
  ,\n    \"df_mevduat[\\\"Dolar (Tüzel Kişiler)\\\"] = df_mevduat[\\\"TP_HPBITABLO4_9\\\
  \"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO4_9%3Ab2880e08f339.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.9

## Target
series | evds:TP.HPBITABLO4.9

## Notebook
dth-blg-v7

## Candidate Title
1.1.2.a.ABD Doları

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
Catalog source: catalog:evds2:TP.HPBITABLO4.9

## Evidence
{
  "ticker": "TP.HPBITABLO4.9",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "a. ABD Doları (Milyon ABD Doları)",
  "context_title": "A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / a. ABD Doları (Milyon ABD Doları)",
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
    "id": "catalog:evds2:TP.HPBITABLO4.9",
    "title": "1.1.2.a.ABD Doları",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO4.9', 'TP.HPBITABLO4.10', 'TP.HPBITABLO4.11', 'TP.HPBITABLO4.12',",
    "'TP_HPBITABLO4_9': 'A.2.a. ABD Doları',",
    "df_mevduat[\"Dolar\"] = df_mevduat[\"TP_HPBITABLO4_4\"] + df_mevduat[\"TP_HPBITABLO4_9\"]",
    "df_mevduat[\"Dolar (Tüzel Kişiler)\"] = df_mevduat[\"TP_HPBITABLO4_9\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
