---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO1_19:f82221d7d90c
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO1_19:f82221d7d90c
title: Semantic proposal for TP.HPBITABLO1.19
status: approved
target_type: series
target_id: evds:TP.HPBITABLO1.19
ticker: TP.HPBITABLO1.19
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 3.1.Repo
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: f82221d7d90c31cef833c450171aaf339c29634a
catalog_record_id: catalog:evds2:TP.HPBITABLO1.19
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO1.19
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Repo (Bin TL)
  context_title: Repo (Bin TL)
  frequency: weekly
  unit: Bin TL
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:resident-financial-assets
  - theme:resident-securities
  - theme:resident-deposits
  indicator_ids: []
  source_dependency_ids:
  - source:yiyrlsk-mkk-hisse-manual
  - source:yiyrlsk-mkk-fon-manual
  - source:yiyrlsk-vap-scrape-attempt
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO1.19
    title: 3.1.Repo
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo1
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO1.19'', ''TP.HPBITABLO1.20'', ''TP.HPBITABLO1.21'', #repo - para
    arzı'
  - '''TP_HPBITABLO1_19'': ''Repo*'','
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO1.19
promoted_memory_rule_id: memory:global-tp-hpbitablo1-19
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO1.19'
body: "# Semantic proposal for TP.HPBITABLO1.19\n\n## Target\nseries | evds:TP.HPBITABLO1.19\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n3.1.Repo\n\n## Candidate\
  \ Unit\nbin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\nbalance_sheet_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n\
  - theme:resident-securities\n- theme:resident-deposits\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.HPBITABLO1.19\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO1.19\"\
  ,\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\":\
  \ \"Repo (Bin TL)\",\n  \"context_title\": \"Repo (Bin TL)\",\n  \"frequency\":\
  \ \"weekly\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"balance_sheet_line\",\n  \"\
  status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO1.19\"\
  ,\n    \"title\": \"3.1.Repo\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  bin TL\",\n    \"data_group\": \"bie_hpbitablo1\",\n    \"category\": \"PARA VE\
  \ BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"\
  source_snippets\": [\n    \"'TP.HPBITABLO1.19', 'TP.HPBITABLO1.20', 'TP.HPBITABLO1.21',\
  \ #repo - para arzı\",\n    \"'TP_HPBITABLO1_19': 'Repo*',\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_HPBITABLO1_19%3Af82221d7d90c.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO1.19

## Target
series | evds:TP.HPBITABLO1.19

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
3.1.Repo

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

## Confidence
0.9

## Candidate Themes
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits

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
Catalog source: catalog:evds2:TP.HPBITABLO1.19

## Evidence
{
  "ticker": "TP.HPBITABLO1.19",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Repo (Bin TL)",
  "context_title": "Repo (Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:resident-financial-assets",
    "theme:resident-securities",
    "theme:resident-deposits"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:yiyrlsk-mkk-hisse-manual",
    "source:yiyrlsk-mkk-fon-manual",
    "source:yiyrlsk-vap-scrape-attempt"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO1.19",
    "title": "3.1.Repo",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo1",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO1.19', 'TP.HPBITABLO1.20', 'TP.HPBITABLO1.21', #repo - para arzı",
    "'TP_HPBITABLO1_19': 'Repo*',"
  ],
  "indicator_hints": [],
  "notes": ""
}
