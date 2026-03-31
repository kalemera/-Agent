---
record_type: proposal
id: proposal:rzrv-blg-v7:series:TP_AB_A10:1b2892d67956
proposal_id: proposal:rzrv-blg-v7:series:TP_AB_A10:1b2892d67956
title: Semantic proposal for TP.AB.A10
status: manual_review
target_type: series
target_id: evds:TP.AB.A10
ticker: TP.AB.A10
notebook_slug: rzrv-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Rzrv_Blg_V7.ipynb
candidate_title: P.1 TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ
candidate_unit: Bin TL
candidate_frequency: i̇ş günü
candidate_role: stock_total
candidate_theme_ids:
- theme:reserves
- theme:net-reserve-estimate
candidate_indicator_inputs:
- derived:estimated-net-reserve
candidate_formula_hint: 'derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan
  tahmini net rezerv uretir.'
confidence: 0.85
source: heuristic
evidence_fingerprint: 1b2892d67956f70afcf166e409031bb73e30fb6c
catalog_record_id: catalog:evds2:TP.AB.A10
memory_rule_ids: []
evidence:
  ticker: TP.AB.A10
  notebook_slug: rzrv-blg-v7
  official_series_name: P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL)
  context_title: P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL)
  frequency: daily
  unit: Bin TL
  role: stock_total
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
    id: catalog:evds2:TP.AB.A10
    title: P.1 TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ
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
  - 'reserve_data_df["Toplam Döviz Yükümlülük"] = (reserve_data_df["TP_AB_A10"]/1000)
    / reserve_data_df["TP_DK_USD_A_YTL"] # pdf verisi milyon dolar, evds verisi bin
    tl'
  - reserve_data = reserve_data_df.drop(columns=["TP_AB_A02", 'TP_AB_A10', 'TP_AB_A11',
    'TP_AB_A14', 'TP_AB_A13', 'TP_DK_USD_A_YTL'])
  indicator_hints:
  - 'derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini
    net rezerv uretir.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: ''
promoted_memory_rule_id: ''
notes: 'Catalog source: catalog:evds2:TP.AB.A10'
body: "# Semantic proposal for TP.AB.A10\n\n## Target\nseries | evds:TP.AB.A10\n\n\
  ## Notebook\nrzrv-blg-v7\n\n## Candidate Title\nP.1 TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ\n\
  \n## Candidate Unit\nBin TL\n\n## Candidate Frequency\ni̇ş günü\n\n## Candidate\
  \ Role\nstock_total\n\n## Confidence\n0.85\n\n## Candidate Themes\n- theme:reserves\n\
  - theme:net-reserve-estimate\n\n## Candidate Indicator Inputs\n- derived:estimated-net-reserve\n\
  \n## Formula Hint\nderived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan\
  \ tahmini net rezerv uretir.\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n\
  ## Approval Reason\n-\n\n## Notes\nCatalog source: catalog:evds2:TP.AB.A10\n\n##\
  \ Evidence\n{\n  \"ticker\": \"TP.AB.A10\",\n  \"notebook_slug\": \"rzrv-blg-v7\"\
  ,\n  \"official_series_name\": \"P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL)\",\n  \"\
  context_title\": \"P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL)\",\n  \"frequency\":\
  \ \"daily\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"stock_total\",\n  \"status\"\
  : \"derived_input\",\n  \"theme_ids\": [\n    \"theme:reserves\",\n    \"theme:net-reserve-estimate\"\
  \n  ],\n  \"indicator_ids\": [\n    \"derived:estimated-net-reserve\"\n  ],\n  \"\
  source_dependency_ids\": [\n    \"source:rzrv-swap-pdf\",\n    \"source:rzrv-manual-swap-ledger\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.AB.A10\",\n    \"\
  title\": \"P.1 TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ\",\n    \"frequency\": \"i̇ş günü\",\n\
  \    \"unit\": \"unknown\",\n    \"data_group\": \"bie_abanlbil\",\n    \"category\"\
  : \"MERKEZ BANKASI ANALİTİK BİLANÇOSU\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\\\
  \"SERIE_CODE\\\"].isin([\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14',\
  \ 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])\",\n \
  \   \"[\\\"TP.AB.A02\\\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL'],\"\
  ,\n    \"reserve_data_df[\\\"Toplam Döviz Yükümlülük\\\"] = (reserve_data_df[\\\"\
  TP_AB_A10\\\"]/1000) / reserve_data_df[\\\"TP_DK_USD_A_YTL\\\"] # pdf verisi milyon\
  \ dolar, evds verisi bin tl\",\n    \"reserve_data = reserve_data_df.drop(columns=[\\\
  \"TP_AB_A02\\\", 'TP_AB_A10', 'TP_AB_A11', 'TP_AB_A14', 'TP_AB_A13', 'TP_DK_USD_A_YTL'])\"\
  \n  ],\n  \"indicator_hints\": [\n    \"derived:estimated-net-reserve: Dis varlik\
  \ ve yukumluluk bloklarindan tahmini net rezerv uretir.\"\n  ],\n  \"notes\": \"\
  \"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Arzrv-blg-v7%3Aseries%3ATP_AB_A10%3A1b2892d67956.md
approval_reason: Confidence 0.85 is below the auto-approve threshold 0.9.
approval_mode: ''
---
# Semantic proposal for TP.AB.A10

## Target
series | evds:TP.AB.A10

## Notebook
rzrv-blg-v7

## Candidate Title
P.1 TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ

## Candidate Unit
Bin TL

## Candidate Frequency
i̇ş günü

## Candidate Role
stock_total

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
heuristic

## Approval Mode
-

## Approval Reason
Confidence 0.85 is below the auto-approve threshold 0.9.

## Notes
Catalog source: catalog:evds2:TP.AB.A10

## Evidence
{
  "ticker": "TP.AB.A10",
  "notebook_slug": "rzrv-blg-v7",
  "official_series_name": "P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL)",
  "context_title": "P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL)",
  "frequency": "daily",
  "unit": "Bin TL",
  "role": "stock_total",
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
    "id": "catalog:evds2:TP.AB.A10",
    "title": "P.1 TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ",
    "frequency": "i̇ş günü",
    "unit": "unknown",
    "data_group": "bie_abanlbil",
    "category": "MERKEZ BANKASI ANALİTİK BİLANÇOSU"
  },
  "memory_rules": [],
  "source_snippets": [
    "print(tcmb_analitik_bilanco_bilgi_detay[tcmb_analitik_bilanco_bilgi_detay[\"SERIE_CODE\"].isin([\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL', 'TP.AB.C1', 'TP.AB.C2', 'TP.AB.N06'])])",
    "[\"TP.AB.A02\", 'TP.AB.A10', 'TP.AB.A11', 'TP.AB.A14', 'TP.AB.A13', 'TP.DK.USD.A.YTL'],",
    "reserve_data_df[\"Toplam Döviz Yükümlülük\"] = (reserve_data_df[\"TP_AB_A10\"]/1000) / reserve_data_df[\"TP_DK_USD_A_YTL\"] # pdf verisi milyon dolar, evds verisi bin tl",
    "reserve_data = reserve_data_df.drop(columns=[\"TP_AB_A02\", 'TP_AB_A10', 'TP_AB_A11', 'TP_AB_A14', 'TP_AB_A13', 'TP_DK_USD_A_YTL'])"
  ],
  "indicator_hints": [
    "derived:estimated-net-reserve: Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir."
  ],
  "notes": ""
}
