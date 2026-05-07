---
record_type: series
id: evds:TP.BL001
title: Altın Rezervi (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL001
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB altın kalemi TL cinsinden (toplam altın stok).
  Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. v9 Excel'de üç ana
  rolü vardır: (1) İma Edilen USD/TL kuru türetme paydası, (2) URDL
  alternatif yolu Brüt Rezerv formülünün altın bileşeni, (3) TCMB Net
  Altın Rezervi formülünde varlık tarafının baz kalemi (yanı sıra BL002
  ile birlikte).
usage: >
  İma Edilen USD/TL = (TP.BL001 / TP.AB.C1) / 1000
  Brüt Rezerv (URDL alternatif) = (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008) / 1.000.000
  Standby Kalıntısı = TP.AB.N07 - (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008)
  Power Query: TcmbHaftalikRezerv sorgusunda Bin TL → Milyar TL ve Milyar USD'ye çevrilir.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids:
- derived:tcmb-implied-fx-usd
- derived:tcmb-brut-rezerv-tl-urdl
- derived:tcmb-standby-kalintisi
- derived:tcmb-net-altin-rezervi
- derived:tcmb-net-doviz-rezervi
- derived:tcmb-swap-haric-net-altin
- derived:tcmb-swap-haric-net-doviz
- derived:tcmb-swap-haric-net-rezerv-gunluk
- derived:tcmb-swap-haric-net-rezerv-urdl
---
# Altın Rezervi (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL001
**Frekans:** Haftalık
**Ham Birim:** Bin TL → ÷1,000,000 → Milyar TL

## Kullanım — Üç Ana Rol

### 1) İma Edilen USD/TL Kuru Türetme

```
İma Edilen USD/TL = (TP.BL001 / TP.AB.C1) / 1000
```

Bu kur tüm Bin TL → Milyar USD dönüşümlerinde TCMB'nin "fiyatlama
kuru" olarak kullanılır.

### 2) URDL Alternatif Brüt Rezerv

```
Brüt Rezerv (URDL alternatif) = TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008
```

EVDS API üzerinden URDL ZIP scrape'in alternatifi.

### 3) Standby Kalıntısı Türetimi

```
Standby Kalıntısı = TP.AB.N07 - (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008)
```

TP.AB.N07 ile çekirdek toplam farkı, Net Döviz hesabı varlık tarafına
eklenir.

## TP.BL002 ile Ayrım

| Seri | Kapsam | Net Altın Formülünde |
|---|---|---|
| **TP.BL001** | Toplam altın (her tip) | İma Edilen Kur paydası |
| **TP.BL002** | Uluslararası standartta altın | Net Altın varlığı |

TP.BL001 toplam, TP.BL002 ise standart altın (uluslararası kabul gören
alt küme); fark = standart-dışı altın.
