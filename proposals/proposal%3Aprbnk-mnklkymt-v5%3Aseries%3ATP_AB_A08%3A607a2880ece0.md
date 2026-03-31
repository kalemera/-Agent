---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_AB_A08:607a2880ece0
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_AB_A08:607a2880ece0
title: Semantic proposal for TP.AB.A08
status: manual_review
target_type: series
target_id: evds:TP.AB.A08
ticker: TP.AB.A08
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: A.3 DEĞERLEME HESABI
candidate_unit: BİN TL
candidate_frequency: i̇ş günü
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.8
source: heuristic
evidence_fingerprint: 607a2880ece0e6bf6ef32675da5ea77f07a433ef
catalog_record_id: catalog:evds2:TP.AB.A08
memory_rule_ids: []
evidence:
  ticker: TP.AB.A08
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: A.3_DEĞERLEME HESABI(BİN TL)
  context_title: A.3_DEĞERLEME HESABI(BİN TL)
  frequency: weekly
  unit: BİN TL
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
    id: catalog:evds2:TP.AB.A08
    title: A.3 DEĞERLEME HESABI
    frequency: i̇ş günü
    unit: unknown
    data_group: bie_abanlbil
    category: MERKEZ BANKASI ANALİTİK BİLANÇOSU
  memory_rules: []
  source_snippets:
  - '"TP.AB.A01", "TP.AB.A02", "TP.AB.A03", "TP.AB.A08", "TP.AB.A09", "TP.AB.A11",
    "TP.AB.A12", "TP.AB.A15", "TP.AB.A16", "TP.AB.A17", "TP.AB.A18", "TP.AB.A23",'
  - '"TP_AB_A08": [2, "III-Değerleme Hesabı"],'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: ''
promoted_memory_rule_id: ''
notes: 'Catalog source: catalog:evds2:TP.AB.A08'
body: "# Semantic proposal for TP.AB.A08\n\n## Target\nseries | evds:TP.AB.A08\n\n\
  ## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\nA.3 DEĞERLEME HESABI\n\n##\
  \ Candidate Unit\nBİN TL\n\n## Candidate Frequency\ni̇ş günü\n\n## Candidate Role\n\
  balance_sheet_line\n\n## Confidence\n0.8\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.AB.A08\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.AB.A08\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"A.3_DEĞERLEME HESABI(BİN TL)\",\n  \"context_title\"\
  : \"A.3_DEĞERLEME HESABI(BİN TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"\
  BİN TL\",\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.A08\",\n    \"title\": \"\
  A.3 DEĞERLEME HESABI\",\n    \"frequency\": \"i̇ş günü\",\n    \"unit\": \"unknown\"\
  ,\n    \"data_group\": \"bie_abanlbil\",\n    \"category\": \"MERKEZ BANKASI ANALİTİK\
  \ BİLANÇOSU\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n    \"\\\
  \"TP.AB.A01\\\", \\\"TP.AB.A02\\\", \\\"TP.AB.A03\\\", \\\"TP.AB.A08\\\", \\\"TP.AB.A09\\\
  \", \\\"TP.AB.A11\\\", \\\"TP.AB.A12\\\", \\\"TP.AB.A15\\\", \\\"TP.AB.A16\\\",\
  \ \\\"TP.AB.A17\\\", \\\"TP.AB.A18\\\", \\\"TP.AB.A23\\\",\",\n    \"\\\"TP_AB_A08\\\
  \": [2, \\\"III-Değerleme Hesabı\\\"],\"\n  ],\n  \"indicator_hints\": [],\n  \"\
  notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_AB_A08%3A607a2880ece0.md
approval_reason: Confidence 0.8 is below the auto-approve threshold 0.9.
approval_mode: ''
---
# Semantic proposal for TP.AB.A08

## Target
series | evds:TP.AB.A08

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
A.3 DEĞERLEME HESABI

## Candidate Unit
BİN TL

## Candidate Frequency
i̇ş günü

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
heuristic

## Approval Mode
-

## Approval Reason
Confidence 0.8 is below the auto-approve threshold 0.9.

## Notes
Catalog source: catalog:evds2:TP.AB.A08

## Evidence
{
  "ticker": "TP.AB.A08",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "A.3_DEĞERLEME HESABI(BİN TL)",
  "context_title": "A.3_DEĞERLEME HESABI(BİN TL)",
  "frequency": "weekly",
  "unit": "BİN TL",
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
    "id": "catalog:evds2:TP.AB.A08",
    "title": "A.3 DEĞERLEME HESABI",
    "frequency": "i̇ş günü",
    "unit": "unknown",
    "data_group": "bie_abanlbil",
    "category": "MERKEZ BANKASI ANALİTİK BİLANÇOSU"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.AB.A01\", \"TP.AB.A02\", \"TP.AB.A03\", \"TP.AB.A08\", \"TP.AB.A09\", \"TP.AB.A11\", \"TP.AB.A12\", \"TP.AB.A15\", \"TP.AB.A16\", \"TP.AB.A17\", \"TP.AB.A18\", \"TP.AB.A23\",",
    "\"TP_AB_A08\": [2, \"III-Değerleme Hesabı\"],"
  ],
  "indicator_hints": [],
  "notes": ""
}
