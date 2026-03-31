---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_24:3695a006e0f3
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_24:3695a006e0f3
title: Semantic proposal for TP.HPBITABLO2.24
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.24
ticker: TP.HPBITABLO2.24
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 2.1.1.TL
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs:
- derived:tl-deposit-total
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 3695a006e0f37f910579243f999bf1c84c1818a9
catalog_record_id: catalog:evds2:TP.HPBITABLO2.24
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.24
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: a. TL (Bin TL)
  context_title: 1. Yurt Ici Yerlesikler (Bin TL) / a. TL (Bin TL)
  frequency: weekly
  unit: Bin TL
  role: currency_split_line
  status: derived_input
  theme_ids:
  - theme:resident-financial-assets
  - theme:resident-securities
  - theme:resident-deposits
  indicator_ids:
  - derived:tl-deposit-total
  source_dependency_ids:
  - source:yiyrlsk-mkk-hisse-manual
  - source:yiyrlsk-mkk-fon-manual
  - source:yiyrlsk-vap-scrape-attempt
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.24
    title: 2.1.1.TL
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.23'', ''TP.HPBITABLO2.24'', ''TP.HPBITABLO2.25'', ''TP.HPBITABLO2.26'',
    ''TP.HPBITABLO2.27'', #kredi - bankalar yurtiçi şube / TL'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.24
promoted_memory_rule_id: memory:global-tp-hpbitablo2-24
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.24'
body: "# Semantic proposal for TP.HPBITABLO2.24\n\n## Target\nseries | evds:TP.HPBITABLO2.24\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n2.1.1.TL\n\n## Candidate\
  \ Unit\nbin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\ncurrency_split_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n\
  - theme:resident-securities\n- theme:resident-deposits\n\n## Candidate Indicator\
  \ Inputs\n- derived:tl-deposit-total\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.24\n\n## Evidence\n{\n  \"\
  ticker\": \"TP.HPBITABLO2.24\",\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\"\
  ,\n  \"official_series_name\": \"a. TL (Bin TL)\",\n  \"context_title\": \"1. Yurt\
  \ Ici Yerlesikler (Bin TL) / a. TL (Bin TL)\",\n  \"frequency\": \"weekly\",\n \
  \ \"unit\": \"Bin TL\",\n  \"role\": \"currency_split_line\",\n  \"status\": \"\
  derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\",\n\
  \    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n  \"\
  indicator_ids\": [\n    \"derived:tl-deposit-total\"\n  ],\n  \"source_dependency_ids\"\
  : [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.HPBITABLO2.24\",\n    \"title\": \"2.1.1.TL\",\n \
  \   \"frequency\": \"weekly\",\n    \"unit\": \"bin TL\",\n    \"data_group\": \"\
  bie_hpbitablo2\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\
  \n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO2.23',\
  \ 'TP.HPBITABLO2.24', 'TP.HPBITABLO2.25', 'TP.HPBITABLO2.26', 'TP.HPBITABLO2.27',\
  \ #kredi - bankalar yurtiçi şube / TL\"\n  ],\n  \"indicator_hints\": [],\n  \"\
  notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_HPBITABLO2_24%3A3695a006e0f3.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.24

## Target
series | evds:TP.HPBITABLO2.24

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
2.1.1.TL

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
currency_split_line

## Confidence
0.9

## Candidate Themes
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits

## Candidate Indicator Inputs
- derived:tl-deposit-total

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.HPBITABLO2.24

## Evidence
{
  "ticker": "TP.HPBITABLO2.24",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "a. TL (Bin TL)",
  "context_title": "1. Yurt Ici Yerlesikler (Bin TL) / a. TL (Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "currency_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:resident-financial-assets",
    "theme:resident-securities",
    "theme:resident-deposits"
  ],
  "indicator_ids": [
    "derived:tl-deposit-total"
  ],
  "source_dependency_ids": [
    "source:yiyrlsk-mkk-hisse-manual",
    "source:yiyrlsk-mkk-fon-manual",
    "source:yiyrlsk-vap-scrape-attempt"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.24",
    "title": "2.1.1.TL",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.23', 'TP.HPBITABLO2.24', 'TP.HPBITABLO2.25', 'TP.HPBITABLO2.26', 'TP.HPBITABLO2.27', #kredi - bankalar yurtiçi şube / TL"
  ],
  "indicator_hints": [],
  "notes": ""
}
