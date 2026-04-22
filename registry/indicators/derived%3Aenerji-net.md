---
record_type: indicator
id: derived:enerji-net
title: Enerji Net Etkisi
status: approved
input_ids:
- evds:TP.HARICCARIACIK.K8
- evds:TP.HARICCARIACIK.K10
formula_expression: K8 - K10
formula_description: Altin haric cari denge - Enerji+altin haric cari denge = Enerji net etkisi
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Enerji ithalatinin cari dengeye net etkisini gosterir. Turkiye enerji bagimlisi oldugu icin genellikle buyuk negatif deger alir.
validation_note: K8 ve K10 ayni donemde mevcut olmali
theme_ids:
- theme:cari-denge
---
# Enerji Net Etkisi

## Formul
K8 - K10

## Formul Aciklamasi
Altin haric cari denge (K8) ile enerji+altin haric cari denge (K10) arasindaki fark, enerjinin cari dengeye net etkisini verir.

## Ekonomik Anlam
Enerji ithalatinin cari dengeye net etkisini gosterir. Turkiye enerji bagimlisi oldugu icin genellikle buyuk negatif deger alir. Petrol fiyatlariyla guclü korelasyon gosterir.

## Dogrulama Notu
K8 ve K10 ayni donemde mevcut olmali.
