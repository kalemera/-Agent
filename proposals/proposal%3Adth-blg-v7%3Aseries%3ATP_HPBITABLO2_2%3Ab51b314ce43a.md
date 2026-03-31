---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_2:b51b314ce43a
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_2:b51b314ce43a
title: Semantic proposal for TP.HPBITABLO2.2
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.2
ticker: TP.HPBITABLO2.2
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.1.Yurt İçi Yerleşikler
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: owner_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs:
- derived:dth-share-in-resident-deposits
- derived:resident-deposit-share-in-total-deposits
candidate_formula_hint: 'derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2
  / evds:TP.HPBITABLO2.2'
confidence: 0.95
source: heuristic
evidence_fingerprint: b51b314ce43aacb4d588305725a8d1c1a270ea93
catalog_record_id: catalog:evds2:TP.HPBITABLO2.2
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.2
  notebook_slug: dth-blg-v7
  official_series_name: 1. Yurt İçi Yerleşikler (Bin TL)
  context_title: A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL)
  frequency: weekly
  unit: Bin TL
  role: owner_split_line
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids:
  - derived:dth-share-in-resident-deposits
  - derived:resident-deposit-share-in-total-deposits
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.2
    title: 1.1.Yurt İçi Yerleşikler
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.1'', ''TP.HPBITABLO2.2'', ''TP.HPBITABLO2.3'', ''TP.HPBITABLO2.3'','
  - '''TP.HPBITABLO2.17'', ''TP.HPBITABLO2.18'', ''TP.HPBITABLO2.19'', ''TP.HPBITABLO2.20'','
  - '''TP.HPBITABLO2.21'', ''TP.HPBITABLO2.22'', ''TP.HPBITABLO2.23'', ''TP.HPBITABLO2.24'','
  - '''TP.HPBITABLO2.28'', ''TP.HPBITABLO2.32'', ''TP.HPBITABLO2.33'', ''TP.HPBITABLO2.34'''
  - '''TP_HPBITABLO2_2'': "",'
  indicator_hints:
  - 'derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.2'
  - 'derived:resident-deposit-share-in-total-deposits: evds:TP.HPBITABLO2.2 / evds:TP.HPBITABLO2.1'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.2
promoted_memory_rule_id: memory:global-tp-hpbitablo2-2
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.2'
body: "# Semantic proposal for TP.HPBITABLO2.2\n\n## Target\nseries | evds:TP.HPBITABLO2.2\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.Yurt İçi Yerleşikler\n\n##\
  \ Candidate Unit\nbin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  owner_split_line\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:dth\n\n\
  ## Candidate Indicator Inputs\n- derived:dth-share-in-resident-deposits\n- derived:resident-deposit-share-in-total-deposits\n\
  \n## Formula Hint\nderived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2\
  \ / evds:TP.HPBITABLO2.2\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval\
  \ Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.2\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.HPBITABLO2.2\",\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"\
  official_series_name\": \"1. Yurt İçi Yerleşikler (Bin TL)\",\n  \"context_title\"\
  : \"A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"owner_split_line\",\n  \"\
  status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n  \"\
  indicator_ids\": [\n    \"derived:dth-share-in-resident-deposits\",\n    \"derived:resident-deposit-share-in-total-deposits\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\n  ],\n\
  \  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO2.2\",\n    \"\
  title\": \"1.1.Yurt İçi Yerleşikler\",\n    \"frequency\": \"weekly\",\n    \"unit\"\
  : \"bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\": \"PARA\
  \ VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n \
  \ \"source_snippets\": [\n    \"'TP.HPBITABLO2.1', 'TP.HPBITABLO2.2', 'TP.HPBITABLO2.3',\
  \ 'TP.HPBITABLO2.3',\",\n    \"'TP.HPBITABLO2.17', 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19',\
  \ 'TP.HPBITABLO2.20',\",\n    \"'TP.HPBITABLO2.21', 'TP.HPBITABLO2.22', 'TP.HPBITABLO2.23',\
  \ 'TP.HPBITABLO2.24',\",\n    \"'TP.HPBITABLO2.28', 'TP.HPBITABLO2.32', 'TP.HPBITABLO2.33',\
  \ 'TP.HPBITABLO2.34'\",\n    \"'TP_HPBITABLO2_2': \\\"\\\",\"\n  ],\n  \"indicator_hints\"\
  : [\n    \"derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.2\"\
  ,\n    \"derived:resident-deposit-share-in-total-deposits: evds:TP.HPBITABLO2.2\
  \ / evds:TP.HPBITABLO2.1\"\n  ],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_2%3Ab51b314ce43a.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.2

## Target
series | evds:TP.HPBITABLO2.2

## Notebook
dth-blg-v7

## Candidate Title
1.1.Yurt İçi Yerleşikler

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
owner_split_line

## Confidence
0.95

## Candidate Themes
- theme:dth

## Candidate Indicator Inputs
- derived:dth-share-in-resident-deposits
- derived:resident-deposit-share-in-total-deposits

## Formula Hint
derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.2

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.HPBITABLO2.2

## Evidence
{
  "ticker": "TP.HPBITABLO2.2",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "1. Yurt İçi Yerleşikler (Bin TL)",
  "context_title": "A. TOPLAM MEVDUAT (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "owner_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [
    "derived:dth-share-in-resident-deposits",
    "derived:resident-deposit-share-in-total-deposits"
  ],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.2",
    "title": "1.1.Yurt İçi Yerleşikler",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.1', 'TP.HPBITABLO2.2', 'TP.HPBITABLO2.3', 'TP.HPBITABLO2.3',",
    "'TP.HPBITABLO2.17', 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19', 'TP.HPBITABLO2.20',",
    "'TP.HPBITABLO2.21', 'TP.HPBITABLO2.22', 'TP.HPBITABLO2.23', 'TP.HPBITABLO2.24',",
    "'TP.HPBITABLO2.28', 'TP.HPBITABLO2.32', 'TP.HPBITABLO2.33', 'TP.HPBITABLO2.34'",
    "'TP_HPBITABLO2_2': \"\","
  ],
  "indicator_hints": [
    "derived:dth-share-in-resident-deposits: evds:TP.HPBITABLO4.2 / evds:TP.HPBITABLO2.2",
    "derived:resident-deposit-share-in-total-deposits: evds:TP.HPBITABLO2.2 / evds:TP.HPBITABLO2.1"
  ],
  "notes": ""
}
