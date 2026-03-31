---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_6:3144533dd78b
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_6:3144533dd78b
title: Semantic proposal for TP.HPBITABLO5.6
status: approved
target_type: series
target_id: evds:TP.HPBITABLO5.6
ticker: TP.HPBITABLO5.6
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 1.1.4.Kıymetli Maden Depo Hesapları
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 3144533dd78b773af6b0c21039e72bbeadb760d8
catalog_record_id: catalog:evds2:TP.HPBITABLO5.6
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO5.6
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları)
  context_title: A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler)
    (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / d. Kıymetli Maden
    Depo Hesapları (Milyon ABD Doları)
  frequency: weekly
  unit: Milyon ABD Doları
  role: currency_split_line
  status: derived_input
  theme_ids:
  - theme:portfolio-flows
  - theme:foreign-ownership
  - theme:swap-and-securities
  indicator_ids: []
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO5.6
    title: 1.1.4.Kıymetli Maden Depo Hesapları
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo5
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO5.5'', ''TP.HPBITABLO5.6'', ''TP.HPBITABLO5.7'', ''TP.HPBITABLO5.8'','
  - '''TP_HPBITABLO5_6'': ''A1d. Kıymetli Maden Depo Hesapları'','
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO5.6
promoted_memory_rule_id: memory:global-tp-hpbitablo5-6
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO5.6'
body: "# Semantic proposal for TP.HPBITABLO5.6\n\n## Target\nseries | evds:TP.HPBITABLO5.6\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n1.1.4.Kıymetli Maden Depo\
  \ Hesapları\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\n\
  weekly\n\n## Candidate Role\ncurrency_split_line\n\n## Confidence\n0.9\n\n## Candidate\
  \ Themes\n- theme:portfolio-flows\n- theme:foreign-ownership\n- theme:swap-and-securities\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nHeuristic source with notebook_slug\
  \ and no matching_memory_rules or approved_series.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.HPBITABLO5.6\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO5.6\"\
  ,\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\",\n  \"official_series_name\": \"d.\
  \ Kıymetli Maden Depo Hesapları (Milyon ABD Doları)\",\n  \"context_title\": \"\
  A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları)\
  \ / 1. Gerçek Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları (Milyon\
  \ ABD Doları)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Milyon ABD Doları\"\
  ,\n  \"role\": \"currency_split_line\",\n  \"status\": \"derived_input\",\n  \"\
  theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO5.6\",\n    \"title\"\
  : \"1.1.4.Kıymetli Maden Depo Hesapları\",\n    \"frequency\": \"weekly\",\n   \
  \ \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo5\",\n  \
  \  \"category\": \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"\
  memory_rules\": [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO5.5', 'TP.HPBITABLO5.6',\
  \ 'TP.HPBITABLO5.7', 'TP.HPBITABLO5.8',\",\n    \"'TP_HPBITABLO5_6': 'A1d. Kıymetli\
  \ Maden Depo Hesapları',\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n\
  }\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_HPBITABLO5_6%3A3144533dd78b.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO5.6

## Target
series | evds:TP.HPBITABLO5.6

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
1.1.4.Kıymetli Maden Depo Hesapları

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
currency_split_line

## Confidence
0.9

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

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
Catalog source: catalog:evds2:TP.HPBITABLO5.6

## Evidence
{
  "ticker": "TP.HPBITABLO5.6",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları)",
  "context_title": "A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 1. Gerçek Kişiler (Milyon ABD Doları) / d. Kıymetli Maden Depo Hesapları (Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "currency_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:portfolio-flows",
    "theme:foreign-ownership",
    "theme:swap-and-securities"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO5.6",
    "title": "1.1.4.Kıymetli Maden Depo Hesapları",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo5",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO5.5', 'TP.HPBITABLO5.6', 'TP.HPBITABLO5.7', 'TP.HPBITABLO5.8',",
    "'TP_HPBITABLO5_6': 'A1d. Kıymetli Maden Depo Hesapları',"
  ],
  "indicator_hints": [],
  "notes": ""
}
