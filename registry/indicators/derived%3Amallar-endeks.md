---
record_type: indicator
id: derived:mallar-endeks
title: Mallar TÜFE Endeksi
status: approved
input_ids: []
formula_expression: tufe_core WHERE indicator_code='M_TOTAL'
formula_description: "İşlenmiş ve işlenmemiş mallar toplamı TÜFE alt endeksi"
output_frequency: monthly
output_unit: Endeks (2025=100)
economic_meaning: "Mal enflasyonu — döviz kuru ve ithalat fiyatlarına duyarlı. Hizmet enflasyonuyla karşılaştırıldığında iç talep baskısı değerlendirilebilir."
validation_note: "source:tufe-ozel-kapsamli Excel dosyasından parse edilir. indicator_code='M_TOTAL' olarak tufe_core tablosuna yazılır."
theme_ids:
- theme:tufe
---
# Mallar TÜFE Endeksi

## Formül
İşlenmiş ve işlenmemiş mallar toplamı TÜFE alt endeksi

## Veri Kaynağı
source:tufe-ozel-kapsamli — Özel Kapsamlı TÜFE Göstergeleri Excel dosyası (TÜIK Press 58295)

## Ekonomik Anlam
Mal enflasyonu — döviz kuru ve ithalat fiyatlarına duyarlı. Hizmet enflasyonuyla karşılaştırıldığında iç talep baskısı değerlendirilebilir.
