---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO4_2:020fc292118b
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO4_2:020fc292118b
title: Semantic proposal for TP.HPBITABLO4.2
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.2
ticker: TP.HPBITABLO4.2
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.1.Yurt İçi Yerleşikler
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs:
- derived:dth-share-in-total-deposits
- derived:dth-share-in-resident-deposits
candidate_formula_hint: 'derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2
  / evds:TP.HPBITABLO2.1'
confidence: 0.95
source: heuristic
evidence_fingerprint: 020fc292118b87bc76f084e098cba2129bc61e6a
catalog_record_id: catalog:evds2:TP.HPBITABLO4.2
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.2
  notebook_slug: dth-blg-v7
  official_series_name: A. Yurt İçi Yerleşikler (Milyon ABD Doları)
  context_title: A. Yurt İçi Yerleşikler (Milyon ABD Doları)
  frequency: weekly
  unit: Milyon ABD Doları
  role: currency_split_line
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids:
  - derived:dth-share-in-total-deposits
  - derived:dth-share-in-resident-deposits
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO4.2
    title: 1.1.Yurt İçi Yerleşikler
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO4.1'', ''TP.HPBITABLO4.2'', ''TP.HPBITABLO4.3'', ''TP.HPBITABLO4.4'','
  - '''TP.HPBITABLO4.17'', ''TP.HPBITABLO4.18'', ''TP.HPBITABLO4.19'', ''TP.HPBITABLO4.20'','
  - '''TP.HPBITABLO4.21'''
  - '''TP_HPBITABLO4_2'': ''A. Yurt İçi Yerleşikler'','
  - '''TP_HPBITABLO4_20'': ''C.d. Kıymetli Maden'','
  indicator_hints:
  - 'derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1'
  - 'derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.2'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.2
promoted_memory_rule_id: memory:global-tp-hpbitablo4-2
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.2'
body: "# Semantic proposal for TP.HPBITABLO4.2\n\n## Target\nseries | evds:TP.HPBITABLO4.2\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.Yurt İçi Yerleşikler\n\n##\
  \ Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\ncurrency_split_line\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:dth\n\
  \n## Candidate Indicator Inputs\n- derived:dth-share-in-total-deposits\n- derived:dth-share-in-resident-deposits\n\
  \n## Formula Hint\nderived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1\n\
  \n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nmatching_memory_rules\
  \ and approved_series are empty; notebook_slug present indicates potential notebook-specific\
  \ scoping\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO4.2\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.HPBITABLO4.2\",\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"\
  official_series_name\": \"A. Yurt İçi Yerleşikler (Milyon ABD Doları)\",\n  \"context_title\"\
  : \"A. Yurt İçi Yerleşikler (Milyon ABD Doları)\",\n  \"frequency\": \"weekly\"\
  ,\n  \"unit\": \"Milyon ABD Doları\",\n  \"role\": \"currency_split_line\",\n  \"\
  status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n  \"\
  indicator_ids\": [\n    \"derived:dth-share-in-total-deposits\",\n    \"derived:dth-share-in-resident-deposits\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\n  ],\n\
  \  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO4.2\",\n    \"\
  title\": \"1.1.Yurt İçi Yerleşikler\",\n    \"frequency\": \"weekly\",\n    \"unit\"\
  : \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo4\",\n    \"category\"\
  : \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\":\
  \ [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO4.1', 'TP.HPBITABLO4.2', 'TP.HPBITABLO4.3',\
  \ 'TP.HPBITABLO4.4',\",\n    \"'TP.HPBITABLO4.17', 'TP.HPBITABLO4.18', 'TP.HPBITABLO4.19',\
  \ 'TP.HPBITABLO4.20',\",\n    \"'TP.HPBITABLO4.21'\",\n    \"'TP_HPBITABLO4_2':\
  \ 'A. Yurt İçi Yerleşikler',\",\n    \"'TP_HPBITABLO4_20': 'C.d. Kıymetli Maden',\"\
  \n  ],\n  \"indicator_hints\": [\n    \"derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2\
  \ / evds:TP.HPBITABLO2.1\",\n    \"derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2\
  \ / evds:TP.HPBITABLO2.2\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO4_2%3A020fc292118b.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.2

## Target
series | evds:TP.HPBITABLO4.2

## Notebook
dth-blg-v7

## Candidate Title
1.1.Yurt İçi Yerleşikler

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
currency_split_line

## Confidence
0.95

## Candidate Themes
- theme:dth

## Candidate Indicator Inputs
- derived:dth-share-in-total-deposits
- derived:dth-share-in-resident-deposits

## Formula Hint
derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.HPBITABLO4.2

## Evidence
{
  "ticker": "TP.HPBITABLO4.2",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "A. Yurt İçi Yerleşikler (Milyon ABD Doları)",
  "context_title": "A. Yurt İçi Yerleşikler (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "currency_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [
    "derived:dth-share-in-total-deposits",
    "derived:dth-share-in-resident-deposits"
  ],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO4.2",
    "title": "1.1.Yurt İçi Yerleşikler",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO4.1', 'TP.HPBITABLO4.2', 'TP.HPBITABLO4.3', 'TP.HPBITABLO4.4',",
    "'TP.HPBITABLO4.17', 'TP.HPBITABLO4.18', 'TP.HPBITABLO4.19', 'TP.HPBITABLO4.20',",
    "'TP.HPBITABLO4.21'",
    "'TP_HPBITABLO4_2': 'A. Yurt İçi Yerleşikler',",
    "'TP_HPBITABLO4_20': 'C.d. Kıymetli Maden',"
  ],
  "indicator_hints": [
    "derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1",
    "derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.2"
  ],
  "notes": ""
}
