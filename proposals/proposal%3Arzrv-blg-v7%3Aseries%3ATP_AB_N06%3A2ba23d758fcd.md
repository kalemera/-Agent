---
record_type: proposal
id: proposal:rzrv-blg-v7:series:TP_AB_N06:2ba23d758fcd
proposal_id: proposal:rzrv-blg-v7:series:TP_AB_N06:2ba23d758fcd
title: Semantic proposal for TP.AB.N06
status: approved
target_type: series
target_id: evds:TP.AB.N06
ticker: TP.AB.N06
notebook_slug: rzrv-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Rzrv_Blg_V7.ipynb
candidate_title: 2A Net Uluslararası Rezervler (1+2+3)
candidate_unit: Bin TL
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:reserves
- theme:net-reserve-estimate
candidate_indicator_inputs:
- derived:net-reserve-standby
candidate_formula_hint: 'derived:net-reserve-standby: Net rezerv TL serisinin USD
  cinsine cevrilmis stand-by tanimi.'
confidence: 0.95
source: hybrid
evidence_fingerprint: 2ba23d758fcdd4a966df7771c72ec84ccd0e0c10
catalog_record_id: catalog:evds2:TP.AB.N06
memory_rule_ids: []
evidence:
  ticker: TP.AB.N06
  notebook_slug: rzrv-blg-v7
  official_series_name: Net Rezerv TL (Bin TL)
  context_title: Net Rezerv TL (Bin TL)
  frequency: weekly
  unit: Bin TL
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:reserves
  - theme:net-reserve-estimate
  indicator_ids:
  - derived:net-reserve-standby
  source_dependency_ids:
  - source:rzrv-swap-pdf
  - source:rzrv-manual-swap-ledger
  catalog_record:
    id: catalog:evds2:TP.AB.N06
    title: 2A Net Uluslararası Rezervler (1+2+3)
    frequency: weekly
    unit: unknown
    data_group: bie_abstc2
    category: MERKEZ BANKASI HAFTALIK VAZİYET
  memory_rules: []
  source_snippets:
  - print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay["SERIE_CODE"].isin(["TP.AB.A02",
    'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1',
    'TP.AB.C2', 'TP.AB.N06'])])
  - '[''TP.AB.C1'', ''TP.AB.C2'', ''TP.AB.N06'', "TP_DK_USD_A_YTL"],'
  indicator_hints:
  - 'derived:net-reserve-standby: Net rezerv TL serisinin USD cinsine cevrilmis stand-by
    tanimi.'
  notes: ''
llm_provider: ollama_cloud
llm_model: qwen3.5:397b-cloud
promoted_record_id: evds:TP.AB.N06
promoted_memory_rule_id: memory:global-tp-ab-n06
notes: 'Catalog source: catalog:evds2:TP.AB.N06'
body: "# Semantic proposal for TP.AB.N06\n\n## Target\nseries | evds:TP.AB.N06\n\n\
  ## Notebook\nrzrv-blg-v7\n\n## Candidate Title\n2A Net Uluslararası Rezervler (1+2+3)\n\
  \n## Candidate Unit\nBin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  balance_sheet_line\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:reserves\n\
  - theme:net-reserve-estimate\n\n## Candidate Indicator Inputs\n- derived:net-reserve-standby\n\
  \n## Formula Hint\nderived:net-reserve-standby: Net rezerv TL serisinin USD cinsine\
  \ cevrilmis stand-by tanimi.\n\n## Source\nhybrid\n\n## Notes\nCatalog source: catalog:evds2:TP.AB.N06\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.AB.N06\",\n  \"notebook_slug\": \"rzrv-blg-v7\"\
  ,\n  \"official_series_name\": \"Net Rezerv TL (Bin TL)\",\n  \"context_title\"\
  : \"Net Rezerv TL (Bin TL)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"Bin TL\"\
  ,\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:reserves\",\n    \"theme:net-reserve-estimate\"\n  ],\n  \"indicator_ids\"\
  : [\n    \"derived:net-reserve-standby\"\n  ],\n  \"source_dependency_ids\": [\n\
  \    \"source:rzrv-swap-pdf\",\n    \"source:rzrv-manual-swap-ledger\"\n  ],\n \
  \ \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.N06\",\n    \"title\"\
  : \"2A Net Uluslararası Rezervler (1+2+3)\",\n    \"frequency\": \"weekly\",\n \
  \   \"unit\": \"unknown\",\n    \"data_group\": \"bie_abstc2\",\n    \"category\"\
  : \"MERKEZ BANKASI HAFTALIK VAZİYET\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\\\
  \"SERIE_CODE\\\"].isin([\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14',\
  \ 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])\",\n \
  \   \"['TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06', \\\"TP_DK_USD_A_YTL\\\"],\"\n  ],\n\
  \  \"indicator_hints\": [\n    \"derived:net-reserve-standby: Net rezerv TL serisinin\
  \ USD cinsine cevrilmis stand-by tanimi.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Arzrv-blg-v7%3Aseries%3ATP_AB_N06%3A2ba23d758fcd.md
---
# Semantic proposal for TP.AB.N06

## Target
series | evds:TP.AB.N06

## Notebook
rzrv-blg-v7

## Candidate Title
2A Net Uluslararası Rezervler (1+2+3)

## Candidate Unit
Bin TL

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
- derived:net-reserve-standby

## Formula Hint
derived:net-reserve-standby: Net rezerv TL serisinin USD cinsine cevrilmis stand-by tanimi.

## Source
hybrid

## Notes
Catalog source: catalog:evds2:TP.AB.N06

## Evidence
{
  "ticker": "TP.AB.N06",
  "notebook_slug": "rzrv-blg-v7",
  "official_series_name": "Net Rezerv TL (Bin TL)",
  "context_title": "Net Rezerv TL (Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:reserves",
    "theme:net-reserve-estimate"
  ],
  "indicator_ids": [
    "derived:net-reserve-standby"
  ],
  "source_dependency_ids": [
    "source:rzrv-swap-pdf",
    "source:rzrv-manual-swap-ledger"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.AB.N06",
    "title": "2A Net Uluslararası Rezervler (1+2+3)",
    "frequency": "weekly",
    "unit": "unknown",
    "data_group": "bie_abstc2",
    "category": "MERKEZ BANKASI HAFTALIK VAZİYET"
  },
  "memory_rules": [],
  "source_snippets": [
    "print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\"SERIE_CODE\"].isin([\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])",
    "['TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06', \"TP_DK_USD_A_YTL\"],"
  ],
  "indicator_hints": [
    "derived:net-reserve-standby: Net rezerv TL serisinin USD cinsine cevrilmis stand-by tanimi."
  ],
  "notes": ""
}
