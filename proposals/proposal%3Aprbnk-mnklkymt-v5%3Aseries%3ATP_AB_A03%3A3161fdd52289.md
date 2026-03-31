---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_AB_A03:3161fdd52289
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_AB_A03:3161fdd52289
title: Semantic proposal for TP.AB.A03
status: approved
target_type: series
target_id: evds:TP.AB.A03
ticker: TP.AB.A03
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: A.2 İÇ VARLIKLAR
candidate_unit: Bin TL
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.8
source: hybrid
evidence_fingerprint: 3161fdd5228945701549865d79aecac1b87eec0f
catalog_record_id: catalog:evds2:TP.AB.A03
memory_rule_ids: []
evidence:
  ticker: TP.AB.A03
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: A.2_İÇ VARLIKLAR(Bin TL)
  context_title: A.2_İÇ VARLIKLAR(Bin TL)
  frequency: weekly
  unit: Bin TL
  role: balance_sheet_line
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
    id: catalog:evds2:TP.AB.A03
    title: A.2 İÇ VARLIKLAR
    frequency: i̇ş günü
    unit: unknown
    data_group: bie_abanlbil
    category: MERKEZ BANKASI ANALİTİK BİLANÇOSU
  memory_rules: []
  source_snippets:
  - '"TP.AB.A01", "TP.AB.A02", "TP.AB.A03", "TP.AB.A08", "TP.AB.A09", "TP.AB.A11",
    "TP.AB.A12", "TP.AB.A15", "TP.AB.A16", "TP.AB.A17", "TP.AB.A18", "TP.AB.A23",'
  - '"TP_AB_A03": [2, "II-İç Varlıklar"],'
  indicator_hints: []
  notes: ''
llm_provider: ollama_cloud
llm_model: qwen3.5:397b-cloud
promoted_record_id: evds:TP.AB.A03
promoted_memory_rule_id: memory:global-tp-ab-a03
notes: 'Catalog source: catalog:evds2:TP.AB.A03'
body: "# Semantic proposal for TP.AB.A03\n\n## Target\nseries | evds:TP.AB.A03\n\n\
  ## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\nA.2 İÇ VARLIKLAR\n\n## Candidate\
  \ Unit\nBin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\nbalance_sheet_line\n\
  \n## Confidence\n0.8\n\n## Candidate Themes\n- theme:portfolio-flows\n- theme:foreign-ownership\n\
  - theme:swap-and-securities\n\n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n\
  -\n\n## Source\nhybrid\n\n## Notes\nCatalog source: catalog:evds2:TP.AB.A03\n\n\
  ## Evidence\n{\n  \"ticker\": \"TP.AB.A03\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"A.2_İÇ VARLIKLAR(Bin TL)\",\n  \"context_title\"\
  : \"A.2_İÇ VARLIKLAR(Bin TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Bin\
  \ TL\",\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\",\n\
  \  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.A03\",\n    \"title\": \"\
  A.2 İÇ VARLIKLAR\",\n    \"frequency\": \"i̇ş günü\",\n    \"unit\": \"unknown\"\
  ,\n    \"data_group\": \"bie_abanlbil\",\n    \"category\": \"MERKEZ BANKASI ANALİTİK\
  \ BİLANÇOSU\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\
  \"TP.AB.A01\\\", \\\"TP.AB.A02\\\", \\\"TP.AB.A03\\\", \\\"TP.AB.A08\\\", \\\"TP.AB.A09\\\
  \", \\\"TP.AB.A11\\\", \\\"TP.AB.A12\\\", \\\"TP.AB.A15\\\", \\\"TP.AB.A16\\\",\
  \ \\\"TP.AB.A17\\\", \\\"TP.AB.A18\\\", \\\"TP.AB.A23\\\",\",\n    \"\\\"TP_AB_A03\\\
  \": [2, \\\"II-İç Varlıklar\\\"],\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_AB_A03%3A3161fdd52289.md
---
# Semantic proposal for TP.AB.A03

## Target
series | evds:TP.AB.A03

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
A.2 İÇ VARLIKLAR

## Candidate Unit
Bin TL

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

## Confidence
0.8

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

## Candidate Indicator Inputs
-

## Formula Hint
-

## Source
hybrid

## Notes
Catalog source: catalog:evds2:TP.AB.A03

## Evidence
{
  "ticker": "TP.AB.A03",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "A.2_İÇ VARLIKLAR(Bin TL)",
  "context_title": "A.2_İÇ VARLIKLAR(Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "balance_sheet_line",
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
    "id": "catalog:evds2:TP.AB.A03",
    "title": "A.2 İÇ VARLIKLAR",
    "frequency": "i̇ş günü",
    "unit": "unknown",
    "data_group": "bie_abanlbil",
    "category": "MERKEZ BANKASI ANALİTİK BİLANÇOSU"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.AB.A01\", \"TP.AB.A02\", \"TP.AB.A03\", \"TP.AB.A08\", \"TP.AB.A09\", \"TP.AB.A11\", \"TP.AB.A12\", \"TP.AB.A15\", \"TP.AB.A16\", \"TP.AB.A17\", \"TP.AB.A18\", \"TP.AB.A23\",",
    "\"TP_AB_A03\": [2, \"II-İç Varlıklar\"],"
  ],
  "indicator_hints": [],
  "notes": ""
}
