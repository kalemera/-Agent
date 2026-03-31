---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S60:f2e2826491da
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S60:f2e2826491da
title: Semantic proposal for TP.YDOSBAPIYDEG.S60
status: approved
target_type: series
target_id: evds:TP.YDOSBAPIYDEG.S60
ticker: TP.YDOSBAPIYDEG.S60
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.D.1.2.Finansal Kuruluşlar (S.12) (Finansal Yardımcı İhraçları)
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
evidence_fingerprint: f2e2826491da717d18fd8b08c5621e12eed694e0
catalog_record_id: catalog:evds2:TP.YDOSBAPIYDEG.S60
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAPIYDEG.S60
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından
    İhraç Edilen)
  context_title: Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç
    Edilen)
  frequency: weekly
  unit: milyon ABD doları
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
    id: catalog:evds2:TP.YDOSBAPIYDEG.S60
    title: 1.D.1.2.Finansal Kuruluşlar (S.12) (Finansal Yardımcı İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAPIYDEG.S59'', ''TP.YDOSBAPIYDEG.S60'', ''TP.YDOSBAPIYDEG.S62'', ''TP.YDOSBAPIYDEG.S68'',
    ''TP.YDOSBAPIYDEG.S74'', #özel sektör eurobond - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Eurobond (Tüzel Kişi, 4)"] = df_yi_yerlesik['TP_DK_USD_A_YTL']
    * (df_yi_yerlesik["TP_YDOSBAPIYDEG_S59"] + (df_yi_yerlesik["TP_YDOSBAPIYDEG_S60"]
    - df_yi_yerlesik["TP_YDOSBAPIYDEG_S62"]) + df_yi_yerlesik["TP_YDOSBAPIYDEG_S68"]
    + df_yi_yerlesik["TP_YDOSBAPIYDEG_S74"])
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAPIYDEG.S60
promoted_memory_rule_id: memory:global-tp-ydosbapiydeg-s60
notes: 'Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S60'
body: "# Semantic proposal for TP.YDOSBAPIYDEG.S60\n\n## Target\nseries | evds:TP.YDOSBAPIYDEG.S60\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.D.1.2.Finansal Kuruluşlar\
  \ (S.12) (Finansal Yardımcı İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\
  \n## Candidate Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n\
  0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.YDOSBAPIYDEG.S60\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YDOSBAPIYDEG.S60\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Finansal Kuruluşlar (S.12)\
  \ (Finansal Yardımcılar Tarafından İhraç Edilen)\",\n  \"context_title\": \"Finansal\
  \ Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç Edilen)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_component\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YDOSBAPIYDEG.S60\"\
  ,\n    \"title\": \"1.D.1.2.Finansal Kuruluşlar (S.12) (Finansal Yardımcı İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_ydosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN\
  \ YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YDOSBAPIYDEG.S59', 'TP.YDOSBAPIYDEG.S60', 'TP.YDOSBAPIYDEG.S62',\
  \ 'TP.YDOSBAPIYDEG.S68', 'TP.YDOSBAPIYDEG.S74', #özel sektör eurobond - tüzel kişiler\"\
  ,\n    \"df_yi_yerlesik[\\\"Özel Sektör Eurobond (Tüzel Kişi, 4)\\\"] = df_yi_yerlesik['TP_DK_USD_A_YTL']\
  \ * (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S59\\\"] + (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S60\\\
  \"] - df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S62\\\"]) + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S68\\\
  \"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S74\\\"])\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YDOSBAPIYDEG_S60%3Af2e2826491da.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAPIYDEG.S60

## Target
series | evds:TP.YDOSBAPIYDEG.S60

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.D.1.2.Finansal Kuruluşlar (S.12) (Finansal Yardımcı İhraçları)

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
Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S60

## Evidence
{
  "ticker": "TP.YDOSBAPIYDEG.S60",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç Edilen)",
  "context_title": "Finansal Kuruluşlar (S.12) (Finansal Yardımcılar Tarafından İhraç Edilen)",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
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
    "id": "catalog:evds2:TP.YDOSBAPIYDEG.S60",
    "title": "1.D.1.2.Finansal Kuruluşlar (S.12) (Finansal Yardımcı İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAPIYDEG.S59', 'TP.YDOSBAPIYDEG.S60', 'TP.YDOSBAPIYDEG.S62', 'TP.YDOSBAPIYDEG.S68', 'TP.YDOSBAPIYDEG.S74', #özel sektör eurobond - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Eurobond (Tüzel Kişi, 4)\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S59\"] + (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S60\"] - df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S62\"]) + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S68\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S74\"])"
  ],
  "indicator_hints": [],
  "notes": ""
}
