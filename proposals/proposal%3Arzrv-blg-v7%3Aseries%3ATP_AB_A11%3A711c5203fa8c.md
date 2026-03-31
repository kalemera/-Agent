---
record_type: proposal
id: proposal:rzrv-blg-v7:series:TP_AB_A11:711c5203fa8c
proposal_id: proposal:rzrv-blg-v7:series:TP_AB_A11:711c5203fa8c
title: Semantic proposal for TP.AB.A11
status: approved
target_type: series
target_id: evds:TP.AB.A11
ticker: TP.AB.A11
notebook_slug: rzrv-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Rzrv_Blg_V7.ipynb
candidate_title: P.1a Dış Yükümlülükler
candidate_unit: Bin TL
candidate_frequency: i̇ş günü
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:reserves
- theme:net-reserve-estimate
candidate_indicator_inputs:
- derived:estimated-net-reserve
candidate_formula_hint: 'derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan
  tahmini net rezerv uretir.'
confidence: 0.85
source: hybrid
evidence_fingerprint: 711c5203fa8c9e691d2d435262f100129f8f94f7
catalog_record_id: catalog:evds2:TP.AB.A11
memory_rule_ids: []
evidence:
  ticker: TP.AB.A11
  notebook_slug: rzrv-blg-v7
  official_series_name: P.1a_Dış Yükümlülükler(Bin TL)
  context_title: P.1a_Dış Yükümlülükler(Bin TL)
  frequency: daily
  unit: Bin TL
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:reserves
  - theme:net-reserve-estimate
  indicator_ids:
  - derived:estimated-net-reserve
  source_dependency_ids:
  - source:rzrv-swap-pdf
  - source:rzrv-manual-swap-ledger
  catalog_record:
    id: catalog:evds2:TP.AB.A11
    title: P.1a Dış Yükümlülükler
    frequency: i̇ş günü
    unit: unknown
    data_group: bie_abanlbil
    category: MERKEZ BANKASI ANALİTİK BİLANÇOSU
  memory_rules: []
  source_snippets:
  - print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay["SERIE_CODE"].isin(["TP.AB.A02",
    'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1',
    'TP.AB.C2', 'TP.AB.N06'])])
  - '["TP.AB.A02", ''TP.AB.A10'', ''TP.AB.A11'', ''TP.AB.A14'', ''TP.AB.A13'', ''TP.DK.USD.A.YTL''],'
  - 'reserve_data_df["Dış Yükümlülük"] = (reserve_data_df["TP_AB_A11"]/1000) / reserve_data_df["TP_DK_USD_A_YTL"]
    # pdf verisi milyon dolar, evds verisi bin tl'
  - reserve_data = reserve_data_df.drop(columns=["TP_AB_A02", 'TP_AB_A10', 'TP_AB_A11',
    'TP_AB_A14', 'TP_AB_A13', 'TP_DK_USD_A_YTL'])
  indicator_hints:
  - 'derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini
    net rezerv uretir.'
  notes: ''
llm_provider: ollama_cloud
llm_model: qwen3.5:397b-cloud
promoted_record_id: ''
promoted_memory_rule_id: memory:rzrv-blg-v7-tp-ab-a11
notes: 'Catalog source: catalog:evds2:TP.AB.A11 Approved via notebook-scoped memory
  rule.'
