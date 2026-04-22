---
record_type: indicator
id: derived:cekirdek-tufe-c
title: Çekirdek TÜFE (C Göstergesi)
status: approved
input_ids: []
formula_expression: tufe_core WHERE indicator_code='C'
formula_description: "Enerji, gıda ve alkolsüz içecekler, alkollü içkiler ile tütün ürünleri ve altın hariç TÜFE"
output_frequency: monthly
output_unit: Endeks (2025=100)
economic_meaning: "Geçici fiyat şoklarından arındırılmış yapısal enflasyon göstergesi. Manşet TÜFE'den düşük seyretmesi geçici baskı, yüksek seyretmesi kalıcı baskı sinyali verir."
validation_note: "source:tufe-ozel-kapsamli Excel dosyasından parse edilir. indicator_code='C' olarak tufe_core tablosuna yazılır."
theme_ids:
- theme:tufe
---
# Çekirdek TÜFE (C Göstergesi)

## Formül
Enerji, gıda ve alkolsüz içecekler, alkollü içkiler ile tütün ürünleri ve altın hariç TÜFE

## Veri Kaynağı
source:tufe-ozel-kapsamli — Özel Kapsamlı TÜFE Göstergeleri Excel dosyası (TÜIK Press 58295)

## Ekonomik Anlam
Geçici fiyat şoklarından arındırılmış yapısal enflasyon göstergesi. Manşet TÜFE'den düşük seyretmesi geçici baskı, yüksek seyretmesi kalıcı baskı sinyali verir.
