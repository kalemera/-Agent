---
record_type: series
id: evds:TP.REZVARPD.K3
title: Menkul Kıymetler (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K3
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB'nin sahip olduğu döviz cinsi menkul kıymetlerin
  Milyar USD karşılığı. Kaynak grubu: ULUSLARARASI REZERVLER VE DÖVİZ
  LİKİDİTESİ. TP.BL012 (haftalık vaziyet menkul kıymetler) ve TP.BL008
  (döviz menkul kıymetler) ile yakın akrabadır.
usage: >
  Aylık fallback olarak menkul kıymet portföyü izlemede kullanılır.
  URDL'deki "I.A.1.a Menkul kıymetler" kalemine karşılık gelir.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Menkul Kıymetler (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K3
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'deki "I.A.1.a Menkul kıymetler" kaleminin aylık değeri. TCMB'nin
sahip olduğu yabancı devlet tahvilleri, kurumsal tahviller ve diğer
borçlanma araçlarını içerir.

## Haftalık Vaziyet ile İlişki

| Seri | Frekans | Birim |
|---|---|---|
| **TP.REZVARPD.K3** | Aylık | Milyar USD (doğrudan) |
| **TP.BL008** | Haftalık | Bin TL (Brüt rezerv formülünde) |
| **TP.BL012** | Haftalık | Bin TL → Milyar USD raporu |

K3 verisi aylık olarak doğrudan USD biriminde geldiği için kur
çevirme (İmaEdilenUSDTL) gerektirmez. Haftalık seriler ise TL'den
çevrilir.
