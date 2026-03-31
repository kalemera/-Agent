---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_10:759a3e31fe18
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_HPBITABLO5_10:759a3e31fe18
title: Semantic proposal for TP.HPBITABLO5.10
status: approved
target_type: series
target_id: evds:TP.HPBITABLO5.10
ticker: TP.HPBITABLO5.10
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 1.2.3.Diğer Para Cinsi Mevduat
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
evidence_fingerprint: 759a3e31fe18f929f1b96d4ec16a5607922c7dc2
catalog_record_id: catalog:evds2:TP.HPBITABLO5.10
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO5.10
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları)
  context_title: A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler)
    (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / c. Diğer Para Cinsi
    Mevduatlar (Milyon ABD Doları)
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
    id: catalog:evds2:TP.HPBITABLO5.10
    title: 1.2.3.Diğer Para Cinsi Mevduat
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo5
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO5.9'', ''TP.HPBITABLO5.10'', ''TP.HPBITABLO5.11'', ''TP.HPBITABLO5.12'','
  - '''TP_HPBITABLO5_10'': ''A2c. Diğer Para Cinsi Mevduatlar'','
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO5.10
promoted_memory_rule_id: memory:global-tp-hpbitablo5-10
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO5.10'
body: "# Semantic proposal for TP.HPBITABLO5.10\n\n## Target\nseries | evds:TP.HPBITABLO5.10\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n1.2.3.Diğer Para Cinsi Mevduat\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\ncurrency_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nInsufficient evidence for global approval as matching_memory_rules\
  \ and approved_series are empty.\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO5.10\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO5.10\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları)\"\
  ,\n  \"context_title\": \"A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler)\
  \ (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / c. Diğer Para Cinsi\
  \ Mevduatlar (Milyon ABD Doları)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"\
  Milyon ABD Doları\",\n  \"role\": \"currency_split_line\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO5.10\",\n    \"title\"\
  : \"1.2.3.Diğer Para Cinsi Mevduat\",\n    \"frequency\": \"weekly\",\n    \"unit\"\
  : \"milyon ABD doları\",\n    \"data_group\": \"bie_hpbitablo5\",\n    \"category\"\
  : \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\":\
  \ [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO5.9', 'TP.HPBITABLO5.10', 'TP.HPBITABLO5.11',\
  \ 'TP.HPBITABLO5.12',\",\n    \"'TP_HPBITABLO5_10': 'A2c. Diğer Para Cinsi Mevduatlar',\"\
  \n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_HPBITABLO5_10%3A759a3e31fe18.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO5.10

## Target
series | evds:TP.HPBITABLO5.10

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
1.2.3.Diğer Para Cinsi Mevduat

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
Catalog source: catalog:evds2:TP.HPBITABLO5.10

## Evidence
{
  "ticker": "TP.HPBITABLO5.10",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları)",
  "context_title": "A. Parite Etkisinden Arındırılmış Değişim (Yurt İçi Yerleşikler) (Milyon ABD Doları) / 2. Tüzel Kişiler (Milyon ABD Doları) / c. Diğer Para Cinsi Mevduatlar (Milyon ABD Doları)",
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
    "id": "catalog:evds2:TP.HPBITABLO5.10",
    "title": "1.2.3.Diğer Para Cinsi Mevduat",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo5",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO5.9', 'TP.HPBITABLO5.10', 'TP.HPBITABLO5.11', 'TP.HPBITABLO5.12',",
    "'TP_HPBITABLO5_10': 'A2c. Diğer Para Cinsi Mevduatlar',"
  ],
  "indicator_hints": [],
  "notes": ""
}
