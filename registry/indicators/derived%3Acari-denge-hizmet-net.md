---
record_type: indicator
id: derived:cari-denge-hizmet-net
title: Hizmet ve Gelir Dengesi (Net)
status: approved
input_ids:
- evds:TP.HARICCARIACIK.K1
formula_expression: Cari Denge - Ticaret Dengesi
formula_description: Cari islemler hesabindan ticaret dengesini cikarinca kalan hizmet ve gelir dengesi
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Turizm, tasimicilik ve diger hizmet gelir/giderlerinin net etkisi. Turkiye icin genellikle pozitif (turizm fazlasi).
validation_note: Ticaret dengesi TUIK veritabanindan gelir, cari denge EVDS'den
theme_ids:
- theme:cari-denge
---
# Hizmet ve Gelir Dengesi (Net)

## Formul
Cari Denge - Ticaret Dengesi

## Formul Aciklamasi
Cari islemler hesabindan (K1) ticaret dengesini (TUIK ihracat-ithalat) cikarinca kalan kisim hizmet ve gelir dengesidir.

## Ekonomik Anlam
Turizm, tasimicilik ve diger hizmet gelir/giderlerinin net etkisi. Turkiye icin genellikle pozitif cunku turizm onemli bir gelir kalemidir. XGBoost tahmin modelinde tahmin edilen bileseni budur.

## Dogrulama Notu
Ticaret dengesi TUIK veritabanindan, cari denge EVDS'den gelir. Iki kaynagin tarihleri eslesmeli.
