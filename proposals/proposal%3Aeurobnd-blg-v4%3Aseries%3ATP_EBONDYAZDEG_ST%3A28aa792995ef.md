---
record_type: proposal
id: proposal:eurobnd-blg-v4:series:TP_EBONDYAZDEG_ST:28aa792995ef
proposal_id: proposal:eurobnd-blg-v4:series:TP_EBONDYAZDEG_ST:28aa792995ef
title: Semantic proposal for TP.EBONDYAZDEG.ST
status: approved
target_type: series
target_id: evds:TP.EBONDYAZDEG.ST
ticker: TP.EBONDYAZDEG.ST
notebook_slug: eurobnd-blg-v4
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Eurobnd_Blg_V4.ipynb
candidate_title: 1.Toplam (S.1, S.2)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:eurobond
- theme:external-financing
candidate_indicator_inputs:
- derived:eurobond-total-stock
- derived:eurobond-foreign-share
- derived:hazine-eurobond-total
- derived:hazine-eurobond-foreign-share
candidate_formula_hint: 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci
  stoklarinin toplam stoga orani.'
confidence: 0.95
source: heuristic
evidence_fingerprint: 28aa792995ef4d81ac32cff3606875d0137110d3
catalog_record_id: catalog:evds2:TP.EBONDYAZDEG.ST
memory_rule_ids: []
evidence:
  ticker: TP.EBONDYAZDEG.ST
  notebook_slug: eurobnd-blg-v4
  official_series_name: Toplam (S.1, S.2)
  context_title: Toplam (S.1, S.2)
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
  - derived:hazine-eurobond-total
  - derived:hazine-eurobond-foreign-share
  source_dependency_ids:
  - source:eurobnd-bbg-upload
  - source:eurobnd-tcmb-vade-pdf
  - source:eurobnd-hmb-odeme-projeksiyonu
  catalog_record:
    id: catalog:evds2:TP.EBONDYAZDEG.ST
    title: 1.Toplam (S.1, S.2)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ebondyazdeg
    category: GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '''TP.YDOSBAYAZDEG.S76'', ''TP.EBONDYAZDEG.ST'', ''TP.YDOSBAYAZDEG.S11T'', ''TP.YDOSBAYAZDEG.S122T'','
  - df_eurobond["Hazine Eurobond Toplam"] = df_eurobond["TP_EBONDYAZDEG_ST"]
  indicator_hints:
  - 'derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam
    stoga orani.'
  - 'derived:hazine-eurobond-foreign-share: evds:TP.EBONDYAZDEG.S2D / evds:TP.EBONDYAZDEG.ST'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.EBONDYAZDEG.ST
promoted_memory_rule_id: memory:global-tp-ebondyazdeg-st
notes: 'Catalog source: catalog:evds2:TP.EBONDYAZDEG.ST'
body: "# Semantic proposal for TP.EBONDYAZDEG.ST\n\n## Target\nseries | evds:TP.EBONDYAZDEG.ST\n\
  \n## Notebook\neurobnd-blg-v4\n\n## Candidate Title\n1.Toplam (S.1, S.2)\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  stock_total\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:eurobond\n- theme:external-financing\n\
  \n## Candidate Indicator Inputs\n- derived:eurobond-total-stock\n- derived:eurobond-foreign-share\n\
  - derived:hazine-eurobond-total\n- derived:hazine-eurobond-foreign-share\n\n## Formula\
  \ Hint\nderived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin\
  \ toplam stoga orani.\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval\
  \ Reason\nProposal contains notebook-specific scoping and relies on heuristic source\
  \ without matching memory rules or approved series to confirm global safety.\n\n\
  ## Notes\nCatalog source: catalog:evds2:TP.EBONDYAZDEG.ST\n\n## Evidence\n{\n  \"\
  ticker\": \"TP.EBONDYAZDEG.ST\",\n  \"notebook_slug\": \"eurobnd-blg-v4\",\n  \"\
  official_series_name\": \"Toplam (S.1, S.2)\",\n  \"context_title\": \"Toplam (S.1,\
  \ S.2)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\",\n  \"\
  role\": \"stock_total\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n\
  \    \"theme:eurobond\",\n    \"theme:external-financing\"\n  ],\n  \"indicator_ids\"\
  : [\n    \"derived:eurobond-total-stock\",\n    \"derived:eurobond-foreign-share\"\
  ,\n    \"derived:hazine-eurobond-total\",\n    \"derived:hazine-eurobond-foreign-share\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:eurobnd-bbg-upload\",\n   \
  \ \"source:eurobnd-tcmb-vade-pdf\",\n    \"source:eurobnd-hmb-odeme-projeksiyonu\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.EBONDYAZDEG.ST\"\
  ,\n    \"title\": \"1.Toplam (S.1, S.2)\",\n    \"frequency\": \"weekly\",\n   \
  \ \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_ebondyazdeg\",\n \
  \   \"category\": \"GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.YDOSBAYAZDEG.S76',\
  \ 'TP.EBONDYAZDEG.ST', 'TP.YDOSBAYAZDEG.S11T', 'TP.YDOSBAYAZDEG.S122T',\",\n   \
  \ \"df_eurobond[\\\"Hazine Eurobond Toplam\\\"] = df_eurobond[\\\"TP_EBONDYAZDEG_ST\\\
  \"]\"\n  ],\n  \"indicator_hints\": [\n    \"derived:eurobond-foreign-share: Hazine\
  \ ve ozel sektor yabanci stoklarinin toplam stoga orani.\",\n    \"derived:hazine-eurobond-foreign-share:\
  \ evds:TP.EBONDYAZDEG.S2D / evds:TP.EBONDYAZDEG.ST\"\n  ],\n  \"notes\": \"\"\n\
  }\n"
path: proposals\proposal%3Aeurobnd-blg-v4%3Aseries%3ATP_EBONDYAZDEG_ST%3A28aa792995ef.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.EBONDYAZDEG.ST

## Target
series | evds:TP.EBONDYAZDEG.ST

## Notebook
eurobnd-blg-v4

## Candidate Title
1.Toplam (S.1, S.2)

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
- derived:hazine-eurobond-total
- derived:hazine-eurobond-foreign-share

## Formula Hint
derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.EBONDYAZDEG.ST

## Evidence
{
  "ticker": "TP.EBONDYAZDEG.ST",
  "notebook_slug": "eurobnd-blg-v4",
  "official_series_name": "Toplam (S.1, S.2)",
  "context_title": "Toplam (S.1, S.2)",
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
    "derived:hazine-eurobond-total",
    "derived:hazine-eurobond-foreign-share"
  ],
  "source_dependency_ids": [
    "source:eurobnd-bbg-upload",
    "source:eurobnd-tcmb-vade-pdf",
    "source:eurobnd-hmb-odeme-projeksiyonu"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.EBONDYAZDEG.ST",
    "title": "1.Toplam (S.1, S.2)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ebondyazdeg",
    "category": "GENEL YÖNETİM YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.YDOSBAYAZDEG.S76', 'TP.EBONDYAZDEG.ST', 'TP.YDOSBAYAZDEG.S11T', 'TP.YDOSBAYAZDEG.S122T',",
    "df_eurobond[\"Hazine Eurobond Toplam\"] = df_eurobond[\"TP_EBONDYAZDEG_ST\"]"
  ],
  "indicator_hints": [
    "derived:eurobond-foreign-share: Hazine ve ozel sektor yabanci stoklarinin toplam stoga orani.",
    "derived:hazine-eurobond-foreign-share: evds:TP.EBONDYAZDEG.S2D / evds:TP.EBONDYAZDEG.ST"
  ],
  "notes": ""
}
