---
record_type: proposal
id: proposal:tbl-apko:series:TP_KALANVADE_K3:234ff81c92d8
proposal_id: proposal:tbl-apko:series:TP_KALANVADE_K3:234ff81c92d8
title: Semantic proposal for TP.KALANVADE.K3
status: approved
target_type: series
target_id: evds:TP.KALANVADE.K3
ticker: TP.KALANVADE.K3
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.2.Mevduat
candidate_unit: milyon ABD doları
candidate_frequency: monthly
candidate_role: term_split_line
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:foreign-resident-deposits-short-term
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 234ff81c92d80f64c00858482b45d845ffcccfcf
catalog_record_id: catalog:evds2:TP.KALANVADE.K3
memory_rule_ids: []
evidence:
  ticker: TP.KALANVADE.K3
  notebook_slug: tbl-apko
  official_series_name: Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler,
    DTH)
  context_title: Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, DTH)
  frequency: monthly
  unit: milyon ABD doları
  role: term_split_line
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:foreign-resident-deposits-short-term
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.KALANVADE.K3
    title: 1.2.Mevduat
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_kalanvade
    category: KISA VADELİ DIŞ BORÇ İSTATİSTİKLERİ (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.KALANVADE.K3": "Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler,
    DTH)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.KALANVADE.K3
promoted_memory_rule_id: memory:global-tp-kalanvade-k3
notes: 'Catalog source: catalog:evds2:TP.KALANVADE.K3'
body: "# Semantic proposal for TP.KALANVADE.K3\n\n## Target\nseries | evds:TP.KALANVADE.K3\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.2.Mevduat\n\n## Candidate Unit\n\
  milyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n## Candidate Role\nterm_split_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n- theme:external-financing\n\
  - theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\n## Candidate Indicator\
  \ Inputs\n- derived:foreign-resident-deposits-short-term\n\n## Formula Hint\n-\n\
  \n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nLLM requested\
  \ manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.KALANVADE.K3\n\n\
  ## Evidence\n{\n  \"ticker\": \"TP.KALANVADE.K3\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler,\
  \ DTH)\",\n  \"context_title\": \"Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı\
  \ Yerleşikler, DTH)\",\n  \"frequency\": \"monthly\",\n  \"unit\": \"milyon ABD\
  \ doları\",\n  \"role\": \"term_split_line\",\n  \"status\": \"derived_input\",\n\
  \  \"theme_ids\": [\n    \"theme:apko-summary\",\n    \"theme:external-financing\"\
  ,\n    \"theme:banking-balance-sheet\",\n    \"theme:reserves-and-liquidity\"\n\
  \  ],\n  \"indicator_ids\": [\n    \"derived:foreign-resident-deposits-short-term\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.KALANVADE.K3\",\n    \"title\": \"1.2.Mevduat\",\n    \"frequency\"\
  : \"monthly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_kalanvade\"\
  ,\n    \"category\": \"KISA VADELİ DIŞ BORÇ İSTATİSTİKLERİ (TCMB)\"\n  },\n  \"\
  memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.KALANVADE.K3\\\": \\\
  \"Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, DTH)\\\",\"\n  ],\n\
  \  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_KALANVADE_K3%3A234ff81c92d8.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.KALANVADE.K3

## Target
series | evds:TP.KALANVADE.K3

## Notebook
tbl-apko

## Candidate Title
1.2.Mevduat

## Candidate Unit
milyon ABD doları

## Candidate Frequency
monthly

## Candidate Role
term_split_line

## Confidence
0.9

## Candidate Themes
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

## Candidate Indicator Inputs
- derived:foreign-resident-deposits-short-term

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.KALANVADE.K3

## Evidence
{
  "ticker": "TP.KALANVADE.K3",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, DTH)",
  "context_title": "Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, DTH)",
  "frequency": "monthly",
  "unit": "milyon ABD doları",
  "role": "term_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:foreign-resident-deposits-short-term"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.KALANVADE.K3",
    "title": "1.2.Mevduat",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_kalanvade",
    "category": "KISA VADELİ DIŞ BORÇ İSTATİSTİKLERİ (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.KALANVADE.K3\": \"Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, DTH)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
