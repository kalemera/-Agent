---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_24:864451e173e2
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_24:864451e173e2
title: Semantic proposal for TP.HPBITABLO2.24
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.24
ticker: TP.HPBITABLO2.24
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 2.1.1.TL
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 864451e173e22820f683a9d32374a1b91f484f82
catalog_record_id: catalog:evds2:TP.HPBITABLO2.24
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.24
  notebook_slug: dth-blg-v7
  official_series_name: a. TL (Bin TL)
  context_title: B. TOPLAM KREDİ (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / a.
    TL (Bin TL)
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
    id: catalog:evds2:TP.HPBITABLO2.24
    title: 2.1.1.TL
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.21'', ''TP.HPBITABLO2.22'', ''TP.HPBITABLO2.23'', ''TP.HPBITABLO2.24'','
  - '''TP_HPBITABLO2_24'': "",'
  - df_kredi_mevduat["A. TL"] = df_kredi_mevduat["TP_HPBITABLO2_24"] + df_kredi_mevduat["TP_HPBITABLO2_33"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.24
promoted_memory_rule_id: memory:global-tp-hpbitablo2-24
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.24'
body: "# Semantic proposal for TP.HPBITABLO2.24\n\n## Target\nseries | evds:TP.HPBITABLO2.24\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n2.1.1.TL\n\n## Candidate Unit\n\
  bin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\ncurrency_split_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nsame_ticker_proposals contains pending review from different\
  \ notebook\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.24\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.HPBITABLO2.24\",\n  \"notebook_slug\": \"dth-blg-v7\",\n \
  \ \"official_series_name\": \"a. TL (Bin TL)\",\n  \"context_title\": \"B. TOPLAM\
  \ KREDİ (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / a. TL (Bin TL)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"currency_split_line\",\n \
  \ \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n\
  \  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO2.24\"\
  ,\n    \"title\": \"2.1.1.TL\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\": \"PARA VE\
  \ BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"\
  source_snippets\": [\n    \"'TP.HPBITABLO2.21', 'TP.HPBITABLO2.22', 'TP.HPBITABLO2.23',\
  \ 'TP.HPBITABLO2.24',\",\n    \"'TP_HPBITABLO2_24': \\\"\\\",\",\n    \"df_kredi_mevduat[\\\
  \"A. TL\\\"] = df_kredi_mevduat[\\\"TP_HPBITABLO2_24\\\"] + df_kredi_mevduat[\\\"\
  TP_HPBITABLO2_33\\\"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_24%3A864451e173e2.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.24

## Target
series | evds:TP.HPBITABLO2.24

## Notebook
dth-blg-v7

## Candidate Title
2.1.1.TL

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
Catalog source: catalog:evds2:TP.HPBITABLO2.24

## Evidence
{
  "ticker": "TP.HPBITABLO2.24",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "a. TL (Bin TL)",
  "context_title": "B. TOPLAM KREDİ (Bin TL) / 1. Yurt İçi Yerleşikler (Bin TL) / a. TL (Bin TL)",
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
    "id": "catalog:evds2:TP.HPBITABLO2.24",
    "title": "2.1.1.TL",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.21', 'TP.HPBITABLO2.22', 'TP.HPBITABLO2.23', 'TP.HPBITABLO2.24',",
    "'TP_HPBITABLO2_24': \"\",",
    "df_kredi_mevduat[\"A. TL\"] = df_kredi_mevduat[\"TP_HPBITABLO2_24\"] + df_kredi_mevduat[\"TP_HPBITABLO2_33\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
