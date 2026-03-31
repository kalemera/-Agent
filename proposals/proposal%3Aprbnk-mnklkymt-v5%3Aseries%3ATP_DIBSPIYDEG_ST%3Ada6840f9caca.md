---
record_type: proposal
id: proposal:prbnk-mnklkymt-v5:series:TP_DIBSPIYDEG_ST:da6840f9caca
proposal_id: proposal:prbnk-mnklkymt-v5:series:TP_DIBSPIYDEG_ST:da6840f9caca
title: Semantic proposal for TP.DIBSPIYDEG.ST
status: approved
target_type: series
target_id: evds:TP.DIBSPIYDEG.ST
ticker: TP.DIBSPIYDEG.ST
notebook_slug: prbnk-mnklkymt-v5
notebook_path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\Telegram Bot\notebooks\PrBnk_MnklKymt_V5.ipynb
candidate_title: 1.Toplam (S.1, S.2)
candidate_unit: milyon TL
candidate_frequency: weekly
candidate_role: stock_component
candidate_theme_ids:
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities
candidate_indicator_inputs:
- derived:dibs-stock
- derived:dibs-foreign-share
- derived:equity-plus-dibs-flow
candidate_formula_hint: 'derived:dibs-foreign-share: DIBS stok ve haftalik ZIP tablosundan
  turetilen yabanci pay.'
confidence: 0.95
source: heuristic
evidence_fingerprint: da6840f9caca18664463562a64bf86b128a82a8f
catalog_record_id: catalog:evds2:TP.DIBSPIYDEG.ST
memory_rule_ids: []
evidence:
  ticker: TP.DIBSPIYDEG.ST
  notebook_slug: prbnk-mnklkymt-v5
  official_series_name: DİBS (Tüm Stok, Piyasa Değeri)
  context_title: DİBS (Tüm Stok, Piyasa Değeri)
  frequency: weekly
  unit: milyon TL
  role: stock_component
  status: derived_input
  theme_ids:
  - theme:portfolio-flows
  - theme:foreign-ownership
  - theme:swap-and-securities
  indicator_ids:
  - derived:dibs-stock
  - derived:dibs-foreign-share
  - derived:equity-plus-dibs-flow
  source_dependency_ids:
  - source:prbnk-weekly-zip
  - source:prbnk-swap-pdf
  catalog_record:
    id: catalog:evds2:TP.DIBSPIYDEG.ST
    title: 1.Toplam (S.1, S.2)
    frequency: weekly
    unit: milyon TL
    data_group: bie_dibspiydeg
    category: DEVLET İÇ BORÇLANMA SENETLERİ
  memory_rules: []
  source_snippets:
  - '"TP.DIBSPIYDEG.ST": [3, "DİBS (Tüm Stok, Piyasa Değeri)"],'
  - df_menkul_kiymet_apko_["DİBS (Tüm Stok, USD)"] = df_menkul_kiymet_apko_["TP_DIBSPIYDEG_ST"]
    / df_menkul_kiymet_apko_["TP_DK_USD_A_YTL"]
  - '"TP_MKNETHAR_M9", "TP_MKNETHAR_M10", "TP_MKNETHAR_M11", "TP_DIBSPIYDEG_ST", "TP_DK_USD_A_YTL"'
  indicator_hints:
  - 'derived:dibs-foreign-share: DIBS stok ve haftalik ZIP tablosundan turetilen yabanci
    pay.'
  - 'derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin birlestirilmis net degisimi.'
  notes: ''
llm_provider: ''
llm_model: ''
promoted_record_id: evds:TP.DIBSPIYDEG.ST
promoted_memory_rule_id: memory:global-tp-dibspiydeg-st
notes: 'Catalog source: catalog:evds2:TP.DIBSPIYDEG.ST'
body: "# Semantic proposal for TP.DIBSPIYDEG.ST\n\n## Target\nseries | evds:TP.DIBSPIYDEG.ST\n\
  \n## Notebook\nprbnk-mnklkymt-v5\n\n## Candidate Title\n1.Toplam (S.1, S.2)\n\n\
  ## Candidate Unit\nmilyon TL\n\n## Candidate Frequency\nweekly\n\n## Candidate Role\n\
  stock_component\n\n## Confidence\n0.95\n\n## Candidate Themes\n- theme:portfolio-flows\n\
  - theme:foreign-ownership\n- theme:swap-and-securities\n\n## Candidate Indicator\
  \ Inputs\n- derived:dibs-stock\n- derived:dibs-foreign-share\n- derived:equity-plus-dibs-flow\n\
  \n## Formula Hint\nderived:dibs-foreign-share: DIBS stok ve haftalik ZIP tablosundan\
  \ turetilen yabanci pay.\n\n## Source\nheuristic\n\n## Approval Mode\n-\n\n## Approval\
  \ Reason\nLLM requested manual review.\n\n## Notes\nCatalog source: catalog:evds2:TP.DIBSPIYDEG.ST\n\
  \n## Evidence\n{\n  \"ticker\": \"TP.DIBSPIYDEG.ST\",\n  \"notebook_slug\": \"prbnk-mnklkymt-v5\"\
  ,\n  \"official_series_name\": \"DİBS (Tüm Stok, Piyasa Değeri)\",\n  \"context_title\"\
  : \"DİBS (Tüm Stok, Piyasa Değeri)\",\n  \"frequency\": \"weekly\",\n  \"unit\"\
  : \"milyon TL\",\n  \"role\": \"stock_component\",\n  \"status\": \"derived_input\"\
  ,\n  \"theme_ids\": [\n    \"theme:portfolio-flows\",\n    \"theme:foreign-ownership\"\
  ,\n    \"theme:swap-and-securities\"\n  ],\n  \"indicator_ids\": [\n    \"derived:dibs-stock\"\
  ,\n    \"derived:dibs-foreign-share\",\n    \"derived:equity-plus-dibs-flow\"\n\
  \  ],\n  \"source_dependency_ids\": [\n    \"source:prbnk-weekly-zip\",\n    \"\
  source:prbnk-swap-pdf\"\n  ],\n  \"catalog_record\": {\n    \"id\": \"catalog:evds2:TP.DIBSPIYDEG.ST\"\
  ,\n    \"title\": \"1.Toplam (S.1, S.2)\",\n    \"frequency\": \"weekly\",\n   \
  \ \"unit\": \"milyon TL\",\n    \"data_group\": \"bie_dibspiydeg\",\n    \"category\"\
  : \"DEVLET İÇ BORÇLANMA SENETLERİ\"\n  },\n  \"memory_rules\": [],\n  \"source_snippets\"\
  : [\n    \"\\\"TP.DIBSPIYDEG.ST\\\": [3, \\\"DİBS (Tüm Stok, Piyasa Değeri)\\\"\
  ],\",\n    \"df_menkul_kiymet_apko_[\\\"DİBS (Tüm Stok, USD)\\\"] = df_menkul_kiymet_apko_[\\\
  \"TP_DIBSPIYDEG_ST\\\"] / df_menkul_kiymet_apko_[\\\"TP_DK_USD_A_YTL\\\"]\",\n \
  \   \"\\\"TP_MKNETHAR_M9\\\", \\\"TP_MKNETHAR_M10\\\", \\\"TP_MKNETHAR_M11\\\",\
  \ \\\"TP_DIBSPIYDEG_ST\\\", \\\"TP_DK_USD_A_YTL\\\"\"\n  ],\n  \"indicator_hints\"\
  : [\n    \"derived:dibs-foreign-share: DIBS stok ve haftalik ZIP tablosundan turetilen\
  \ yabanci pay.\",\n    \"derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin\
  \ birlestirilmis net degisimi.\"\n  ],\n  \"notes\": \"\"\n}\n"
