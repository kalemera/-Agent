---
record_type: series
id: evds:TP.REZVARPD.K8
title: IMF Rezerv Pozisyonu (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K8
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — Türkiye'nin IMF nezdindeki rezerv pozisyonu Milyar USD
  karşılığı. Kaynak grubu: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ.
  TP.BL098 (haftalık IMF rezerv pozisyonu) serisinin USD biriminde
  aylık karşılığıdır.
usage: >
  Aylık fallback olarak IMF rezerv pozisyonu izleme.
  TP.BL098 ile akraba (haftalık Bin TL versiyonu).
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# IMF Rezerv Pozisyonu (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K8
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'deki "I.A.1.c IMF rezerv pozisyonu" kaleminin aylık değeri.
Türkiye'nin IMF kotasının ödenmiş döviz kısmıdır ve istenildiğinde
çekilebilir; rezerv varlık niteliği taşır.

## Haftalık Vaziyet Akrabası

| Seri | Frekans | Birim |
|---|---|---|
| **TP.REZVARPD.K8** | Aylık | Milyar USD (doğrudan) |
| **TP.BL098** | Haftalık | Bin TL → Milyar USD (İmaEdilenUSDTL üzerinden) |

İkisi aynı kavramı temsil eder; aylık doğrudan USD biriminde
geldiği için kur çevirme gerekmez.
