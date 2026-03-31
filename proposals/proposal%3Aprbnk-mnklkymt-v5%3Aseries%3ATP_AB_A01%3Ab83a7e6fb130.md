---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_AB_A01:b83a7e6fb130
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_AB_A01:b83a7e6fb130
title: Semantic proposal for TP.AB.A01
status: approved
target_type: series
target_id: evds:TP.AB.A01
ticker: TP.AB.A01
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: A.AKTİF
candidate_unit: Bin TL
candidate_frequency: i̇ş günü
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs:
- derived:swap-stock
candidate_formula_hint: 'derived:swap-stock: Swap PDF ve analitik bilanco destek serilerinden
  uretilir.'
confidence: 0.85
source: hybrid
evidence_fingerprint: b83a7e6fb130e8bcf973c8027ca679b8fa595160
catalog_record_id: catalog:evds2:TP.AB.A01
memory_rule_ids: []
evidence:
  ticker: TP.AB.A01
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: A.AKTİF(Bin TL)
  context_title: A.AKTİF(Bin TL)
  frequency: weekly
  unit: Bin TL
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:portfolio-flows
  - theme:foreign-ownership
  - theme:swap-and-securities
  indicator_ids:
  - derived:swap-stock
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.AB.A01
    title: A.AKTİF
    frequency: i̇ş günü
    unit: unknown
    data_group: bie_abanlbil
    category: MERKEZ BANKASI ANALİTİK BİLANÇOSU
  memory_rules: []
  source_snippets:
  - '"TP.AB.A01", "TP.AB.A02", "TP.AB.A03", "TP.AB.A08", "TP.AB.A09", "TP.AB.A11",
    "TP.AB.A12", "TP.AB.A15", "TP.AB.A16", "TP.AB.A17", "TP.AB.A18", "TP.AB.A23",'
  - '"TP_AB_A01": [1, "AKTİF"],'
  indicator_hints:
  - 'derived:swap-stock: Swap PDF ve analitik bilanco destek serilerinden uretilir.'
  notes: ''
llm_provider: ollama_cloud
llm_model: qwen3.5:397b-cloud
promoted_record_id: evds:TP.AB.A01
promoted_memory_rule_id: memory:global-tp-ab-a01
notes: 'Catalog source: catalog:evds2:TP.AB.A01'
body: "# Semantic proposal for TP.AB.A01\n\n## Target\nseries | evds:TP.AB.A01\n\n\
  ## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\nA.AKTİF\n\n## Candidate Unit\n\
  Bin TL\n\n## Candidate Frequency\ni̇ş günü\n\n## Candidate Role\nbalance_sheet_line\n\
  \n## Confidence\n0.85\n\n## Candidate Themes\n- theme:portfolio-flows\n- theme:foreign-ownership\n\
  - theme:swap-and-securities\n\n## Candidate Indicator Inputs\n- derived:swap-stock\n\
  \n## Formula Hint\nderived:swap-stock: Swap PDF ve analitik bilanco destek serilerinden\
  \ uretilir.\n\n## Source\nhybrid\n\n## Notes\nCatalog source: catalog:evds2:TP.AB.A01\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.AB.A01\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"A.AKTİF(Bin TL)\",\n  \"context_title\": \"A.AKTİF(Bin\
  \ TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"\
  balance_sheet_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n  \
  \  \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\",\n    \"theme:swap-and-securities\"\
  \n  ],\n  \"indicator_ids\": [\n    \"derived:swap-stock\"\n  ],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.A01\",\n    \"title\": \"\
  A.AKTİF\",\n    \"frequency\": \"i̇ş günü\",\n    \"unit\": \"unknown\",\n    \"\
  data_group\": \"bie_abanlbil\",\n    \"category\": \"MERKEZ BANKASI ANALİTİK BİLANÇOSU\"\
  \n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.AB.A01\\\
  \", \\\"TP.AB.A02\\\", \\\"TP.AB.A03\\\", \\\"TP.AB.A08\\\", \\\"TP.AB.A09\\\",\
  \ \\\"TP.AB.A11\\\", \\\"TP.AB.A12\\\", \\\"TP.AB.A15\\\", \\\"TP.AB.A16\\\", \\\
  \"TP.AB.A17\\\", \\\"TP.AB.A18\\\", \\\"TP.AB.A23\\\",\",\n    \"\\\"TP_AB_A01\\\
  \": [1, \\\"AKTİF\\\"],\"\n  ],\n  \"indicator_hints\": [\n    \"derived:swap-stock:\
  \ Swap PDF ve analitik bilanco destek serilerinden uretilir.\"\n  ],\n  \"notes\"\
  : \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_AB_A01%3Ab83a7e6fb130.md
---
# Semantic proposal for TP.AB.A01

## Target
series | evds:TP.AB.A01

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
A.AKTİF

## Candidate Unit
Bin TL

## Candidate Frequency
i̇ş günü

## Candidate Role
balance_sheet_line

## Confidence
0.85

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

## Candidate Indicator Inputs
- derived:swap-stock

## Formula Hint
derived:swap-stock: Swap PDF ve analitik bilanco destek serilerinden uretilir.

## Source
hybrid

## Notes
Catalog source: catalog:evds2:TP.AB.A01

## Evidence
{
  "ticker": "TP.AB.A01",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "A.AKTİF(Bin TL)",
  "context_title": "A.AKTİF(Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:portfolio-flows",
    "theme:foreign-ownership",
    "theme:swap-and-securities"
  ],
  "indicator_ids": [
    "derived:swap-stock"
  ],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.AB.A01",
    "title": "A.AKTİF",
    "frequency": "i̇ş günü",
    "unit": "unknown",
    "data_group": "bie_abanlbil",
    "category": "MERKEZ BANKASI ANALİTİK BİLANÇOSU"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.AB.A01\", \"TP.AB.A02\", \"TP.AB.A03\", \"TP.AB.A08\", \"TP.AB.A09\", \"TP.AB.A11\", \"TP.AB.A12\", \"TP.AB.A15\", \"TP.AB.A16\", \"TP.AB.A17\", \"TP.AB.A18\", \"TP.AB.A23\",",
    "\"TP_AB_A01\": [1, \"AKTİF\"],"
  ],
  "indicator_hints": [
    "derived:swap-stock: Swap PDF ve analitik bilanco destek serilerinden uretilir."
  ],
  "notes": ""
}
