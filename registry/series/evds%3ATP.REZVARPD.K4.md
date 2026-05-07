---
record_type: series
id: evds:TP.REZVARPD.K4
title: Toplam Nakit ve Mevduatlar (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K4
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB'nin yurtdışında ve uluslararası kurumlarda tuttuğu
  toplam döviz nakit ve mevduat tutarı. Kaynak grubu: ULUSLARARASI
  REZERVLER VE DÖVİZ LİKİDİTESİ. K5 + K6 + K7 toplamına eşittir
  (Diğer MB/BIS/IMF + Yurtiçi Bankalar + Yurtdışı Bankalar).
usage: >
  TP.REZVARPD.K4 = K5 + K6 + K7 (yaklaşık)
  Aylık döviz mevduat varlıklarının üst toplamı.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Toplam Nakit ve Mevduatlar (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K4
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'deki "I.A.1.b Nakit ve Mevduatlar" kaleminin aylık üst toplamı.
TCMB'nin yurtdışında ve uluslararası kurumlarda tuttuğu döviz nakit
ve mevduat hesaplarını özetler.

## Alt Bileşenleri

```
TP.REZVARPD.K4 ≈ K5 + K6 + K7
                 ↑     ↑     ↑
                 │     │     └─ Merkezi Türkiye dışında olan bankalar
                 │     └─────── Merkezi Türkiye'de olan bankalar
                 └───────────── Diğer MB, BIS ve IMF
```

Üç alt kalem ayrı ayrı izlenir; üst toplamla karşılaştırarak veri
tutarlılığı kontrol edilebilir.
