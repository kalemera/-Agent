---
record_type: proposal
id: proposal:tbl-apko:series:TP_YDOSBAYAZDEG_S122T:c8db2cadd082
proposal_id: proposal:tbl-apko:series:TP_YDOSBAYAZDEG_S122T:c8db2cadd082
title: Semantic proposal for TP.YDOSBAYAZDEG.S122T
status: approved
target_type: series
target_id: evds:TP.YDOSBAYAZDEG.S122T
ticker: TP.YDOSBAYAZDEG.S122T
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: 1.B.Toplam (S.1, S.2) (Banka İhraçları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: c8db2cadd082c3f497bf1edc745bb03d48f22b0e
catalog_record_id: catalog:evds2:TP.YDOSBAYAZDEG.S122T
memory_rule_ids: []
evidence:
  ticker: TP.YDOSBAYAZDEG.S122T
  notebook_slug: tbl-apko
  official_series_name: Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)
  context_title: Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)
  frequency: weekly
  unit: Eurobond - Yaşayan Stok
  role: stock_component
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
    id: catalog:evds2:TP.YDOSBAYAZDEG.S122T
    title: 1.B.Toplam (S.1, S.2) (Banka İhraçları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_ydosbayazdeg
    category: GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI
  memory_rules: []
  source_snippets:
  - '"TP.YDOSBAYAZDEG.S122T": "Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)",'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.YDOSBAYAZDEG.S122T
promoted_memory_rule_id: memory:global-tp-ydosbayazdeg-s122t
notes: 'Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S122T'
body: "# Semantic proposal for TP.YDOSBAYAZDEG.S122T\n\n## Target\nseries | evds:TP.YDOSBAYAZDEG.S122T\n\
  \n## Notebook\ntbl-apko\n\n## Candidate Title\n1.B.Toplam (S.1, S.2) (Banka İhraçları)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nstock_component\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.YDOSBAYAZDEG.S122T\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.YDOSBAYAZDEG.S122T\",\n  \"notebook_slug\"\
  : \"tbl-apko\",\n  \"official_series_name\": \"Bankalar Brüt Dış Borç Stoku (Eurobond\
  \ - Yaşayan Stok)\",\n  \"context_title\": \"Bankalar Brüt Dış Borç Stoku (Eurobond\
  \ - Yaşayan Stok)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Eurobond - Yaşayan\
  \ Stok\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\",\n\
  \  \"theme_ids\": [\n    \"theme:apko-summary\",\n    \"theme:external-financing\"\
  ,\n    \"theme:banking-balance-sheet\",\n    \"theme:reserves-and-liquidity\"\n\
  \  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\"\
  ,\n    \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n \
  \   \"source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n   \
  \ \"id\": \"catalog:evds2:TP.YDOSBAYAZDEG.S122T\",\n    \"title\": \"1.B.Toplam\
  \ (S.1, S.2) (Banka İhraçları)\",\n    \"frequency\": \"weekly\",\n    \"unit\"\
  : \"milyon ABD doları\",\n    \"data_group\": \"bie_ydosbayazdeg\",\n    \"category\"\
  : \"GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI\"\n  },\n\
  \  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.YDOSBAYAZDEG.S122T\\\
  \": \\\"Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)\\\",\"\n  ],\n  \"\
  indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Atbl-apko%3Aseries%3ATP_YDOSBAYAZDEG_S122T%3Ac8db2cadd082.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.YDOSBAYAZDEG.S122T

## Target
series | evds:TP.YDOSBAYAZDEG.S122T

## Notebook
tbl-apko

## Candidate Title
1.B.Toplam (S.1, S.2) (Banka İhraçları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
stock_component

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
Catalog source: catalog:evds2:TP.YDOSBAYAZDEG.S122T

## Evidence
{
  "ticker": "TP.YDOSBAYAZDEG.S122T",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)",
  "context_title": "Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)",
  "frequency": "weekly",
  "unit": "Eurobond - Yaşayan Stok",
  "role": "stock_component",
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
    "id": "catalog:evds2:TP.YDOSBAYAZDEG.S122T",
    "title": "1.B.Toplam (S.1, S.2) (Banka İhraçları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ydosbayazdeg",
    "category": "GENEL YÖNETİM DIŞI SEKTÖRLERİN YURT DIŞI BORÇLANMA SENEDİ İHRAÇLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.YDOSBAYAZDEG.S122T\": \"Bankalar Brüt Dış Borç Stoku (Eurobond - Yaşayan Stok)\","
  ],
  "indicator_hints": [],
  "notes": ""
}
