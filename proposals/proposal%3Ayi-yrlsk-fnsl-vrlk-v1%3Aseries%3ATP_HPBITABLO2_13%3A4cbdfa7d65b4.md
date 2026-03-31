---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_13:4cbdfa7d65b4
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_13:4cbdfa7d65b4
title: Semantic proposal for TP.HPBITABLO2.13
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.13
ticker: TP.HPBITABLO2.13
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.2.Yurt İçi Yerleşik Bankalar
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
evidence_fingerprint: 4cbdfa7d65b4333eb6ad0311a6045553c61d51dd
catalog_record_id: catalog:evds2:TP.HPBITABLO2.13
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.13
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: TL+YP Mevduat (Bankalar)
  context_title: TL+YP Mevduat (Bankalar)
  frequency: weekly
  unit: bin TL
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
    id: catalog:evds2:TP.HPBITABLO2.13
    title: 1.2.Yurt İçi Yerleşik Bankalar
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.13'', ''TP.HPBITABLO2.14'', ''TP.HPBITABLO2.15'',  #mevduat -
    bankalar yurtiçi şube / Bankalar'
  - '''TP_HPBITABLO2_13'': ''TL+YP Mevduat (Bankalar)'','
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.13
promoted_memory_rule_id: memory:global-tp-hpbitablo2-13
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.13'
body: "# Semantic proposal for TP.HPBITABLO2.13\n\n## Target\nseries | evds:TP.HPBITABLO2.13\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.2.Yurt İçi Yerleşik\
  \ Bankalar\n\n## Candidate Unit\nbin TL\n\n## Candidate Frequency\nweekly\n\n##\
  \ Candidate Role\nbalance_sheet_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n\
  - theme:resident-financial-assets\n- theme:resident-securities\n- theme:resident-deposits\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.13\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO2.13\",\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\"\
  ,\n  \"official_series_name\": \"TL+YP Mevduat (Bankalar)\",\n  \"context_title\"\
  : \"TL+YP Mevduat (Bankalar)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"bin\
  \ TL\",\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\",\n\
  \  \"theme_ids\": [\n    \"theme:resident-financial-assets\",\n    \"theme:resident-securities\"\
  ,\n    \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.HPBITABLO2.13\",\n    \"title\": \"1.2.Yurt İçi Yerleşik\
  \ Bankalar\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"bin TL\",\n    \"\
  data_group\": \"bie_hpbitablo2\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ\
  \ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n\
  \    \"'TP.HPBITABLO2.13', 'TP.HPBITABLO2.14', 'TP.HPBITABLO2.15',  #mevduat - bankalar\
  \ yurtiçi şube / Bankalar\",\n    \"'TP_HPBITABLO2_13': 'TL+YP Mevduat (Bankalar)',\"\
  \n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_HPBITABLO2_13%3A4cbdfa7d65b4.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.13

## Target
series | evds:TP.HPBITABLO2.13

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.2.Yurt İçi Yerleşik Bankalar

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
Catalog source: catalog:evds2:TP.HPBITABLO2.13

## Evidence
{
  "ticker": "TP.HPBITABLO2.13",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "TL+YP Mevduat (Bankalar)",
  "context_title": "TL+YP Mevduat (Bankalar)",
  "frequency": "weekly",
  "unit": "bin TL",
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
    "id": "catalog:evds2:TP.HPBITABLO2.13",
    "title": "1.2.Yurt İçi Yerleşik Bankalar",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.13', 'TP.HPBITABLO2.14', 'TP.HPBITABLO2.15',  #mevduat - bankalar yurtiçi şube / Bankalar",
    "'TP_HPBITABLO2_13': 'TL+YP Mevduat (Bankalar)',"
  ],
  "indicator_hints": [],
  "notes": ""
}
