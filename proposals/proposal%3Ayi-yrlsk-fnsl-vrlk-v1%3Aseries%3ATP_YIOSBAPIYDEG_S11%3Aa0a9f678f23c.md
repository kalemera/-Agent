---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S11:a0a9f678f23c
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S11:a0a9f678f23c
title: Semantic proposal for TP.YIOSBAPIYDEG.S11
status: approved
target_type: series
target_id: evds:TP.YIOSBAPIYDEG.S11
ticker: TP.YIOSBAPIYDEG.S11
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.A.1.3.Genel Yönetim (S.13) (Finansal Olmayan Kuruluş İhraçları)
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
evidence_fingerprint: a0a9f678f23c822c4bba4b7b233627edf8ce4459
catalog_record_id: catalog:evds2:TP.YIOSBAPIYDEG.S11
memory_rule_ids: []
evidence:
  ticker: TP.YIOSBAPIYDEG.S11
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç
    Edilen)
  context_title: Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç Edilen)
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
    id: catalog:evds2:TP.YIOSBAPIYDEG.S11
    title: 1.A.1.3.Genel Yönetim (S.13) (Finansal Olmayan Kuruluş İhraçları)
    frequency: weekly
    unit: milyon TL
    data_group: bie_yiosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YIOSBAPIYDEG.S2'', ''TP.YIOSBAPIYDEG.S3'', ''TP.YIOSBAPIYDEG.S5'', ''TP.YIOSBAPIYDEG.S11'',
    ''TP.YIOSBAPIYDEG.S16'', #özel sektör tahvil TL - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Tahvil (Tüzel Kişi, 1)"] = df_yi_yerlesik["TP_YIOSBAPIYDEG_S2"]
    + (df_yi_yerlesik["TP_YIOSBAPIYDEG_S3"] - df_yi_yerlesik["TP_YIOSBAPIYDEG_S5"])
    + df_yi_yerlesik["TP_YIOSBAPIYDEG_S11"] + df_yi_yerlesik["TP_YIOSBAPIYDEG_S16"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YIOSBAPIYDEG.S11
promoted_memory_rule_id: memory:global-tp-yiosbapiydeg-s11
notes: 'Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S11'
body: "# Semantic proposal for TP.YIOSBAPIYDEG.S11\n\n## Target\nseries | evds:TP.YIOSBAPIYDEG.S11\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.A.1.3.Genel Yönetim\
  \ (S.13) (Finansal Olmayan Kuruluş İhraçları)\n\n## Candidate Unit\nmilyon TL\n\n\
  ## Candidate Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n\
  0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.YIOSBAPIYDEG.S11\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YIOSBAPIYDEG.S11\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Genel Yönetim (S.13) (Finansal\
  \ Olmayan Kuruluşlarca İhraç Edilen)\",\n  \"context_title\": \"Genel Yönetim (S.13)\
  \ (Finansal Olmayan Kuruluşlarca İhraç Edilen)\",\n  \"frequency\": \"weekly\",\n\
  \  \"unit\": \"milyon TL\",\n  \"role\": \"stock_component\",\n  \"status\": \"\
  derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\",\n\
  \    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n  \"\
  indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YIOSBAPIYDEG.S11\"\
  ,\n    \"title\": \"1.A.1.3.Genel Yönetim (S.13) (Finansal Olmayan Kuruluş İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon TL\",\n    \"data_group\"\
  : \"bie_yiosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ İÇİ BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YIOSBAPIYDEG.S2', 'TP.YIOSBAPIYDEG.S3', 'TP.YIOSBAPIYDEG.S5', 'TP.YIOSBAPIYDEG.S11',\
  \ 'TP.YIOSBAPIYDEG.S16', #özel sektör tahvil TL - tüzel kişiler\",\n    \"df_yi_yerlesik[\\\
  \"Özel Sektör Tahvil (Tüzel Kişi, 1)\\\"] = df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S2\\\
  \"] + (df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S3\\\"] - df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S5\\\
  \"]) + df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S11\\\"] + df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S16\\\
  \"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YIOSBAPIYDEG_S11%3Aa0a9f678f23c.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YIOSBAPIYDEG.S11

## Target
series | evds:TP.YIOSBAPIYDEG.S11

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.A.1.3.Genel Yönetim (S.13) (Finansal Olmayan Kuruluş İhraçları)

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
Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S11

## Evidence
{
  "ticker": "TP.YIOSBAPIYDEG.S11",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
  "context_title": "Genel Yönetim (S.13) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
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
    "id": "catalog:evds2:TP.YIOSBAPIYDEG.S11",
    "title": "1.A.1.3.Genel Yönetim (S.13) (Finansal Olmayan Kuruluş İhraçları)",
    "frequency": "weekly",
    "unit": "milyon TL",
    "data_group": "bie_yiosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YIOSBAPIYDEG.S2', 'TP.YIOSBAPIYDEG.S3', 'TP.YIOSBAPIYDEG.S5', 'TP.YIOSBAPIYDEG.S11', 'TP.YIOSBAPIYDEG.S16', #özel sektör tahvil TL - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Tahvil (Tüzel Kişi, 1)\"] = df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S2\"] + (df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S3\"] - df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S5\"]) + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S11\"] + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S16\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
