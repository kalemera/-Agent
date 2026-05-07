---
record_type: series
id: evds:TP.REZVARPD.K5
title: Diğer Merkez Bankaları, BIS ve IMF (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K5
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB'nin diğer merkez bankaları (FED, ECB, vb.), BIS
  ve IMF nezdinde tuttuğu döviz mevduatlarının Milyar USD karşılığı.
  Kaynak grubu: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ. Toplam
  Nakit ve Mevduatların (TP.REZVARPD.K4) üç alt bileşeninden biridir.
usage: >
  Aylık fallback olarak resmi kurum mevduat varlıkları izlemede
  kullanılır. K4 = K5 + K6 + K7 ilişkisinin alt kalemi.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Diğer Merkez Bankaları, BIS ve IMF (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K5
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'de "I.A.1.b.i Diğer merkez bankaları, BIS ve IMF" alt kaleminin
aylık değeri. TCMB'nin uluslararası resmi kurumlarda tuttuğu döviz
mevduatlarını gösterir.

## İçerik

- Diğer merkez bankaları (FED, ECB, BoJ, vb.) nezdindeki mevduatlar
- Bank for International Settlements (BIS) hesapları
- IMF nezdindeki rutin operasyonel hesaplar (rezerv pozisyonu hariç)

## TP.BL098 ile Ayrım

Bu seri **mevduat** niteliğindeki varlıkları içerir. IMF rezerv
pozisyonu (TP.BL098, kotanın ödenmiş kısmı) ayrı bir kavramdır ve
URDL'de **TP.REZVARPD.K8** olarak takip edilir.
