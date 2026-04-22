---
record_type: indicator
id: derived:altin-net
title: Altin Net Etkisi
status: approved
input_ids:
- evds:TP.HARICCARIACIK.K1
- evds:TP.HARICCARIACIK.K8
formula_expression: K1 - K8
formula_description: Cari denge - Altin haric cari denge = Altin net etkisi
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Altin ithalat/ihracatinin cari dengeye net etkisini gosterir. Negatif deger altin ithalatinin cari acigi artirdigini ifade eder.
validation_note: K1 ve K8 ayni donemde mevcut olmali
theme_ids:
- theme:cari-denge
---
# Altin Net Etkisi

## Formul
K1 - K8

## Formul Aciklamasi
Cari denge (K1) ile altin haric cari denge (K8) arasindaki fark, altinin cari dengeye net etkisini verir.

## Ekonomik Anlam
Altin ithalat/ihracatinin cari dengeye net etkisini gosterir. Turkiye onemli altin ithalatcisi oldugu icin genellikle negatif deger alir.

## Dogrulama Notu
K1 ve K8 ayni donemde mevcut olmali. Her ikisi de EVDS bie_odeayrsunum6 grubundan gelir.
