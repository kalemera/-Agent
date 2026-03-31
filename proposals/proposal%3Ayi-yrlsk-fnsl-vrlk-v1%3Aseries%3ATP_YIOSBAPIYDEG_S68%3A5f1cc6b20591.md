---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S68:5f1cc6b20591
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S68:5f1cc6b20591
title: Semantic proposal for TP.YIOSBAPIYDEG.S68
status: approved
target_type: series
target_id: evds:TP.YIOSBAPIYDEG.S68
ticker: TP.YIOSBAPIYDEG.S68
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.D.1.3.Genel Yönetim (S.13) (Finansal Yardımcı İhraçları)
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
evidence_fingerprint: 5f1cc6b20591805d62f4235ad4e4b674de779f87
catalog_record_id: catalog:evds2:TP.YIOSBAPIYDEG.S68
memory_rule_ids: []
evidence:
  ticker: TP.YIOSBAPIYDEG.S68
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç
    Edilen)
  context_title: Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen)
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
    id: catalog:evds2:TP.YIOSBAPIYDEG.S68
    title: 1.D.1.3.Genel Yönetim (S.13) (Finansal Yardımcı İhraçları)
    frequency: weekly
    unit: milyon TL
    data_group: bie_yiosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YIOSBAPIYDEG.S59'', ''TP.YIOSBAPIYDEG.S60'', ''TP.YIOSBAPIYDEG.S62'', ''TP.YIOSBAPIYDEG.S68'',
    ''TP.YIOSBAPIYDEG.S74'', #özel sektör tahvil TL - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Tahvil (Tüzel Kişi, 4)"] = df_yi_yerlesik["TP_YIOSBAPIYDEG_S59"]
    + (df_yi_yerlesik["TP_YIOSBAPIYDEG_S60"] - df_yi_yerlesik["TP_YIOSBAPIYDEG_S62"])
    + df_yi_yerlesik["TP_YIOSBAPIYDEG_S68"] + df_yi_yerlesik["TP_YIOSBAPIYDEG_S74"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YIOSBAPIYDEG.S68
promoted_memory_rule_id: memory:global-tp-yiosbapiydeg-s68
notes: 'Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S68'
body: "# Semantic proposal for TP.YIOSBAPIYDEG.S68\n\n## Target\nseries | evds:TP.YIOSBAPIYDEG.S68\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.D.1.3.Genel Yönetim\
  \ (S.13) (Finansal Yardımcı İhraçları)\n\n## Candidate Unit\nmilyon TL\n\n## Candidate\
  \ Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n0.9\n\
  \n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.YIOSBAPIYDEG.S68\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YIOSBAPIYDEG.S68\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Genel Yönetim (S.13) (Finansal\
  \ Yardımcılar Tarafından İhraç Edilen)\",\n  \"context_title\": \"Genel Yönetim\
  \ (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen)\",\n  \"frequency\": \"\
  weekly\",\n  \"unit\": \"milyon TL\",\n  \"role\": \"stock_component\",\n  \"status\"\
  : \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YIOSBAPIYDEG.S68\"\
  ,\n    \"title\": \"1.D.1.3.Genel Yönetim (S.13) (Finansal Yardımcı İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon TL\",\n    \"data_group\"\
  : \"bie_yiosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ İÇİ BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YIOSBAPIYDEG.S59', 'TP.YIOSBAPIYDEG.S60', 'TP.YIOSBAPIYDEG.S62',\
  \ 'TP.YIOSBAPIYDEG.S68', 'TP.YIOSBAPIYDEG.S74', #özel sektör tahvil TL - tüzel kişiler\"\
  ,\n    \"df_yi_yerlesik[\\\"Özel Sektör Tahvil (Tüzel Kişi, 4)\\\"] = df_yi_yerlesik[\\\
  \"TP_YIOSBAPIYDEG_S59\\\"] + (df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S60\\\"] - df_yi_yerlesik[\\\
  \"TP_YIOSBAPIYDEG_S62\\\"]) + df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S68\\\"] + df_yi_yerlesik[\\\
  \"TP_YIOSBAPIYDEG_S74\\\"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\
  \n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YIOSBAPIYDEG_S68%3A5f1cc6b20591.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YIOSBAPIYDEG.S68

## Target
series | evds:TP.YIOSBAPIYDEG.S68

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.D.1.3.Genel Yönetim (S.13) (Finansal Yardımcı İhraçları)

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
Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S68

## Evidence
{
  "ticker": "TP.YIOSBAPIYDEG.S68",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen)",
  "context_title": "Genel Yönetim (S.13) (Finansal Yardımcılar Tarafından İhraç Edilen)",
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
    "id": "catalog:evds2:TP.YIOSBAPIYDEG.S68",
    "title": "1.D.1.3.Genel Yönetim (S.13) (Finansal Yardımcı İhraçları)",
    "frequency": "weekly",
    "unit": "milyon TL",
    "data_group": "bie_yiosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YIOSBAPIYDEG.S59', 'TP.YIOSBAPIYDEG.S60', 'TP.YIOSBAPIYDEG.S62', 'TP.YIOSBAPIYDEG.S68', 'TP.YIOSBAPIYDEG.S74', #özel sektör tahvil TL - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Tahvil (Tüzel Kişi, 4)\"] = df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S59\"] + (df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S60\"] - df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S62\"]) + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S68\"] + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S74\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
