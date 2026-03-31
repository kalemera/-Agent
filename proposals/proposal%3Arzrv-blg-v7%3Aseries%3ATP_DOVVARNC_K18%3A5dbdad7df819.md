---
record_type: proposal
id: proposal:rzrv-blg-v7:series:TP_DOVVARNC_K18:5dbdad7df819
proposal_id: proposal:rzrv-blg-v7:series:TP_DOVVARNC_K18:5dbdad7df819
title: Semantic proposal for TP.DOVVARNC.K18
status: approved
target_type: series
target_id: evds:TP.DOVVARNC.K18
ticker: TP.DOVVARNC.K18
notebook_slug: rzrv-blg-v7
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Rzrv_Blg_V7.ipynb
candidate_title: 2.2.1.3.Dört Ay Bir Yıl Arası
candidate_unit: milyon ABD doları
candidate_frequency: monthly
candidate_role: dormant_candidate
candidate_theme_ids:
- theme:reserves
- theme:net-reserve-estimate
candidate_indicator_inputs: []
candidate_formula_hint: ''
confidence: 0.9
source: heuristic
evidence_fingerprint: 5dbdad7df8194b58dcf717a48e44e5e74fbbc291
catalog_record_id: catalog:evds2:TP.DOVVARNC.K18
memory_rule_ids: []
evidence:
  ticker: TP.DOVVARNC.K18
  notebook_slug: rzrv-blg-v7
  official_series_name: Swap (Aylik, MB)
  context_title: Swap (Aylik, MB)
  frequency: monthly
  unit: Aylik, MB
  role: dormant_candidate
  status: listed_only
  theme_ids:
  - theme:reserves
  - theme:net-reserve-estimate
  indicator_ids: []
  source_dependency_ids:
  - source:rzrv-swap-pdf
  - source:rzrv-manual-swap-ledger
  catalog_record:
    id: catalog:evds2:TP.DOVVARNC.K18
    title: 2.2.1.3.Dört Ay Bir Yıl Arası
    frequency: monthly
    unit: milyon ABD doları
    data_group: bie_ulusdovlkd
    category: ULUSLARARASI REZERVLER (TCMB)
  memory_rules: []
  source_snippets:
  - '[''TP.DOVVARNC.K18''],'
  - 'swap_data_df_2.rename(columns={''TP_DOVVARNC_K18'': ''Swap (Aylık, MB)''}, inplace=True)'
  indicator_hints: []
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DOVVARNC.K18
promoted_memory_rule_id: memory:global-tp-dovvarnc-k18
notes: 'Catalog source: catalog:evds2:TP.DOVVARNC.K18'
body: "# Semantic proposal for TP.DOVVARNC.K18\n\n## Target\nseries | evds:TP.DOVVARNC.K18\n\
  \n## Notebook\nrzrv-blg-v7\n\n## Candidate Title\n2.2.1.3.Dört Ay Bir Yıl Arası\n\
  \n## Candidate Unit\nmilyon ABD doları\n\n## Candidate Frequency\nmonthly\n\n##\
  \ Candidate Role\ndormant_candidate\n\n## Confidence\n0.9\n\n## Candidate Themes\n\
  - theme:reserves\n- theme:net-reserve-estimate\n\n## Candidate Indicator Inputs\n\
  -\n\n## Formula Hint\n-\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval\
  \ Reason\nNo matching memory rules; heuristic source; dormant candidate role.\n\n\
  ## Notes\nCatalog source: catalog:evds2:TP.DOVVARNC.K18\n\n## Evidence\n{\n  \"\
  ticker\": \"TP.DOVVARNC.K18\",\n  \"notebook_slug\": \"rzrv-blg-v7\",\n  \"official_series_name\"\
  : \"Swap (Aylik, MB)\",\n  \"context_title\": \"Swap (Aylik, MB)\",\n  \"frequency\"\
  : \"monthly\",\n  \"unit\": \"Aylik, MB\",\n  \"role\": \"dormant_candidate\",\n\
  \  \"status\": \"listed_only\",\n  \"theme_ids\": [\n    \"theme:reserves\",\n \
  \   \"theme:net-reserve-estimate\"\n  ],\n  \"indicator_ids\": [],\n  \"source_dependency_ids\"\
  : [\n    \"source:rzrv-swap-pdf\",\n    \"source:rzrv-manual-swap-ledger\"\n  ],\n\
  \  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.DOVVARNC.K18\",\n    \"\
  title\": \"2.2.1.3.Dört Ay Bir Yıl Arası\",\n    \"frequency\": \"monthly\",\n \
  \   \"unit\": \"milyon ABD doları\",\n    \"data_group\": \"bie_ulusdovlkd\",\n\
  \    \"category\": \"ULUSLARARASI REZERVLER (TCMB)\"\n  },\n  \"memory_rules\":\
  \ [],\n  \"source_snippets\": [\n    \"['TP.DOVVARNC.K18'],\",\n    \"swap_data_df_2.rename(columns={'TP_DOVVARNC_K18':\
  \ 'Swap (Aylık, MB)'}, inplace=True)\"\n  ],\n  \"indicator_hints\": [],\n  \"notes\"\
  : \"\"\n}\n"
path: proposals\proposal%3Arzrv-blg-v7%3Aseries%3ATP_DOVVARNC_K18%3A5dbdad7df819.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DOVVARNC.K18

## Target
series | evds:TP.DOVVARNC.K18

## Notebook
rzrv-blg-v7

## Candidate Title
2.2.1.3.Dört Ay Bir Yıl Arası

## Candidate Unit
milyon ABD doları

## Candidate Frequency
monthly

## Candidate Role
dormant_candidate

## Confidence
0.9

## Candidate Themes
- theme:reserves
- theme:net-reserve-estimate

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
Catalog source: catalog:evds2:TP.DOVVARNC.K18

## Evidence
{
  "ticker": "TP.DOVVARNC.K18",
  "notebook_slug": "rzrv-blg-v7",
  "official_series_name": "Swap (Aylik, MB)",
  "context_title": "Swap (Aylik, MB)",
  "frequency": "monthly",
  "unit": "Aylik, MB",
  "role": "dormant_candidate",
  "status": "listed_only",
  "theme_ids": [
    "theme:reserves",
    "theme:net-reserve-estimate"
  ],
  "indicator_ids": [],
  "source_dependency_ids": [
    "source:rzrv-swap-pdf",
    "source:rzrv-manual-swap-ledger"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DOVVARNC.K18",
    "title": "2.2.1.3.Dört Ay Bir Yıl Arası",
    "frequency": "monthly",
    "unit": "milyon ABD doları",
    "data_group": "bie_ulusdovlkd",
    "category": "ULUSLARARASI REZERVLER (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "['TP.DOVVARNC.K18'],",
    "swap_data_df_2.rename(columns={'TP_DOVVARNC_K18': 'Swap (Aylık, MB)'}, inplace=True)"
  ],
  "indicator_hints": [],
  "notes": ""
}
