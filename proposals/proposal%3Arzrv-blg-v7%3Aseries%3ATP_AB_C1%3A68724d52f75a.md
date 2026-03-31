---
record_type: proposal
id: proposal:rzrv-blg-v7:series:TP_AB_C1:68724d52f75a
proposal_id: proposal:rzrv-blg-v7:series:TP_AB_C1:68724d52f75a
title: Semantic proposal for TP.AB.C1
status: approved
target_type: series
target_id: evds:TP.AB.C1
ticker: TP.AB.C1
notebook_slug: rzrv-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Rzrv_Blg_V7.ipynb
candidate_title: Altın (Milyon ABD Doları)
candidate_unit: milyon ABD doları
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:reserves
- theme:net-reserve-estimate
candidate_indicator_inputs:
- derived:reserve-total
- derived:reserve-gold
- derived:gold-share-in-reserves
candidate_formula_hint: 'derived:reserve-total: Rezerv altin ve rezerv doviz toplamindan
  uretilir.'
confidence: 0.95
source: heuristic
evidence_fingerprint: 68724d52f75a11316d09e27a187541a8edabaf29
catalog_record_id: catalog:evds2:TP.AB.C1
memory_rule_ids: []
evidence:
  ticker: TP.AB.C1
  notebook_slug: rzrv-blg-v7
  official_series_name: Altın(Milyon ABD Doları)
  context_title: Altın(Milyon ABD Doları)
  frequency: weekly
  unit: Milyon ABD Doları
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:reserves
  - theme:net-reserve-estimate
  indicator_ids:
  - derived:reserve-total
  - derived:reserve-gold
  - derived:gold-share-in-reserves
  source_dependency_ids:
  - source:rzrv-swap-pdf
  - source:rzrv-manual-swap-ledger
  catalog_record:
    id: catalog:evds2:TP.AB.C1
    title: Altın (Milyon ABD Doları)
    frequency: weekly
    unit: milyon ABD doları
    data_group: bie_abres2
    category: ULUSLARARASI REZERVLER (TCMB)
  memory_rules: []
  source_snippets:
  - print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay["SERIE_CODE"].isin(["TP.AB.A02",
    'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1',
    'TP.AB.C2', 'TP.AB.N06'])])
  - '[''TP.AB.C1'', ''TP.AB.C2'', ''TP.AB.N06'', "TP_DK_USD_A_YTL"],'
  indicator_hints:
  - 'derived:reserve-total: Rezerv altin ve rezerv doviz toplamindan uretilir.'
  - 'derived:gold-share-in-reserves: Altin rezervinin toplam rezerv icindeki payi.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.AB.C1
promoted_memory_rule_id: memory:global-tp-ab-c1
notes: 'Catalog source: catalog:evds2:TP.AB.C1'
body: "# Semantic proposal for TP.AB.C1\n\n## Target\nseries | evds:TP.AB.C1\n\n##\
  \ Notebook\nrzrv-blg-v7\n\n## Candidate Title\nAltın (Milyon ABD Doları)\n\n## Candidate\
  \ Unit\nmilyon ABD doları\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  balance_sheet_line\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:reserves\n\
  - theme:net-reserve-estimate\n\n## Candidate Indicator Inputs\n- derived:reserve-total\n\
  - derived:reserve-gold\n- derived:gold-share-in-reserves\n\n## Formula Hint\nderived:reserve-total:\
  \ Rezerv altin ve rezerv doviz toplamindan uretilir.\n\n## Source\nheuristic\n\n\
  ## Approval Mode\n-\n\n## Approval Reason\nSame ticker TP.AB.C1 has existing proposal\
  \ in notebook prbnk-mnklkymt-v5 with status review_pending\n\n## Notes\nCatalog\
  \ source: catalog:evds2:TP.AB.C1\n\n## Evidence\n{\n  \"ticker\": \"TP.AB.C1\",\n\
  \  \"notebook_slug\": \"rzrv-blg-v7\",\n  \"official_series_name\": \"Altın(Milyon\
  \ ABD Doları)\",\n  \"context_title\": \"Altın(Milyon ABD Doları)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Milyon ABD Doları\",\n  \"role\": \"balance_sheet_line\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:reserves\"\
  ,\n    \"theme:net-reserve-estimate\"\n  ],\n  \"indicator_ids\": [\n    \"derived:reserve-total\"\
  ,\n    \"derived:reserve-gold\",\n    \"derived:gold-share-in-reserves\"\n  ],\n\
  \  \"source_dependency_ids\": [\n    \"source:rzrv-swap-pdf\",\n    \"source:rzrv-manual-swap-ledger\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.C1\",\n    \"\
  title\": \"Altın (Milyon ABD Doları)\",\n    \"frequency\": \"weekly\",\n    \"\
  unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_abres2\",\n    \"category\"\
  : \"ULUSLARARASI REZERVLER (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\\\
  \"SERIE_CODE\\\"].isin([\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14',\
  \ 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])\",\n \
  \   \"['TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06', \\\"TP_DK_USD_A_YTL\\\"],\"\n  ],\n\
  \  \"indicator_hints\": [\n    \"derived:reserve-total: Rezerv altin ve rezerv doviz\
  \ toplamindan uretilir.\",\n    \"derived:gold-share-in-reserves: Altin rezervinin\
  \ toplam rezerv icindeki payi.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Arzrv-blg-v7%3Aseries%3ATP_AB_C1%3A68724d52f75a.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.AB.C1

## Target
series | evds:TP.AB.C1

## Notebook
rzrv-blg-v7

## Candidate Title
Altın (Milyon ABD Doları)

## Candidate Unit
milyon ABD doları

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

## Confidence
0.95

## Candidate Themes
- theme:reserves
- theme:net-reserve-estimate

## Candidate Indicator Inputs
- derived:reserve-total
- derived:reserve-gold
- derived:gold-share-in-reserves

## Formula Hint
derived:reserve-total: Rezerv altin ve rezerv doviz toplamindan uretilir.

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
  "notebook_slug": "rzrv-blg-v7",
  "official_series_name": "Altın(Milyon ABD Doları)",
  "context_title": "Altın(Milyon ABD Doları)",
  "frequency": "weekly",
  "unit": "Milyon ABD Doları",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:reserves",
    "theme:net-reserve-estimate"
  ],
  "indicator_ids": [
    "derived:reserve-total",
    "derived:reserve-gold",
    "derived:gold-share-in-reserves"
  ],
  "source_dependency_ids": [
    "source:rzrv-swap-pdf",
    "source:rzrv-manual-swap-ledger"
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
    "print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\"SERIE_CODE\"].isin([\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])",
    "['TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06', \"TP_DK_USD_A_YTL\"],"
  ],
  "indicator_hints": [
    "derived:reserve-total: Rezerv altin ve rezerv doviz toplamindan uretilir.",
    "derived:gold-share-in-reserves: Altin rezervinin toplam rezerv icindeki payi."
  ],
  "notes": ""
}
