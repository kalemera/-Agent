---
record_type: proposal
id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_2:a4b87621183a
proposal_id: proposal:yi-yrlsk-fnsl-vrlk-v1:series:TP_HPBITABLO2_2:a4b87621183a
title: Semantic proposal for TP.HPBITABLO2.2
status: approved
target_type: series
target_id: evds:TP.HPBITABLO2.2
ticker: TP.HPBITABLO2.2
notebook_slug: yi-yrlsk-fnsl-vrlk-v1
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\Yi_Yrlsk_Fnsl_Vrlk_V1.ipynb
candidate_title: 1.1.Yurt İçi Yerleşikler
candidate_unit: bin TL
candidate_frequency: weekly
candidate_role: stock_total
candidate_theme_ids:
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits
candidate_indicator_inputs:
- derived:resident-financial-assets-total
candidate_formula_hint: 'derived:resident-financial-assets-total: Mevduat, menkul
  kiymet ve MKK kaynakli varlik bloklarini birlestirir.'
confidence: 0.95
source: heuristic
evidence_fingerprint: a4b87621183a09052845c1d510f0d9718d7d8ad5
catalog_record_id: catalog:evds2:TP.HPBITABLO2.2
memory_rule_ids: []
evidence:
  ticker: TP.HPBITABLO2.2
  notebook_slug: yi-yrlsk-fnsl-vrlk-v1
  official_series_name: TL+YP Mevduat (Toplam, Bankalar Hariç)
  context_title: TL+YP Mevduat (Toplam, Bankalar Hariç)
  frequency: weekly
  unit: bin TL
  role: stock_total
  status: derived_input
  theme_ids:
  - theme:resident-financial-assets
  - theme:resident-securities
  - theme:resident-deposits
  indicator_ids:
  - derived:resident-financial-assets-total
  source_dependency_ids:
  - source:yiyrlsk-mkk-hisse-manual
  - source:yiyrlsk-mkk-fon-manual
  - source:yiyrlsk-vap-scrape-attempt
  catalog_record:
    id: catalog:evds2:TP.HPBITABLO2.2
    title: 1.1.Yurt İçi Yerleşikler
    frequency: weekly
    unit: bin TL
    data_group: bie_hpbitablo2
    category: PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)
  memory_rules: []
  source_snippets:
  - '''TP.HPBITABLO2.2'', ''TP.HPBITABLO2.3'', ''TP.HPBITABLO2.4'', ''TP.HPBITABLO2.5'',
    #mevduat - bankalar yurtiçi şube / TL'
  - '''TP.HPBITABLO2.23'', ''TP.HPBITABLO2.24'', ''TP.HPBITABLO2.25'', ''TP.HPBITABLO2.26'',
    ''TP.HPBITABLO2.27'', #kredi - bankalar yurtiçi şube / TL'
  - '''TP.HPBITABLO2.28'', ''TP.HPBITABLO2.29'', ''TP.HPBITABLO2.30'', ''TP.HPBITABLO2.31'',
    #kredi - bankalar yurtiçi şube / YP'
  - '''TP_HPBITABLO2_2'': ''TL+YP Mevduat (Toplam, Bankalar Hariç)'','
  indicator_hints:
  - 'derived:resident-financial-assets-total: Mevduat, menkul kiymet ve MKK kaynakli
    varlik bloklarini birlestirir.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.HPBITABLO2.2
