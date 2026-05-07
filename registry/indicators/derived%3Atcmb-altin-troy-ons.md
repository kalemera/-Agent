---
record_type: indicator
id: derived:tcmb-altin-troy-ons
title: TCMB Altın Stoku (Troy Ons)
status: approved
input_ids:
- evds:TP.BL0021
formula_expression: TP.BL0021 / 31.1034768
formula_description: Safi gram cinsinden altın miktarını troy ons cinsine çevirir (1 troy ons = 31.1034768 gram).
output_frequency: weekly
output_unit: Troy Ons
economic_meaning: >
  TCMB altın stokunun uluslararası birim olan troy ons cinsinden ifadesi.
  Altın fiyat türetmesi (USD/troy ons) ve uluslararası karşılaştırma için kullanılır.
  Fiziksel altın miktarı sabit kalsa da bu seri raporlanan gram'a duyarlıdır;
  genellikle sıçramalar TCMB'nin altın alım/satımına işaret eder.
validation_note: >
  Sabit dönüşüm faktörü 31.1034768. TP.BL0021 = null ise null döner.
  Excel'deki ayrıca yapılan "Ton = Troy Ons × 31.1034768 / 1.000.000" hesabı,
  Troy Ons → Ton dönüşümü olduğu için aslında doğrudan TP.BL0021 / 1.000.000
  ile aynı sonuca ulaşır (kod yeniden kullanım amaçlı).
theme_ids:
- theme:reserves
---
# TCMB Altın Stoku (Troy Ons)

## Formül

```
Altın (Troy Ons) = TP.BL0021 / 31.1034768
                   [Safi Gram]   [gram/troy ons]
```

Sabit: 1 troy ons = **31.1034768** gram (uluslararası standart).

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1334-1339):

```python
T_Troy = (
    "Altın (Troy Ons)",
    each
        let g = Record.FieldOrDefault(_, "Uluslararası Standartta Altın (Safi Gram)", null)
        in if g = null then null else g / 31.1034768
)
```

## Birincil Kullanım: Altın Fiyat Türetme

Bu indicator'un asıl amacı **uluslararası ons altın fiyatı** elde
etmek için ara hesap olmasıdır:

```
Uluslararası Ons Altın Fiyatı (USD/oz) =
    TP.AB.C1 (Milyon USD × 1.000.000) / TroyOns
```

Bu "ima edilen ons fiyatı" piyasa altın fiyatına yakın olmalıdır;
sapmalar TCMB değerleme metoduyla piyasa arasında ufak farkları gösterir.

## Ton Dönüşümü Notu

Excel raporlamasında ek olarak Ton hesabı yapılır:

```
Ton = Troy Ons × 31.1034768 / 1.000.000
    = TP.BL0021 / 31.1034768 × 31.1034768 / 1.000.000
    = TP.BL0021 / 1.000.000
```

Yani matematiksel olarak Ton = TP.BL0021 (gram) / 1 milyon. Excel'de
Troy Ons üzerinden hesaplama, kod yeniden kullanımı içindir; fiziksel
anlamda direkt gram/1M ile aynı sonuçtur.
