---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_AB_C1:19fa609fa0e0
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_AB_C1:19fa609fa0e0
title: Semantic proposal for TP.AB.C1
status: approved
target_type: series
target_id: evds:TP.AB.C1
ticker: TP.AB.C1
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: Altın (Milyon ABD Doları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 19fa609fa0e0666edb6809e98cec586b67007e7a
catalog_record_id: catalog:evds2:TP.AB.C1
memory_rule_ids: []
evidence:
  ticker: TP.AB.C1
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: I-Altın
  context_title: I-Altın
  frequency: weekly
  unit: milyon ABD doları
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
    id: catalog:evds2:TP.AB.C1
    title: Altın (Milyon ABD Doları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_abres2
    category: ULUSLARARASI REZERVLER (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.AB.TOPLAM", "TP.AB.C1", "TP.AB.C2"'
  - altin_rezerv_s0 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[0],
    "TP_AB_C1"].astype(float)
  - altin_rezerv_s1 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[1],
    "TP_AB_C1"].astype(float)
  - '"TP_AB_C1": [2, "I-Altın"],'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.AB.C1
promoted_memory_rule_id: memory:global-tp-ab-c1
notes: 'Catalog source: catalog:evds2:TP.AB.C1'
body: "# Semantic proposal for TP.AB.C1\n\n## Target\nseries | evds:TP.AB.C1\n\n##\
  \ Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\nAltın (Milyon ABD Doları)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nbalance_sheet_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.AB.C1\n\n## Evidence\n{\n  \"ticker\": \"TP.AB.C1\",\n  \"notebook_slug\"\
  : \"prbnk-mnklkymt-v5\",\n  \"official_series_name\": \"I-Altın\",\n  \"context_title\"\
  : \"I-Altın\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"milyon ABD doları\"\
  ,\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\",\n    \"theme:swap-and-securities\"\
  \n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:prbnk-weekly-zip\"\
  ,\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"catalog_record\": {\n    \"id\": \"\
  catalog:evds2:TP.AB.C1\",\n    \"title\": \"Altın (Milyon ABD Doları)\",\n    \"\
  frequency\": \"weekly\",\n    \"unit\": \"milyon ABD doları\",\n    \"data_group\"\
  : \"bie_abres2\",\n    \"category\": \"ULUSLARARASI REZERVLER (TCMB)\"\n  },\n \
  \ \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\"TP.AB.TOPLAM\\\", \\\
  \"TP.AB.C1\\\", \\\"TP.AB.C2\\\"\",\n    \"altin_rezerv_s0 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[0],\
  \ \\\"TP_AB_C1\\\"].astype(float)\",\n    \"altin_rezerv_s1 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[1],\
  \ \\\"TP_AB_C1\\\"].astype(float)\",\n    \"\\\"TP_AB_C1\\\": [2, \\\"I-Altın\\\"\
  ],\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_AB_C1%3A19fa609fa0e0.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.AB.C1

## Target
series | evds:TP.AB.C1

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
Altın (Milyon ABD Doları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

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
Catalog source: catalog:evds2:TP.AB.C1

## Evidence
{
  "ticker": "TP.AB.C1",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "I-Altın",
  "context_title": "I-Altın",
  "frequency": "weekly",
  "unit": "milyon ABD doları",
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
    "id": "catalog:evds2:TP.AB.C1",
    "title": "Altın (Milyon ABD Doları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_abres2",
    "category": "ULUSLARARASI REZERVLER (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.AB.TOPLAM\", \"TP.AB.C1\", \"TP.AB.C2\"",
    "altin_rezerv_s0 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[0], \"TP_AB_C1\"].astype(float)",
    "altin_rezerv_s1 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[1], \"TP_AB_C1\"].astype(float)",
    "\"TP_AB_C1\": [2, \"I-Altın\"],"
  ],
  "indicator_hints": [],
  "notes": ""
}
