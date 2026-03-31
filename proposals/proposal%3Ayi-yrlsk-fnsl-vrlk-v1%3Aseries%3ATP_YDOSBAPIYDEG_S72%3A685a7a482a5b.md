---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S72:685a7a482a5b
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S72:685a7a482a5b
title: Semantic proposal for TP.YDOSBAPIYDEG.S72
status: approved
target_type: series
target_id: evds:TP.YDOSBAPIYDEG.S72
ticker: TP.YDOSBAPIYDEG.S72
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.D.1.4.Hanehalkı (S.14) (Finansal Yardımcı İhraçları)
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
evidence_fingerprint: 685a7a482a5b0e58bf060bcc8fc2023d86bd4819
catalog_record_id: catalog:evds2:TP.YDOSBAPIYDEG.S72
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAPIYDEG.S72
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen)
  context_title: Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen)
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
    id: catalog:evds2:TP.YDOSBAPIYDEG.S72
    title: 1.D.1.4.Hanehalkı (S.14) (Finansal Yardımcı İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAPIYDEG.S15'', ''TP.YDOSBAPIYDEG.S34'', ''TP.YDOSBAPIYDEG.S53'', ''TP.YDOSBAPIYDEG.S72'',
    #özel sektör eurobond - gerçek kişiler'
  - df_yi_yerlesik["Özel Sektör Eurobond (Gerçek Kişi)"] = df_yi_yerlesik['TP_DK_USD_A_YTL']
    * (df_yi_yerlesik["TP_YDOSBAPIYDEG_S15"] + df_yi_yerlesik["TP_YDOSBAPIYDEG_S34"]
    + df_yi_yerlesik["TP_YDOSBAPIYDEG_S53"] + df_yi_yerlesik["TP_YDOSBAPIYDEG_S72"])
  - '#      df_mevduat[''TP_YDOSBAPIYDEG_S59''] + df_mevduat[''TP_YDOSBAPIYDEG_S72'']
    #+ df_mevduat[''TP_YDOSBAPIYDEG_S73'']'
  indicator_hints: []
  notes: Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak
    'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAPIYDEG.S72
promoted_memory_rule_id: memory:global-tp-ydosbapiydeg-s72
notes: 'Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S72 | Notebookta diger hanehalki
  alt kirilimlariyla birlikte USD/TL ile carpilarak ''Ozel Sektor Eurobond (Gercek
  Kisi)'' hesabinda kullaniliyor.'
body: "# Semantic proposal for TP.YDOSBAPIYDEG.S72\n\n## Target\nseries | evds:TP.YDOSBAPIYDEG.S72\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.D.1.4.Hanehalkı (S.14)\
  \ (Finansal Yardımcı İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate\
  \ Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n0.9\n\
  \n## Candidate Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n\
  - theme:resident-deposits\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n-\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.YDOSBAPIYDEG.S72 | Notebookta diger hanehalki\
  \ alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek\
  \ Kisi)' hesabinda kullaniliyor.\n\n## Evidence\n{\n  \"ticker\": \"TP.YDOSBAPIYDEG.S72\"\
  ,\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\":\
  \ \"Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen)\",\n  \"context_title\"\
  : \"Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Milyon ABD Dolari\",\n  \"role\": \"stock_component\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:resident-financial-assets\"\
  ,\n    \"theme:resident-securities\",\n    \"theme:resident-deposits\"\n  ],\n \
  \ \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YDOSBAPIYDEG.S72\"\
  ,\n    \"title\": \"1.D.1.4.Hanehalkı (S.14) (Finansal Yardımcı İhraçları)\",\n\
  \    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_ydosbapiydeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YDOSBAPIYDEG.S15', 'TP.YDOSBAPIYDEG.S34', 'TP.YDOSBAPIYDEG.S53',\
  \ 'TP.YDOSBAPIYDEG.S72', #özel sektör eurobond - gerçek kişiler\",\n    \"df_yi_yerlesik[\\\
  \"Özel Sektör Eurobond (Gerçek Kişi)\\\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] *\
  \ (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S15\\\"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S34\\\
  \"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S53\\\"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S72\\\
  \"])\",\n    \"#      df_mevduat['TP_YDOSBAPIYDEG_S59'] + df_mevduat['TP_YDOSBAPIYDEG_S72']\
  \ #+ df_mevduat['TP_YDOSBAPIYDEG_S73']\"\n  ],\n  \"indicator_hints\": [],\n  \"\
  notes\": \"Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak\
  \ 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YDOSBAPIYDEG_S72%3A685a7a482a5b.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAPIYDEG.S72

## Target
series | evds:TP.YDOSBAPIYDEG.S72

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.D.1.4.Hanehalkı (S.14) (Finansal Yardımcı İhraçları)

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
Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S72 | Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.

## Evidence
{
  "ticker": "TP.YDOSBAPIYDEG.S72",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen)",
  "context_title": "Hanehalkı (S.14) (Finansal Yardımcılar Tarafından İhraç Edilen)",
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
    "id": "catalog:evds2:TP.YDOSBAPIYDEG.S72",
    "title": "1.D.1.4.Hanehalkı (S.14) (Finansal Yardımcı İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAPIYDEG.S15', 'TP.YDOSBAPIYDEG.S34', 'TP.YDOSBAPIYDEG.S53', 'TP.YDOSBAPIYDEG.S72', #özel sektör eurobond - gerçek kişiler",
    "df_yi_yerlesik[\"Özel Sektör Eurobond (Gerçek Kişi)\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S15\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S34\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S53\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S72\"])",
    "#      df_mevduat['TP_YDOSBAPIYDEG_S59'] + df_mevduat['TP_YDOSBAPIYDEG_S72'] #+ df_mevduat['TP_YDOSBAPIYDEG_S73']"
  ],
  "indicator_hints": [],
  "notes": "Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor."
}
