---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_20:d9c7d93113d8
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_20:d9c7d93113d8
title: Semantic proposal for TP.HPBITABLO2.20
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.20
ticker: TP.HPBITABLO2.20
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.4.1.TL
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: d9c7d93113d81b8748ab3686a255c1b368ea0d24
catalog_record_id: catalog:evds2:TP.HPBITABLO2.20
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.20
  notebook_slug: dth-blg-v7
  official_series_name: a. TL (Bin TL)
  context_title: A. TOPLAM MEVDUAT (Bin TL) / 4. Yurt Dışı Yerleşik Bankalar (Bin
    TL) / a. TL (Bin TL)
  frequency: weekly
  unit: Bin TL
  role: currency_split_line
  status: derived_input
  theme_ids:
  - theme:dth
  indicator_ids: []
  source_dependency_ids:
  - source:dth-old-series-excel
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.20
    title: 1.4.1.TL
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.17'', ''TP.HPBITABLO2.18'', ''TP.HPBITABLO2.19'', ''TP.HPBITABLO2.20'','
  - '"TP_HPBITABLO2_20": "4. Yurtdışında Yerleşik Bankalar", #4. Yurtdışında Yerleşik
    Bankalar(Bin TL)-Düzey'
  - df_kredi_mevduat["A. TL (1+2+3+4)"] = df_kredi_mevduat["TP_HPBITABLO2_3"] + df_kredi_mevduat["TP_HPBITABLO2_14"]
    + df_kredi_mevduat["TP_HPBITABLO2_17"] + df_kredi_mevduat["TP_HPBITABLO2_20"]
  - df_kredi_mevduat["A.4. Yurtdışında Yerleşik Bankalar"] = df_kredi_mevduat["TP_HPBITABLO2_20"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.20
promoted_memory_rule_id: memory:global-tp-hpbitablo2-20
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.20'
body: "# Semantic proposal for TP.HPBITABLO2.20\n\n## Target\nseries | evds:TP.HPBITABLO2.20\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.4.1.TL\n\n## Candidate Unit\n\
  bin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\ncurrency_split_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nProposal contains notebook_slug 'dth-blg-v7' indicating\
  \ notebook-specific scoping. approved_series and matching_memory_rules are empty.\n\
  \n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.20\n\n## Evidence\n{\n \
  \ \"ticker\": \"TP.HPBITABLO2.20\",\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"\
  official_series_name\": \"a. TL (Bin TL)\",\n  \"context_title\": \"A. TOPLAM MEVDUAT\
  \ (Bin TL) / 4. Yurt Dışı Yerleşik Bankalar (Bin TL) / a. TL (Bin TL)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"currency_split_line\",\n \
  \ \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n\
  \  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO2.20\"\
  ,\n    \"title\": \"1.4.1.TL\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\": \"PARA VE\
  \ BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"\
  source_snippets\": [\n    \"'TP.HPBITABLO2.17', 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19',\
  \ 'TP.HPBITABLO2.20',\",\n    \"\\\"TP_HPBITABLO2_20\\\": \\\"4. Yurtdışında Yerleşik\
  \ Bankalar\\\", #4. Yurtdışında Yerleşik Bankalar(Bin TL)-Düzey\",\n    \"df_kredi_mevduat[\\\
  \"A. TL (1+2+3+4)\\\"] = df_kredi_mevduat[\\\"TP_HPBITABLO2_3\\\"] + df_kredi_mevduat[\\\
  \"TP_HPBITABLO2_14\\\"] + df_kredi_mevduat[\\\"TP_HPBITABLO2_17\\\"] + df_kredi_mevduat[\\\
  \"TP_HPBITABLO2_20\\\"]\",\n    \"df_kredi_mevduat[\\\"A.4. Yurtdışında Yerleşik\
  \ Bankalar\\\"] = df_kredi_mevduat[\\\"TP_HPBITABLO2_20\\\"]\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_20%3Ad9c7d93113d8.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.20

## Target
series | evds:TP.HPBITABLO2.20

## Notebook
dth-blg-v7

## Candidate Title
1.4.1.TL

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
currency_split_line

## Confidence
0.9

## Candidate Themes
- theme:dth

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
Catalog source: catalog:evds2:TP.HPBITABLO2.20

## Evidence
{
  "ticker": "TP.HPBITABLO2.20",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "a. TL (Bin TL)",
  "context_title": "A. TOPLAM MEVDUAT (Bin TL) / 4. Yurt Dışı Yerleşik Bankalar (Bin TL) / a. TL (Bin TL)",
  "frequency": "weekly",
  "unit": "Bin TL",
  "role": "currency_split_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:dth"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:dth-old-series-excel"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.20",
    "title": "1.4.1.TL",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.17', 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19', 'TP.HPBITABLO2.20',",
    "\"TP_HPBITABLO2_20\": \"4. Yurtdışında Yerleşik Bankalar\", #4. Yurtdışında Yerleşik Bankalar(Bin TL)-Düzey",
    "df_kredi_mevduat[\"A. TL (1+2+3+4)\"] = df_kredi_mevduat[\"TP_HPBITABLO2_3\"] + df_kredi_mevduat[\"TP_HPBITABLO2_14\"] + df_kredi_mevduat[\"TP_HPBITABLO2_17\"] + df_kredi_mevduat[\"TP_HPBITABLO2_20\"]",
    "df_kredi_mevduat[\"A.4. Yurtdışında Yerleşik Bankalar\"] = df_kredi_mevduat[\"TP_HPBITABLO2_20\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
