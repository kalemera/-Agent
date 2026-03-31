---
record_type: proposal
id: proposal:tbl-apko:series:TP_HPBITABLO4_12:2dc431f8393b
proposal_id: proposal:tbl-apko:series:TP_HPBITABLO4_12:2dc431f8393b
title: Semantic proposal for TP.HPBITABLO4.12
status: approved
target_type: series
target_id: evds:TP.HPBITABLO4.12
ticker: TP.HPBITABLO4.12
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.1.2.d.Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı
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
evidence_fingerprint: 2dc431f8393b56332a8269fca6e50d6ac8b19766
catalog_record_id: catalog:evds2:TP.HPBITABLO4.12
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO4.12
  notebook_slug: tbl-apko
  official_series_name: Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi,
    Kıymetli Maden)
  context_title: Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli
    Maden)
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
    id: catalog:evds2:TP.HPBITABLO4.12
    title: 1.1.2.d.Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_hpbitablo4
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.HPBITABLO4.12": "Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi,
    Kıymetli Maden)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO4.12
promoted_memory_rule_id: memory:global-tp-hpbitablo4-12
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO4.12'
body: "# Semantic proposal for TP.HPBITABLO4.12\n\n## Target\nseries | evds:TP.HPBITABLO4.12\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.1.2.d.Kıymetli Maden Depo Hesapları\
  \ - ABD Doları Karşılığı\n\n## Candidate Unit\nmilyon ABD doları\n\n## Candidate\
  \ Frequency\nweekly\n\n## Candidate Role\nbalance_sheet_line\n\n## Confidence\n\
  0.9\n\n## Candidate Themes\n- theme:apko-summary\n- theme:external-financing\n-\
  \ theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO4.12\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO4.12\",\n  \"notebook_slug\": \"tbl-apko\"\
  ,\n  \"official_series_name\": \"Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler,\
  \ Tüzel Kişi, Kıymetli Maden)\",\n  \"context_title\": \"Bankalar YP Mevduat Stoku\
  \ (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli Maden)\",\n  \"frequency\": \"weekly\"\
  ,\n  \"unit\": \"milyon ABD doları\",\n  \"role\": \"balance_sheet_line\",\n  \"\
  status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:apko-summary\",\n\
  \    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\",\n    \"\
  theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:tblapko-bbg-upload\",\n    \"source:tblapko-hmb-ab-borc-xls\"\
  ,\n    \"source:tblapko-swap-pdf\",\n    \"source:tblapko-bddk-weekly-bulletin\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO4.12\"\
  ,\n    \"title\": \"1.1.2.d.Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı\"\
  ,\n    \"frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"\
  data_group\": \"bie_hpbitablo4\",\n    \"category\": \"PARA VE BANKA İSTATİSTİKLERİ\
  \ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n\
  \    \"\\\"TP.HPBITABLO4.12\\\": \\\"Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler,\
  \ Tüzel Kişi, Kıymetli Maden)\\\",\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Atbl-apko%3Aseries%3ATP_HPBITABLO4_12%3A2dc431f8393b.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO4.12

## Target
series | evds:TP.HPBITABLO4.12

## Notebook
tbl-apko

## Candidate Title
1.1.2.d.Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı

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
Catalog source: catalog:evds2:TP.HPBITABLO4.12

## Evidence
{
  "ticker": "TP.HPBITABLO4.12",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli Maden)",
  "context_title": "Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli Maden)",
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
    "id": "catalog:evds2:TP.HPBITABLO4.12",
    "title": "1.1.2.d.Kıymetli Maden Depo Hesapları - ABD Doları Karşılığı",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_hpbitablo4",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.HPBITABLO4.12\": \"Bankalar YP Mevduat Stoku (Yurtiçi Yerleşikler, Tüzel Kişi, Kıymetli Maden)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
