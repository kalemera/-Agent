---
record_type: indicator
id: derived:tcmb-implied-fx-usd
title: TCMB Altın Bazlı İma Edilen USD/TL Kuru
status: approved
input_ids:
- evds:TP.BL001
- evds:TP.AB.C1
formula_expression: (TP.BL001 / TP.AB.C1) / 1000
formula_description: TL cinsi altın rezervinin USD cinsi altın rezervine oranı, USD/TL kurunu verir.
output_frequency: weekly
output_unit: TL/USD
economic_meaning: >
  TCMB'nin altın stokunu hem TL hem USD biriminde raporlaması, ikisinin oranı USD/TL kuru
  vermesi sağlar. Bu "ima edilen" kur, haftalık vaziyet TL kalemlerini USD'ye çevirmek
  için TCMB Net Altın/Döviz Rezervi formüllerinde kullanılır.
  Resmi USD/TL piyasa kuruna yakın bir değer döndürür ama TCMB'nin altın
  fiyatlama anına özgü ufak sapmalar gösterebilir.
validation_note: >
  TP.BL001 (Bin TL) ve TP.AB.C1 (Milyon USD) birim çarpanı uyumu için /1000 uygulanır.
  TP.AB.C1 = 0 ise null döner. Pre-2018 dönemlerde TP.BL001 değer farklılıkları nedeniyle
  ima edilen kurun piyasa kurundan ufak sapmaları normaldir.
theme_ids:
- theme:reserves
---
# TCMB Altın Bazlı İma Edilen USD/TL Kuru

## Formül

```
İma Edilen USD/TL = (TP.BL001 / TP.AB.C1) / 1000
                    [Bin TL]   [Milyon USD]
```

Birim mantığı:
- TP.BL001: Altın rezervi (Bin TL) → 1000 ile çarpılırsa TL
- TP.AB.C1: Altın rezervi (Milyon USD) → 1.000.000 ile çarpılırsa USD
- Oran: (TP.BL001 × 1000) / (TP.AB.C1 × 1.000.000) = (TP.BL001 / TP.AB.C1) / 1000

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1284-1293):

```python
T_ImpliedFX = (
    "İma Edilen USD/TL (Altın TL / Altın USD)",
    each
        let tl  = Record.FieldOrDefault(_, "Altın Rezervi (Bin TL)", null),
            usd = Record.FieldOrDefault(_, "Altın Rezervi (Milyon USD)", null)
        in if tl = null or usd = null or usd = 0 then null
           else (tl / usd) / 1000
)
```

## Ekonomik Anlam

TCMB her hafta aynı altın stokunu hem TL hem USD biriminde raporlar.
İkisinin oranı, raporlama anındaki USD/TL kurunu **dolaylı yoldan** verir.
Bu "ima edilen kur" özellikle pre-2018 günlük EVDS verisinin olmadığı
dönemlerde (TP.DK.USD.A.YTL boşluğu) haftalık TL→USD çevrimi için
referans kur olarak kullanılır.

## Kullanım Yerleri

`TcmbHaftalikRezerv`'de tüm Bin TL→Milyar USD dönüşümlerinde:
- TCMB Net Altın Rezervi (Milyar USD)
- TCMB Net Döviz Rezervi (Milyar USD)
- Net Uluslararası Rezerv (Milyar USD)
- Menkul Kıymetler / IMF Rezerv Pozisyonu / SDR'lar (Milyar USD)
