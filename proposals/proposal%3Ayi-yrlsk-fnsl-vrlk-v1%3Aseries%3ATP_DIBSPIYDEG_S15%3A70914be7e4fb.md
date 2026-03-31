---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_DIBSPIYDEG_S15:70914be7e4fb
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_DIBSPIYDEG_S15:70914be7e4fb
title: Semantic proposal for TP.DIBSPIYDEG.S15
status: approved
target_type: series
target_id: evds:TP.DIBSPIYDEG.S15
ticker: TP.DIBSPIYDEG.S15
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
candidate_unit: milyon TL
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs:
- derived:private-sector-bond-total
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 70914be7e4fb4c241d139e269b2a6d8d7b0b8f20
catalog_record_id: catalog:evds2:TP.DIBSPIYDEG.S15
memory_rule_ids: []
evidence:
  ticker: TP.DIBSPIYDEG.S15
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
  context_title: Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
  frequency: weekly
  unit: milyon TL
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:resident-financial-assets
  - theme:resident-securities
  - theme:resident-deposits
  indicator_ids:
  - derived:private-sector-bond-total
  source_dependency_ids:
  - source:yiyrlsk-mkk-hisse-manual
  - source:yiyrlsk-mkk-fon-manual
  - source:yiyrlsk-vap-scrape-attempt
  catalog_record:
    id: catalog:evds2:TP.DIBSPIYDEG.S15
    title: 1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
    frequency: weekly
    unit: milyon TL
    data_group: bie_dibspiydeg
    category: DEVLET İÇ BORÇLANMA SENETLERİ
  memory_rules: []
  source_snippets:
  - '''TP.DIBSPIYDEG.S13'',''TP.DIBSPIYDEG.S14'', ''TP.DIBSPIYDEG.S15'', #dibs'
  - df_yi_yerlesik['DİBS (Tüzel Kişi)'] = df_yi_yerlesik['TP_DIBSPIYDEG_S11'] + (df_yi_yerlesik['TP_DIBSPIYDEG_S12']
    - df_yi_yerlesik['TP_DIBSPIYDEG_S122']) + df_yi_yerlesik['TP_DIBSPIYDEG_S13']
    + df_yi_yerlesik['TP_DIBSPIYDEG_S15']
  - '#df_mevduat[''DİBS''] = df_mevduat[''TP_DIBSPIYDEG_S11''] + df_mevduat[''TP_DIBSPIYDEG_S14'']
    #+ df_mevduat[''TP_DIBSPIYDEG_S15'']'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DIBSPIYDEG.S15
promoted_memory_rule_id: memory:global-tp-dibspiydeg-s15
notes: 'Catalog source: catalog:evds2:TP.DIBSPIYDEG.S15'
body: "# Semantic proposal for TP.DIBSPIYDEG.S15\n\n## Target\nseries | evds:TP.DIBSPIYDEG.S15\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.1.5.Hanehalkına Hizmet\
  \ Veren Kar Amacı Olmayan Kuruluşlar (S.15)\n\n## Candidate Unit\nmilyon TL\n\n\
  ## Candidate Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n\
  0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n- derived:private-sector-bond-total\n\
  \n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval\
  \ Reason\nLLM requested manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.DIBSPIYDEG.S15\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.DIBSPIYDEG.S15\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Hanehalkına Hizmet Veren\
  \ Kar Amacı Olmayan Kuruluşlar (S.15)\",\n  \"context_title\": \"Hanehalkına Hizmet\
  \ Veren Kar Amacı Olmayan Kuruluşlar (S.15)\",\n  \"frequency\": \"weekly\",\n \
  \ \"unit\": \"milyon TL\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\",\n    \"theme:resident-securities\"\
  ,\n    \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [\n    \"derived:private-sector-bond-total\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.DIBSPIYDEG.S15\"\
  ,\n    \"title\": \"1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar\
  \ (S.15)\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon TL\",\n    \"\
  data_group\": \"bie_dibspiydeg\",\n    \"category\": \"DEVLET İÇ BORÇLANMA SENETLERİ\"\
  \n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.DIBSPIYDEG.S13','TP.DIBSPIYDEG.S14',\
  \ 'TP.DIBSPIYDEG.S15', #dibs\",\n    \"df_yi_yerlesik['DİBS (Tüzel Kişi)'] = df_yi_yerlesik['TP_DIBSPIYDEG_S11']\
  \ + (df_yi_yerlesik['TP_DIBSPIYDEG_S12'] - df_yi_yerlesik['TP_DIBSPIYDEG_S122'])\
  \ + df_yi_yerlesik['TP_DIBSPIYDEG_S13'] + df_yi_yerlesik['TP_DIBSPIYDEG_S15']\"\
  ,\n    \"#df_mevduat['DİBS'] = df_mevduat['TP_DIBSPIYDEG_S11'] + df_mevduat['TP_DIBSPIYDEG_S14']\
  \ #+ df_mevduat['TP_DIBSPIYDEG_S15']\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_DIBSPIYDEG_S15%3A70914be7e4fb.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DIBSPIYDEG.S15

## Target
series | evds:TP.DIBSPIYDEG.S15

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)

## Candidate Unit
milyon TL

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.9

## Candidate Themes
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits

## Candidate Indicator Inputs
- derived:private-sector-bond-total

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.DIBSPIYDEG.S15

## Evidence
{
  "ticker": "TP.DIBSPIYDEG.S15",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)",
  "context_title": "Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)",
  "frequency": "weekly",
  "unit": "milyon TL",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:resident-financial-assets",
    "theme:resident-securities",
    "theme:resident-deposits"
  ],
  "indicator_ids": [
    "derived:private-sector-bond-total"
  ],
  "source_dependency_ids": [
    "source:yiyrlsk-mkk-hisse-manual",
    "source:yiyrlsk-mkk-fon-manual",
    "source:yiyrlsk-vap-scrape-attempt"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DIBSPIYDEG.S15",
    "title": "1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)",
    "frequency": "weekly",
    "unit": "milyon TL",
    "data_group": "bie_dibspiydeg",
    "category": "DEVLET İÇ BORÇLANMA SENETLERİ"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.DIBSPIYDEG.S13','TP.DIBSPIYDEG.S14', 'TP.DIBSPIYDEG.S15', #dibs",
    "df_yi_yerlesik['DİBS (Tüzel Kişi)'] = df_yi_yerlesik['TP_DIBSPIYDEG_S11'] + (df_yi_yerlesik['TP_DIBSPIYDEG_S12'] - df_yi_yerlesik['TP_DIBSPIYDEG_S122']) + df_yi_yerlesik['TP_DIBSPIYDEG_S13'] + df_yi_yerlesik['TP_DIBSPIYDEG_S15']",
    "#df_mevduat['DİBS'] = df_mevduat['TP_DIBSPIYDEG_S11'] + df_mevduat['TP_DIBSPIYDEG_S14'] #+ df_mevduat['TP_DIBSPIYDEG_S15']"
  ],
  "indicator_hints": [],
  "notes": ""
}