promoted_memory_rule_id: memory:global-tp-hpbitablo2-2
notes: 'Catalog source: catalog:evds2:TP.HPBITABLO2.2'
body: "# Semantic proposal for TP.HPBITABLO2.2\n\n## Target\nseries | evds:TP.HPBITABLO2.2\n\
  \n## Notebook\nyi-yrlsk-fnsl-vrlk-v1\n\n## Candidate Title\n1.1.Yurt İçi Yerleşikler\n\
  \n## Candidate Unit\nbin TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  stock_total\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:resident-financial-assets\n\
  - theme:resident-securities\n- theme:resident-deposits\n\n## Candidate Indicator\
  \ Inputs\n- derived:resident-financial-assets-total\n\n## Formula Hint\nderived:resident-financial-assets-total:\
  \ Mevduat, menkul kiymet ve MKK kaynakli varlik bloklarini birlestirir.\n\n## Source\n\
  heuristic\n\n## Approval Mode\n-\n\n## Approval Reason\n-\n\n## Notes\nCatalog source:\
  \ catalog:evds2:TP.HPBITABLO2.2\n\n## Evidence\n{\n  \"ticker\": \"TP.HPBITABLO2.2\"\
  ,\n  \"notebook_slug\": \"yi-yrlsk-fnsl-vrlk-v1\",\n  \"official_series_name\":\
  \ \"TL+YP Mevduat (Toplam, Bankalar Hariç)\",\n  \"context_title\": \"TL+YP Mevduat\
  \ (Toplam, Bankalar Hariç)\",\n  \"frequency\": \"weekly\",\n  \"unit\": \"bin TL\"\
  ,\n  \"role\": \"stock_total\",\n  \"status\": \"derived_input\",\n  \"theme_ids\"\
  : [\n    \"theme:resident-financial-assets\",\n    \"theme:resident-securities\"\
  ,\n    \"theme:resident-deposits\"\n  ],\n  \"indicator_ids\": [\n    \"derived:resident-financial-assets-total\"\
  \n  ],\n  \"source_dependency_ids\": [\n    \"source:yiyrlsk-mkk-hisse-manual\"\
  ,\n    \"source:yiyrlsk-mkk-fon-manual\",\n    \"source:yiyrlsk-vap-scrape-attempt\"\
  \n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.HPBITABLO2.2\",\n\
  \    \"title\": \"1.1.Yurt İçi Yerleşikler\",\n    \"frequency\": \"weekly\",\n\
  \    \"unit\": \"bin TL\",\n    \"data_group\": \"bie_hpbitablo2\",\n    \"category\"\
  : \"PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)\"\n  },\n  \"memory_rules\":\
  \ [],\n  \"source_snippets\": [\n    \"'TP.HPBITABLO2.2', 'TP.HPBITABLO2.3', 'TP.HPBITABLO2.4',\
  \ 'TP.HPBITABLO2.5', #mevduat - bankalar yurtiçi şube / TL\",\n    \"'TP.HPBITABLO2.23',\
  \ 'TP.HPBITABLO2.24', 'TP.HPBITABLO2.25', 'TP.HPBITABLO2.26', 'TP.HPBITABLO2.27',\
  \ #kredi - bankalar yurtiçi şube / TL\",\n    \"'TP.HPBITABLO2.28', 'TP.HPBITABLO2.29',\
  \ 'TP.HPBITABLO2.30', 'TP.HPBITABLO2.31', #kredi - bankalar yurtiçi şube / YP\"\
  ,\n    \"'TP_HPBITABLO2_2': 'TL+YP Mevduat (Toplam, Bankalar Hariç)',\"\n  ],\n\
  \  \"indicator_hints\": [\n    \"derived:resident-financial-assets-total: Mevduat,\
  \ menkul kiymet ve MKK kaynakli varlik bloklarini birlestirir.\"\n  ],\n  \"notes\"\
  : \"\"\n}\n"
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Ayi-yrlsk-fnsl-vrlk-v1%3Aseries%3ATP_HPBITABLO2_2%3Aa4b87621183a.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.HPBITABLO2.2

## Target
series | evds:TP.HPBITABLO2.2

## Notebook
yi-yrlsk-fnsl-vrlk-v1

## Candidate Title
1.1.Yurt İçi Yerleşikler

## Candidate Unit
bin TL

## Candidate Frequency
weekly

## Candidate Role
stock_total

## Confidence
0.95

## Candidate Themes
- theme:resident-financial-assets
- theme:resident-securities
- theme:resident-deposits

## Candidate Indicator Inputs
- derived:resident-financial-assets-total

## Formula Hint
derived:resident-financial-assets-total: Mevduat, menkul kiymet ve MKK kaynakli varlik bloklarini birlestirir.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.HPBITABLO2.2

## Evidence
{
  "ticker": "TP.HPBITABLO2.2",
  "notebook_slug": "yi-yrlsk-fnsl-vrlk-v1",
  "official_series_name": "TL+YP Mevduat (Toplam, Bankalar Hariç)",
  "context_title": "TL+YP Mevduat (Toplam, Bankalar Hariç)",
  "frequency": "weekly",
  "unit": "bin TL",
  "role": "stock_total",
  "status": "derived_input",
  "theme_ids": [
    "theme:resident-financial-assets",
    "theme:resident-securities",
    "theme:resident-deposits"
  ],
  "indicator_ids": [
    "derived:resident-financial-assets-total"
  ],
  "source_dependency_ids": [
    "source:yiyrlsk-mkk-hisse-manual",
    "source:yiyrlsk-mkk-fon-manual",
    "source:yiyrlsk-vap-scrape-attempt"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.HPBITABLO2.2",
    "title": "1.1.Yurt İçi Yerleşikler",
    "frequency": "weekly",
    "unit": "bin TL",
    "data_group": "bie_hpbitablo2",
    "category": "PARA VE BANKA İSTATİSTİKLERİ (HAFTALIK) (TCMB)"
  },
  "memory_rules": [],
  "source_snippets": [
    "'TP.HPBITABLO2.2', 'TP.HPBITABLO2.3', 'TP.HPBITABLO2.4', 'TP.HPBITABLO2.5', #mevduat - bankalar yurtiçi şube / TL",
    "'TP.HPBITABLO2.23', 'TP.HPBITABLO2.24', 'TP.HPBITABLO2.25', 'TP.HPBITABLO2.26', 'TP.HPBITABLO2.27', #kredi - bankalar yurtiçi şube / TL",
    "'TP.HPBITABLO2.28', 'TP.HPBITABLO2.29', 'TP.HPBITABLO2.30', 'TP.HPBITABLO2.31', #kredi - bankalar yurtiçi şube / YP",
    "'TP_HPBITABLO2_2': 'TL+YP Mevduat (Toplam, Bankalar Hariç)',"
  ],
  "indicator_hints": [
    "derived:resident-financial-assets-total: Mevduat, menkul kiymet ve MKK kaynakli varlik bloklarini birlestirir."
  ],
  "notes": ""
}
