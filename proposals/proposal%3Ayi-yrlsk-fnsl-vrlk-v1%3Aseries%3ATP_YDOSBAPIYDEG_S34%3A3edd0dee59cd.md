---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S34:3edd0dee59cd
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_YDOSBAPIYDEG_S34:3edd0dee59cd
title: Semantic proposal for TP.YDOSBAPIYDEG.S34
status: approved
target_type: series
target_id: evds:TP.YDOSBAPIYDEG.S34
ticker: TP.YDOSBAPIYDEG.S34
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.B.1.4.Hanehalkı (S.14) (Banka İhraçları)
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
evidence_fingerprint: 3edd0dee59cdb4f3ac2a6dc6b82785c060791452
catalog_record_id: catalog:evds2:TP.YDOSBAPIYDEG.S34
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAPIYDEG.S34
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen)
  context_title: Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen)
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
    id: catalog:evds2:TP.YDOSBAPIYDEG.S34
    title: 1.B.1.4.Hanehalkı (S.14) (Banka İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbapiydeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAPIYDEG.S15'', ''TP.YDOSBAPIYDEG.S34'', ''TP.YDOSBAPIYDEG.S53'', ''TP.YDOSBAPIYDEG.S72'',
    #özel sektör eurobond - gerçek kişiler'
  - '''TP.YDOSBAPIYDEG.S21'', ''TP.YDOSBAPIYDEG.S22'', ''TP.YDOSBAPIYDEG.S24'', ''TP.YDOSBAPIYDEG.S30'',
    ''TP.YDOSBAPIYDEG.S34'', #özel sektör eurobond - tüzel kişiler'
  - df_yi_yerlesik["Özel Sektör Eurobond (Gerçek Kişi)"] = df_yi_yerlesik['TP_DK_USD_A_YTL']
    * (df_yi_yerlesik["TP_YDOSBAPIYDEG_S15"] + df_yi_yerlesik["TP_YDOSBAPIYDEG_S34"]
    + df_yi_yerlesik["TP_YDOSBAPIYDEG_S53"] + df_yi_yerlesik["TP_YDOSBAPIYDEG_S72"])
  - df_yi_yerlesik["Özel Sektör Eurobond (Tüzel Kişi, 2)"] = df_yi_yerlesik['TP_DK_USD_A_YTL']
    * (df_yi_yerlesik["TP_YDOSBAPIYDEG_S21"] + (df_yi_yerlesik["TP_YDOSBAPIYDEG_S22"]
    - df_yi_yerlesik["TP_YDOSBAPIYDEG_S24"]) + df_yi_yerlesik["TP_YDOSBAPIYDEG_S30"]
    + df_yi_yerlesik["TP_YDOSBAPIYDEG_S34"])
  - '#      df_mevduat[''TP_YDOSBAPIYDEG_S21''] + df_mevduat[''TP_YDOSBAPIYDEG_S34'']
    #+ df_mevduat[''TP_YDOSBAPIYDEG_S35'']'
  indicator_hints: []
  notes: Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak
    'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAPIYDEG.S34
promoted_memory_rule_id: memory:global-tp-ydosbapiydeg-s34
notes: 'Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S34 | Notebookta diger hanehalki
  alt kirilimlariyla birlikte USD/TL ile carpilarak ''Ozel Sektor Eurobond (Gercek
  Kisi)'' hesabinda kullaniliyor.'
body: "# Semantic proposal for TP.YDOSBAPIYDEG.S34\n\n## Target\nseries | evds:TP.YDOSBAPIYDEG.S34\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.B.1.4.Hanehalkı (S.14)\
  \ (Banka İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\n\
  weekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate\
  \ Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n- theme:resident-deposits\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.YDOSBAPIYDEG.S34\
  \ | Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak\
  \ 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.YDOSBAPIYDEG.S34\",\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\"\
  ,\n  \"official_series_name\": \"Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen)\"\
  ,\n  \"context_title\": \"Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen)\"\
  ,\n  \"frequency\": \"weekly\",\n  \"unit\": \"Milyon ABD Dolari\",\n  \"role\"\
  : \"stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n \
  \   \"theme:resident-financial-assets\",\n    \"theme:resident-securities\",\n \
  \   \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.YDOSBAPIYDEG.S34\",\n    \"title\": \"1.B.1.4.Hanehalkı\
  \ (S.14) (Banka İhraçları)\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  milyon ABD doları\",\n    \"data_group\": \"bie_ydosbapiydeg\",\n    \"category\"\
  : \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.YDOSBAPIYDEG.S15',\
  \ 'TP.YDOSBAPIYDEG.S34', 'TP.YDOSBAPIYDEG.S53', 'TP.YDOSBAPIYDEG.S72', #özel sektör\
  \ eurobond - gerçek kişiler\",\n    \"'TP.YDOSBAPIYDEG.S21', 'TP.YDOSBAPIYDEG.S22',\
  \ 'TP.YDOSBAPIYDEG.S24', 'TP.YDOSBAPIYDEG.S30', 'TP.YDOSBAPIYDEG.S34', #özel sektör\
  \ eurobond - tüzel kişiler\",\n    \"df_yi_yerlesik[\\\"Özel Sektör Eurobond (Gerçek\
  \ Kişi)\\\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S15\\\
  \"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S34\\\"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S53\\\
  \"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S72\\\"])\",\n    \"df_yi_yerlesik[\\\"\
  Özel Sektör Eurobond (Tüzel Kişi, 2)\\\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] *\
  \ (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S21\\\"] + (df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S22\\\
  \"] - df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S24\\\"]) + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S30\\\
  \"] + df_yi_yerlesik[\\\"TP_YDOSBAPIYDEG_S34\\\"])\",\n    \"#      df_mevduat['TP_YDOSBAPIYDEG_S21']\
  \ + df_mevduat['TP_YDOSBAPIYDEG_S34'] #+ df_mevduat['TP_YDOSBAPIYDEG_S35']\"\n \
  \ ],\n  \"indicator_hints\": [],\n  \"notes\": \"Notebookta diger hanehalki alt\
  \ kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)'\
  \ hesabinda kullaniliyor.\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_YDOSBAPIYDEG_S34%3A3edd0dee59cd.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAPIYDEG.S34

## Target
series | evds:TP.YDOSBAPIYDEG.S34

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.B.1.4.Hanehalkı (S.14) (Banka İhraçları)

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
Catalog source: catalog:evds2:TP.YDOSBAPIYDEG.S34 | Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor.

## Evidence
{
  "ticker": "TP.YDOSBAPIYDEG.S34",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen)",
  "context_title": "Hanehalkı (S.14) (Bankalar Tarafından İhraç Edilen)",
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
    "id": "catalog:evds2:TP.YDOSBAPIYDEG.S34",
    "title": "1.B.1.4.Hanehalkı (S.14) (Banka İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbapiydeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAPIYDEG.S15', 'TP.YDOSBAPIYDEG.S34', 'TP.YDOSBAPIYDEG.S53', 'TP.YDOSBAPIYDEG.S72', #özel sektör eurobond - gerçek kişiler",
    "'TP.YDOSBAPIYDEG.S21', 'TP.YDOSBAPIYDEG.S22', 'TP.YDOSBAPIYDEG.S24', 'TP.YDOSBAPIYDEG.S30', 'TP.YDOSBAPIYDEG.S34', #özel sektör eurobond - tüzel kişiler",
    "df_yi_yerlesik[\"Özel Sektör Eurobond (Gerçek Kişi)\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S15\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S34\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S53\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S72\"])",
    "df_yi_yerlesik[\"Özel Sektör Eurobond (Tüzel Kişi, 2)\"] = df_yi_yerlesik['TP_DK_USD_A_YTL'] * (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S21\"] + (df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S22\"] - df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S24\"]) + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S30\"] + df_yi_yerlesik[\"TP_YDOSBAPIYDEG_S34\"])",
    "#      df_mevduat['TP_YDOSBAPIYDEG_S21'] + df_mevduat['TP_YDOSBAPIYDEG_S34'] #+ df_mevduat['TP_YDOSBAPIYDEG_S35']"
  ],
  "indicator_hints": [],
  "notes": "Notebookta diger hanehalki alt kirilimlariyla birlikte USD/TL ile carpilarak 'Ozel Sektor Eurobond (Gercek Kisi)' hesabinda kullaniliyor."
}
