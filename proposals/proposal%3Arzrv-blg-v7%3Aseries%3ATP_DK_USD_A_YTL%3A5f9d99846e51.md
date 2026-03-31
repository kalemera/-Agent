---
record_type: proposal
id: proposal:rzrv-blg-v7:series:TP_DK_USD_A_YTL:5f9d99846e51
proposal_id: proposal:rzrv-blg-v7:series:TP_DK_USD_A_YTL:5f9d99846e51
title: Semantic proposal for TP.DK.USD.A.YTL
status: approved
target_type: series
target_id: evds:TP.DK.USD.A.YTL
ticker: TP.DK.USD.A.YTL
notebook_slug: rzrv-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Rzrv_Blg_V7.ipynb
candidate_title: (USD)  ABD  Doları  (Döviz  Alış)
candidate_unit: Türk lirası
candidate_frequency: daily
candidate_role: ratio_input
candidate_theme_ids:
- theme:reserves
- theme:net-reserve-estimate
candidate_indicator_inputs:
- derived:net-reserve-standby
- derived:estimated-net-reserve
candidate_formula_hint: 'derived:net-reserve-standby: Net rezerv TL serisinin USD
  cinsine cevrilmis stand-by tanimi.'
confidence: 0.95
source: heuristic
evidence_fingerprint: 5f9d99846e518c919a79118c2834ceb99b07a301
catalog_record_id: catalog:evds2:TP.DK.USD.A.YTL
memory_rule_ids: []
evidence:
  ticker: TP.DK.USD.A.YTL
  notebook_slug: rzrv-blg-v7
  official_series_name: (USD) ABD Doları (Döviz Alış)
  context_title: (USD) ABD Doları (Döviz Alış)
  frequency: daily
  unit: USD
  role: ratio_input
  status: derived_input
  theme_ids:
  - theme:reserves
  - theme:net-reserve-estimate
  indicator_ids:
  - derived:net-reserve-standby
  - derived:estimated-net-reserve
  source_dependency_ids:
  - source:rzrv-swap-pdf
  - source:rzrv-manual-swap-ledger
  catalog_record:
    id: catalog:evds2:TP.DK.USD.A.YTL
    title: (USD)  ABD  Doları  (Döviz  Alış)
    frequency: daily
    unit: Türk lirası
    data_group: bie_dkdovytl
    category: TCMB DÖVİZ KURLARI
  memory_rules: []
  source_snippets:
  - print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay["SERIE_CODE"].isin(["TP.AB.A02",
    'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1',
    'TP.AB.C2', 'TP.AB.N06'])])
  - '["TP.AB.A02", ''TP.AB.A10'', ''TP.AB.A11'', ''TP.AB.A14'', ''TP.AB.A13'', ''TP.DK.USD.A.YTL''],'
  - 'reserve_data_df["Dış Varlık"] = (reserve_data_df["TP_AB_A02"]/1000) / reserve_data_df["TP_DK_USD_A_YTL"]
    # pdf verisi milyon dolar, evds verisi bin tl'
  - 'reserve_data_df["Toplam Döviz Yükümlülük"] = (reserve_data_df["TP_AB_A10"]/1000)
    / reserve_data_df["TP_DK_USD_A_YTL"] # pdf verisi milyon dolar, evds verisi bin
    tl'
  - 'reserve_data_df["Dış Yükümlülük"] = (reserve_data_df["TP_AB_A11"]/1000) / reserve_data_df["TP_DK_USD_A_YTL"]
    # pdf verisi milyon dolar, evds verisi bin tl'
  indicator_hints:
  - 'derived:net-reserve-standby: Net rezerv TL serisinin USD cinsine cevrilmis stand-by
    tanimi.'
  - 'derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini
    net rezerv uretir.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DK.USD.A.YTL
