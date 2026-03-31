---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_12:628744124b95
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_12:628744124b95
title: Semantic proposal for TP.HPBITABLO2.12
status: manual_review
target_type: series
target_id: evds:TP.HPBITABLO2.12
ticker: TP.HPBITABLO2.12
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: '1.1.2.i.b. Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)'
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 628744124b953d3643cfb8259afe0aa500105bd4
catalog_record_id: catalog:evds2:TP.HPBITABLO2.12
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.12
  notebook_slug: dth-blg-v7
  official_series_name: 'Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)'
  context_title: 'Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)'
  frequency: weekly
  unit: Milyon ABD Doları
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids: []
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.12
    title: '1.1.2.i.b. Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)'
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.8'', ''TP.HPBITABLO2.10'', ''TP.HPBITABLO2.11'', ''TP.HPBITABLO2.12'','
  - '"TP_HPBITABLO2_12": "b. Tüzel Kişi****", #Bilgi İçin: Tüzel Kişi YP Mevduatı
    (Milyon ABD Doları)'
  - 'if col not in ["TP_HPBITABLO2_10", "TP_HPBITABLO2_11", "TP_HPBITABLO2_12", "DTH
    STOKU"]:'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: ''
promoted_memory_rule_id: ''
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.12'
body: "# Semantic proposal for TP.HPBITABLO2.12\n\n## Target\nseries | evds:TP.HPBITABLO2.12\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.2.i.b. Bilgi İçin: Tüzel Kişi\
  \ YP Mevduatı (Milyon ABD Doları)\n\n## Candidate Unit\nbin TL\n\n## Candidate Frequency\n\
  weekly\n\n## Candidate Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate\
  \ Themes\n- theme:dth\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\
  \n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\n\
  Catalog source: catalog:evds2:TP.HPBITABLO2.12\n\n## Evidence\n{\n  \"ticker\":\
  \ \"TP.HPBITABLO2.12\",\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\"\
  : \"Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)\",\n  \"context_title\"\
  : \"Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)\",\n  \"frequency\":\
  \ \"weekly\",\n  \"unit\": \"Milyon ABD Doları\",\n  \"role\": \"stock_component\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n\
  \  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO2.12\"\
  ,\n    \"title\": \"1.1.2.i.b. Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"bin TL\",\n    \"data_group\"\
  : \"bie_hpbitablo2\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK)\
  \ (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO2.8',\
  \ 'TP.HPBITABLO2.10', 'TP.HPBITABLO2.11', 'TP.HPBITABLO2.12',\",\n    \"\\\"TP_HPBITABLO2_12\\\
  \": \\\"b. Tüzel Kişi****\\\", #Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)\"\
  ,\n    \"if col not in [\\\"TP_HPBITABLO2_10\\\", \\\"TP_HPBITABLO2_11\\\", \\\"\
  TP_HPBITABLO2_12\\\", \\\"DTH STOKU\\\"]:\"\n  ],\n  \"indicator_hints\": [],\n\
  \  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_12%3A628744124b95.md
approval_reason: 'candidate_title (1.1.2.i.b. Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon
  ABD Doları)) contradicts candidate_unit (bin TL).'
approval_mode: ''
---
# Semantic proposal for TP.HPBITABLO2.12

## Target
series | evds:TP.HPBITABLO2.12

## Notebook
dth-blg-v7

## Candidate Title
1.1.2.i.b. Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.9

## Candidate Themes
- theme:dth

## Candidate Indicator Inputs
-

## Formula Hint
-

## Source
heuristic

## Approval Mode
-

## Approval Reason
candidate_title (1.1.2.i.b. Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)) contradicts candidate_unit (bin TL).

## Notes
Catalog source: catalog:evds2:TP.HPBITABLO2.12

## Evidence
{
  "ticker": "TP.HPBITABLO2.12",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)",
  "context_title": "Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.12",
    "title": "1.1.2.i.b. Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.8', 'TP.HPBITABLO2.10', 'TP.HPBITABLO2.11', 'TP.HPBITABLO2.12',",
    "\"TP_HPBITABLO2_12\": \"b. Tüzel Kişi****\", #Bilgi İçin: Tüzel Kişi YP Mevduatı (Milyon ABD Doları)",
    "if col not in [\"TP_HPBITABLO2_10\", \"TP_HPBITABLO2_11\", \"TP_HPBITABLO2_12\", \"DTH STOKU\"]:"
  ],
  "indicator_hints": [],
  "notes": ""
}
