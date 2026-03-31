---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S49:667f7861584f
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S49:667f7861584f
title: Semantic proposal for TP.YIOSBAPIYDEG.S49
status: approved
target_type: series
target_id: evds:TP.YIOSBAPIYDEG.S49
ticker: TP.YIOSBAPIYDEG.S49
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.C.1.3.Genel Yönetim (S.13) (Diğer Finansal Aracı İhraçları)
candidate_unit: milyon TL
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
evidence_fingerprint: 667f7861584f29064fc1f17ee6f871914babd60a
catalog_record_id: catalog:evds2:TP.YIOSBAPIYDEG.S49
memory_rule_ids: []
evidence:
  ticker: TP.YIOSBAPIYDEG.S49
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç
    Edilen)
  context_title: Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen)
  frequency: weekly
  unit: milyon TL
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
    id: catalog:evds2:TP.YIOSBAPIYDEG.S49
    title: 1.C.1.3.Genel Yönetim (S.13) (Diğer Finansal Aracı İhraçları)
    frequency: weekly
    unit: milyon TL
    data_group: bie_yiosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YIOSBAPIYDEG.S40'', ''TP.YIOSBAPIYDEG.S41'', ''TP.YIOSBAPIYDEG.S43'', ''TP.YIOSBAPIYDEG.S49'',
    ''TP.YIOSBAPIYDEG.S54'', #özel sektör tahvil TL - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Tahvil (Tüzel Kişi, 3)"] = df_yi_yerlesik["TP_YIOSBAPIYDEG_S40"]
    + (df_yi_yerlesik["TP_YIOSBAPIYDEG_S41"] - df_yi_yerlesik["TP_YIOSBAPIYDEG_S43"])
    + df_yi_yerlesik["TP_YIOSBAPIYDEG_S49"] + df_yi_yerlesik["TP_YIOSBAPIYDEG_S54"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YIOSBAPIYDEG.S49
promoted_memory_rule_id: memory:global-tp-yiosbapiydeg-s49
notes: 'Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S49'
body: "# Semantic proposal for TP.YIOSBAPIYDEG.S49\n\n## Target\nseries | evds:TP.YIOSBAPIYDEG.S49\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.C.1.3.Genel Yönetim\
  \ (S.13) (Diğer Finansal Aracı İhraçları)\n\n## Candidate Unit\nmilyon TL\n\n##\
  \ Candidate Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n\
  0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.YIOSBAPIYDEG.S49\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YIOSBAPIYDEG.S49\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Genel Yönetim (S.13) (Diğer\
  \ Finansal Aracılar Tarafından İhraç Edilen)\",\n  \"context_title\": \"Genel Yönetim\
  \ (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen)\",\n  \"frequency\":\
  \ \"weekly\",\n  \"unit\": \"milyon TL\",\n  \"role\": \"stock_component\",\n  \"\
  status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YIOSBAPIYDEG.S49\"\
  ,\n    \"title\": \"1.C.1.3.Genel Yönetim (S.13) (Diğer Finansal Aracı İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon TL\",\n    \"data_group\"\
  : \"bie_yiosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ İÇİ BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YIOSBAPIYDEG.S40', 'TP.YIOSBAPIYDEG.S41', 'TP.YIOSBAPIYDEG.S43',\
  \ 'TP.YIOSBAPIYDEG.S49', 'TP.YIOSBAPIYDEG.S54', #özel sektör tahvil TL - tüzel kişiler\"\
  ,\n    \"df_yi_yerlesik[\\\"Özel Sektör Tahvil (Tüzel Kişi, 3)\\\"] = df_yi_yerlesik[\\\
  \"TP_YIOSBAPIYDEG_S40\\\"] + (df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S41\\\"] - df_yi_yerlesik[\\\
  \"TP_YIOSBAPIYDEG_S43\\\"]) + df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S49\\\"] + df_yi_yerlesik[\\\
  \"TP_YIOSBAPIYDEG_S54\\\"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\
  \n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YIOSBAPIYDEG_S49%3A667f7861584f.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YIOSBAPIYDEG.S49

## Target
series | evds:TP.YIOSBAPIYDEG.S49

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.C.1.3.Genel Yönetim (S.13) (Diğer Finansal Aracı İhraçları)

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
Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S49

## Evidence
{
  "ticker": "TP.YIOSBAPIYDEG.S49",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen)",
  "context_title": "Genel Yönetim (S.13) (Diğer Finansal Aracılar Tarafından İhraç Edilen)",
  "frequency": "weekly",
  "unit": "milyon TL",
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
    "id": "catalog:evds2:TP.YIOSBAPIYDEG.S49",
    "title": "1.C.1.3.Genel Yönetim (S.13) (Diğer Finansal Aracı İhraçları)",
    "frequency": "weekly",
    "unit": "milyon TL",
    "data_group": "bie_yiosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YIOSBAPIYDEG.S40', 'TP.YIOSBAPIYDEG.S41', 'TP.YIOSBAPIYDEG.S43', 'TP.YIOSBAPIYDEG.S49', 'TP.YIOSBAPIYDEG.S54', #özel sektör tahvil TL - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Tahvil (Tüzel Kişi, 3)\"] = df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S40\"] + (df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S41\"] - df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S43\"]) + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S49\"] + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S54\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
