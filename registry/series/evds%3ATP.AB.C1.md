---
record_type: series
id: evds:TP.AB.C1
title: Brüt Altın Rezervi (Milyon USD)
status: approved
source: evds
source_version: evds2
ticker: TP.AB.C1
frequency: weekly
unit: Milyon USD
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB brüt altın rezervinin Milyon USD karşılığı.
  Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. URDL'in I.A.2 (Altın)
  kalemine denk gelir; uluslararası ons fiyatlarıyla değerlenmiş USD
  cinsi resmi altın stokunu gösterir. İma Edilen USD/TL kuru türetmenin
  paydası, brüt rezerv kompozisyonunun altın bileşeni.
usage: >
  Brüt Altın Rezervi (Milyar USD) = TP.AB.C1 / 1000
  İma Edilen USD/TL = (TP.BL001 / TP.AB.C1) / 1000
  Power Query: TcmbHaftalikRezerv sorgusunda TP.AB.C1 ham çekilir, sonra
  Milyar USD ve İma Edilen Kur formüllerinde kullanılır.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids:
- derived:tcmb-implied-fx-usd
- derived:tcmb-net-altin-rezervi
- derived:tcmb-net-doviz-rezervi
- derived:tcmb-swap-haric-net-altin
---
# Brüt Altın Rezervi (Milyon USD)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.AB.C1
**Frekans:** Haftalık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

TCMB'nin brüt altın stokunun USD karşılığı. Uluslararası ons altın
fiyatları ile değerlenmiş resmi rezerv kalemi.

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1116):

```python
Series = "...-TP.AB.C1-..."  # "Altın Rezervi (Milyon USD)"
```

Daha sonra (satır 1348-1350):
```python
T_AltinUSD = "Altın Rezervi (Milyar USD)"
    each
        let x = "Altın Rezervi (Milyon USD)"
        in if x = null then null else x / 1000
```

## İma Edilen USD/TL Türetmesinde Paydası

```
İma Edilen USD/TL = (TP.BL001 / TP.AB.C1) / 1000
                    [Bin TL]   [Milyon USD]
```

Bu kur tüm Bin TL → Milyar USD dönüşümlerinde TCMB'nin "kendi
fiyatlama kuru" olarak kullanılır.

## Akraba Seriler

| Seri | Birim | Frekans |
|---|---|---|
| **TP.AB.C1** | Milyon USD | Haftalık |
| **TP.BL001** | Bin TL | Haftalık |
| **TP.REZVARPD.K10** | Milyar USD | Aylık |

İkisi (C1 + BL001) aynı altın stokunun iki para biriminde gösterimi;
oranı USD/TL kurunu verir.

## Kullanan Indicator'lar

- `derived:tcmb-implied-fx-usd` (kur türetme paydası)
- `derived:tcmb-net-altin-rezervi` (USD'ye çevirme paydası)
- `derived:tcmb-net-doviz-rezervi` (USD'ye çevirme paydası)
- `derived:tcmb-swap-haric-net-altin` (Net Altın bağlamı)
