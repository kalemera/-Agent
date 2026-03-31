---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO4_11:ca5f91266efe
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO4_11:ca5f91266efe
title: Semantic proposal for TP.HPBITABLO4.11
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.11
ticker: TP.HPBITABLO4.11
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.1.2.c.Diğer - ABD Doları Karşılığı
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: ca5f91266efe55ae82cb48a770df63632e16131f
catalog_record_id: catalog:evds2:TP.HPBITABLO4.11
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.11
  notebook_slug: dth-blg-v7
  official_series_name: c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)
  context_title: A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon
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
    id: catalog:evds2:TP.HPBITABLO4.11
    title: 1.1.2.c.Diğer - ABD Doları Karşılığı
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO4.9'', ''TP.HPBITABLO4.10'', ''TP.HPBITABLO4.11'', ''TP.HPBITABLO4.12'','
  - '''TP_HPBITABLO4_11'': ''A.2.c. Diğer'','
  - df_mevduat["Diğer"] = df_mevduat["TP_HPBITABLO4_6"] + df_mevduat["TP_HPBITABLO4_11"]
  - df_mevduat["Diğer (Tüzel Kişiler)"] = df_mevduat["TP_HPBITABLO4_11"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.11
promoted_memory_rule_id: memory:global-tp-hpbitablo4-11
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.11'
body: "# Semantic proposal for TP.HPBITABLO4.11\n\n## Target\nseries | evds:TP.HPBITABLO4.11\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.2.c.Diğer - ABD Doları Karşılığı\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\ncurrency_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.HPBITABLO4.11\n\n## Evidence\n{\n  \"\
  ticker\": \"TP.HPBITABLO4.11\",\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\"\
  : \"c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)\",\n  \"context_title\"\
  : \"A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları)\
  \ / c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)\",\n  \"frequency\": \"\
  weekly\",\n  \"unit\": \"Milyon ABD Doları\",\n  \"role\": \"currency_split_line\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n\
  \  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO4.11\"\
  ,\n    \"title\": \"1.1.2.c.Diğer - ABD Doları Karşılığı\",\n    \"frequency\":\
  \ \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo4\"\
  ,\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO4.9', 'TP.HPBITABLO4.10',\
  \ 'TP.HPBITABLO4.11', 'TP.HPBITABLO4.12',\",\n    \"'TP_HPBITABLO4_11': 'A.2.c.\
  \ Diğer',\",\n    \"df_mevduat[\\\"Diğer\\\"] = df_mevduat[\\\"TP_HPBITABLO4_6\\\
  \"] + df_mevduat[\\\"TP_HPBITABLO4_11\\\"]\",\n    \"df_mevduat[\\\"Diğer (Tüzel\
  \ Kişiler)\\\"] = df_mevduat[\\\"TP_HPBITABLO4_11\\\"]\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO4_11%3Aca5f91266efe.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.11

## Target
series | evds:TP.HPBITABLO4.11

## Notebook
dth-blg-v7

## Candidate Title
1.1.2.c.Diğer - ABD Doları Karşılığı

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
Catalog source: catalog:evds2:TP.HPBITABLO4.11

## Evidence
{
  "ticker": "TP.HPBITABLO4.11",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)",
  "context_title": "A. Yurt İçi Yerleşikler (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / c. Diğer - ABD Doları Karşılığı (Milyon ABD Doları)",
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
    "id": "catalog:evds2:TP.HPBITABLO4.11",
    "title": "1.1.2.c.Diğer - ABD Doları Karşılığı",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO4.9', 'TP.HPBITABLO4.10', 'TP.HPBITABLO4.11', 'TP.HPBITABLO4.12',",
    "'TP_HPBITABLO4_11': 'A.2.c. Diğer',",
    "df_mevduat[\"Diğer\"] = df_mevduat[\"TP_HPBITABLO4_6\"] + df_mevduat[\"TP_HPBITABLO4_11\"]",
    "df_mevduat[\"Diğer (Tüzel Kişiler)\"] = df_mevduat[\"TP_HPBITABLO4_11\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
