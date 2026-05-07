---
record_type: indicator
id: derived:tcmb-doviz-rezervi-tl-urdl
title: TCMB Döviz Rezervi (Milyar TL, URDL Alternatif Yolu)
status: approved
input_ids:
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
formula_expression: (TP.BL003 + TP.BL004 + TP.BL008) / 1000000
formula_description: Brüt Rezerv'den altın bileşeni (BL001) çıkarılarak elde edilen sadece-döviz brüt rezerv (Bin TL → Milyar TL).
output_frequency: weekly
output_unit: Milyar TL
economic_meaning: >
  TCMB brüt döviz rezervi (altın hariç) TL cinsi bileşen toplamı.
  URDL'in döviz varlıklar (banknot + yurtdışı YP varlık + menkul kıymet)
  toplamına denk gelir. Brüt altın rezervi ayrı olarak TP.BL001'den izlenir.
validation_note: >
  Bu indicator (BL003+BL004+BL008) tek başına brüt döviz rezervidir;
  TP.AB.C2 (Brüt Döviz Rezervi, Milyon USD) ile USD/TL üzerinden
  karşılaştırılabilir. Standby kalıntısı bu hesaba dahil edilmez.
theme_ids:
- theme:reserves
---
# TCMB Döviz Rezervi (Milyar TL, URDL Alternatif Yolu)

## Formül

```
Döviz Rezervi (Milyar TL) = (TP.BL003 + TP.BL004 + TP.BL008) / 1.000.000
```

Bileşenler:
- **TP.BL003**: Yabancı Para Banknotlar
- **TP.BL004**: Yurtdışı Banka Toplam YP Varlık
- **TP.BL008**: Döviz Menkul Kıymetler

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1385-1396):

```python
T_DovizTL = "Döviz Rezervi (Milyar TL)"
    each
        let kalemler = List.RemoveNulls({BL003, BL004, BL008})
        in if List.Count(kalemler) = 0 then null
           else List.Sum(kalemler) / 1000000
```

## Brüt Rezerv ile İlişki

```
Brüt Rezerv (TL) = Altın (BL001) + Döviz (BL003+BL004+BL008)
Döviz Rezervi (TL) = Brüt Rezerv (TL) - Altın (BL001)
```

## TP.AB.C2 ile Karşılaştırma

TP.AB.C2 doğrudan "Brüt Döviz Rezervi (Milyon USD)" verir. Bu indicator
ile karşılaştırma için USD/TL kuru gerekir:

```
Bu indicator (Milyar TL) ≈ TP.AB.C2 (Milyon USD) × USD/TL_Kur / 1000
```

İki yol birbirini doğrular; sapmalar fiyatlama anı farklarından kaynaklanır.
