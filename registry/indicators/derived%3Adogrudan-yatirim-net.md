---
record_type: indicator
id: derived:dogrudan-yatirim-net
title: Doğrudan Yatırımlar Net (Finans Hesabı)
status: approved
input_ids:
- evds:TP.ODANA6.Q14
- evds:TP.ODANA6.Q15
formula_expression: Q15 - Q14
formula_description: Net Yükümlülük Oluşumu eksi Net Varlık Edinimi
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Yabancı doğrudan yatırım girişi (FDI inflow net). Pozitif = net sermaye girişi. Türkiye için DYY kalitesi cari açık finansmanının en sağlıklı parçası.
validation_note: bie_odana6 veri grubundan — BPM6 analitik sunum
theme_ids:
- theme:cari-denge
- theme:external-financing
---
# Doğrudan Yatırımlar Net

## Formül
Q15 (Net Yükümlülük) − Q14 (Net Varlık)

## Seri Kaynakları
- TP.ODANA6.Q14 — 3.1.Doğrudan Yatırımlar: Net Varlık Edinimi
- TP.ODANA6.Q15 — 3.2.Doğrudan Yatırımlar: Net Yükümlülük Oluşumu

## Hesaplama Notu
Kod: `presentation_table.py::extract_row_value` → calculation="direct_investment"
Yükümlülük - Varlık = Net giriş pozisyonu.
