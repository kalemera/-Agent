---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_18:ddb0076dd960
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_18:ddb0076dd960
title: Semantic proposal for TP.HPBITABLO2.18
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.18
ticker: TP.HPBITABLO2.18
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 1.3.2.YP
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: ddb0076dd960c4580d142d439c7a550d8377f597
catalog_record_id: catalog:evds2:TP.HPBITABLO2.18
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.18
  notebook_slug: dth-blg-v7
  official_series_name: b. YP (Bin TL)
  context_title: A. TOPLAM MEVDUAT (Bin TL) / 3. Yurt Dışı Yerleşikler (Bin TL) /
    b. YP (Bin TL)
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
    id: catalog:evds2:TP.HPBITABLO2.18
    title: 1.3.2.YP
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.17'', ''TP.HPBITABLO2.18'', ''TP.HPBITABLO2.19'', ''TP.HPBITABLO2.20'','
  - '"TP_HPBITABLO2_18": "2. Yurtdışında Yerleşikler", #2. Yurtdışında Yerleşikler(Bin
    TL)-Düzey"'
  - df_kredi_mevduat["B. YP (1+2+3+4)"] = df_kredi_mevduat["TP_HPBITABLO2_6"] + df_kredi_mevduat["TP_HPBITABLO2_15"]
    + df_kredi_mevduat["TP_HPBITABLO2_18"] + df_kredi_mevduat["TP_HPBITABLO2_21"]
  - df_kredi_mevduat["B.2. Yurtdışında Yerleşikler"] = df_kredi_mevduat["TP_HPBITABLO2_18"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.18
promoted_memory_rule_id: memory:global-tp-hpbitablo2-18
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.18'
body: "# Semantic proposal for TP.HPBITABLO2.18\n\n## Target\nseries | evds:TP.HPBITABLO2.18\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n1.3.2.YP\n\n## Candidate Unit\n\
  bin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\ncurrency_split_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nnotebook_slug exists, matching_memory_rules is empty, approved_series\
  \ is empty\n\n## Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.18\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.HPBITABLO2.18\",\n  \"notebook_slug\": \"dth-blg-v7\",\n \
  \ \"official_series_name\": \"b. YP (Bin TL)\",\n  \"context_title\": \"A. TOPLAM\
  \ MEVDUAT (Bin TL) / 3. Yurt Dışı Yerleşikler (Bin TL) / b. YP (Bin TL)\",\n  \"\
  frequency\": \"weekly\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"currency_split_line\"\
  ,\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n\
  \  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO2.18\"\
  ,\n    \"title\": \"1.3.2.YP\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\": \"PARA VE\
  \ BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"\
  source_snippets\": [\n    \"'TP.HPBITABLO2.17', 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19',\
  \ 'TP.HPBITABLO2.20',\",\n    \"\\\"TP_HPBITABLO2_18\\\": \\\"2. Yurtdışında Yerleşikler\\\
  \", #2. Yurtdışında Yerleşikler(Bin TL)-Düzey\\\"\",\n    \"df_kredi_mevduat[\\\"\
  B. YP (1+2+3+4)\\\"] = df_kredi_mevduat[\\\"TP_HPBITABLO2_6\\\"] + df_kredi_mevduat[\\\
  \"TP_HPBITABLO2_15\\\"] + df_kredi_mevduat[\\\"TP_HPBITABLO2_18\\\"] + df_kredi_mevduat[\\\
  \"TP_HPBITABLO2_21\\\"]\",\n    \"df_kredi_mevduat[\\\"B.2. Yurtdışında Yerleşikler\\\
  \"] = df_kredi_mevduat[\\\"TP_HPBITABLO2_18\\\"]\"\n  ],\n  \"indicator_hints\"\
  : [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_18%3Addb0076dd960.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.18

## Target
series | evds:TP.HPBITABLO2.18

## Notebook
dth-blg-v7

## Candidate Title
1.3.2.YP

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
Catalog source: catalog:evds2:TP.HPBITABLO2.18

## Evidence
{
  "ticker": "TP.HPBITABLO2.18",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "b. YP (Bin TL)",
  "context_title": "A. TOPLAM MEVDUAT (Bin TL) / 3. Yurt Dışı Yerleşikler (Bin TL) / b. YP (Bin TL)",
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
    "id": "catalog:evds2:TP.HPBITABLO2.18",
    "title": "1.3.2.YP",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.17', 'TP.HPBITABLO2.18', 'TP.HPBITABLO2.19', 'TP.HPBITABLO2.20',",
    "\"TP_HPBITABLO2_18\": \"2. Yurtdışında Yerleşikler\", #2. Yurtdışında Yerleşikler(Bin TL)-Düzey\"",
    "df_kredi_mevduat[\"B. YP (1+2+3+4)\"] = df_kredi_mevduat[\"TP_HPBITABLO2_6\"] + df_kredi_mevduat[\"TP_HPBITABLO2_15\"] + df_kredi_mevduat[\"TP_HPBITABLO2_18\"] + df_kredi_mevduat[\"TP_HPBITABLO2_21\"]",
    "df_kredi_mevduat[\"B.2. Yurtdışında Yerleşikler\"] = df_kredi_mevduat[\"TP_HPBITABLO2_18\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
