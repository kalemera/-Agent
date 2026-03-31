---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_DK_USD_A_YTL:61093dfee3d1
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_DK_USD_A_YTL:61093dfee3d1
title: Semantic proposal for TP.DK.USD.A.YTL
status: approved
target_type: series
target_id: evds:TP.DK.USD.A.YTL
ticker: TP.DK.USD.A.YTL
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: (USD)  ABD  Doları  (Döviz  Alış)
candidate_unit: Türk lirası
candidate_frequency: daily
candidate_role: ratio_input
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 61093dfee3d1b143e8aa2018e19b25052c029438
catalog_record_id: catalog:evds2:TP.DK.USD.A.YTL
memory_rule_ids: []
evidence:
  ticker: TP.DK.USD.A.YTL
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: USD/TL (Alis Kuru)
  context_title: USD/TL (Alis Kuru)
  frequency: weekly
  unit: Türk lirası
  role: ratio_input
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
    id: catalog:evds2:TP.DK.USD.A.YTL
    title: (USD)  ABD  Doları  (Döviz  Alış)
    frequency: daily
    unit: Türk lirası
    data_group: bie_dkdovytl
    category: TCMB DÖVİZ KURLARI
  memory_rules: []
  source_snippets:
  - '''TP.EBONDPIYDEG.S13'', ''TP.EBONDPIYDEG.S14'', ''TP.EBONDPIYDEG.S15'', ''TP.DK.USD.A.YTL'',
    #eurobond'
  - df_yi_yerlesik['Eurobond (Gerçek Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] *
    df_yi_yerlesik['TP_EBONDPIYDEG_S14']
  - df_yi_yerlesik['Eurobond (Tüzel Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] *
    (df_yi_yerlesik['TP_EBONDPIYDEG_S11'] + (df_yi_yerlesik['TP_EBONDPIYDEG_S12']
    - df_yi_yerlesik['TP_EBONDPIYDEG_S122']) + df_yi_yerlesik['TP_EBONDPIYDEG_S13']
    + df_yi_yerlesik['TP_EBONDPIYDEG_S15'])
  - df_yi_yerlesik['Eurobond (Bankalar)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * df_yi_yerlesik['TP_EBONDPIYDEG_S122']
  - df_yi_yerlesik["Özel Sektör Eurobond (Gerçek Kişi)"] = df_yi_yerlesik['TP_DK_USD_A_YTL']
    * (df_yi_yerlesik["TP_YDOSBAPIYDEG_S15"] + df_yi_yerlesik["TP_YDOSBAPIYDEG_S34"]
    + df_yi_yerlesik["TP_YDOSBAPIYDEG_S53"] + df_yi_yerlesik["TP_YDOSBAPIYDEG_S72"])
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DK.USD.A.YTL
promoted_memory_rule_id: memory:global-tp-dk-usd-a-ytl
notes: 'Catalog source: catalog:evds2:TP.DK.USD.A.YTL'
body: "# Semantic proposal for TP.DK.USD.A.YTL\n\n## Target\nseries | evds:TP.DK.USD.A.YTL\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n(USD)  ABD  Doları \
  \ (Döviz  Alış)\n\n## Candidate Unit\nTürk lirası\n\n## Candidate Frequency\ndaily\n\
  \n## Candidate Role\nratio_input\n\n## Confidence\n0.9\n\n## Candidate Themes\n\
  - theme:resident-financial-assets\n- theme:resident-securities\n- theme:resident-deposits\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.DK.USD.A.YTL\n\n## Evidence\n{\n  \"ticker\"\
  : \"TP.DK.USD.A.YTL\",\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\"\
  : \"USD/TL (Alis Kuru)\",\n  \"context_title\": \"USD/TL (Alis Kuru)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Türk lirası\",\n  \"role\": \"ratio_input\",\n  \"\
  status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.DK.USD.A.YTL\",\n\
  \    \"title\": \"(USD)  ABD  Doları  (Döviz  Alış)\",\n    \"frequency\": \"daily\"\
  ,\n    \"unit\": \"Türk lirası\",\n    \"data_group\": \"bie_dkdovytl\",\n    \"\
  category\": \"TCMB DÖVİZ KURLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.EBONDPIYDEG.S13', 'TP.EBONDPIYDEG.S14', 'TP.EBONDPIYDEG.S15', 'TP.DK.USD.A.YTL',\
  \ #eurobond\",\n    \"df_yi_yerlesik['Eurobond (Gerçek Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL']\
  \ * df_yi_yerlesik['TP_EBONDPIYDEG_S14']\",\n    \"df_yi_yerlesik['Eurobond (Tüzel\
  \ Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik['TP_EBONDPIYDEG_S11']\
  \ + (df_yi_yerlesik['TP_EBONDPIYDEG_S12'] - df_yi_yerlesik['TP_EBONDPIYDEG_S122'])\
  \ + df_yi_yerlesik['TP_EBONDPIYDEG_S13'] + df_yi_yerlesik['TP_EBONDPIYDEG_S15'])\"\
  ,\n    \"df_yi_yerlesik['Eurobond (Bankalar)'] = df_yi_yerlesik['TP_DK_USD_A_YTL']\
  \ * df_yi_yerlesik['TP_EBONDPIYDEG_S122']\",\n    \"df_yi_yerlesik[\\\"Özel Sektör\
  \ Eurobond (Gerçek Kişi)\\\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\\\
  \"TP_YDOSBAPIYDEG_S15\\\"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S34\\\"] + df_yi_yerlesik[\\\
  \"TP_YDOSBAPIYDEG_S53\\\"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S72\\\"])\"\n  ],\n\
  \  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_DK_USD_A_YTL%3A61093dfee3d1.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DK.USD.A.YTL

## Target
series | evds:TP.DK.USD.A.YTL

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
(USD)  ABD  Doları  (Döviz  Alış)

## Candidate Unit
Türk lirası

## Candidate Frequency
daily

## Candidate Role
ratio_input

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
Catalog source: catalog:evds2:TP.DK.USD.A.YTL

## Evidence
{
  "ticker": "TP.DK.USD.A.YTL",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "USD/TL (Alis Kuru)",
  "context_title": "USD/TL (Alis Kuru)",
  "frequency": "weekly",
  "unit": "Türk lirası",
  "role": "ratio_input",
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
    "id": "catalog:evds2:TP.DK.USD.A.YTL",
    "title": "(USD)  ABD  Doları  (Döviz  Alış)",
    "frequency": "daily",
    "unit": "Türk lirası",
    "data_group": "bie_dkdovytl",
    "category": "TCMB DÖVİZ KURLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.EBONDPIYDEG.S13', 'TP.EBONDPIYDEG.S14', 'TP.EBONDPIYDEG.S15', 'TP.DK.USD.A.YTL', #eurobond",
    "df_yi_yerlesik['Eurobond (Gerçek Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * df_yi_yerlesik['TP_EBONDPIYDEG_S14']",
    "df_yi_yerlesik['Eurobond (Tüzel Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik['TP_EBONDPIYDEG_S11'] + (df_yi_yerlesik['TP_EBONDPIYDEG_S12'] - df_yi_yerlesik['TP_EBONDPIYDEG_S122']) + df_yi_yerlesik['TP_EBONDPIYDEG_S13'] + df_yi_yerlesik['TP_EBONDPIYDEG_S15'])",
    "df_yi_yerlesik['Eurobond (Bankalar)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * df_yi_yerlesik['TP_EBONDPIYDEG_S122']",
    "df_yi_yerlesik[\"Özel Sektör Eurobond (Gerçek Kişi)\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S15\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S34\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S53\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S72\"])"
  ],
  "indicator_hints": [],
  "notes": ""
}
