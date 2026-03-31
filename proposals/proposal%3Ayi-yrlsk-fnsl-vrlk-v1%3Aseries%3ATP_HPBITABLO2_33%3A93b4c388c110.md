---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_33:93b4c388c110
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_33:93b4c388c110
title: Semantic proposal for TP.HPBITABLO2.33
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.33
ticker: TP.HPBITABLO2.33
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 2.2.1.TL
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 93b4c388c110640d31190a0e18d1283c8f1e8a9a
catalog_record_id: catalog:evds2:TP.HPBITABLO2.33
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.33
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: a. TL (Bin TL)
  context_title: 2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL) / a. TL (Bin TL)
  frequency: weekly
  unit: Bin TL
  role: currency_split_line
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
    id: catalog:evds2:TP.HPBITABLO2.33
    title: 2.2.1.TL
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.32'', ''TP.HPBITABLO2.33'', ''TP.HPBITABLO2.34'', #kredi - bankalar
    yurtiçi şube / bankalar'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.33
promoted_memory_rule_id: memory:global-tp-hpbitablo2-33
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.33'
body: "# Semantic proposal for TP.HPBITABLO2.33\n\n## Target\nseries | evds:TP.HPBITABLO2.33\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n2.2.1.TL\n\n## Candidate\
  \ Unit\nbin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\ncurrency_split_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n\
  - theme:resident-securities\n- theme:resident-deposits\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.HPBITABLO2.33\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO2.33\"\
  ,\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\":\
  \ \"a. TL (Bin TL)\",\n  \"context_title\": \"2. Yurt Ici Yerlesik Finansal Kuruluslar\
  \ (Bin TL) / a. TL (Bin TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Bin\
  \ TL\",\n  \"role\": \"currency_split_line\",\n  \"status\": \"derived_input\",\n\
  \  \"theme_ids\": [\n    \"theme:resident-financial-assets\",\n    \"theme:resident-securities\"\
  ,\n    \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.HPBITABLO2.33\",\n    \"title\": \"2.2.1.TL\",\n \
  \   \"frequency\": \"weekly\",\n    \"unit\": \"bin TL\",\n    \"data_group\": \"\
  bie_hpbitablo2\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\
  \n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO2.32',\
  \ 'TP.HPBITABLO2.33', 'TP.HPBITABLO2.34', #kredi - bankalar yurtiçi şube / bankalar\"\
  \n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_HPBITABLO2_33%3A93b4c388c110.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.33

## Target
series | evds:TP.HPBITABLO2.33

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
2.2.1.TL

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
Catalog source: catalog:evds2:TP.HPBITABLO2.33

## Evidence
{
  "ticker": "TP.HPBITABLO2.33",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "a. TL (Bin TL)",
  "context_title": "2. Yurt Ici Yerlesik Finansal Kuruluslar (Bin TL) / a. TL (Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "currency_split_line",
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
    "id": "catalog:evds2:TP.HPBITABLO2.33",
    "title": "2.2.1.TL",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.32', 'TP.HPBITABLO2.33', 'TP.HPBITABLO2.34', #kredi - bankalar yurtiçi şube / bankalar"
  ],
  "indicator_hints": [],
  "notes": ""
}
