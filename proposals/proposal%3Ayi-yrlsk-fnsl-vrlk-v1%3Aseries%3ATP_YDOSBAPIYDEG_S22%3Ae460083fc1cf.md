---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S22:e460083fc1cf
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S22:e460083fc1cf
title: Semantic proposal for TP.YDOSBAPIYDEG.S22
status: approved
target_type: series
target_id: evds:TP.YDOSBAPIYDEG.S22
ticker: TP.YDOSBAPIYDEG.S22
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.B.1.2.Finansal Kuruluşlar (S.12) (Banka İhraçları)
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
evidence_fingerprint: e460083fc1cf02712e2628b6eb324687184f21c4
catalog_record_id: catalog:evds2:TP.YDOSBAPIYDEG.S22
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAPIYDEG.S22
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen)
  context_title: Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen)
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
    id: catalog:evds2:TP.YDOSBAPIYDEG.S22
    title: 1.B.1.2.Finansal Kuruluşlar (S.12) (Banka İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAPIYDEG.S21'', ''TP.YDOSBAPIYDEG.S22'', ''TP.YDOSBAPIYDEG.S24'', ''TP.YDOSBAPIYDEG.S30'',
    ''TP.YDOSBAPIYDEG.S34'', #özel sektör eurobond - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Eurobond (Tüzel Kişi, 2)"] = df_yi_yerlesik['TP_DK_USD_A_YTL']
    * (df_yi_yerlesik["TP_YDOSBAPIYDEG_S21"] + (df_yi_yerlesik["TP_YDOSBAPIYDEG_S22"]
    - df_yi_yerlesik["TP_YDOSBAPIYDEG_S24"]) + df_yi_yerlesik["TP_YDOSBAPIYDEG_S30"]
    + df_yi_yerlesik["TP_YDOSBAPIYDEG_S34"])
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAPIYDEG.S22
promoted_memory_rule_id: memory:global-tp-ydosbapiydeg-s22
notes: 'Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S22'
body: "# Semantic proposal for TP.YDOSBAPIYDEG.S22\n\n## Target\nseries | evds:TP.YDOSBAPIYDEG.S22\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.B.1.2.Finansal Kuruluşlar\
  \ (S.12) (Banka İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate\
  \ Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n0.9\n\
  \n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.YDOSBAPIYDEG.S22\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YDOSBAPIYDEG.S22\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Finansal Kuruluşlar (S.12)\
  \ (Bankalar Tarafından İhraç Edilen)\",\n  \"context_title\": \"Finansal Kuruluşlar\
  \ (S.12) (Bankalar Tarafından İhraç Edilen)\",\n  \"frequency\": \"weekly\",\n \
  \ \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_component\",\n  \"status\"\
  : \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YDOSBAPIYDEG.S22\"\
  ,\n    \"title\": \"1.B.1.2.Finansal Kuruluşlar (S.12) (Banka İhraçları)\",\n  \
  \  \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_ydosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YDOSBAPIYDEG.S21', 'TP.YDOSBAPIYDEG.S22', 'TP.YDOSBAPIYDEG.S24',\
  \ 'TP.YDOSBAPIYDEG.S30', 'TP.YDOSBAPIYDEG.S34', #özel sektör eurobond - tüzel kişiler\"\
  ,\n    \"df_yi_yerlesik[\\\"Özel Sektör Eurobond (Tüzel Kişi, 2)\\\"] = df_yi_yerlesik['TP_DK_USD_A_YTL']\
  \ * (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S21\\\"] + (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S22\\\
  \"] - df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S24\\\"]) + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S30\\\
  \"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S34\\\"])\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YDOSBAPIYDEG_S22%3Ae460083fc1cf.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAPIYDEG.S22

## Target
series | evds:TP.YDOSBAPIYDEG.S22

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.B.1.2.Finansal Kuruluşlar (S.12) (Banka İhraçları)

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
Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S22

## Evidence
{
  "ticker": "TP.YDOSBAPIYDEG.S22",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen)",
  "context_title": "Finansal Kuruluşlar (S.12) (Bankalar Tarafından İhraç Edilen)",
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
    "id": "catalog:evds2:TP.YDOSBAPIYDEG.S22",
    "title": "1.B.1.2.Finansal Kuruluşlar (S.12) (Banka İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAPIYDEG.S21', 'TP.YDOSBAPIYDEG.S22', 'TP.YDOSBAPIYDEG.S24', 'TP.YDOSBAPIYDEG.S30', 'TP.YDOSBAPIYDEG.S34', #özel sektör eurobond - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Eurobond (Tüzel Kişi, 2)\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S21\"] + (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S22\"] - df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S24\"]) + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S30\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S34\"])"
  ],
  "indicator_hints": [],
  "notes": ""
}