body: "# Semantic proposal for TP.AB.A11\n\n## Target\nseries | evds:TP.AB.A11\n\n\
  ## Notebook\nrzrv-blg-v7\n\n## Candidate Title\nP.1a Dış Yükümlülükler\n\n## Candidate\
  \ Unit\nBin TL\n\n## Candidate Frequency\ni̇ş günü\n\n## Candidate Role\nbalance_sheet_line\n\
  \n## Confidence\n0.85\n\n## Candidate Themes\n- theme:reserves\n- theme:net-reserve-estimate\n\
  \n## Candidate Indicator Inputs\n- derived:estimated-net-reserve\n\n## Formula Hint\n\
  derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini net\
  \ rezerv uretir.\n\n## Source\nhybrid\n\n## Notes\nCatalog source: catalog:evds2:TP.AB.A11\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.AB.A11\",\n  \"notebook_slug\": \"rzrv-blg-v7\"\
  ,\n  \"official_series_name\": \"P.1a_Dış Yükümlülükler(Bin TL)\",\n  \"context_title\"\
  : \"P.1a_Dış Yükümlülükler(Bin TL)\",\n  \"frequency\": \"daily\",\n  \"unit\":\
  \ \"Bin TL\",\n  \"role\": \"balance_sheet_line\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:reserves\",\n    \"theme:net-reserve-estimate\"\
  \n  ],\n  \"indicator_ids\": [\n    \"derived:estimated-net-reserve\"\n  ],\n  \"\
  source_dependency_ids\": [\n    \"source:rzrv-swap-pdf\",\n    \"source:rzrv-manual-swap-ledger\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.A11\",\n    \"\
  title\": \"P.1a Dış Yükümlülükler\",\n    \"frequency\": \"i̇ş günü\",\n    \"unit\"\
  : \"unknown\",\n    \"data_group\": \"bie_abanlbil\",\n    \"category\": \"MERKEZ\
  \ BANKASI ANALİTİK BİLANÇOSU\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\\\
  \"SERIE_CODE\\\"].isin([\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14',\
  \ 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])\",\n \
  \   \"[\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL'],\"\
  ,\n    \"reserve_data_df[\\\"Dış Yükümlülük\\\"] = (reserve_data_df[\\\"TP_AB_A11\\\
  \"]/1000) / reserve_data_df[\\\"TP_DK_USD_A_YTL\\\"] # pdf verisi milyon dolar,\
  \ evds verisi bin tl\",\n    \"reserve_data = reserve_data_df.drop(columns=[\\\"\
  TP_AB_A02\\\", 'TP_AB_A10', 'TP_AB_A11', 'TP_AB_A14', 'TP_AB_A13', 'TP_DK_USD_A_YTL'])\"\
  \n  ],\n  \"indicator_hints\": [\n    \"derived:estimated-net-reserve: Dis varlik\
  \ ve yukumluluk bloklarindan tahmini net rezerv uretir.\"\n  ],\n  \"notes\": \"\
  \"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Arzrv-blg-v7%3Aseries%3ATP_AB_A11%3A711c5203fa8c.md
---
# Semantic proposal for TP.AB.A11

## Target
series | evds:TP.AB.A11

## Notebook
rzrv-blg-v7

## Candidate Title
P.1a Dış Yükümlülükler

## Candidate Unit
Bin TL

## Candidate Frequency
i̇ş günü

## Candidate Role
balance_sheet_line

## Confidence
0.85

## Candidate Themes
- theme:reserves
- theme:net-reserve-estimate

## Candidate Indicator Inputs
- derived:estimated-net-reserve

## Formula Hint
derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir.

## Source
hybrid

## Notes
Catalog source: catalog:evds2:TP.AB.A11 Approved via notebook-scoped memory rule.

## Evidence
{
  "ticker": "TP.AB.A11",
  "notebook_slug": "rzrv-blg-v7",
  "official_series_name": "P.1a_Dış Yükümlülükler(Bin TL)",
  "context_title": "P.1a_Dış Yükümlülükler(Bin TL)",
  "frequency": "daily",
  "unit": "Bin TL",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:reserves",
    "theme:net-reserve-estimate"
  ],
  "indicator_ids": [
    "derived:estimated-net-reserve"
  ],
  "source_dependency_ids": [
    "source:rzrv-swap-pdf",
    "source:rzrv-manual-swap-ledger"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.AB.A11",
    "title": "P.1a Dış Yükümlülükler",
    "frequency": "i̇ş günü",
    "unit": "unknown",
    "data_group": "bie_abanlbil",
    "category": "MERKEZ BANKASI ANALİTİK BİLANÇOSU"
  },
  "memory_rules": [],
  "source_snippets": [
    "print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\"SERIE_CODE\"].isin([\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])",
    "[\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL'],",
    "reserve_data_df[\"Dış Yükümlülük\"] = (reserve_data_df[\"TP_AB_A11\"]/1000) / reserve_data_df[\"TP_DK_USD_A_YTL\"] # pdf verisi milyon dolar, evds verisi bin tl",
    "reserve_data = reserve_data_df.drop(columns=[\"TP_AB_A02\", 'TP_AB_A10', 'TP_AB_A11', 'TP_AB_A14', 'TP_AB_A13', 'TP_DK_USD_A_YTL'])"
  ],
  "indicator_hints": [
    "derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir."
  ],
  "notes": ""
}
