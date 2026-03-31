---
record_type: proposal
id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S55:246104b5beb3
proposal_id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S55:246104b5beb3
title: Semantic proposal for TP.YDOSBAYAZDEG.S55
status: approved
target_type: series
target_id: evds:TP.YDOSBAYAZDEG.S55
ticker: TP.YDOSBAYAZDEG.S55
notebook_slug: eurobnd-blg-v4
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Eurobnd_Blg_V4.ipynb
candidate_title: 1.C.2.Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracı İhraçları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:eurobond
- theme:external-financing
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 246104b5beb398d9f2bb3487d52261ce79269df7
catalog_record_id: catalog:evds2:TP.YDOSBAYAZDEG.S55
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAYAZDEG.S55
  notebook_slug: eurobnd-blg-v4
  official_series_name: Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından
    İhraç Edilen)
  context_title: Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından İhraç
    Edilen)
  frequency: weekly
  unit: milyon ABD doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:eurobond
  - theme:external-financing
  indicator_ids: []
  source_dependency_ids:
  - source:eurobnd-bbg-upload
  - source:eurobnd-tcmb-vade-pdf
  - source:eurobnd-hmb-odeme-projeksiyonu
  catalog_record:
    id: catalog:evds2:TP.YDOSBAYAZDEG.S55
    title: 1.C.2.Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracı İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbayazdeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.EBONDYAZDEG.S2D'', ''TP.YDOSBAYAZDEG.S19'', ''TP.YDOSBAYAZDEG.S38'', ''TP.YDOSBAYAZDEG.S55'','
  - df_eurobond["Özel Sektör Eurobond Yabancılar"] = df_eurobond["TP_YDOSBAYAZDEG_S19"]
    + df_eurobond["TP_YDOSBAYAZDEG_S38"] + df_eurobond["TP_YDOSBAYAZDEG_S55"] + df_eurobond["TP_YDOSBAYAZDEG_S76"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAYAZDEG.S55
promoted_memory_rule_id: memory:global-tp-ydosbayazdeg-s55
notes: 'Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S55'
body: "# Semantic proposal for TP.YDOSBAYAZDEG.S55\n\n## Target\nseries | evds:TP.YDOSBAYAZDEG.S55\n\
  \n## Notebook\neurobnd-blg-v4\n\n## Candidate Title\n1.C.2.Dünyanın Geri Kalanı\
  \ (S.2) (Diğer Finansal Aracı İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\
  \n## Candidate Frequency\nweekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n\
  0.9\n\n## Candidate Themes\n- theme:eurobond\n- theme:external-financing\n\n## Candidate\
  \ Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval\
  \ Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog\
  \ source: catalog:evds2:TP.YDOSBAYAZDEG.S55\n\n## Evidence\n{\n  \"ticker\": \"\
  TP.YDOSBAYAZDEG.S55\",\n  \"notebook_slug\": \"eurobnd-blg-v4\",\n  \"official_series_name\"\
  : \"Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)\"\
  ,\n  \"context_title\": \"Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından\
  \ İhraç Edilen)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\"\
  ,\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:eurobond\",\n    \"theme:external-financing\"\n  ],\n  \"indicator_ids\"\
  : [],\n  \"source_dependency_ids\": [\n    \"source:eurobnd-bbg-upload\",\n    \"\
  source:eurobnd-tcmb-vade-pdf\",\n    \"source:eurobnd-hmb-odeme-projeksiyonu\"\n\
  \  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YDOSBAYAZDEG.S55\"\
  ,\n    \"title\": \"1.C.2.Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracı İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_ydosbayazdeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN\
  \ YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.EBONDYAZDEG.S2D', 'TP.YDOSBAYAZDEG.S19', 'TP.YDOSBAYAZDEG.S38', 'TP.YDOSBAYAZDEG.S55',\"\
  ,\n    \"df_eurobond[\\\"Özel Sektör Eurobond Yabancılar\\\"] = df_eurobond[\\\"\
  TP_YDOSBAYAZDEG_S19\\\"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S38\\\"] + df_eurobond[\\\
  \"TP_YDOSBAYAZDEG_S55\\\"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S76\\\"]\"\n  ],\n\
  \  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aeurobnd-blg-v4%3Aseries%3ATP_YDOSBAYAZDEG_S55%3A246104b5beb3.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAYAZDEG.S55

## Target
series | evds:TP.YDOSBAYAZDEG.S55

## Notebook
eurobnd-blg-v4

## Candidate Title
1.C.2.Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracı İhraçları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.9

## Candidate Themes
- theme:eurobond
- theme:external-financing

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
Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S55

## Evidence
{
  "ticker": "TP.YDOSBAYAZDEG.S55",
  "notebook_slug": "eurobnd-blg-v4",
  "official_series_name": "Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)",
  "context_title": "Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:eurobond",
    "theme:external-financing"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:eurobnd-bbg-upload",
    "source:eurobnd-tcmb-vade-pdf",
    "source:eurobnd-hmb-odeme-projeksiyonu"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.YDOSBAYAZDEG.S55",
    "title": "1.C.2.Dünyanın Geri Kalanı (S.2) (Diğer Finansal Aracı İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbayazdeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.EBONDYAZDEG.S2D', 'TP.YDOSBAYAZDEG.S19', 'TP.YDOSBAYAZDEG.S38', 'TP.YDOSBAYAZDEG.S55',",
    "df_eurobond[\"Özel Sektör Eurobond Yabancılar\"] = df_eurobond[\"TP_YDOSBAYAZDEG_S19\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S38\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S55\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S76\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
