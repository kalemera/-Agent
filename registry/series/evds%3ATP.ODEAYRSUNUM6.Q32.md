---
record_type: series
id: evds:TP.ODEAYRSUNUM6.Q32
title: "1.2.3.1.Yolcu (Hizmet Gelirleri - Tasimaci Yolcu)"
status: approved
source: evds
source_version: evds2
ticker: TP.ODEAYRSUNUM6.Q32
frequency: monthly
unit: Milyon USD
description: BPM6 odemeler dengesi ayrıntılı sunum — Hizmet gelirleri altında tasimaci yolcu kalemi. Yolcu ve Seyahat toplamının bir bileşeni.
usage: Turizm ve hizmet dengesi analizi, Yolcu+Seyahat (turizm_sum) hesaplamasi icin Q41 ile birlikte kullanilir
official_url: ''
theme_ids:
- theme:cari-denge
indicator_ids:
- derived:yolcu-seyahat-net
---
# 1.2.3.1.Yolcu (Hizmet Gelirleri - Taşımacı Yolcu)

## Aciklama

BPM6 Odemeler Dengesi Ayrintili Sunum (bie_odeayrsunum6) — Hizmet gelirleri (1.2) altindaki tasimaci yolcu kalemi (1.2.3.1).
EVDS SERIE_NAME: "1.2.3.1.Yolcu", SERIE_NAME_ENG: "1.2.3.1.Passenger".
Ust seri: TP.ODEAYRSUNUM6.Q29 (1.2.3 Tasimaci).

## Kullanim

Ozet tablo (cari_denge_ozet.py) icinde Q41 (Seyahat) ile toplanarak "Yolcu ve Seyahat" satirini olusturur.
_find_col(df, ["1.2.3.1.Yolcu"]) ile keyword eslesmesi yapilir.
