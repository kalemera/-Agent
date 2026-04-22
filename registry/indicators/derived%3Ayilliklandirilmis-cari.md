---
record_type: indicator
id: derived:yilliklandirilmis-cari
title: Yilliklandirilmis Cari Denge (12 Aylik Kumulatif)
status: approved
input_ids:
- evds:TP.HARICCARIACIK.K1
formula_expression: rolling_sum(K1, window=12)
formula_description: Son 12 ayin cari denge toplami (yilliklandirilmis)
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Mevsimsellikten arindirilmis yillik cari denge gidisati. Trend analizi icin temel gosterge.
validation_note: Minimum 12 ay veri gerektirir
theme_ids:
- theme:cari-denge
---
# Yilliklandirilmis Cari Denge (12 Aylik Kumulatif)

## Formul
rolling_sum(K1, window=12)

## Formul Aciklamasi
Son 12 ayin cari denge toplamini hesaplar. Her yeni ay eklendikce 12 ay onceki ay duser.

## Ekonomik Anlam
Mevsimsellikten arindirilmis yillik cari denge gidisati. Aylık veriler mevsimsel dalgalanma gosterirken, 12 aylik kumulatif yapisal trendi ortaya koyar. Politika yapicilarin en cok takip ettigi gostergelerden biri.

## Dogrulama Notu
Minimum 12 ay veri gerektirir. Ilk 11 ayda NaN doner.
