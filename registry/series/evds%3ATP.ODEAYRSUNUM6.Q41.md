---
record_type: series
id: evds:TP.ODEAYRSUNUM6.Q41
title: "1.2.4.Seyahat (Hizmet Gelirleri - Turizm)"
status: approved
source: evds
source_version: evds2
ticker: TP.ODEAYRSUNUM6.Q41
frequency: monthly
unit: Milyon USD
description: BPM6 odemeler dengesi ayrıntılı sunum — Hizmet gelirleri altında seyahat (turizm) kalemi. Yolcu ve Seyahat toplamının temel bileşeni.
usage: Turizm dengesi analizi, Yolcu+Seyahat (turizm_sum) hesaplamasi icin Q32 ile birlikte kullanilir
official_url: ''
theme_ids:
- theme:cari-denge
indicator_ids:
- derived:yolcu-seyahat-net
---
# 1.2.4.Seyahat (Hizmet Gelirleri - Turizm)

## Aciklama

BPM6 Odemeler Dengesi Ayrintili Sunum (bie_odeayrsunum6) — Hizmet gelirleri (1.2) altindaki seyahat (turizm) kalemi (1.2.4).
EVDS SERIE_NAME: "1.2.4.Seyahat", SERIE_NAME_ENG: "1.2.4.Travel".
Ust seri: TP.ODEAYRSUNUM6.Q20 (1.2 Hizmetler Dengesi).

## Kullanim

Ozet tablo (cari_denge_ozet.py) icinde Q32 (Yolcu) ile toplanarak "Yolcu ve Seyahat" satirini olusturur.
_find_col(df, ["1.2.4.Seyahat"]) ile keyword eslesmesi yapilir.
Seyahat kalmei Turkiye'nin en buyuk hizmet geliri kaynagi (turizm).
