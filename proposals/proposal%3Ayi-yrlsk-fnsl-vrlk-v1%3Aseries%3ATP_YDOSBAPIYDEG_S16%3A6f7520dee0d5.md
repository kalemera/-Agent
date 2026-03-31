---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S16:6f7520dee0d5
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S16:6f7520dee0d5
title: Semantic proposal for TP.YDOSBAPIYDEG.S16
status: approved
target_type: series
target_id: evds:TP.YDOSBAPIYDEG.S16
ticker: TP.YDOSBAPIYDEG.S16
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.A.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
  (Finansal Olmayan Kuruluş İhraçları)
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
evidence_fingerprint: 6f7520dee0d579fa28a2b416329381dabc1db56f
catalog_record_id: catalog:evds2:TP.YDOSBAPIYDEG.S16
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAPIYDEG.S16
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15)
    (Finansal Olmayan Kuruluşlarca İhraç Edilen)
  context_title: Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal
    Olmayan Kuruluşlarca İhraç Edilen)
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
    id: catalog:evds2:TP.YDOSBAPIYDEG.S16
    title: 1.A.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal
      Olmayan Kuruluş İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAPIYDEG.S2'', ''TP.YDOSBAPIYDEG.S3'', ''TP.YDOSBAPIYDEG.S5'', ''TP.YDOSBAPIYDEG.S11'',
    ''TP.YDOSBAPIYDEG.S16'', #özel sektör eurobond - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Eurobond (Tüzel Kişi, 1)"] = df_yi_yerlesik['TP_DK_USD_A_YTL']
    * (df_yi_yerlesik["TP_YDOSBAPIYDEG_S2"] + (df_yi_yerlesik["TP_YDOSBAPIYDEG_S3"]
    - df_yi_yerlesik["TP_YDOSBAPIYDEG_S5"]) + df_yi_yerlesik["TP_YDOSBAPIYDEG_S11"]
    + df_yi_yerlesik["TP_YDOSBAPIYDEG_S16"])
  - '#      df_mevduat[''TP_YDOSBAPIYDEG_S2''] + df_mevduat[''TP_YDOSBAPIYDEG_S15'']
    #+ df_mevduat[''TP_YDOSBAPIYDEG_S16'']'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAPIYDEG.S16
promoted_memory_rule_id: memory:global-tp-ydosbapiydeg-s16
notes: 'Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S16'
body: "# Semantic proposal for TP.YDOSBAPIYDEG.S16\n\n## Target\nseries | evds:TP.YDOSBAPIYDEG.S16\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.A.1.5.Hanehalkına\
  \ Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluş İhraçları)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:resident-financial-assets\n\
  - theme:resident-securities\n- theme:resident-deposits\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.YDOSBAPIYDEG.S16\n\n## Evidence\n{\n  \"ticker\": \"TP.YDOSBAPIYDEG.S16\"\
  ,\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\":\
  \ \"Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan\
  \ Kuruluşlarca İhraç Edilen)\",\n  \"context_title\": \"Hanehalkına Hizmet Veren\
  \ Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluşlarca İhraç Edilen)\"\
  ,\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\"\
  : \"stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n \
  \   \"theme:resident-financial-assets\",\n    \"theme:resident-securities\",\n \
  \   \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.YDOSBAPIYDEG.S16\",\n    \"title\": \"1.A.1.5.Hanehalkına\
  \ Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluş İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_ydosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN\
  \ YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YDOSBAPIYDEG.S2', 'TP.YDOSBAPIYDEG.S3', 'TP.YDOSBAPIYDEG.S5', 'TP.YDOSBAPIYDEG.S11',\
  \ 'TP.YDOSBAPIYDEG.S16', #özel sektör eurobond - tüzel kişiler\",\n    \"df_yi_yerlesik[\\\
  \"Özel Sektör Eurobond (Tüzel Kişi, 1)\\\"] = df_yi_yerlesik['TP_DK_USD_A_YTL']\
  \ * (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S2\\\"] + (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S3\\\
  \"] - df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S5\\\"]) + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S11\\\
  \"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S16\\\"])\",\n    \"#      df_mevduat['TP_YDOSBAPIYDEG_S2']\
  \ + df_mevduat['TP_YDOSBAPIYDEG_S15'] #+ df_mevduat['TP_YDOSBAPIYDEG_S16']\"\n \
  \ ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YDOSBAPIYDEG_S16%3A6f7520dee0d5.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAPIYDEG.S16

## Target
series | evds:TP.YDOSBAPIYDEG.S16

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.A.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluş İhraçları)

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
Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S16

## Evidence
{
  "ticker": "TP.YDOSBAPIYDEG.S16",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
  "context_title": "Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
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
    "id": "catalog:evds2:TP.YDOSBAPIYDEG.S16",
    "title": "1.A.1.5.Hanehalkına Hizmet Veren Kar Amacı Olmayan Kuruluşlar (S.15) (Finansal Olmayan Kuruluş İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAPIYDEG.S2', 'TP.YDOSBAPIYDEG.S3', 'TP.YDOSBAPIYDEG.S5', 'TP.YDOSBAPIYDEG.S11', 'TP.YDOSBAPIYDEG.S16', #özel sektör eurobond - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Eurobond (Tüzel Kişi, 1)\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S2\"] + (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S3\"] - df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S5\"]) + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S11\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S16\"])",
    "#      df_mevduat['TP_YDOSBAPIYDEG_S2'] + df_mevduat['TP_YDOSBAPIYDEG_S15'] #+ df_mevduat['TP_YDOSBAPIYDEG_S16']"
  ],
  "indicator_hints": [],
  "notes": ""
}
