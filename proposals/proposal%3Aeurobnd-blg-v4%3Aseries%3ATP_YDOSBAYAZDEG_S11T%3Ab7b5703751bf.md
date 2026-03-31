---
record_type: proposal
id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S11T:b7b5703751bf
proposal_id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S11T:b7b5703751bf
title: Semantic proposal for TP.YDOSBAYAZDEG.S11T
status: approved
target_type: series
target_id: evds:TP.YDOSBAYAZDEG.S11T
ticker: TP.YDOSBAYAZDEG.S11T
notebook_slug: eurobnd-blg-v4
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Eurobnd_Blg_V4.ipynb
candidate_title: 1.A.Toplam (S.1, S.2) (Finansal Olmayan Kuruluş İhraçları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:eurobond
- theme:external-financing
candidate_indicator_inputs:
- derived:eurobond-total-stock
- derived:eurobond-foreign-share
- derived:ozel-sektor-eurobond-total
- derived:ozel-sektor-eurobond-foreign-share
candidate_formula_hint: 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci
  stoklarinin toplam stoga orani.'
confidence: 0.95
source: heuristic
evidence_fingerprint: b7b5703751bfebdc69c304e36a462e58b742238c
catalog_record_id: catalog:evds2:TP.YDOSBAYAZDEG.S11T
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAYAZDEG.S11T
  notebook_slug: eurobnd-blg-v4
  official_series_name: Toplam (S.1, S.2) (Finansal Olmayan Kuruluşlarca İhraç Edilen)
  context_title: Toplam (S.1, S.2) (Finansal Olmayan Kuruluşlarca İhraç Edilen)
  frequency: weekly
  unit: milyon ABD doları
  role: stock_total
  status: derived_input
  theme_ids:
  - theme:eurobond
  - theme:external-financing
  indicator_ids:
  - derived:eurobond-total-stock
  - derived:eurobond-foreign-share
  - derived:ozel-sektor-eurobond-total
  - derived:ozel-sektor-eurobond-foreign-share
  source_dependency_ids:
  - source:eurobnd-bbg-upload
  - source:eurobnd-tcmb-vade-pdf
  - source:eurobnd-hmb-odeme-projeksiyonu
  catalog_record:
    id: catalog:evds2:TP.YDOSBAYAZDEG.S11T
    title: 1.A.Toplam (S.1, S.2) (Finansal Olmayan Kuruluş İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbayazdeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAYAZDEG.S76'', ''TP.EBONDYAZDEG.ST'', ''TP.YDOSBAYAZDEG.S11T'', ''TP.YDOSBAYAZDEG.S122T'','
  - df_eurobond["Özel Sektör Eurobond Toplam"] = df_eurobond["TP_YDOSBAYAZDEG_S11T"]
    + df_eurobond["TP_YDOSBAYAZDEG_S122T"] + df_eurobond["TP_YDOSBAYAZDEG_S125T"]
    + df_eurobond["TP_YDOSBAYAZDEG_S126T"]
  indicator_hints:
  - 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam
    stoga orani.'
  - 'derived:ozel-sektor-eurobond-foreign-share: evds:TP.YDOSBAYAZDEG.S19 / evds:TP.YDOSBAYAZDEG.S11T'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAYAZDEG.S11T
promoted_memory_rule_id: memory:global-tp-ydosbayazdeg-s11t
notes: 'Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S11T'
body: "# Semantic proposal for TP.YDOSBAYAZDEG.S11T\n\n## Target\nseries | evds:TP.YDOSBAYAZDEG.S11T\n\
  \n## Notebook\neurobnd-blg-v4\n\n## Candidate Title\n1.A.Toplam (S.1, S.2) (Finansal\
  \ Olmayan Kuruluş İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate\
  \ Frequency\nweekly\n\n## Candidate Role\nstock_total\n\n## Confidence\n0.95\n\n\
  ## Candidate Themes\n- theme:eurobond\n- theme:external-financing\n\n## Candidate\
  \ Indicator Inputs\n- derived:eurobond-total-stock\n- derived:eurobond-foreign-share\n\
  - derived:ozel-sektor-eurobond-total\n- derived:ozel-sektor-eurobond-foreign-share\n\
  \n## Formula Hint\nderived:eurobond-foreign-share: Hazine ve ozel sektor yabanci\
  \ stoklarinin toplam stoga orani.\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.YDOSBAYAZDEG.S11T\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YDOSBAYAZDEG.S11T\",\n  \"notebook_slug\":\
  \ \"eurobnd-blg-v4\",\n  \"official_series_name\": \"Toplam (S.1, S.2) (Finansal\
  \ Olmayan Kuruluşlarca İhraç Edilen)\",\n  \"context_title\": \"Toplam (S.1, S.2)\
  \ (Finansal Olmayan Kuruluşlarca İhraç Edilen)\",\n  \"frequency\": \"weekly\",\n\
  \  \"unit\": \"milyon ABD doları\",\n  \"role\": \"stock_total\",\n  \"status\"\
  : \"derived_input\",\n  \"theme_ids\": [\n    \"theme:eurobond\",\n    \"theme:external-financing\"\
  \n  ],\n  \"indicator_ids\": [\n    \"derived:eurobond-total-stock\",\n    \"derived:eurobond-foreign-share\"\
  ,\n    \"derived:ozel-sektor-eurobond-total\",\n    \"derived:ozel-sektor-eurobond-foreign-share\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:eurobnd-bbg-upload\",\n   \
  \ \"source:eurobnd-tcmb-vade-pdf\",\n    \"source:eurobnd-hmb-odeme-projeksiyonu\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YDOSBAYAZDEG.S11T\"\
  ,\n    \"title\": \"1.A.Toplam (S.1, S.2) (Finansal Olmayan Kuruluş İhraçları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_ydosbayazdeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN\
  \ YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YDOSBAYAZDEG.S76', 'TP.EBONDYAZDEG.ST', 'TP.YDOSBAYAZDEG.S11T', 'TP.YDOSBAYAZDEG.S122T',\"\
  ,\n    \"df_eurobond[\\\"Özel Sektör Eurobond Toplam\\\"] = df_eurobond[\\\"TP_YDOSBAYAZDEG_S11T\\\
  \"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S122T\\\"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S125T\\\
  \"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S126T\\\"]\"\n  ],\n  \"indicator_hints\"\
  : [\n    \"derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin\
  \ toplam stoga orani.\",\n    \"derived:ozel-sektor-eurobond-foreign-share: evds:TP.YDOSBAYAZDEG.S19\
  \ / evds:TP.YDOSBAYAZDEG.S11T\"\n  ],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Aeurobnd-blg-v4%3Aseries%3ATP_YDOSBAYAZDEG_S11T%3Ab7b5703751bf.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAYAZDEG.S11T

## Target
series | evds:TP.YDOSBAYAZDEG.S11T

## Notebook
eurobnd-blg-v4

## Candidate Title
1.A.Toplam (S.1, S.2) (Finansal Olmayan Kuruluş İhraçları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_total

## Confidence
0.95

## Candidate Themes
- theme:eurobond
- theme:external-financing

## Candidate Indicator Inputs
- derived:eurobond-total-stock
- derived:eurobond-foreign-share
- derived:ozel-sektor-eurobond-total
- derived:ozel-sektor-eurobond-foreign-share

## Formula Hint
derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S11T

## Evidence
{
  "ticker": "TP.YDOSBAYAZDEG.S11T",
  "notebook_slug": "eurobnd-blg-v4",
  "official_series_name": "Toplam (S.1, S.2) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
  "context_title": "Toplam (S.1, S.2) (Finansal Olmayan Kuruluşlarca İhraç Edilen)",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_total",
  "status": "derived_input",
  "theme_ids": [
    "theme:eurobond",
    "theme:external-financing"
  ],
  "indicator_ids": [
    "derived:eurobond-total-stock",
    "derived:eurobond-foreign-share",
    "derived:ozel-sektor-eurobond-total",
    "derived:ozel-sektor-eurobond-foreign-share"
  ],
  "source_dependency_ids": [
    "source:eurobnd-bbg-upload",
    "source:eurobnd-tcmb-vade-pdf",
    "source:eurobnd-hmb-odeme-projeksiyonu"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.YDOSBAYAZDEG.S11T",
    "title": "1.A.Toplam (S.1, S.2) (Finansal Olmayan Kuruluş İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbayazdeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAYAZDEG.S76', 'TP.EBONDYAZDEG.ST', 'TP.YDOSBAYAZDEG.S11T', 'TP.YDOSBAYAZDEG.S122T',",
    "df_eurobond[\"Özel Sektör Eurobond Toplam\"] = df_eurobond[\"TP_YDOSBAYAZDEG_S11T\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S122T\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S125T\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S126T\"]"
  ],
  "indicator_hints": [
    "derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.",
    "derived:ozel-sektor-eurobond-foreign-share: evds:TP.YDOSBAYAZDEG.S19 / evds:TP.YDOSBAYAZDEG.S11T"
  ],
  "notes": ""
}
