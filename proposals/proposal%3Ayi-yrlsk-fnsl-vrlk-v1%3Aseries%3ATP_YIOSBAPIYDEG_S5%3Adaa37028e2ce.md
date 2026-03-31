---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S5:daa37028e2ce
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YIOSBAPIYDEG_S5:daa37028e2ce
title: Semantic proposal for TP.YIOSBAPIYDEG.S5
status: approved
target_type: series
target_id: evds:TP.YIOSBAPIYDEG.S5
ticker: TP.YIOSBAPIYDEG.S5
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.A.1.2.2.Bankalar (S.122) (Finansal Olmayan Kuruluş İhraçları)
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
evidence_fingerprint: daa37028e2ce4e03e3cf5aa44d73da22efe0bdfb
catalog_record_id: catalog:evds2:TP.YIOSBAPIYDEG.S5
memory_rule_ids: []
evidence:
  ticker: TP.YIOSBAPIYDEG.S5
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen)
  context_title: Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen)
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
    id: catalog:evds2:TP.YIOSBAPIYDEG.S5
    title: 1.A.1.2.2.Bankalar (S.122) (Finansal Olmayan Kuruluş İhraçları)
    frequency: weekly
    unit: milyon TL
    data_group: bie_yiosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YIOSBAPIYDEG.S15'', ''TP.YIOSBAPIYDEG.S34'', ''TP.YIOSBAPIYDEG.S53'', ''TP.YIOSBAPIYDEG.S72'',
    #özel sektör tahvil TL - gerçek kişiler'
  - '''TP.YIOSBAPIYDEG.S2'', ''TP.YIOSBAPIYDEG.S3'', ''TP.YIOSBAPIYDEG.S5'', ''TP.YIOSBAPIYDEG.S11'',
    ''TP.YIOSBAPIYDEG.S16'', #özel sektör tahvil TL - tüzel kişiler'
  - '''TP.YIOSBAPIYDEG.S40'', ''TP.YIOSBAPIYDEG.S41'', ''TP.YIOSBAPIYDEG.S43'', ''TP.YIOSBAPIYDEG.S49'',
    ''TP.YIOSBAPIYDEG.S54'', #özel sektör tahvil TL - tüzel kişiler'
  - '''TP.YIOSBAPIYDEG.S59'', ''TP.YIOSBAPIYDEG.S60'', ''TP.YIOSBAPIYDEG.S62'', ''TP.YIOSBAPIYDEG.S68'',
    ''TP.YIOSBAPIYDEG.S74'', #özel sektör tahvil TL - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Tahvil (Gerçek Kişi)"] = df_yi_yerlesik["TP_YIOSBAPIYDEG_S15"]
    + df_yi_yerlesik["TP_YIOSBAPIYDEG_S34"] + df_yi_yerlesik["TP_YIOSBAPIYDEG_S53"]
    + df_yi_yerlesik["TP_YIOSBAPIYDEG_S72"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YIOSBAPIYDEG.S5
promoted_memory_rule_id: memory:global-tp-yiosbapiydeg-s5
notes: 'Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S5'
body: "# Semantic proposal for TP.YIOSBAPIYDEG.S5\n\n## Target\nseries | evds:TP.YIOSBAPIYDEG.S5\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.A.1.2.2.Bankalar (S.122)\
  \ (Finansal Olmayan Kuruluş İhraçları)\n\n## Candidate Unit\nmilyon TL\n\n## Candidate\
  \ Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n0.9\n\
  \n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.YIOSBAPIYDEG.S5\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YIOSBAPIYDEG.S5\",\n  \"notebook_slug\": \"\
  yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\": \"Bankalar (S.122) (Finansal\
  \ Olmayan Kuruluşlarca İhraç Edilen)\",\n  \"context_title\": \"Bankalar (S.122)\
  \ (Finansal Olmayan Kuruluşlarca İhraç Edilen)\",\n  \"frequency\": \"weekly\",\n\
  \  \"unit\": \"milyon TL\",\n  \"role\": \"stock_component\",\n  \"status\": \"\
  derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\",\n\
  \    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n  \"\
  indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YIOSBAPIYDEG.S5\"\
  ,\n    \"title\": \"1.A.1.2.2.Bankalar (S.122) (Finansal Olmayan Kuruluş İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon TL\",\n    \"data_group\"\
  : \"bie_yiosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ İÇİ BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YIOSBAPIYDEG.S15', 'TP.YIOSBAPIYDEG.S34', 'TP.YIOSBAPIYDEG.S53',\
  \ 'TP.YIOSBAPIYDEG.S72', #özel sektör tahvil TL - gerçek kişiler\",\n    \"'TP.YIOSBAPIYDEG.S2',\
  \ 'TP.YIOSBAPIYDEG.S3', 'TP.YIOSBAPIYDEG.S5', 'TP.YIOSBAPIYDEG.S11', 'TP.YIOSBAPIYDEG.S16',\
  \ #özel sektör tahvil TL - tüzel kişiler\",\n    \"'TP.YIOSBAPIYDEG.S40', 'TP.YIOSBAPIYDEG.S41',\
  \ 'TP.YIOSBAPIYDEG.S43', 'TP.YIOSBAPIYDEG.S49', 'TP.YIOSBAPIYDEG.S54', #özel sektör\
  \ tahvil TL - tüzel kişiler\",\n    \"'TP.YIOSBAPIYDEG.S59', 'TP.YIOSBAPIYDEG.S60',\
  \ 'TP.YIOSBAPIYDEG.S62', 'TP.YIOSBAPIYDEG.S68', 'TP.YIOSBAPIYDEG.S74', #özel sektör\
  \ tahvil TL - tüzel kişiler\",\n    \"df_yi_yerlesik[\\\"Özel Sektör Tahvil (Gerçek\
  \ Kişi)\\\"] = df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S15\\\"] + df_yi_yerlesik[\\\"\
  TP_YIOSBAPIYDEG_S34\\\"] + df_yi_yerlesik[\\\"TP_YIOSBAPIYDEG_S53\\\"] + df_yi_yerlesik[\\\
  \"TP_YIOSBAPIYDEG_S72\\\"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\
  \n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YIOSBAPIYDEG_S5%3Adaa37028e2ce.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YIOSBAPIYDEG.S5

## Target
series | evds:TP.YIOSBAPIYDEG.S5

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.A.1.2.2.Bankalar (S.122) (Finansal Olmayan Kuruluş İhraçları)

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
Catalog source: catalog:evds2:TP.YIOSBAPIYDEG.S5

## Evidence
{
  "ticker": "TP.YIOSBAPIYDEG.S5",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
  "context_title": "Bankalar (S.122) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
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
    "id": "catalog:evds2:TP.YIOSBAPIYDEG.S5",
    "title": "1.A.1.2.2.Bankalar (S.122) (Finansal Olmayan Kuruluş İhraçları)",
    "frequency": "weekly",
    "unit": "milyon TL",
    "data_group": "bie_yiosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT İÇİ BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YIOSBAPIYDEG.S15', 'TP.YIOSBAPIYDEG.S34', 'TP.YIOSBAPIYDEG.S53', 'TP.YIOSBAPIYDEG.S72', #özel sektör tahvil TL - gerçek kişiler",
    "'TP.YIOSBAPIYDEG.S2', 'TP.YIOSBAPIYDEG.S3', 'TP.YIOSBAPIYDEG.S5', 'TP.YIOSBAPIYDEG.S11', 'TP.YIOSBAPIYDEG.S16', #özel sektör tahvil TL - tüzel kişiler",
    "'TP.YIOSBAPIYDEG.S40', 'TP.YIOSBAPIYDEG.S41', 'TP.YIOSBAPIYDEG.S43', 'TP.YIOSBAPIYDEG.S49', 'TP.YIOSBAPIYDEG.S54', #özel sektör tahvil TL - tüzel kişiler",
    "'TP.YIOSBAPIYDEG.S59', 'TP.YIOSBAPIYDEG.S60', 'TP.YIOSBAPIYDEG.S62', 'TP.YIOSBAPIYDEG.S68', 'TP.YIOSBAPIYDEG.S74', #özel sektör tahvil TL - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Tahvil (Gerçek Kişi)\"] = df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S15\"] + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S34\"] + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S53\"] + df_yi_yerlesik[\"TP_YIOSBAPIYDEG_S72\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
