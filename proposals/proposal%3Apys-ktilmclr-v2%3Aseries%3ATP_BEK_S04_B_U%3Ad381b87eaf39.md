---
record_type: proposal
id: proposal:pys-ktilmclr-v2:series:TP_BEK_S04_B_U:d381b87eaf39
proposal_id: proposal:pys-ktilmclr-v2:series:TP_BEK_S04_B_U:d381b87eaf39
title: Semantic proposal for TP.BEK.S04.B.U
status: approved
target_type: series
target_id: evds:TP.BEK.S04.B.U
ticker: TP.BEK.S04.B.U
notebook_slug: pys-ktilmclr-v2
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Pys_Ktlmclr_V2.ipynb
candidate_title: 4B. (Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale
  Faiz Oranı Beklentisi (%)
candidate_unit: '%'
candidate_frequency: monthly
candidate_role: commentary_driver
candidate_theme_ids:
- theme:survey-expectations
candidate_indicator_inputs:
- derived:inflation-expectation-24m
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: d381b87eaf3990082d8b835671da65b69bea791f
catalog_record_id: catalog:evds2:TP.BEK.S04.B.U
memory_rule_ids: []
evidence:
  ticker: TP.BEK.S04.B.U
  notebook_slug: pys-ktilmclr-v2
  official_series_name: 4B.(Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli
    Repo İhale Faiz Oranı Beklentisi (%)
  context_title: 4B.(Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale
    Faiz Oranı Beklentisi (%)
  frequency: monthly
  unit: '%'
  role: commentary_driver
  status: derived_input
  theme_ids:
  - theme:survey-expectations
  indicator_ids:
  - derived:inflation-expectation-24m
  source_dependency_ids: []
  catalog_record:
    id: catalog:evds2:TP.BEK.S04.B.U
    title: 4B. (Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale Faiz
      Oranı Beklentisi (%)
    frequency: monthly
    unit: '%'
    data_group: bie_urbek
    category: PİYASA KATILIMCILARI ANKETİ (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.BEK.S04.B.U'', ''TP.BEK.S04.D.U'', ''TP.BEK.S04.E.U'', ''TP.BEK.S06.A.U'','
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.BEK.S04.B.U
promoted_memory_rule_id: memory:global-tp-bek-s04-b-u
notes: 'Catalog source: catalog:evds2:TP.BEK.S04.B.U'
body: "# Semantic proposal for TP.BEK.S04.B.U\n\n## Target\nseries | evds:TP.BEK.S04.B.U\n\
  \n## Notebook\npys-ktilmclr-v2\n\n## Candidate Title\n4B. (Uygun Ortalama) 3 Ay\
  \ Sonrasının TCMB Bir Hafta Vadeli Repo İhale Faiz Oranı Beklentisi (%)\n\n## Candidate\
  \ Unit\n%\n\n## Candidate Frequency\nmonthly\n\n## Candidate Role\ncommentary_driver\n\
  \n## Confidence\n0.9\n\n## Candidate Themes\n- theme:survey-expectations\n\n## Candidate\
  \ Indicator Inputs\n- derived:inflation-expectation-24m\n\n## Formula Hint\n-\n\n\
  ## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval Reason\nProposal originates\
  \ from a heuristic source and is associated with a specific notebook_slug without\
  \ matching memory rules or approved series to confirm global safety.\n\n## Notes\n\
  Catalog source: catalog:evds2:TP.BEK.S04.B.U\n\n## Evidence\n{\n  \"ticker\": \"\
  TP.BEK.S04.B.U\",\n  \"notebook_slug\": \"pys-ktilmclr-v2\",\n  \"official_series_name\"\
  : \"4B.(Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale Faiz Oranı\
  \ Beklentisi (%)\",\n  \"context_title\": \"4B.(Uygun Ortalama) 3 Ay Sonrasının\
  \ TCMB Bir Hafta Vadeli Repo İhale Faiz Oranı Beklentisi (%)\",\n  \"frequency\"\
  : \"monthly\",\n  \"unit\": \"%\",\n  \"role\": \"commentary_driver\",\n  \"status\"\
  : \"derived_input\",\n  \"theme_ids\": [\n    \"theme:survey-expectations\"\n  ],\n\
  \  \"indicator_ids\": [\n    \"derived:inflation-expectation-24m\"\n  ],\n  \"source_dependency_ids\"\
  : [],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.BEK.S04.B.U\",\n\
  \    \"title\": \"4B. (Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo\
  \ İhale Faiz Oranı Beklentisi (%)\",\n    \"frequency\": \"monthly\",\n    \"unit\"\
  : \"%\",\n    \"data_group\": \"bie_urbek\",\n    \"category\": \"PİYASA KATILIMCILARI\
  \ ANKETİ (TCMB)\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\": [\n   \
  \ \"'TP.BEK.S04.B.U', 'TP.BEK.S04.D.U', 'TP.BEK.S04.E.U', 'TP.BEK.S06.A.U',\"\n\
  \  ],\n  \"indicator_hints\": [],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Apys-ktilmclr-v2%3Aseries%3ATP_BEK_S04_B_U%3Ad381b87eaf39.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.BEK.S04.B.U

## Target
series | evds:TP.BEK.S04.B.U

## Notebook
pys-ktilmclr-v2

## Candidate Title
4B. (Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale Faiz Oranı Beklentisi (%)

## Candidate Unit
%

## Candidate Frequency
monthly

## Candidate Role
commentary_driver

## Confidence
0.9

## Candidate Themes
- theme:survey-expectations

## Candidate Indicator Inputs
- derived:inflation-expectation-24m

## Formula Hint
-

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.BEK.S04.B.U

## Evidence
{
  "ticker": "TP.BEK.S04.B.U",
  "notebook_slug": "pys-ktilmclr-v2",
  "official_series_name": "4B.(Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale Faiz Oranı Beklentisi (%)",
  "context_title": "4B.(Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale Faiz Oranı Beklentisi (%)",
  "frequency": "monthly",
  "unit": "%",
  "role": "commentary_driver",
  "status": "derived_input",
  "theme_ids": [
    "theme:survey-expectations"
  ],
  "indicator_ids": [
    "derived:inflation-expectation-24m"
  ],
  "source_dependency_ids": [],
  "catalog_record": {
    "id": "catalog:evds2:TP.BEK.S04.B.U",
    "title": "4B. (Uygun Ortalama) 3 Ay Sonrasının TCMB Bir Hafta Vadeli Repo İhale Faiz Oranı Beklentisi (%)",
    "frequency": "monthly",
    "unit": "%",
    "data_group": "bie_urbek",
    "category": "PİYASA KATILIMCILARI ANKETİ (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.BEK.S04.B.U', 'TP.BEK.S04.D.U', 'TP.BEK.S04.E.U', 'TP.BEK.S06.A.U',"
  ],
  "indicator_hints": [],
  "notes": ""
}
