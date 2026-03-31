---
record_type: proposal
id: proposal:dth-blg-v7:series:TP_HPBITABLO2_33:e084294442e0
proposal_id: proposal:dth-blg-v7:series:TP_HPBITABLO2_33:e084294442e0
title: Semantic proposal for TP.HPBITABLO2.33
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.33
ticker: TP.HPBITABLO2.33
notebook_slug: dth-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\DTH_Blg_V7.ipynb
candidate_title: 2.2.1.TL
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: currency_split_line
candidate_theme_ids:
- theme:dth
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: e084294442e0290389b15da83deb52a7153f5465
catalog_record_id: catalog:evds2:TP.HPBITABLO2.33
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.33
  notebook_slug: dth-blg-v7
  official_series_name: a. TL (Bin TL)
  context_title: B. TOPLAM KREDİ (Bin TL) / 2. Yurt İçi Yerleşik Finansal Kuruluşlar
    (Bin TL) / a. TL (Bin TL)
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
    id: catalog:evds2:TP.HPBITABLO2.33
    title: 2.2.1.TL
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.28'', ''TP.HPBITABLO2.32'', ''TP.HPBITABLO2.33'', ''TP.HPBITABLO2.34'''
  - '''TP_HPBITABLO2_33'': "",'
  - '#"TP_HPBITABLO2_33": "A. TL", #A. TL(Bin TL)-Düzey'
  - df_kredi_mevduat["A. TL"] = df_kredi_mevduat["TP_HPBITABLO2_24"] + df_kredi_mevduat["TP_HPBITABLO2_33"]
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.33
promoted_memory_rule_id: memory:global-tp-hpbitablo2-33
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.33'
body: "# Semantic proposal for TP.HPBITABLO2.33\n\n## Target\nseries | evds:TP.HPBITABLO2.33\n\
  \n## Notebook\ndth-blg-v7\n\n## Candidate Title\n2.2.1.TL\n\n## Candidate Unit\n\
  bin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\ncurrency_split_line\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:dth\n\n## Candidate Indicator\
  \ Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n\
  -\n\n## Approval Reason\nSame ticker proposal exists with status review_pending\
  \ and identical signature, indicating uncertainty regarding global safety.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.33\n\n## Evidence\n{\n  \"\
  ticker\": \"TP.HPBITABLO2.33\",\n  \"notebook_slug\": \"dth-blg-v7\",\n  \"official_series_name\"\
  : \"a. TL (Bin TL)\",\n  \"context_title\": \"B. TOPLAM KREDİ (Bin TL) / 2. Yurt\
  \ İçi Yerleşik Finansal Kuruluşlar (Bin TL) / a. TL (Bin TL)\",\n  \"frequency\"\
  : \"weekly\",\n  \"unit\": \"Bin TL\",\n  \"role\": \"currency_split_line\",\n \
  \ \"status\": \"derived_input\",\n  \"theme_ids\": [\n    \"theme:dth\"\n  ],\n\
  \  \"indicator_ids\": [],\n  \"source_dependency_ids\": [\n    \"source:dth-old-series-excel\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO2.33\"\
  ,\n    \"title\": \"2.2.1.TL\",\n    \"frequency\": \"weekly\",\n    \"unit\": \"\
  bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\": \"PARA VE\
  \ BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"\
  source_snippets\": [\n    \"'TP.HPBITABLO2.28', 'TP.HPBITABLO2.32', 'TP.HPBITABLO2.33',\
  \ 'TP.HPBITABLO2.34'\",\n    \"'TP_HPBITABLO2_33': \\\"\\\",\",\n    \"#\\\"TP_HPBITABLO2_33\\\
  \": \\\"A. TL\\\", #A. TL(Bin TL)-Düzey\",\n    \"df_kredi_mevduat[\\\"A. TL\\\"\
  ] = df_kredi_mevduat[\\\"TP_HPBITABLO2_24\\\"] + df_kredi_mevduat[\\\"TP_HPBITABLO2_33\\\
  \"]\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Adth-blg-v7%3Aseries%3ATP_HPBITABLO2_33%3Ae084294442e0.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.33

## Target
series | evds:TP.HPBITABLO2.33

## Notebook
dth-blg-v7

## Candidate Title
2.2.1.TL

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
Catalog source: catalog:evds2:TP.HPBITABLO2.33

## Evidence
{
  "ticker": "TP.HPBITABLO2.33",
  "notebook_slug": "dth-blg-v7",
  "official_series_name": "a. TL (Bin TL)",
  "context_title": "B. TOPLAM KREDİ (Bin TL) / 2. Yurt İçi Yerleşik Finansal Kuruluşlar (Bin TL) / a. TL (Bin TL)",
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
    "id": "catalog:evds2:TP.HPBITABLO2.33",
    "title": "2.2.1.TL",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.28', 'TP.HPBITABLO2.32', 'TP.HPBITABLO2.33', 'TP.HPBITABLO2.34'",
    "'TP_HPBITABLO2_33': \"\",",
    "#\"TP_HPBITABLO2_33\": \"A. TL\", #A. TL(Bin TL)-Düzey",
    "df_kredi_mevduat[\"A. TL\"] = df_kredi_mevduat[\"TP_HPBITABLO2_24\"] + df_kredi_mevduat[\"TP_HPBITABLO2_33\"]"
  ],
  "indicator_hints": [],
  "notes": ""
}
