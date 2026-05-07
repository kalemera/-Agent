---
record_type: series
id: evds:TP.REZVARPD.K10
title: Resmi Altın Rezervleri (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K10
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB'nin sahip olduğu resmi altın rezervinin Milyar USD
  karşılığı. Kaynak grubu: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ.
  TP.AB.C1 (Altın Rezervi Milyon USD) ile aynı kavramın aylık
  versiyonudur.
usage: >
  Aylık fallback olarak brüt altın rezervi izleme.
  TP.AB.C1 (haftalık) ile akraba.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Resmi Altın Rezervleri (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K10
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'deki "I.A.2 Altın" kaleminin aylık USD karşılığı. TCMB'nin
toplam brüt altın rezervinin uluslararası ons fiyatlarıyla
değerlenmiş USD tutarını gösterir.

## Akraba Seriler

| Seri | Frekans | Birim | Kavram |
|---|---|---|---|
| **TP.REZVARPD.K10** | Aylık | Milyar USD | URDL aylık altın rezervi |
| **TP.AB.C1** | Haftalık | Milyon USD | Brüt altın rezervi (haftalık) |
| **TP.BL001** | Haftalık | Bin TL | Altın Rezervi (TL karşılık) |
| **TP.REZVARPD.K11** | Aylık | Milyar Troy Ons | Saf altın miktarı |

K10 değerlemesi USD bazlıdır (ons fiyatı × miktar), K11 ise sadece
fiziksel miktarı (troy ons) verir.
