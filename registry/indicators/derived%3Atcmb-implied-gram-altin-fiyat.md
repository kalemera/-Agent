---
record_type: indicator
id: derived:tcmb-implied-gram-altin-fiyat
title: TCMB İma Edilen Gram Altın TL Fiyatı
status: approved
input_ids:
- evds:TP.BL002
- evds:TP.BL0021
formula_expression: (TP.BL002 * 1000) / TP.BL0021
formula_description: Uluslararası standartta altın TL değerinin safi gram miktarına oranı, TL/gram fiyat verir.
output_frequency: weekly
output_unit: TL/gram
economic_meaning: >
  TCMB'nin uluslararası standart altın stokunu (BL002) TL ve gram cinsi olarak ayrı
  raporlamasından türetilen TL/gram altın fiyatı. Bu fiyat, BL142 (yurtdışı banka
  altın yükümlülük gram) verisini Bin TL karşılığa çevirmek için kullanılır.
  TCMB raporlama anındaki uluslararası ons fiyatı × USD/TL'yi yansıtır.
validation_note: >
  TP.BL002 (Bin TL) × 1000 ile TL'ye, TP.BL0021 (Safi Gram) ile bölünür.
  TP.BL0021 = 0 veya null ise null döner.
theme_ids:
- theme:reserves
---
# TCMB İma Edilen Gram Altın TL Fiyatı

## Formül

```
İma Edilen Gram Altın/TL = (TP.BL002 × 1000) / TP.BL0021
                            [Bin TL → TL]    [Safi Gram]
                          = TL / gram
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1297-1306):

```python
T_GramFiyat = (
    "İma Edilen Gram Altın/TL Fiyatı",
    each
        let tlBin = Record.FieldOrDefault(_, "Uluslararası Standartta Altın (Bin TL)", null),
            gram  = Record.FieldOrDefault(_, "Uluslararası Standartta Altın (Safi Gram)", null)
        in if tlBin = null or gram = null or gram = 0 then null
           else (tlBin * 1000) / gram
)
```

## Kullanım: BL141 Türetilen Hesabı

BL142 (Yurtdışı Banka Altın Yükümlülük, Safi Gram) verisinden Bin TL
karşılık türetmek için kullanılır:

```
Yurtdışı Banka Altın Yük. Türetilen (Bin TL) =
    TP.BL142 × İmaEdilenGramAltinTL / 1000
```

Bu, BL141 verisinin null olduğu tarihlerde altın yükümlülük TL
karşılığını gram cinsinden hesaplamaya yarar.

## Ekonomik Anlam

TCMB'nin altını TL bazında değerlendirme fiyatı. Uluslararası ons
fiyatı (USD/oz) × USD/TL kuru / 31.1034768 ile yaklaşık olarak aynı
değeri vermelidir. Tutarsızlıklar TCMB'nin altın değerleme yöntemine
veya raporlama zaman farkına işaret edebilir.
