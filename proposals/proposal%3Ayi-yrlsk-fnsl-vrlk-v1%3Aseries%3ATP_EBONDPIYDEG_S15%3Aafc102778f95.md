---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_EBONDPIYDEG_S15:afc102778f95
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_EBONDPIYDEG_S15:afc102778f95
title: Semantic proposal for TP.EBONDPIYDEG.S15
status: approved
target_type: series
target_id: evds:TP.EBONDPIYDEG.S15
ticker: TP.EBONDPIYDEG.S15
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs:
- derived:private-sector-eurobond-total
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: afc102778f9581fe12a4aa04eb3658730cfa39d4
catalog_record_id: catalog:evds2:TP.EBONDPIYDEG.S15
memory_rule_ids: []
evidence:
  ticker: TP.EBONDPIYDEG.S15
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
  context_title: Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
  frequency: weekly
  unit: milyon ABD doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:resident-financial-assets
  - theme:resident-securities
  - theme:resident-deposits
  indicator_ids:
  - derived:private-sector-eurobond-total
  source_dependency_ids:
  - source:yiyrlsk-mkk-hisse-manual
  - source:yiyrlsk-mkk-fon-manual
  - source:yiyrlsk-vap-scrape-attempt
  catalog_record:
    id: catalog:evds2:TP.EBONDPIYDEG.S15
    title: 1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ebondpiydeg
    category: GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.EBONDPIYDEG.S13'', ''TP.EBONDPIYDEG.S14'', ''TP.EBONDPIYDEG.S15'', ''TP.DK.USD.A.YTL'',
    #eurobond'
  - df_yi_yerlesik['Eurobond (Tüzel Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] *
    (df_yi_yerlesik['TP_EBONDPIYDEG_S11'] + (df_yi_yerlesik['TP_EBONDPIYDEG_S12']
    - df_yi_yerlesik['TP_EBONDPIYDEG_S122']) + df_yi_yerlesik['TP_EBONDPIYDEG_S13']
    + df_yi_yerlesik['TP_EBONDPIYDEG_S15'])
  - '#df_mevduat[''Eurobond''] = df_mevduat[''TP_DK_USD_A_YTL''] * (df_mevduat[''TP_EBONDPIYDEG_S11'']
    + df_mevduat[''TP_EBONDPIYDEG_S14''])#+ df_mevduat[''TP_EBONDPIYDEG_S15''])'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.EBONDPIYDEG.S15
promoted_memory_rule_id: memory:global-tp-ebondpiydeg-s15
notes: 'Catalog source: catalog:evds2:TP.EBONDPIYDEG.S15'
body: "# Semantic proposal for TP.EBONDPIYDEG.S15\n\n## Target\nseries | evds:TP.EBONDPIYDEG.S15\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.1.5.Hanehalkına Hizmet\
  \ Veren Kar Amacı Olmayan Kuruluşlar (S.15)\n\n## Candidate Unit\nmilyon ABD doları\n\
  \n## Candidate Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n\
  0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n- derived:private-sector-eurobond-total\n\
  \n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval\
  \ Reason\nLLM requested manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.EBONDPIYDEG.S15\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.EBONDPIYDEG.S15\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Hanehalkına Hizmet Veren\
  \ Kar Amacı Olmayan Kuruluşlar (S.15)\",\n  \"context_title\": \"Hanehalkına Hizmet\
  \ Veren Kar Amacı Olmayan Kuruluşlar (S.15)\",\n  \"frequency\": \"weekly\",\n \
  \ \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_component\",\n  \"status\"\
  : \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [\n    \"derived:private-sector-eurobond-total\"\n  ],\n  \"\
  source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.EBONDPIYDEG.S15\",\n    \"title\": \"1.1.5.Hanehalkına\
  \ Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)\",\n    \"frequency\": \"weekly\"\
  ,\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_ebondpiydeg\"\
  ,\n    \"category\": \"GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.EBONDPIYDEG.S13',\
  \ 'TP.EBONDPIYDEG.S14', 'TP.EBONDPIYDEG.S15', 'TP.DK.USD.A.YTL', #eurobond\",\n\
  \    \"df_yi_yerlesik['Eurobond (Tüzel Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL']\
  \ * (df_yi_yerlesik['TP_EBONDPIYDEG_S11'] + (df_yi_yerlesik['TP_EBONDPIYDEG_S12']\
  \ - df_yi_yerlesik['TP_EBONDPIYDEG_S122']) + df_yi_yerlesik['TP_EBONDPIYDEG_S13']\
  \ + df_yi_yerlesik['TP_EBONDPIYDEG_S15'])\",\n    \"#df_mevduat['Eurobond'] = df_mevduat['TP_DK_USD_A_YTL']\
  \ * (df_mevduat['TP_EBONDPIYDEG_S11'] + df_mevduat['TP_EBONDPIYDEG_S14'])#+ df_mevduat['TP_EBONDPIYDEG_S15'])\"\
  \n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_EBONDPIYDEG_S15%3Aafc102778f95.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.EBONDPIYDEG.S15

## Target
series | evds:TP.EBONDPIYDEG.S15

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)

## Candidate Unit
milyon ABD doları

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
- derived:private-sector-eurobond-total

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.EBONDPIYDEG.S15

## Evidence
{
  "ticker": "TP.EBONDPIYDEG.S15",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)",
  "context_title": "Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:resident-financial-assets",
    "theme:resident-securities",
    "theme:resident-deposits"
  ],
  "indicator_ids": [
    "derived:private-sector-eurobond-total"
  ],
  "source_dependency_ids": [
    "source:yiyrlsk-mkk-hisse-manual",
    "source:yiyrlsk-mkk-fon-manual",
    "source:yiyrlsk-vap-scrape-attempt"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.EBONDPIYDEG.S15",
    "title": "1.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ebondpiydeg",
    "category": "GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.EBONDPIYDEG.S13', 'TP.EBONDPIYDEG.S14', 'TP.EBONDPIYDEG.S15', 'TP.DK.USD.A.YTL', #eurobond",
    "df_yi_yerlesik['Eurobond (Tüzel Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik['TP_EBONDPIYDEG_S11'] + (df_yi_yerlesik['TP_EBONDPIYDEG_S12'] - df_yi_yerlesik['TP_EBONDPIYDEG_S122']) + df_yi_yerlesik['TP_EBONDPIYDEG_S13'] + df_yi_yerlesik['TP_EBONDPIYDEG_S15'])",
    "#df_mevduat['Eurobond'] = df_mevduat['TP_DK_USD_A_YTL'] * (df_mevduat['TP_EBONDPIYDEG_S11'] + df_mevduat['TP_EBONDPIYDEG_S14'])#+ df_mevduat['TP_EBONDPIYDEG_S15'])"
  ],
  "indicator_hints": [],
  "notes": ""
}
