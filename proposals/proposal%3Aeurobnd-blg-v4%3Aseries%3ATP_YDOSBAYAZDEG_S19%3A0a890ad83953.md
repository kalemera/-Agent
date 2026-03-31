---
record_type: proposal
id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S19:0a890ad83953
proposal_id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S19:0a890ad83953
title: Semantic proposal for TP.YDOSBAYAZDEG.S19
status: approved
target_type: series
target_id: evds:TP.YDOSBAYAZDEG.S19
ticker: TP.YDOSBAYAZDEG.S19
notebook_slug: eurobnd-blg-v4
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Eurobnd_Blg_V4.ipynb
candidate_title: 1.A.2.2.Diğer (Finansal Olmayan Kuruluş İhraçları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:eurobond
- theme:external-financing
candidate_indicator_inputs:
- derived:eurobond-foreign-stock
- derived:eurobond-foreign-share
- derived:ozel-sektor-eurobond-foreign-stock
- derived:ozel-sektor-eurobond-foreign-share
candidate_formula_hint: 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci
  stoklarinin toplam stoga orani.'
confidence: 0.95
source: heuristic
evidence_fingerprint: 0a890ad83953a6f26c412a97ddd646494722458d
catalog_record_id: catalog:evds2:TP.YDOSBAYAZDEG.S19
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAYAZDEG.S19
  notebook_slug: eurobnd-blg-v4
  official_series_name: Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen)
  context_title: Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen)
  frequency: weekly
  unit: milyon ABD doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:eurobond
  - theme:external-financing
  indicator_ids:
  - derived:eurobond-foreign-stock
  - derived:eurobond-foreign-share
  - derived:ozel-sektor-eurobond-foreign-stock
  - derived:ozel-sektor-eurobond-foreign-share
  source_dependency_ids:
  - source:eurobnd-bbg-upload
  - source:eurobnd-tcmb-vade-pdf
  - source:eurobnd-hmb-odeme-projeksiyonu
  catalog_record:
    id: catalog:evds2:TP.YDOSBAYAZDEG.S19
    title: 1.A.2.2.Diğer (Finansal Olmayan Kuruluş İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbayazdeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.EBONDYAZDEG.S2D'', ''TP.YDOSBAYAZDEG.S19'', ''TP.YDOSBAYAZDEG.S38'', ''TP.YDOSBAYAZDEG.S55'','
  - df_eurobond["Özel Sektör Eurobond Yabancılar"] = df_eurobond["TP_YDOSBAYAZDEG_S19"]
    + df_eurobond["TP_YDOSBAYAZDEG_S38"] + df_eurobond["TP_YDOSBAYAZDEG_S55"] + df_eurobond["TP_YDOSBAYAZDEG_S76"]
  indicator_hints:
  - 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam
    stoga orani.'
  - 'derived:ozel-sektor-eurobond-foreign-share: evds:TP.YDOSBAYAZDEG.S19 / evds:TP.YDOSBAYAZDEG.S11T'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAYAZDEG.S19
promoted_memory_rule_id: memory:global-tp-ydosbayazdeg-s19
notes: 'Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S19'
body: "# Semantic proposal for TP.YDOSBAYAZDEG.S19\n\n## Target\nseries | evds:TP.YDOSBAYAZDEG.S19\n\
  \n## Notebook\neurobnd-blg-v4\n\n## Candidate Title\n1.A.2.2.Diğer (Finansal Olmayan\
  \ Kuruluş İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\n\
  weekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n0.95\n\n## Candidate\
  \ Themes\n- theme:eurobond\n- theme:external-financing\n\n## Candidate Indicator\
  \ Inputs\n- derived:eurobond-foreign-stock\n- derived:eurobond-foreign-share\n-\
  \ derived:ozel-sektor-eurobond-foreign-stock\n- derived:ozel-sektor-eurobond-foreign-share\n\
  \n## Formula Hint\nderived:eurobond-foreign-share: Hazine ve ozel sektor yabanci\
  \ stoklarinin toplam stoga orani.\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nInsufficient evidence for global safety; matching_memory_rules\
  \ and approved_series are empty; notebook_slug suggests scoping; source is heuristic.\n\
  \n## Notes\nCatalog source: catalog:evds2:TP.YDOSBAYAZDEG.S19\n\n## Evidence\n{\n\
  \  \"ticker\": \"TP.YDOSBAYAZDEG.S19\",\n  \"notebook_slug\": \"eurobnd-blg-v4\"\
  ,\n  \"official_series_name\": \"Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen)\"\
  ,\n  \"context_title\": \"Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen)\",\n\
  \  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"\
  stock_component\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"\
  theme:eurobond\",\n    \"theme:external-financing\"\n  ],\n  \"indicator_ids\":\
  \ [\n    \"derived:eurobond-foreign-stock\",\n    \"derived:eurobond-foreign-share\"\
  ,\n    \"derived:ozel-sektor-eurobond-foreign-stock\",\n    \"derived:ozel-sektor-eurobond-foreign-share\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:eurobnd-bbg-upload\",\n   \
  \ \"source:eurobnd-tcmb-vade-pdf\",\n    \"source:eurobnd-hmb-odeme-projeksiyonu\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YDOSBAYAZDEG.S19\"\
  ,\n    \"title\": \"1.A.2.2.Diğer (Finansal Olmayan Kuruluş İhraçları)\",\n    \"\
  frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_ydosbayazdeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.EBONDYAZDEG.S2D', 'TP.YDOSBAYAZDEG.S19', 'TP.YDOSBAYAZDEG.S38', 'TP.YDOSBAYAZDEG.S55',\"\
  ,\n    \"df_eurobond[\\\"Özel Sektör Eurobond Yabancılar\\\"] = df_eurobond[\\\"\
  TP_YDOSBAYAZDEG_S19\\\"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S38\\\"] + df_eurobond[\\\
  \"TP_YDOSBAYAZDEG_S55\\\"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S76\\\"]\"\n  ],\n\
  \  \"indicator_hints\": [\n    \"derived:eurobond-foreign-share: Hazine ve ozel\
  \ sektor yabanci stoklarinin toplam stoga orani.\",\n    \"derived:ozel-sektor-eurobond-foreign-share:\
  \ evds:TP.YDOSBAYAZDEG.S19 / evds:TP.YDOSBAYAZDEG.S11T\"\n  ],\n  \"notes\": \"\"\
  \n}\n"
path: proposals\proposal%3Aeurobnd-blg-v4%3Aseries%3ATP_YDOSBAYAZDEG_S19%3A0a890ad83953.md
approval_reason: Prechecked guards passed. No concrete blockers identified in payload.
  Instructions specify absence of approved_series or matching_memory_rules is not
  a blocker.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAYAZDEG.S19

## Target
series | evds:TP.YDOSBAYAZDEG.S19

## Notebook
eurobnd-blg-v4

## Candidate Title
1.A.2.2.Diğer (Finansal Olmayan Kuruluş İhraçları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.95

## Candidate Themes
- theme:eurobond
- theme:external-financing

## Candidate Indicator Inputs
- derived:eurobond-foreign-stock
- derived:eurobond-foreign-share
- derived:ozel-sektor-eurobond-foreign-stock
- derived:ozel-sektor-eurobond-foreign-share

## Formula Hint
derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
Prechecked guards passed. No concrete blockers identified in payload. Instructions specify absence of approved_series or matching_memory_rules is not a blocker.

## Notes
Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S19

## Evidence
{
  "ticker": "TP.YDOSBAYAZDEG.S19",
  "notebook_slug": "eurobnd-blg-v4",
  "official_series_name": "Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
  "context_title": "Diğer (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:eurobond",
    "theme:external-financing"
  ],
  "indicator_ids": [
    "derived:eurobond-foreign-stock",
    "derived:eurobond-foreign-share",
    "derived:ozel-sektor-eurobond-foreign-stock",
    "derived:ozel-sektor-eurobond-foreign-share"
  ],
  "source_dependency_ids": [
    "source:eurobnd-bbg-upload",
    "source:eurobnd-tcmb-vade-pdf",
    "source:eurobnd-hmb-odeme-projeksiyonu"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.YDOSBAYAZDEG.S19",
    "title": "1.A.2.2.Diğer (Finansal Olmayan Kuruluş İhraçları)",
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
  "indicator_hints": [
    "derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.",
    "derived:ozel-sektor-eurobond-foreign-share: evds:TP.YDOSBAYAZDEG.S19 / evds:TP.YDOSBAYAZDEG.S11T"
  ],
  "notes": ""
}
