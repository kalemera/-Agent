---
record_type: series
id: evds:TP.BL0021
title: Uluslararası Standartta Altın (Safi Gram)
status: approved
source: evds
source_version: evds2
ticker: TP.BL0021
frequency: weekly
unit: Safi Gram
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — uluslararası standartta altın miktar serisi, safi gram. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET.
  Power Query'de Troy Ons sütunu türetilir: gram / 31.1034768.
  Asıl kullanım: ima edilen haftalık altın fiyatı (USD/troy ons) = Altın USD / Troy Ons.
usage: >
  Troy Ons = TP.BL0021 / 31.1034768  →  altın fiyatı tespiti için
  Altın (Ton) = TP.BL0021 / 1,000,000  →  miktar değişimi takibi
  Haftalık ton Δ → fiyat etkisi ve miktar etkisi ayrıştırması
official_url: ''
theme_ids:
- theme:reserves
indicator_ids:
- derived:tcmb-altin-troy-ons
- derived:tcmb-implied-gram-altin-fiyat
- derived:tcmb-bl141-etkin
- derived:tcmb-net-altin-rezervi
- derived:tcmb-net-doviz-rezervi
- derived:tcmb-swap-haric-net-altin
- derived:tcmb-swap-haric-net-doviz
- derived:tcmb-swap-haric-net-rezerv-gunluk
---
# Uluslararası Standartta Altın (Safi Gram)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL0021
**Frekans:** Haftalık
**Ham Birim:** Safi Gram

## Kullanım

Power Query `TcmbHaftalikRezerv` sorgusunda önce Troy Ons sütunu türetilir:

```
Troy Ons = TP.BL0021 / 31.1034768
```

**Asıl amaç — ima edilen altın fiyatı (Excel BO kolonu):**
```
İma Edilen Altın Fiyatı (USD/troy ons) = Altın Rezervi (USD) / Troy Ons
```

**Miktar analizi:**
```
Altın (Ton) = TP.BL0021 / 1,000,000
Haftalık Δ (Ton) = Bu haftaki ton − önceki haftaki ton
Fiyat Etkisi (USD) = Toplam USD Δ − (Miktar Δ ton × önceki hafta USD/ton fiyatı)
Miktar Etkisi (USD) = Toplam USD Δ − Fiyat Etkisi
```

Not: Excel'de Ton formülü Troy Ons hücresine referansla yazılmış (`TroyOns × 31.1034768 / 1,000,000`)
ancak matematiksel olarak `gram / 1,000,000` ile özdeştir.
