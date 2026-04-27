---
record_type: indicator
id: derived:yolcu-seyahat-net
title: Yolcu ve Seyahat (Turizm Net)
status: approved
input_ids:
- evds:TP.ODEAYRSUNUM6.Q32
- evds:TP.ODEAYRSUNUM6.Q41
formula_expression: Q32 + Q41
formula_description: "1.2.3.1.Yolcu + 1.2.4.Seyahat — BPM6 hizmet gelirleri altindaki iki turizm kaleminin toplami"
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: Turkiye'nin turizm ve seyahat kaynakli hizmet gelirlerinin net denges. Yolcu tasimaciligi (Q32) ve seyahat/turizm (Q41) kalemlerinin toplami. Turkiye icin genellikle pozitif ve buyuk rakamlar (turizm fazlasi).
validation_note: Her iki seri de bie_odeayrsunum6 grubundan gelir, ayni donemde mevcut olmali. Cari denge ozet tablosunda "Yolcu ve Seyahat" satiri bu hesaplama ile olusturulur.
theme_ids:
- theme:cari-denge
---
# Yolcu ve Seyahat (Turizm Net)

## Formul

Q32 + Q41 — TP.ODEAYRSUNUM6.Q32 (Yolcu) + TP.ODEAYRSUNUM6.Q41 (Seyahat)

## Formul Aciklamasi

BPM6 hizmet gelirleri altindaki iki turizm kaleminin toplami:
- Q32: 1.2.3.1.Yolcu — tasimaci yolcu geliri/gideri
- Q41: 1.2.4.Seyahat — seyahat/turizm geliri/gideri

Her iki seri de `bie_odeayrsunum6` grubundan dinamik olarak cekiliyor.
Ozet tabloda `turizm_sum` hesaplamasi: `_find_col(df, ["1.2.3.1.Yolcu"])` + `_find_col(df, ["1.2.4.Seyahat"])`.

## Ekonomik Anlam

Turkiye'nin turizm ve seyahat kalemleri odemeler dengesi icinde en buyuk hizmet geliri kaynagi.
Seyahat (Q41) ana kalem — turizm gelirleri buraya giriyor.
Yolcu (Q32) daha kucuk — tasimacilik odull yolcu segmenti.
Toplam, "hizmet dengesi" anaizinde "Hizmetler Dengesi" satirinin ana bilesenini olusturuyor.

## Dogrulama Notu

- Her iki seri de `bie_odeayrsunum6` grubundan, ayni tarih araliginda mevcut olmali
- EVDS keyword eslesme: seri adi normalizasyon ile yapiliyor (`_tr_normalize`)
- Cari denge ozet tablosu (cari_denge_ozet.py) bu hesaplamayi `turizm_sum` calculation tipi olarak uyguliyor
