---
record_type: proposal
id: proposal:indicator:derivedestimated-net-reserve
proposal_id: proposal:indicator:derivedestimated-net-reserve
title: Implied indicator proposal for derived:estimated-net-reserve
status: approved
target_type: indicator
target_id: derived:estimated-net-reserve
ticker: ''
notebook_slug: ''
notebook_path: ''
candidate_title: Estimated Net Reserve
candidate_unit: ''
candidate_frequency: ''
candidate_role: ''
candidate_theme_ids:
- theme:net-reserve-estimate
candidate_indicator_inputs:
- evds:TP.AB.A02
- evds:TP.AB.A10
- evds:TP.AB.A11
- evds:TP.AB.A13
- evds:TP.AB.A14
- evds:TP.DK.USD.A.YTL
- source:rzrv-manual-swap-ledger
candidate_formula_hint: Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir.
confidence: 0.7
source: heuristic
evidence_fingerprint: ''
catalog_record_id: ''
memory_rule_ids: []
evidence: {}
llm_provider: ''
llm_model: ''
promoted_record_id: derived:estimated-net-reserve
promoted_memory_rule_id: memory:global-estimated-net-reserve
approval_mode: auto_heuristic
approval_reason: Implied proposal passed deterministic safety checks.
notes: 'Implied from 1 notebook(s): rzrv-blg-v7'
body: '# Implied indicator proposal for derived:estimated-net-reserve


  ## Target

  indicator | derived:estimated-net-reserve


  ## Notebook

  -


  ## Candidate Title

  Estimated Net Reserve


  ## Candidate Unit

  -


  ## Candidate Frequency

  -


  ## Candidate Role

  -


  ## Confidence

  0.7


  ## Candidate Themes

  - theme:net-reserve-estimate


  ## Candidate Indicator Inputs

  - evds:TP.AB.A02

  - evds:TP.AB.A10

  - evds:TP.AB.A11

  - evds:TP.AB.A13

  - evds:TP.AB.A14

  - evds:TP.DK.USD.A.YTL

  - source:rzrv-manual-swap-ledger


  ## Formula Hint

  Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir.


  ## Source

  heuristic


  ## Approval Mode

  -


  ## Approval Reason

  -


  ## Notes

  Implied from 1 notebook(s): rzrv-blg-v7


  ## Evidence

  -

  '
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\proposals\proposal%3Aindicator%3Aderivedestimated-net-reserve.md
---
# Implied indicator proposal for derived:estimated-net-reserve

## Target
indicator | derived:estimated-net-reserve

## Notebook
-

## Candidate Title
Estimated Net Reserve

## Candidate Unit
-

## Candidate Frequency
-

## Candidate Role
-

## Confidence
0.7

## Candidate Themes
- theme:net-reserve-estimate

## Candidate Indicator Inputs
- evds:TP.AB.A02
- evds:TP.AB.A10
- evds:TP.AB.A11
- evds:TP.AB.A13
- evds:TP.AB.A14
- evds:TP.DK.USD.A.YTL
- source:rzrv-manual-swap-ledger

## Formula Hint
Dis varlik ve yukumluluk bloklarindan tahmini net rezerv uretir.

## Source
heuristic

## Approval Mode
auto_heuristic

## Approval Reason
Implied proposal passed deterministic safety checks.

## Notes
Implied from 1 notebook(s): rzrv-blg-v7

## Evidence
-
