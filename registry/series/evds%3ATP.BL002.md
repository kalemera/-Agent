---
record_type: series
id: evds:TP.BL002
title: Uluslararası Standartta Altın (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL002
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — uluslararası standartta altın (uluslararası kabul
  gören saflık ve form) Bin TL karşılığı. Kaynak grubu: MERKEZ BANKASI
  HAFTALIK VAZİYET. TP.BL001'in alt kümesi; farkı (TP.BL001 − TP.BL002)
  standart dışı altını gösterir. v9 Excel'de iki ana role sahiptir:
  (1) İma Edilen Gram Altın TL Fiyatı türetme (BL0021 ile birlikte),
  (2) TCMB Net Altın Rezervi formülünde varlık tarafının baz kalemi.
usage: >
  Uluslararası Standartta Altın (Milyar TL) = TP.BL002 / 1.000.000
  İma Edilen Gram Altın/TL = (TP.BL002 × 1000) / TP.BL0021
  TCMB Net Altın Ara (Bin TL) = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + BL141Etkin)
  Power Query: TcmbHaftalikRezerv sorgusunda hem türev fiyat hem Net Altın hesabında.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids:
- derived:tcmb-implied-gram-altin-fiyat
- derived:tcmb-bl141-etkin
- derived:tcmb-net-altin-rezervi
- derived:tcmb-swap-haric-net-altin
- derived:tcmb-swap-haric-net-rezerv-gunluk
---
# Uluslararası Standartta Altın (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL002
**Frekans:** Haftalık
**Ham Birim:** Bin TL → ÷1,000,000 → Milyar TL

## Kullanım — İki Ana Rol

### 1) İma Edilen Gram Altın TL Fiyatı

```
İma Edilen Gram Altın/TL = (TP.BL002 × 1000) / TP.BL0021
                          [Bin TL → TL]      [Safi Gram]
                        = TL / gram
```

Bu fiyat, TP.BL142 (yurtdışı banka altın yük., gram) verisini Bin TL
karşılığa çevirmek için kullanılır.

### 2) TCMB Net Altın Rezervi Varlık Tarafı

```
TCMB Net Altın Ara (Bin TL) = TP.BL002 - (BL132 + BL136 + BL089 + BL141_Etkin)
                              ↑
                    Burada varlık baz kalemi
```

Net Altın hesabında varlık olarak **TP.BL002** kullanılır (TP.BL001
yerine), çünkü uluslararası standartta altın yükümlülükle netleştirilir.

## TP.BL001 ile Ayrım

```
Standart Dışı Altın (TL) = TP.BL001 − TP.BL002
```

| Seri | Kapsam | Net Altın'da |
|---|---|---|
| **TP.BL001** | Toplam altın (standart + standart dışı) | İma Edilen Kur paydası |
| **TP.BL002** | Standart altın (international good delivery) | Net Altın varlığı |

Standart dışı altın (BL001 - BL002 farkı) sertifikalandırma için
ayrılmış altını içerir; net hesaba dahil edilmez çünkü uluslararası
işlem yapılamaz.
