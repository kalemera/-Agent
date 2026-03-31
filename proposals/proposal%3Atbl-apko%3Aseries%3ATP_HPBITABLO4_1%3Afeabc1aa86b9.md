---
record_type: proposal
id: proposal:tbl-apko:series:TP_HPBITABLO4_1:feabc1aa86b9
proposal_id: proposal:tbl-apko:series:TP_HPBITABLO4_1:feabc1aa86b9
title: Semantic proposal for TP.HPBITABLO4.1
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.1
ticker: TP.HPBITABLO4.1
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.TOPLAM YP MEVDUAT
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: feabc1aa86b97870ea81005ed1e63ea5d1358ad5
catalog_record_id: catalog:evds2:TP.HPBITABLO4.1
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.1
  notebook_slug: tbl-apko
  official_series_name: Bankalar YP Mevduat Stoku
  context_title: Bankalar YP Mevduat Stoku
  frequency: weekly
  unit: milyon ABD doları
  role: balance_sheet_line
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
    id: catalog:evds2:TP.HPBITABLO4.1
    title: 1.TOPLAM YP MEVDUAT
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.HPBITABLO4.1": "Bankalar YP Mevduat Stoku",'
  - '"TP.HPBITABLO4.16": "Bankalar YP Mevduat Stoku (Yurtdışı Yerleşikler)",'
  - '"TP.HPBITABLO4.12": "Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi,
    Kıymetli Maden)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.1
promoted_memory_rule_id: memory:global-tp-hpbitablo4-1
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.1'
body: "# Semantic proposal for TP.HPBITABLO4.1\n\n## Target\nseries | evds:TP.HPBITABLO4.1\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.TOPLAM YP MEVDUAT\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  balance_sheet_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO4.1\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO4.1\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Bankalar YP Mevduat Stoku\",\n  \"context_title\"\
  : \"Bankalar YP Mevduat Stoku\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon\
  \ ABD doları\",\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:apko-summary\",\n    \"theme:external-financing\"\
  ,\n    \"theme:banking-balance-sheet\",\n    \"theme:reserves-and-liquidity\"\n\
  \  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\"\
  ,\n    \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n \
  \   \"source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n   \
  \ \"id\": \"catalog:evds2:TP.HPBITABLO4.1\",\n    \"title\": \"1.TOPLAM YP MEVDUAT\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_hpbitablo4\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ\
  \ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n\
  \    \"\\\"TP.HPBITABLO4.1\\\": \\\"Bankalar YP Mevduat Stoku\\\",\",\n    \"\\\"\
  TP.HPBITABLO4.16\\\": \\\"Bankalar YP Mevduat Stoku (Yurtdışı Yerleşikler)\\\",\"\
  ,\n    \"\\\"TP.HPBITABLO4.12\\\": \\\"Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler,\
  \ Tüzel Kişi, Kıymetli Maden)\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Atbl-apko%3Aseries%3ATP_HPBITABLO4_1%3Afeabc1aa86b9.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.1

## Target
series | evds:TP.HPBITABLO4.1

## Notebook
tbl-apko

## Candidate Title
1.TOPLAM YP MEVDUAT

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

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
Catalog source: catalog:evds2:TP.HPBITABLO4.1

## Evidence
{
  "ticker": "TP.HPBITABLO4.1",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Bankalar YP Mevduat Stoku",
  "context_title": "Bankalar YP Mevduat Stoku",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
  "role": "balance_sheet_line",
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
    "id": "catalog:evds2:TP.HPBITABLO4.1",
    "title": "1.TOPLAM YP MEVDUAT",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.HPBITABLO4.1\": \"Bankalar YP Mevduat Stoku\",",
    "\"TP.HPBITABLO4.16\": \"Bankalar YP Mevduat Stoku (Yurtdışı Yerleşikler)\",",
    "\"TP.HPBITABLO4.12\": \"Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli Maden)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
