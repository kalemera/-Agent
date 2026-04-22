---
record_type: indicator
id: derived:gelir-dengesi-net
title: Gelir Dengesi (Birincil + İkincil)
status: approved
input_ids:
- evds:TP.ODANA6.Q08
- evds:TP.ODANA6.Q09
- evds:TP.ODANA6.Q11
formula_expression: (Q08 - Q09) + Q11
formula_description: Birincil Yatırım Geliri Dengesi artı İkincil Yatırım Kaynaklı Gelirler
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Yabancı sermayenin yurt içindeki kar/faiz transferleri eksi Türkiye'nin yurt dışı gelir tahsilatı. Genellikle negatif (sermaye açığı baskısı).
validation_note: bie_odana6 veri grubundan — BPM6 analitik sunum
theme_ids:
- theme:cari-denge
---
# Gelir Dengesi (Birincil + İkincil)

## Formül
(Q08 − Q09) + Q11

## Seri Kaynakları
- TP.ODANA6.Q08 — 1.5.Birincil Yatırım Kaynaklı Gelirler
- TP.ODANA6.Q09 — 1.6.Birincil Yatırım Kaynaklı Giderler
- TP.ODANA6.Q11 — 1.7.İkincil Yatırım Kaynaklı Gelirler

## Hesaplama Notu
Kod: `presentation_table.py::extract_row_value` → calculation="income_balance"
Birincil denge = Q08 - Q09; İkincil = Q11; Toplam = ikisi toplanır.
