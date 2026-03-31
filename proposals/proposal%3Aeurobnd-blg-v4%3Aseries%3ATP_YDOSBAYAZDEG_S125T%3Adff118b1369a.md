---
record_type: proposal
id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S125T:dff118b1369a
proposal_id: proposal:eurobnd-blg-v4:series:TP_YDOSBAYAZDEG_S125T:dff118b1369a
title: Semantic proposal for TP.YDOSBAYAZDEG.S125T
status: approved
target_type: series
target_id: evds:TP.YDOSBAYAZDEG.S125T
ticker: TP.YDOSBAYAZDEG.S125T
notebook_slug: eurobnd-blg-v4
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Eurobnd_Blg_V4.ipynb
candidate_title: 1.C.Toplam (S.1, S.2) (Diğer Finansal Aracı İhraçları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:eurobond
- theme:external-financing
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: dff118b1369a7db39bbaba4cb8910728b74f912e
catalog_record_id: catalog:evds2:TP.YDOSBAYAZDEG.S125T
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAYAZDEG.S125T
  notebook_slug: eurobnd-blg-v4
  official_series_name: Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç
    Edilen)
  context_title: Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)
  frequency: weekly
  unit: milyon ABD doları
  role: stock_total
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
    id: catalog:evds2:TP.YDOSBAYAZDEG.S125T
    title: 1.C.Toplam (S.1, S.2) (Diğer Finansal Aracı İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbayazdeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAYAZDEG.S125T'', ''TP.YDOSBAYAZDEG.S126T'''
  - df_eurobond["Özel Sektör Eurobond Toplam"] = df_eurobond["TP_YDOSBAYAZDEG_S11T"]
    + df_eurobond["TP_YDOSBAYAZDEG_S122T"] + df_eurobond["TP_YDOSBAYAZDEG_S125T"]
    + df_eurobond["TP_YDOSBAYAZDEG_S126T"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAYAZDEG.S125T
promoted_memory_rule_id: memory:global-tp-ydosbayazdeg-s125t
notes: 'Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S125T'
body: "# Semantic proposal for TP.YDOSBAYAZDEG.S125T\n\n## Target\nseries | evds:TP.YDOSBAYAZDEG.S125T\n\
  \n## Notebook\neurobnd-blg-v4\n\n## Candidate Title\n1.C.Toplam (S.1, S.2) (Diğer\
  \ Finansal Aracı İhraçları)\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate\
  \ Frequency\nweekly\n\n## Candidate Role\nstock_total\n\n## Confidence\n0.9\n\n\
  ## Candidate Themes\n- theme:eurobond\n- theme:external-financing\n\n## Candidate\
  \ Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval\
  \ Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog\
  \ source: catalog:evds2:TP.YDOSBAYAZDEG.S125T\n\n## Evidence\n{\n  \"ticker\": \"\
  TP.YDOSBAYAZDEG.S125T\",\n  \"notebook_slug\": \"eurobnd-blg-v4\",\n  \"official_series_name\"\
  : \"Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)\",\n  \"\
  context_title\": \"Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)\"\
  ,\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\"\
  : \"stock_total\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"\
  theme:eurobond\",\n    \"theme:external-financing\"\n  ],\n  \"indicator_ids\":\
  \ [],\n  \"source_dependency_ids\": [\n    \"source:eurobnd-bbg-upload\",\n    \"\
  source:eurobnd-tcmb-vade-pdf\",\n    \"source:eurobnd-hmb-odeme-projeksiyonu\"\n\
  \  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.YDOSBAYAZDEG.S125T\"\
  ,\n    \"title\": \"1.C.Toplam (S.1, S.2) (Diğer Finansal Aracı İhraçları)\",\n\
  \    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_ydosbayazdeg\",\n    \"category\": \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT\
  \ DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"'TP.YDOSBAYAZDEG.S125T', 'TP.YDOSBAYAZDEG.S126T'\",\n    \"df_eurobond[\\\
  \"Özel Sektör Eurobond Toplam\\\"] = df_eurobond[\\\"TP_YDOSBAYAZDEG_S11T\\\"] +\
  \ df_eurobond[\\\"TP_YDOSBAYAZDEG_S122T\\\"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S125T\\\
  \"] + df_eurobond[\\\"TP_YDOSBAYAZDEG_S126T\\\"]\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aeurobnd-blg-v4%3Aseries%3ATP_YDOSBAYAZDEG_S125T%3Adff118b1369a.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAYAZDEG.S125T

## Target
series | evds:TP.YDOSBAYAZDEG.S125T

## Notebook
eurobnd-blg-v4

## Candidate Title
1.C.Toplam (S.1, S.2) (Diğer Finansal Aracı İhraçları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_total

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
Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S125T

## Evidence
{
  "ticker": "TP.YDOSBAYAZDEG.S125T",
  "notebook_slug": "eurobnd-blg-v4",
  "official_series_name": "Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)",
  "context_title": "Toplam (S.1, S.2) (Diğer Finansal Aracılar Tarafından İhraç Edilen)",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "stock_total",
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
    "id": "catalog:evds2:TP.YDOSBAYAZDEG.S125T",
    "title": "1.C.Toplam (S.1, S.2) (Diğer Finansal Aracı İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbayazdeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAYAZDEG.S125T', 'TP.YDOSBAYAZDEG.S126T'",
    "df_eurobond[\"Özel Sektör Eurobond Toplam\"] = df_eurobond[\"TP_YDOSBAYAZDEG_S11T\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S122T\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S125T\"] + df_eurobond[\"TP_YDOSBAYAZDEG_S126T\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
