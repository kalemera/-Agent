---
record_type: proposal
id: proposal:tbl-apko:series:TP_FDVY37:eae6ed4d83f7
proposal_id: proposal:tbl-apko:series:TP_FDVY37:eae6ed4d83f7
title: Semantic proposal for TP.FDVY37
status: approved
target_type: series
target_id: evds:TP.FDVY37
ticker: TP.FDVY37
notebook_slug: tbl-apko
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Tbl_Apko.ipynb
candidate_title: C.Net Döviz Pozisyonu
candidate_unit: milyon ABD doları
candidate_frequency: monthly
candidate_role: ratio_input
candidate_theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
candidate_indicator_inputs:
- derived:gross-external-debt-to-gdp
candidate_formula_hint: 'derived:gross-external-debt-to-gdp: Dis borc stoku ve GSYH
  yardimci serisinden uretilir.'
confidence: 0.95
source: heuristic
evidence_fingerprint: eae6ed4d83f7e8fb80ba9344d6ae43a94a94bdb6
catalog_record_id: catalog:evds2:TP.FDVY37
memory_rule_ids: []
evidence:
  ticker: TP.FDVY37
  notebook_slug: tbl-apko
  official_series_name: Reel Sektör Net Döviz Pozisyonu
  context_title: Reel Sektör Net Döviz Pozisyonu
  frequency: quarterly
  unit: milyon ABD doları
  role: ratio_input
  status: derived_input
  theme_ids:
  - theme:apko-summary
  - theme:external-financing
  - theme:banking-balance-sheet
  - theme:reserves-and-liquidity
  indicator_ids:
  - derived:gross-external-debt-to-gdp
  source_dependency_ids:
  - source:tblapko-bbg-upload
  - source:tblapko-hmb-ab-borc-xls
  - source:tblapko-swap-pdf
  - source:tblapko-bddk-weekly-bulletin
  catalog_record:
    id: catalog:evds2:TP.FDVY37
    title: C.Net Döviz Pozisyonu
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_fdvy
    category: FİNANSAL KESİM DIŞINDAKİ FİRMALARIN DÖVİZ VARLIK VE YÜKÜMLÜLÜKLERİ (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.FDVY37": "Reel Sektör Net Döviz Pozisyonu",'
  indicator_hints:
  - 'derived:gross-external-debt-to-gdp: Dis borc stoku ve GSYH yardimci serisinden
    uretilir.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.FDVY37
promoted_memory_rule_id: memory:global-tp-fdvy37
notes: 'Catalog source: catalog:evds2:TP.FDVY37'
body: "# Semantic proposal for TP.FDVY37\n\n## Target\nseries | evds:TP.FDVY37\n\n\
  ## Notebook\ntbl-apko\n\n## Candidate Title\nC.Net Döviz Pozisyonu\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n## Candidate Role\n\
  ratio_input\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:apko-summary\n\
  - theme:external-financing\n- theme:banking-balance-sheet\n- theme:reserves-and-liquidity\n\
  \n## Candidate Indicator Inputs\n- derived:gross-external-debt-to-gdp\n\n## Formula\
  \ Hint\nderived:gross-external-debt-to-gdp: Dis borc stoku ve GSYH yardimci serisinden\
  \ uretilir.\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n\
  Heuristic source and empty matching memory rules indicate uncertainty for global\
  \ approval.\n\n## Notes\nCatalog source: catalog:evds2:TP.FDVY37\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.FDVY37\",\n  \"notebook_slug\": \"tbl-apko\",\n  \"official_series_name\"\
  : \"Reel Sektör Net Döviz Pozisyonu\",\n  \"context_title\": \"Reel Sektör Net Döviz\
  \ Pozisyonu\",\n  \"frequency\": \"quarterly\",\n  \"unit\": \"milyon ABD doları\"\
  ,\n  \"role\": \"ratio_input\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:apko-summary\",\n    \"theme:external-financing\",\n    \"theme:banking-balance-sheet\"\
  ,\n    \"theme:reserves-and-liquidity\"\n  ],\n  \"indicator_ids\": [\n    \"derived:gross-external-debt-to-gdp\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:tblapko-bbg-upload\",\n   \
  \ \"source:tblapko-hmb-ab-borc-xls\",\n    \"source:tblapko-swap-pdf\",\n    \"\
  source:tblapko-bddk-weekly-bulletin\"\n  ],\n  \"catalog_record\": {\n    \"id\"\
  : \"catalog:evds2:TP.FDVY37\",\n    \"title\": \"C.Net Döviz Pozisyonu\",\n    \"\
  frequency\": \"monthly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_fdvy\",\n    \"category\": \"FİNANSAL KESİM DIŞINDAKİ FİRMALARIN DÖVİZ VARLIK\
  \ VE YÜKÜMLÜLÜKLERİ (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"\\\"TP.FDVY37\\\": \\\"Reel Sektör Net Döviz Pozisyonu\\\",\"\n  ],\n\
  \  \"indicator_hints\": [\n    \"derived:gross-external-debt-to-gdp: Dis borc stoku\
  \ ve GSYH yardimci serisinden uretilir.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Atbl-apko%3Aseries%3ATP_FDVY37%3Aeae6ed4d83f7.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.FDVY37

## Target
series | evds:TP.FDVY37

## Notebook
tbl-apko

## Candidate Title
C.Net Döviz Pozisyonu

## Candidate Unit
milyon ABD doları

## Candidate Frequency
monthly

## Candidate Role
ratio_input

## Confidence
0.95

## Candidate Themes
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity

## Candidate Indicator Inputs
- derived:gross-external-debt-to-gdp

## Formula Hint
derived:gross-external-debt-to-gdp: Dis borc stoku ve GSYH yardimci serisinden uretilir.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.FDVY37

## Evidence
{
  "ticker": "TP.FDVY37",
  "notebook_slug": "tbl-apko",
  "official_series_name": "Reel Sektör Net Döviz Pozisyonu",
  "context_title": "Reel Sektör Net Döviz Pozisyonu",
  "frequency": "quarterly",
  "unit": "milyon ABD doları",
  "role": "ratio_input",
  "status": "derived_input",
  "theme_ids": [
    "theme:apko-summary",
    "theme:external-financing",
    "theme:banking-balance-sheet",
    "theme:reserves-and-liquidity"
  ],
  "indicator_ids": [
    "derived:gross-external-debt-to-gdp"
  ],
  "source_dependency_ids": [
    "source:tblapko-bbg-upload",
    "source:tblapko-hmb-ab-borc-xls",
    "source:tblapko-swap-pdf",
    "source:tblapko-bddk-weekly-bulletin"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.FDVY37",
    "title": "C.Net Döviz Pozisyonu",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_fdvy",
    "category": "FİNANSAL KESİM DIŞINDAKİ FİRMALARIN DÖVİZ VARLIK VE YÜKÜMLÜLÜKLERİ (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.FDVY37\": \"Reel Sektör Net Döviz Pozisyonu\","
  ],
  "indicator_hints": [
    "derived:gross-external-debt-to-gdp: Dis borc stoku ve GSYH yardimci serisinden uretilir."
  ],
  "notes": ""
}
