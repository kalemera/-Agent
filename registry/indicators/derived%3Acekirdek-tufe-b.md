---
record_type: indicator
id: derived:cekirdek-tufe-b
title: Çekirdek TÜFE (B Göstergesi)
status: approved
input_ids: []
formula_expression: tufe_core WHERE indicator_code='B'
formula_description: "Enerji ve işlenmemiş gıda hariç TÜFE"
output_frequency: monthly
output_unit: Endeks (2025=100)
economic_meaning: "Enerji fiyat oynaklığından arındırılmış çekirdek enflasyon. C göstergesine kıyasla daha geniş kapsamlı filtreleme."
validation_note: "source:tufe-ozel-kapsamli Excel dosyasından parse edilir. indicator_code='B' olarak tufe_core tablosuna yazılır."
theme_ids:
- theme:tufe
---
# Çekirdek TÜFE (B Göstergesi)

## Formül
Enerji ve işlenmemiş gıda hariç TÜFE

## Veri Kaynağı
source:tufe-ozel-kapsamli — Özel Kapsamlı TÜFE Göstergeleri Excel dosyası (TÜIK Press 58295)

## Ekonomik Anlam
Enerji fiyat oynaklığından arındırılmış çekirdek enflasyon. C göstergesine kıyasla daha geniş kapsamlı filtreleme.
