---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_EBONDPIYDEG_S14:24304af15b1f
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_EBONDPIYDEG_S14:24304af15b1f
title: Semantic proposal for TP.EBONDPIYDEG.S14
status: approved
target_type: series
target_id: evds:TP.EBONDPIYDEG.S14
ticker: TP.EBONDPIYDEG.S14
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.1.4.Hanehalkı (S.14)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 24304af15b1f2366aab81a50b019064713f76c8f
catalog_record_id: catalog:evds2:TP.EBONDPIYDEG.S14
memory_rule_ids: []
evidence:
  ticker: TP.EBONDPIYDEG.S14
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Hanehalkı (S.14)
  context_title: Hanehalkı (S.14)
  frequency: weekly
  unit: Milyon ABD Dolari
  role: stock_component
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
    id: catalog:evds2:TP.EBONDPIYDEG.S14
    title: 1.1.4.Hanehalkı (S.14)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ebondpiydeg
    category: GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.EBONDPIYDEG.S13'', ''TP.EBONDPIYDEG.S14'', ''TP.EBONDPIYDEG.S15'', ''TP.DK.USD.A.YTL'',
    #eurobond'
  - df_yi_yerlesik['Eurobond (Gerçek Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] *
    df_yi_yerlesik['TP_EBONDPIYDEG_S14']
  - '#df_mevduat[''Eurobond''] = df_mevduat[''TP_DK_USD_A_YTL''] * (df_mevduat[''TP_EBONDPIYDEG_S11'']
    + df_mevduat[''TP_EBONDPIYDEG_S14''])#+ df_mevduat[''TP_EBONDPIYDEG_S15''])'
  indicator_hints: []
  notes: Notebookta USD/TL ile carpilarak 'Eurobond (Gercek Kisi)' TL karsiligina
    cevriliyor.
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.EBONDPIYDEG.S14
promoted_memory_rule_id: memory:global-tp-ebondpiydeg-s14
notes: 'Catalog source: catalog:evds2:TP.EBONDPIYDEG.S14 | Notebookta USD/TL ile carpilarak
  ''Eurobond (Gercek Kisi)'' TL karsiligina cevriliyor.'
body: "# Semantic proposal for TP.EBONDPIYDEG.S14\n\n## Target\nseries | evds:TP.EBONDPIYDEG.S14\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.1.4.Hanehalkı (S.14)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n\
  - theme:resident-securities\n- theme:resident-deposits\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.EBONDPIYDEG.S14\
  \ | Notebookta USD/TL ile carpilarak 'Eurobond (Gercek Kisi)' TL karsiligina cevriliyor.\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.EBONDPIYDEG.S14\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Hanehalkı (S.14)\",\n  \"\
  context_title\": \"Hanehalkı (S.14)\",\n  \"frequency\": \"weekly\",\n  \"unit\"\
  : \"Milyon ABD Dolari\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\",\n    \"theme:resident-securities\"\
  ,\n    \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.EBONDPIYDEG.S14\",\n    \"title\": \"1.1.4.Hanehalkı\
  \ (S.14)\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\"\
  ,\n    \"data_group\": \"bie_ebondpiydeg\",\n    \"category\": \"GENEL YÖNETİM YURT\
  \ DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.EBONDPIYDEG.S13', 'TP.EBONDPIYDEG.S14', 'TP.EBONDPIYDEG.S15', 'TP.DK.USD.A.YTL',\
  \ #eurobond\",\n    \"df_yi_yerlesik['Eurobond (Gerçek Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL']\
  \ * df_yi_yerlesik['TP_EBONDPIYDEG_S14']\",\n    \"#df_mevduat['Eurobond'] = df_mevduat['TP_DK_USD_A_YTL']\
  \ * (df_mevduat['TP_EBONDPIYDEG_S11'] + df_mevduat['TP_EBONDPIYDEG_S14'])#+ df_mevduat['TP_EBONDPIYDEG_S15'])\"\
  \n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"Notebookta USD/TL ile carpilarak\
  \ 'Eurobond (Gercek Kisi)' TL karsiligina cevriliyor.\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_EBONDPIYDEG_S14%3A24304af15b1f.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.EBONDPIYDEG.S14

## Target
series | evds:TP.EBONDPIYDEG.S14

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.1.4.Hanehalkı (S.14)

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
Catalog source: catalog:evds2:TP.EBONDPIYDEG.S14 | Notebookta USD/TL ile carpilarak 'Eurobond (Gercek Kisi)' TL karsiligina cevriliyor.

## Evidence
{
  "ticker": "TP.EBONDPIYDEG.S14",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Hanehalkı (S.14)",
  "context_title": "Hanehalkı (S.14)",
  "frequency": "weekly",
  "unit": "Milyon ABD Dolari",
  "role": "stock_component",
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
    "id": "catalog:evds2:TP.EBONDPIYDEG.S14",
    "title": "1.1.4.Hanehalkı (S.14)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ebondpiydeg",
    "category": "GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.EBONDPIYDEG.S13', 'TP.EBONDPIYDEG.S14', 'TP.EBONDPIYDEG.S15', 'TP.DK.USD.A.YTL', #eurobond",
    "df_yi_yerlesik['Eurobond (Gerçek Kişi)'] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * df_yi_yerlesik['TP_EBONDPIYDEG_S14']",
    "#df_mevduat['Eurobond'] = df_mevduat['TP_DK_USD_A_YTL'] * (df_mevduat['TP_EBONDPIYDEG_S11'] + df_mevduat['TP_EBONDPIYDEG_S14'])#+ df_mevduat['TP_EBONDPIYDEG_S15'])"
  ],
  "indicator_hints": [],
  "notes": "Notebookta USD/TL ile carpilarak 'Eurobond (Gercek Kisi)' TL karsiligina cevriliyor."
}
