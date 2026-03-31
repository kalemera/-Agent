---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_1:5132bf3288ee
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_1:5132bf3288ee
title: Semantic proposal for TP.HPBITABLO2.1
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.1
ticker: TP.HPBITABLO2.1
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.TOPLAM MEVDUAT
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs:
- derived:dth-share-in-total-deposits
- derived:resident-deposit-share-in-total-deposits
candidate_formula_hint: 'derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2
  / evds:TP.HPBITABLO2.1'
confidence: 0.95
source: heuristic
evidence_fingerprint: 5132bf3288eef69c316738a21b04c094c87be7c2
catalog_record_id: catalog:evds2:TP.HPBITABLO2.1
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.1
  notebook_slug: dth-blg-v7
  official_series_name: A. TOPLAM MEVDUAT (Bin TL)
  context_title: A. TOPLAM MEVDUAT (Bin TL)
  frequency: weekly
  unit: Bin TL
  role: stock_total
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids:
  - derived:dth-share-in-total-deposits
  - derived:resident-deposit-share-in-total-deposits
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.1
    title: 1.TOPLAM MEVDUAT
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.1'', ''TP.HPBITABLO2.2'', ''TP.HPBITABLO2.3'', ''TP.HPBITABLO2.3'','
  - '''TP.HPBITABLO2.8'', ''TP.HPBITABLO2.10'', ''TP.HPBITABLO2.11'', ''TP.HPBITABLO2.12'','
  - '''TP.HPBITABLO2.13'', ''TP.HPBITABLO2.14'', ''TP.HPBITABLO2.15'', ''TP.HPBITABLO2.16'','
  - '''TP.HPBITABLO2.17'', ''TP.HPBITABLO2.18'', ''TP.HPBITABLO2.19'', ''TP.HPBITABLO2.20'','
  - '''TP_HPBITABLO2_13'': "",'
  indicator_hints:
  - 'derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1'
  - 'derived:resident-deposit-share-in-total-deposits: evds:TP.HPBITABLO2.2 / evds:TP.HPBITABLO2.1'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.1
promoted_memory_rule_id: memory:global-tp-hpbitablo2-1
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.1'
body: "# Semantic proposal for TP.HPBITABLO2.1\n\n## Target\nseries | evds:TP.HPBITABLO2.1\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.TOPLAM MEVDUAT\n\n## Candidate\
  \ Unit\nbin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\nstock_total\n\
  \n## Confidence\n0.95\n\n## Candidate Themes\n- theme:dth\n\n## Candidate Indicator\
  \ Inputs\n- derived:dth-share-in-total-deposits\n- derived:resident-deposit-share-in-total-deposits\n\
  \n## Formula Hint\nderived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1\n\
  \n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.1\n\n\
  ## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO2.1\",\n  \"notebook_slug\": \"dth-blg-v7\"\
  ,\n  \"official_series_name\": \"A. TOPLAM MEVDUAT (Bin TL)\",\n  \"context_title\"\
  : \"A. TOPLAM MEVDUAT (Bin TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"\
  Bin TL\",\n  \"role\": \"stock_total\",\n  \"status\": \"derived_input\",\n  \"\
  theme_ids\": [\n    \"theme:dth\"\n  ],\n  \"indicator_ids\": [\n    \"derived:dth-share-in-total-deposits\"\
  ,\n    \"derived:resident-deposit-share-in-total-deposits\"\n  ],\n  \"source_dependency_ids\"\
  : [\n    \"source:dth-old-series-excel\"\n  ],\n  \"catalog_record\": {\n    \"\
  id\": \"catalog:evds2:TP.HPBITABLO2.1\",\n    \"title\": \"1.TOPLAM MEVDUAT\",\n\
  \    \"frequency\": \"weekly\",\n    \"unit\": \"bin TL\",\n    \"data_group\":\
  \ \"bie_hpbitablo2\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK)\
  \ (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO2.1',\
  \ 'TP.HPBITABLO2.2', 'TP.HPBITABLO2.3', 'TP.HPBITABLO2.3',\",\n    \"'TP.HPBITABLO2.8',\
  \ 'TP.HPBITABLO2.10', 'TP.HPBITABLO2.11', 'TP.HPBITABLO2.12',\",\n    \"'TP.HPBITABLO2.13',\
  \ 'TP.HPBITABLO2.14', 'TP.HPBITABLO2.15', 'TP.HPBITABLO2.16',\",\n    \"'TP.HPBITABLO2.17',\
  \ 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19', 'TP.HPBITABLO2.20',\",\n    \"'TP_HPBITABLO2_13':\
  \ \\\"\\\",\"\n  ],\n  \"indicator_hints\": [\n    \"derived:dth-share-in-total-deposits:\
  \ evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1\",\n    \"derived:resident-deposit-share-in-total-deposits:\
  \ evds:TP.HPBITABLO2.2 / evds:TP.HPBITABLO2.1\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_1%3A5132bf3288ee.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.1

## Target
series | evds:TP.HPBITABLO2.1

## Notebook
dth-blg-v7

## Candidate Title
1.TOPLAM MEVDUAT

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
stock_total

## Confidence
0.95

## Candidate Themes
- theme:dth

## Candidate Indicator Inputs
- derived:dth-share-in-total-deposits
- derived:resident-deposit-share-in-total-deposits

## Formula Hint
derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.HPBITABLO2.1

## Evidence
{
  "ticker": "TP.HPBITABLO2.1",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "A. TOPLAM MEVDUAT (Bin TL)",
  "context_title": "A. TOPLAM MEVDUAT (Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "stock_total",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [
    "derived:dth-share-in-total-deposits",
    "derived:resident-deposit-share-in-total-deposits"
  ],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.1",
    "title": "1.TOPLAM MEVDUAT",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.1', 'TP.HPBITABLO2.2', 'TP.HPBITABLO2.3', 'TP.HPBITABLO2.3',",
    "'TP.HPBITABLO2.8', 'TP.HPBITABLO2.10', 'TP.HPBITABLO2.11', 'TP.HPBITABLO2.12',",
    "'TP.HPBITABLO2.13', 'TP.HPBITABLO2.14', 'TP.HPBITABLO2.15', 'TP.HPBITABLO2.16',",
    "'TP.HPBITABLO2.17', 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19', 'TP.HPBITABLO2.20',",
    "'TP_HPBITABLO2_13': \"\","
  ],
  "indicator_hints": [
    "derived:dth-share-in-total-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.1",
    "derived:resident-deposit-share-in-total-deposits: evds:TP.HPBITABLO2.2 / evds:TP.HPBITABLO2.1"
  ],
  "notes": ""
}
