---
record_type: indicator
id: derived:portfoy-yatirim-net
title: Portföy Yatırımları Net (Finans Hesabı)
status: approved
input_ids:
- evds:TP.ODANA6.Q16
- evds:TP.ODANA6.Q17
- evds:TP.ODANA6.Q18
- evds:TP.ODANA6.Q19
formula_expression: Q17 - Q16
formula_description: Net Yükümlülük Oluşumu eksi Net Varlık Edinimi
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: "Yabancı portföy yatırımı (hisse + tahvil) net girişi. Volatil — faiz/kur değişimlerine duyarlı. Alt kalemler: Hisse (Q18) ve Borç Senetleri (Q19)."
validation_note: bie_odana6 veri grubundan — BPM6 analitik sunum
theme_ids:
- theme:cari-denge
- theme:external-financing
- theme:portfolio-flows
---
# Portföy Yatırımları Net

## Formül
Q17 (Net Yükümlülük) − Q16 (Net Varlık)

## Seri Kaynakları
- TP.ODANA6.Q16 — 3.3.Portföy Yatırımları: Net Varlık Edinimi
- TP.ODANA6.Q17 — 3.4.Portföy Yatırımları: Net Yükümlülük Oluşumu
- TP.ODANA6.Q18 — 3.4.1.Hisse Senetleri (alt kalem)
- TP.ODANA6.Q19 — 3.4.2.Borç Senetleri (alt kalem)

## Hesaplama Notu
Kod: `presentation_table.py::extract_row_value` → calculation="portfolio_investment"
