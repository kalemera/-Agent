---
record_type: series
id: evds:TP.REZVARPD.K2
title: Döviz Varlıkları (Merkez Bankasınca Alım Satım Konusu Yapılan Dövizler) (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K2
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB tarafından alım satım konusu yapılan döviz varlıklarının
  toplam değeri. Kaynak grubu: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ.
  TP.REZVARPD.K1 (Resmi Rezerv Varlıkları) altındaki ana döviz portföyü
  alt kalemidir; menkul kıymet, mevduat ve nakit kombinasyonu içerir.
usage: >
  Aylık fallback olarak haftalık brüt döviz rezervi izleme analizinde
  kullanılır. URDL tablosunun döviz varlıkları üst toplamıdır.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Döviz Varlıkları (Merkez Bankasınca Alım Satım Konusu Yapılan Dövizler) (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K2
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL tablosunda "I.A.1 Döviz varlıkları" kaleminin aylık değeri.
Resmi Rezerv Varlıklarının (TP.REZVARPD.K1) altın hariç tüm döviz
bileşenlerini özetler:

```
TP.REZVARPD.K2 ≈ K3 (Menkul Kıymet) + K4 (Nakit/Mevduat) + K8 (IMF) + K9 (SDR)
```

## Haftalık Eşleşme

Haftalık dünyada TCMB sayfasından scrape edilen URDL ZIP'inde aynı
kalem "I.A.1 Döviz varlıkları (Merkez Bankasınca alım satım konusu
yapılan)" başlığı altında haftalık olarak yer alır.
