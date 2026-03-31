---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_AB_TOPLAM:51e5ae17e487
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_AB_TOPLAM:51e5ae17e487
title: Semantic proposal for TP.AB.TOPLAM
status: approved
target_type: series
target_id: evds:TP.AB.TOPLAM
ticker: TP.AB.TOPLAM
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: Toplam (Milyon ABD Doları)
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
evidence_fingerprint: 51e5ae17e4871e7079755912913adf6a05a0d23f
catalog_record_id: catalog:evds2:TP.AB.TOPLAM
memory_rule_ids: []
evidence:
  ticker: TP.AB.TOPLAM
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: MERKEZ BANKASI REZERVLERİ (Milyon usd) (**)
  context_title: MERKEZ BANKASI REZERVLERİ (Milyon usd) (**)
  frequency: weekly
  unit: Milyon usd
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
    id: catalog:evds2:TP.AB.TOPLAM
    title: Toplam (Milyon ABD Doları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_abres2
    category: ULUSLARARASI REZERVLER (TCMB)
  memory_rules: []
  source_snippets:
  - '"TP.AB.TOPLAM", "TP.AB.C1", "TP.AB.C2"'
  - brut_rezerv_s0 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[0],
    "TP_AB_TOPLAM"].astype(float)
  - brut_rezerv_s1 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[1],
    "TP_AB_TOPLAM"].astype(float)
  - '"TP_AB_TOPLAM": [1, "MERKEZ BANKASI REZERVLERİ (Milyon usd) (**)"],'
  - 'if pd.isna(df_analitik_bilanco_t.at["TP_AB_TOPLAM", col1]) or df_analitik_bilanco_t.at["TP_AB_TOPLAM",
    col1] is None:'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.AB.TOPLAM
promoted_memory_rule_id: memory:global-tp-ab-toplam
notes: 'Catalog source: catalog:evds2:TP.AB.TOPLAM'
body: "# Semantic proposal for TP.AB.TOPLAM\n\n## Target\nseries | evds:TP.AB.TOPLAM\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\nToplam (Milyon ABD Doları)\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate\
  \ Role\nbalance_sheet_line\n\n## Confidence\n0.9\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nLLM requested manual review.\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.AB.TOPLAM\n\n## Evidence\n{\n  \"ticker\": \"TP.AB.TOPLAM\",\n\
  \  \"notebook_slug\": \"prbnk-mnklkymt-v5\",\n  \"official_series_name\": \"MERKEZ\
  \ BANKASI REZERVLERİ (Milyon usd) (**)\",\n  \"context_title\": \"MERKEZ BANKASI\
  \ REZERVLERİ (Milyon usd) (**)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"\
  Milyon usd\",\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:prbnk-weekly-zip\",\n    \"source:prbnk-swap-pdf\"\n  ],\n  \"\
  catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.TOPLAM\",\n    \"title\"\
  : \"Toplam (Milyon ABD Doları)\",\n    \"frequency\": \"weekly\",\n    \"unit\"\
  : \"milyon ABD doları\",\n    \"data_group\": \"bie_abres2\",\n    \"category\"\
  : \"ULUSLARARASI REZERVLER (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"\\\"TP.AB.TOPLAM\\\", \\\"TP.AB.C1\\\", \\\"TP.AB.C2\\\"\",\n    \"brut_rezerv_s0\
  \ = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[0], \\\"TP_AB_TOPLAM\\\
  \"].astype(float)\",\n    \"brut_rezerv_s1 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[1],\
  \ \\\"TP_AB_TOPLAM\\\"].astype(float)\",\n    \"\\\"TP_AB_TOPLAM\\\": [1, \\\"MERKEZ\
  \ BANKASI REZERVLERİ (Milyon usd) (**)\\\"],\",\n    \"if pd.isna(df_analitik_bilanco_t.at[\\\
  \"TP_AB_TOPLAM\\\", col1]) or df_analitik_bilanco_t.at[\\\"TP_AB_TOPLAM\\\", col1]\
  \ is None:\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_AB_TOPLAM%3A51e5ae17e487.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.AB.TOPLAM

## Target
series | evds:TP.AB.TOPLAM

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
Toplam (Milyon ABD Doları)

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
Catalog source: catalog:evds2:TP.AB.TOPLAM

## Evidence
{
  "ticker": "TP.AB.TOPLAM",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "MERKEZ BANKASI REZERVLERİ (Milyon usd) (**)",
  "context_title": "MERKEZ BANKASI REZERVLERİ (Milyon usd) (**)",
  "frequency": "weekly",
  "unit": "Milyon usd",
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
    "id": "catalog:evds2:TP.AB.TOPLAM",
    "title": "Toplam (Milyon ABD Doları)",
    "frequency": "weekly",
    "unit": "milyon ABD doları",
    "data_group": "bie_abres2",
    "category": "ULUSLARARASI REZERVLER (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.AB.TOPLAM\", \"TP.AB.C1\", \"TP.AB.C2\"",
    "brut_rezerv_s0 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[0], \"TP_AB_TOPLAM\"].astype(float)",
    "brut_rezerv_s1 = df_analitik_bilanco_com.loc[df_analitik_bilanco_com.index[1], \"TP_AB_TOPLAM\"].astype(float)",
    "\"TP_AB_TOPLAM\": [1, \"MERKEZ BANKASI REZERVLERİ (Milyon usd) (**)\"],",
    "if pd.isna(df_analitik_bilanco_t.at[\"TP_AB_TOPLAM\", col1]) or df_analitik_bilanco_t.at[\"TP_AB_TOPLAM\", col1] is None:"
  ],
  "indicator_hints": [],
  "notes": ""
}
