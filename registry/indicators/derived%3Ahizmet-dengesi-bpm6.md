---
record_type: indicator
id: derived:hizmet-dengesi-bpm6
title: Hizmetler Dengesi (BPM6 Analitik)
status: approved
input_ids:
- evds:TP.ODANA6.Q05
- evds:TP.ODANA6.Q06
formula_expression: Q05 - Q06
formula_description: Hizmet Gelirleri eksi Hizmet Giderleri
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Turizm, taşımacılık ve diğer hizmetlerin net dengesi. Türkiye için turizm sezonu etkisiyle yılın belirli aylarında güçlü pozitif.
validation_note: bie_odana6 veri grubundan — BPM6 analitik sunum. BPM5/eski serilerle karıştırılmamalı.
theme_ids:
- theme:cari-denge
---
# Hizmetler Dengesi (BPM6 Analitik)

## Formül
Q05 (Hizmet Gelirleri) − Q06 (Hizmet Giderleri)

## Seri Kaynakları
- TP.ODANA6.Q05 — 1.3.Hizmet Gelirleri
- TP.ODANA6.Q06 — 1.4.Hizmet Giderleri

## Hesaplama Notu
Kod: `presentation_table.py::extract_row_value` → calculation="hizmet_balance"
Sütun arama: `find_column_by_keywords(df_analitik, ["Hizmet Gelirleri"])` ve `["Hizmet Giderleri"]`
Türkçe normalizasyon `_tr_normalize()` ile yapılır.

## Ekonomik Anlam
Turizm sezonunda (Mayıs–Eylül) güçlü artış gösterir. Yıllık turizm geliri ~50-60 milyar USD civarında seyreder.
