---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_26:eb1dc5db61bd
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_26:eb1dc5db61bd
title: Semantic proposal for TP.HPBITABLO2.26
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.26
ticker: TP.HPBITABLO2.26
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: balance_sheet_line
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: eb1dc5db61bd9ca060efbe57c0ba34db87c27374
catalog_record_id: catalog:evds2:TP.HPBITABLO2.26
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.26
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: 2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)
  context_title: 2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)
  frequency: weekly
  unit: bin TL
  role: balance_sheet_line
  status: derived_input
  theme_ids:
  - theme:resident-financial-assets
  - theme:resident-securities
  - theme:resident-deposits
  indicator_ids: []
  source_dependency_ids:
  - source:yiyrlsk-mkk-hisse-manual
  - source:yiyrlsk-mkk-fon-manual
  - source:yiyrlsk-vap-scrape-attempt
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.26
    title: 2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.23'', ''TP.HPBITABLO2.24'', ''TP.HPBITABLO2.25'', ''TP.HPBITABLO2.26'',
    ''TP.HPBITABLO2.27'', #kredi - bankalar yurtiçi şube / TL'
  indicator_hints: []
  notes: Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook
    olarak isaretlendi. Catalog metadata applied from catalog:evds2:TP.HPBITABLO2.26.
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.26
promoted_memory_rule_id: memory:global-tp-hpbitablo2-26
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.26 | Notebook icindeki kayitli
  EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. Catalog
  metadata applied from catalog:evds2:TP.HPBITABLO2.26.'
body: "# Semantic proposal for TP.HPBITABLO2.26\n\n## Target\nseries | evds:TP.HPBITABLO2.26\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n2.1.1.b.Ticari Krediler\
  \ (Kurumsal Kredi Kartları Dahil)\n\n## Candidate Unit\nbin TL\n\n## Candidate Frequency\n\
  weekly\n\n## Candidate Role\nbalance_sheet_line\n\n## Confidence\n0.9\n\n## Candidate\
  \ Themes\n- theme:resident-financial-assets\n- theme:resident-securities\n- theme:resident-deposits\n\
  \n## Candidate Indicator Inputs\n-\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\
  \n## Approval Mode\n-\n\n## Approval Reason\nLLM requested manual review.\n\n##\
  \ Notes\nCatalog source: catalog:evds2:TP.HPBITABLO2.26 | Notebook icindeki kayitli\
  \ EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi.\
  \ Catalog metadata applied from catalog:evds2:TP.HPBITABLO2.26.\n\n## Evidence\n\
  {\n  \"ticker\": \"TP.HPBITABLO2.26\",\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\"\
  ,\n  \"official_series_name\": \"2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları\
  \ Dahil)\",\n  \"context_title\": \"2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları\
  \ Dahil)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"bin TL\",\n  \"role\":\
  \ \"balance_sheet_line\",\n  \"status\": \"derived_input\",\n  \"theme_ids\": [\n\
  \    \"theme:resident-financial-assets\",\n    \"theme:resident-securities\",\n\
  \    \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:yiyrlsk-mkk-hisse-manual\",\n    \"source:yiyrlsk-mkk-fon-manual\"\
  ,\n    \"source:yiyrlsk-vap-scrape-attempt\"\n  ],\n  \"catalog_record\": {\n  \
  \  \"id\": \"catalog:evds2:TP.HPBITABLO2.26\",\n    \"title\": \"2.1.1.b.Ticari\
  \ Krediler (Kurumsal Kredi Kartları Dahil)\",\n    \"frequency\": \"weekly\",\n\
  \    \"unit\": \"bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\"\
  : \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\":\
  \ [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO2.23', 'TP.HPBITABLO2.24', 'TP.HPBITABLO2.25',\
  \ 'TP.HPBITABLO2.26', 'TP.HPBITABLO2.27', #kredi - bankalar yurtiçi şube / TL\"\n\
  \  ],\n  \"indicator_hints\": [],\n  \"notes\": \"Notebook icindeki kayitli EVDS\
  \ seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. Catalog\
  \ metadata applied from catalog:evds2:TP.HPBITABLO2.26.\"\n}\n"
path: proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_HPBITABLO2_26%3Aeb1dc5db61bd.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.26

## Target
series | evds:TP.HPBITABLO2.26

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
balance_sheet_line

## Confidence
0.9

## Candidate Themes
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits

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
Catalog source: catalog:evds2:TP.HPBITABLO2.26 | Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. Catalog metadata applied from catalog:evds2:TP.HPBITABLO2.26.

## Evidence
{
  "ticker": "TP.HPBITABLO2.26",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)",
  "context_title": "2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)",
  "frequency": "weekly",
  "unit": "bin TL",
  "role": "balance_sheet_line",
  "status": "derived_input",
  "theme_ids": [
    "theme:resident-financial-assets",
    "theme:resident-securities",
    "theme:resident-deposits"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:yiyrlsk-mkk-hisse-manual",
    "source:yiyrlsk-mkk-fon-manual",
    "source:yiyrlsk-vap-scrape-attempt"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.26",
    "title": "2.1.1.b.Ticari Krediler (Kurumsal Kredi Kartları Dahil)",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.23', 'TP.HPBITABLO2.24', 'TP.HPBITABLO2.25', 'TP.HPBITABLO2.26', 'TP.HPBITABLO2.27', #kredi - bankalar yurtiçi şube / TL"
  ],
  "indicator_hints": [],
  "notes": "Notebook icindeki kayitli EVDS seri adinda gorunmedigi icin unresolved_from_notebook olarak isaretlendi. Catalog metadata applied from catalog:evds2:TP.HPBITABLO2.26."
}
