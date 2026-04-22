---
record_type: indicator
id: derived:hizmet-endeks
title: Hizmet TÜFE Endeksi
status: approved
input_ids: []
formula_expression: tufe_core WHERE indicator_code='H_TOTAL'
formula_description: "Hizmet sektörü TÜFE alt endeksi (kira, ulaşım, eğitim, sağlık vb.)"
output_frequency: monthly
output_unit: Endeks (2025=100)
economic_meaning: "Hizmet enflasyonu — iç talep ve ücret baskısına duyarlı. Mal enflasyonuna göre daha katı ve kalıcı olma eğilimi taşır."
validation_note: "source:tufe-ozel-kapsamli Excel dosyasından parse edilir. indicator_code='H_TOTAL' olarak tufe_core tablosuna yazılır."
theme_ids:
- theme:tufe
---
# Hizmet TÜFE Endeksi

## Formül
Hizmet sektörü TÜFE alt endeksi (kira, ulaşım, eğitim, sağlık vb.)

## Veri Kaynağı
source:tufe-ozel-kapsamli — Özel Kapsamlı TÜFE Göstergeleri Excel dosyası (TÜIK Press 58295)

## Ekonomik Anlam
Hizmet enflasyonu — iç talep ve ücret baskısına duyarlı. Mal enflasyonuna göre daha katı ve kalıcı olma eğilimi taşır.
