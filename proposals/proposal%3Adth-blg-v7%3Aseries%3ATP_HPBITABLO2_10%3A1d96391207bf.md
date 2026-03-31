---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_10:1d96391207bf
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_10:1d96391207bf
title: Semantic proposal for TP.HPBITABLO2.10
status: manual_review
target_type: series
target_id: evds:TP.HPBITABLO2.10
ticker: TP.HPBITABLO2.10
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: '1.1.2.i. Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)'
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 1d96391207bf0ee37dafbf97a12c2b49d6801456
catalog_record_id: catalog:evds2:TP.HPBITABLO2.10
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.10
  notebook_slug: dth-blg-v7
  official_series_name: 'Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)'
  context_title: 'Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)'
  frequency: weekly
  unit: Milyon ABD Doları
  role: stock_total
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids: []
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.10
    title: '1.1.2.i. Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)'
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.8'', ''TP.HPBITABLO2.10'', ''TP.HPBITABLO2.11'', ''TP.HPBITABLO2.12'','
  - '"TP_HPBITABLO2_10": "C. BİLGİ İÇİN YP (ABD Doları) (1+2+3+4)****", #BİLGİ İÇİN
    YP (Milyon ABD Doları)(1+2+3+4)-Düzey'
  - 'if col not in ["TP_HPBITABLO2_10", "TP_HPBITABLO2_11", "TP_HPBITABLO2_12", "DTH
    STOKU"]:'
  - df_kredi_mevduat["Bilgi İçin DTH (B.1.) (ABD Doları)****"] = df_kredi_mevduat["TP_HPBITABLO2_10"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: ''
promoted_memory_rule_id: ''
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.10'
body: "# Semantic proposal for TP.HPBITABLO2.10\n\n## Target\nseries | evds:TP.HPBITABLO2.10\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.1.2.i. Bilgi İçin: Toplam YP\
  \ Mevduat (Milyon ABD Doları)\n\n## Candidate Unit\nbin TL\n\n## Candidate Frequency\n\
  weekly\n\n## Candidate Role\nstock_total\n\n## Confidence\n0.9\n\n## Candidate Themes\n\
  - theme:dth\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\n\
  heuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.HPBITABLO2.10\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO2.10\"\
  ,\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\": \"Bilgi İçin:\
  \ Toplam YP Mevduat (Milyon ABD Doları)\",\n  \"context_title\": \"Bilgi İçin: Toplam\
  \ YP Mevduat (Milyon ABD Doları)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"\
  Milyon ABD Doları\",\n  \"role\": \"stock_total\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:dth-old-series-excel\"\n  ],\n  \"catalog_record\": {\n    \"\
  id\": \"catalog:evds2:TP.HPBITABLO2.10\",\n    \"title\": \"1.1.2.i. Bilgi İçin:\
  \ Toplam YP Mevduat (Milyon ABD Doları)\",\n    \"frequency\": \"weekly\",\n   \
  \ \"unit\": \"bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\"\
  : \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\":\
  \ [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO2.8', 'TP.HPBITABLO2.10', 'TP.HPBITABLO2.11',\
  \ 'TP.HPBITABLO2.12',\",\n    \"\\\"TP_HPBITABLO2_10\\\": \\\"C. BİLGİ İÇİN YP (ABD\
  \ Doları) (1+2+3+4)****\\\", #BİLGİ İÇİN YP (Milyon ABD Doları)(1+2+3+4)-Düzey\"\
  ,\n    \"if col not in [\\\"TP_HPBITABLO2_10\\\", \\\"TP_HPBITABLO2_11\\\", \\\"\
  TP_HPBITABLO2_12\\\", \\\"DTH STOKU\\\"]:\",\n    \"df_kredi_mevduat[\\\"Bilgi İçin\
  \ DTH (B.1.) (ABD Doları)****\\\"] = df_kredi_mevduat[\\\"TP_HPBITABLO2_10\\\"]\"\
  \n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_10%3A1d96391207bf.md
approval_reason: 'candidate_title (1.1.2.i. Bilgi İçin: Toplam YP Mevduat (Milyon
  ABD Doları)) contradicts candidate_unit (bin TL).'
approval_mode: ''
---
# Semantic proposal for TP.HPBITABLO2.10

## Target
series | evds:TP.HPBITABLO2.10

## Notebook
dth-blg-v7

## Candidate Title
1.1.2.i. Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
stock_total

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
candidate_title (1.1.2.i. Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)) contradicts candidate_unit (bin TL).

## Notes
Catalog source: catalog:evds2:TP.HPBITABLO2.10

## Evidence
{
  "ticker": "TP.HPBITABLO2.10",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)",
  "context_title": "Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "stock_total",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.10",
    "title": "1.1.2.i. Bilgi İçin: Toplam YP Mevduat (Milyon ABD Doları)",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.8', 'TP.HPBITABLO2.10', 'TP.HPBITABLO2.11', 'TP.HPBITABLO2.12',",
    "\"TP_HPBITABLO2_10\": \"C. BİLGİ İÇİN YP (ABD Doları) (1+2+3+4)****\", #BİLGİ İÇİN YP (Milyon ABD Doları)(1+2+3+4)-Düzey",
    "if col not in [\"TP_HPBITABLO2_10\", \"TP_HPBITABLO2_11\", \"TP_HPBITABLO2_12\", \"DTH STOKU\"]:",
    "df_kredi_mevduat[\"Bilgi İçin DTH (B.1.) (ABD Doları)****\"] = df_kredi_mevduat[\"TP_HPBITABLO2_10\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