path: proposals\proposal%3Aprbnk-mnklkymt-v5%3Aseries%3ATP_DIBSPIYDEG_ST%3Ada6840f9caca.md
approval_reason: LLM returned no concrete blocker after deterministic safety checks.
approval_mode: auto_llm
---
# Semantic proposal for TP.DIBSPIYDEG.ST

## Target
series | evds:TP.DIBSPIYDEG.ST

## Notebook
prbnk-mnklkymt-v5

## Candidate Title
1.Toplam (S.1, S.2)

## Candidate Unit
milyon TL

## Candidate Frequency
weekly

## Candidate Role
stock_component

## Confidence
0.95

## Candidate Themes
- theme:portfolio-flows
- theme:foreign-ownership
- theme:swap-and-securities

## Candidate Indicator Inputs
- derived:dibs-stock
- derived:dibs-foreign-share
- derived:equity-plus-dibs-flow

## Formula Hint
derived:dibs-foreign-share: DIBS stok ve haftalik ZIP tablosundan turetilen yabanci pay.

## Source
heuristic

## Approval Mode
auto_llm

## Approval Reason
LLM returned no concrete blocker after deterministic safety checks.

## Notes
Catalog source: catalog:evds2:TP.DIBSPIYDEG.ST

## Evidence
{
  "ticker": "TP.DIBSPIYDEG.ST",
  "notebook_slug": "prbnk-mnklkymt-v5",
  "official_series_name": "DİBS (Tüm Stok, Piyasa Değeri)",
  "context_title": "DİBS (Tüm Stok, Piyasa Değeri)",
  "frequency": "weekly",
  "unit": "milyon TL",
  "role": "stock_component",
  "status": "derived_input",
  "theme_ids": [
    "theme:portfolio-flows",
    "theme:foreign-ownership",
    "theme:swap-and-securities"
  ],
  "indicator_ids": [
    "derived:dibs-stock",
    "derived:dibs-foreign-share",
    "derived:equity-plus-dibs-flow"
  ],
  "source_dependency_ids": [
    "source:prbnk-weekly-zip",
    "source:prbnk-swap-pdf"
  ],
  "catalog_record": {
    "id": "catalog:evds2:TP.DIBSPIYDEG.ST",
    "title": "1.Toplam (S.1, S.2)",
    "frequency": "weekly",
    "unit": "milyon TL",
    "data_group": "bie_dibspiydeg",
    "category": "DEVLET İÇ BORÇLANMA SENETLERİ"
  },
  "memory_rules": [],
  "source_snippets": [
    "\"TP.DIBSPIYDEG.ST\": [3, \"DİBS (Tüm Stok, Piyasa Değeri)\"],",
    "df_menkul_kiymet_apko_[\"DİBS (Tüm Stok, USD)\"] = df_menkul_kiymet_apko_[\"TP_DIBSPIYDEG_ST\"] / df_menkul_kiymet_apko_[\"TP_DK_USD_A_YTL\"]",
    "\"TP_MKNETHAR_M9\", \"TP_MKNETHAR_M10\", \"TP_MKNETHAR_M11\", \"TP_DIBSPIYDEG_ST\", \"TP_DK_USD_A_YTL\""
  ],
  "indicator_hints": [
    "derived:dibs-foreign-share: DIBS stok ve haftalik ZIP tablosundan turetilen yabanci pay.",
    "derived:equity-plus-dibs-flow: Hisse ve DIBS akimlarinin birlestirilmis net degisimi."
  ],
  "notes": ""
}