promoted_memory_rule_id: memory:global-tp-dk-usd-a-ytl
notes: 'Catalog source: catalog:evds2:TP.DK.USD.A.YTL'
body: "# Semantic proposal for TP.DK.USD.A.YTL\n\n## Target\nseries | evds:TP.DK.USD.A.YTL\n\
  \n## Notebook\nrzrv-blg-v7\n\n## Candidate Title\n(USD)  ABD  Doları  (Döviz  Alış)\n\
  \n## Candidate Unit\nTürk lirası\n\n## Candidate Frequency\ndaily\n\n## Candidate\
  \ Role\nratio_input\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:reserves\n\
  - theme:net-reserve-estimate\n\n## Candidate Indicator Inputs\n- derived:net-reserve-standby\n\
  - derived:estimated-net-reserve\n\n## Formula Hint\nderived:net-reserve-standby:\
  \ Net rezerv TL serisinin USD cinsine cevrilmis stand-by tanimi.\n\n## Source\n\
  heuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.DK.USD.A.YTL\n\n## Evidence\n{\n  \"ticker\": \"TP.DK.USD.A.YTL\"\
  ,\n  \"notebook_slug\": \"rzrv-blg-v7\",\n  \"official_series_name\": \"(USD) ABD\
  \ Doları (Döviz Alış)\",\n  \"context_title\": \"(USD) ABD Doları (Döviz Alış)\"\
  ,\n  \"frequency\": \"daily\",\n  \"unit\": \"USD\",\n  \"role\": \"ratio_input\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:reserves\"\
  ,\n    \"theme:net-reserve-estimate\"\n  ],\n  \"indicator_ids\": [\n    \"derived:net-reserve-standby\"\
  ,\n    \"derived:estimated-net-reserve\"\n  ],\n  \"source_dependency_ids\": [\n\
  \    \"source:rzrv-swap-pdf\",\n    \"source:rzrv-manual-swap-ledger\"\n  ],\n \
  \ \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.DK.USD.A.YTL\",\n    \"\
  title\": \"(USD)  ABD  Doları  (Döviz  Alış)\",\n    \"frequency\": \"daily\",\n\
  \    \"unit\": \"Türk lirası\",\n    \"data_group\": \"bie_dkdovytl\",\n    \"category\"\
  : \"TCMB DÖVİZ KURLARI\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\":\
  \ [\n    \"print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\\\
  \"SERIE_CODE\\\"].isin([\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14',\
  \ 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])\",\n \
  \   \"[\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL'],\"\
  ,\n    \"reserve_data_df[\\\"Dış Varlık\\\"] = (reserve_data_df[\\\"TP_AB_A02\\\"\
  ]/1000) / reserve_data_df[\\\"TP_DK_USD_A_YTL\\\"] # pdf verisi milyon dolar, evds\
  \ verisi bin tl\",\n    \"reserve_data_df[\\\"Toplam Döviz Yükümlülük\\\"] = (reserve_data_df[\\\
  \"TP_AB_A10\\\"]/1000) / reserve_data_df[\\\"TP_DK_USD_A_YTL\\\"] # pdf verisi milyon\
  \ dolar, evds verisi bin tl\",\n    \"reserve_data_df[\\\"Dış Yükümlülük\\\"] =\
  \ (reserve_data_df[\\\"TP_AB_A11\\\"]/1000) / reserve_data_df[\\\"TP_DK_USD_A_YTL\\\
  \"] # pdf verisi milyon dolar, evds verisi bin tl\"\n  ],\n  \"indicator_hints\"\
  : [\n    \"derived:net-reserve-standby: Net rezerv TL serisinin USD cinsine cevrilmis\
  \ stand-by tanimi.\",\n    \"derived:estimated-net-reserve: Dis varlik ve yukumluluk\
  \ bloklarindan tahmini net rezerv uretir.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Arzrv-blg-v7%3Aseries%3ATP_DK_USD_A_YTL%3A5f9d99846e51.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DK.USD.A.YTL

## Target
series | evds:TP.DK.USD.A.YTL

## Notebook
rzrv-blg-v7

## Candidate Title
(USD)  ABD  Doları  (Döviz  Alış)

## Candidate Unit
Türk lirası

## Candidate Frequency
daily

## Candidate Role
ratio_input

## Confidence
0.95

## Candidate Themes
- theme:reserves
- theme:net-reserve-estimate

## Candidate Indicator Inputs
- derived:net-reserve-standby
- derived:estimated-net-reserve

## Formula Hint
derived:net-reserve-standby: Net rezerv TL serisinin USD cinsine cevrilmis stand-by tanimi.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.DK.USD.A.YTL

## Evidence
{
  "ticker": "TP.DK.USD.A.YTL",
  "notebook_slug": "rzrv-blg-v7",
  "official_series_name": "(USD) ABD Doları (Döviz Alış)",
  "context_title": "(USD) ABD Doları (Döviz Alış)",
  "frequency": "daily",
  "unit": "USD",
  "role": "ratio_input",
  "status": "derived_input",
  "theme_ids": [
    "theme:reserves",
    "theme:net-reserve-estimate"
  ],
  "indicator_ids": [
    "derived:net-reserve-standby",
    "derived:estimated-net-reserve"
  ],
  "source_dependency_ids": [
    "source:rzrv-swap-pdf",
    "source:rzrv-manual-swap-ledger"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DK.USD.A.YTL",
    "title": "(USD)  ABD  Doları  (Döviz  Alış)",
    "frequency": "daily",
    "unit": "Türk lirası",
    "data_group": "bie_dkdovytl",
    "category": "TCMB DÖVİZ KURLARI"
  },
  "memory_rules": [],
  "source_snippets": [
    "print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\"SERIE_CODE\"].isin([\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])",
    "[\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL'],",
    "reserve_data_df[\"Dış Varlık\"] = (reserve_data_df[\"TP_AB_A02\"]/1000) / reserve_data_df[\"TP_DK_USD_A_YTL\"] # pdf verisi milyon dolar, evds verisi bin tl",
    "reserve_data_df[\"Toplam Döviz Yükümlülük\"] = (reserve_data_df[\"TP_AB_A10\"]/1000) / reserve_data_df[\"TP_DK_USD_A_YTL\"] # pdf verisi milyon dolar, evds verisi bin tl",
    "reserve_data_df[\"Dış Yükümlülük\"] = (reserve_data_df[\"TP_AB_A11\"]/1000) / reserve_data_df[\"TP_DK_USD_A_YTL\"] # pdf verisi milyon dolar, evds verisi bin tl"
  ],
  "indicator_hints": [
    "derived:net-reserve-standby: Net rezerv TL serisinin USD cinsine cevrilmis stand-by tanimi.",
    "derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir."
  ],
  "notes": ""
}
