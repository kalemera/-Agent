---
record_type: proposal
id: proposal:tbl-apko:series:TP_KALANVADE_K8:154abc3ae36f
proposal_id: proposal:tbl-apko:series:TP_KALANVADE_K8:154abc3ae36f
title: Semantic proposal for TP.KALANVADE.K8
status: approved
target_type: series
target_id: evds:TP.KALANVADE.K8
ticker: TP.KALANVADE.K8
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 3.3.Banka Mevduatı
candidate_unit: milyon ABD doları
candidate_frequency: monthly
candidate_role: term_split_line
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 154abc3ae36f4179433db7d91e6caf4682f09870
catalog_record_id: catalog:evds2:TP.KALANVADE.K8
memory_rule_ids: []
evidence:
  ticker: TP.KALANVADE.K8
  notebook_slug: tbl-apko
  official_series_name: Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler,
    TL Mevduat)
  context_title: Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat)
  frequency: monthly
  unit: milyon ABD doları
  role: term_split_line
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids: []
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.KALANVADE.K8
    title: 3.3.Banka Mevduatı
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_kalanvade
    category: KISA VADELİ DIŞ BORÇ İSTATİSTİKLERİ (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.KALANVADE.K8": "Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler,
    TL Mevduat)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.KALANVADE.K8
promoted_memory_rule_id: memory:global-tp-kalanvade-k8
notes: 'Catalog source: catalog:evds2:TP.KALANVADE.K8'
body: "# Semantic proposal for TP.KALANVADE.K8\n\n## Target\nseries | evds:TP.KALANVADE.K8\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n3.3.Banka Mevduatı\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n## Candidate Role\n\
  term_split_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nNo matching memory rules or approved\
  \ series found; source is heuristic and tied to notebook slug\n\n## Notes\nCatalog\
  \ source: catalog:evds2:TP.KALANVADE.K8\n\n## Evidence\n{\n  \"ticker\": \"TP.KALANVADE.K8\"\
  ,\n  \"notebook_slug\": \"tbl-apko\",\n  \"official_series_name\": \"Vadesine 1\
  \ Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat)\",\n  \"context_title\"\
  : \"Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat)\",\n\
  \  \"frequency\": \"monthly\",\n  \"unit\": \"milyon ABD doları\",\n  \"role\":\
  \ \"term_split_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n \
  \   \"theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:tblapko-bbg-upload\",\n    \"source:tblapko-hmb-ab-borc-xls\"\
  ,\n    \"source:tblapko-swap-pdf\",\n    \"source:tblapko-bddk-weekly-bulletin\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.KALANVADE.K8\",\n\
  \    \"title\": \"3.3.Banka Mevduatı\",\n    \"frequency\": \"monthly\",\n    \"\
  unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_kalanvade\",\n    \"category\"\
  : \"KISA VADELİ DIŞ BORÇ İSTATİSTİKLERİ (TCMB)\"\n  },\n  \"memory_rules\": [],\n\
  \  \"source_snippets\": [\n    \"\\\"TP.KALANVADE.K8\\\": \\\"Vadesine 1 Yıldan\
  \ Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat)\\\",\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_KALANVADE_K8%3A154abc3ae36f.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.KALANVADE.K8

## Target
series | evds:TP.KALANVADE.K8

## Notebook
tbl-apko

## Candidate Title
3.3.Banka Mevduatı

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
Catalog source: catalog:evds2:TP.KALANVADE.K8

## Evidence
{
  "ticker": "TP.KALANVADE.K8",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat)",
  "context_title": "Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat)",
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
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.KALANVADE.K8",
    "title": "3.3.Banka Mevduatı",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_kalanvade",
    "category": "KISA VADELİ DIŞ BORÇ İSTATİSTİKLERİ (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.KALANVADE.K8\": \"Vadesine 1 Yıldan Az Kalan Dış Borç (Yurtdışı Yerleşikler, TL Mevduat)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
