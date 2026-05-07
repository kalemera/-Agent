---
record_type: indicator
id: derived:tcmb-brut-rezerv-tl-urdl
title: TCMB Brüt Rezerv (Milyar TL, URDL Alternatif Yolu)
status: approved
input_ids:
- evds:TP.BL001
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
formula_expression: (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008) / 1000000
formula_description: URDL'in I.A. Resmi Rezerv Varlıkları kalemini TP.BL haftalık vaziyet bileşenlerinden türetir (Bin TL → Milyar TL).
output_frequency: weekly
output_unit: Milyar TL
economic_meaning: >
  TCMB brüt rezervinin TL cinsinden bileşen toplamı. URDL haftalık ZIP
  yayınında "I.A. Resmi rezerv varlıkları" satırına denk gelen değeri
  doğrudan EVDS API üzerinden hesaplar. ZIP scrape kırılganlığını
  bypass eden alternatif yol.
validation_note: >
  Tüm dört bileşen aynı tarihte mevcut olmalı. Fark TP.AB.N07 (Standby
  Brüt) ile karşılaştırılarak Standby Kalıntısı hesaplanır. Pre-2018
  dönemde BL004/BL008 değerleri farklı yapı içerebilir, ufak sapmalar
  beklenir.
theme_ids:
- theme:reserves
---
# TCMB Brüt Rezerv (Milyar TL, URDL Alternatif Yolu)

## Formül

```
Brüt Rezerv (Milyar TL) = (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008) / 1.000.000
                          [Bin TL toplam]                              [Bin TL → Milyar TL]
```

Bileşenler:
- **TP.BL001**: Altın Rezervi
- **TP.BL003**: Yabancı Para Banknotlar
- **TP.BL004**: Yurtdışı Banka Toplam YP Varlık
- **TP.BL008**: Döviz Menkul Kıymetler

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1370-1382):

```python
T_BrutTL = "Brüt Rezerv (Milyar TL)"
    each
        let kalemler = List.RemoveNulls({
                BL001, BL003, BL004, BL008
            })
        in if List.Count(kalemler) = 0 then null
           else List.Sum(kalemler) / 1000000
```

## URDL Alternatif Yolu

URDL haftalık ZIP'inde "I.A. Resmi rezerv varlıkları" satırına bu
formül denk gelir. İki yol arasındaki fark:

| Yol | Kanal | Güvenilirlik | Frekans |
|---|---|---|---|
| **URDL ZIP scrape** | TCMB sayfası HTML→ZIP | Kırılgan | Haftalık |
| **TP.BL toplama (bu indicator)** | EVDS API standart | Sağlam | Haftalık |

`TcmbHaftalikSwap` URDL ZIP başarısız olursa bu yol fallback olarak
kullanılır. Aynı zamanda haftalık ZIP'in gelmediği günlerde de bu
yol çalışır.

## Standby Kalıntısı ile İlişki

```
Brüt Rezerv (URDL bileşen toplamı) ≠ TP.AB.N07 (Standby Brüt)
Fark = Standby Kalıntısı (TP.AB.N07 - bileşenler)
```

Standby kalıntısı bu fark olarak ayrı izlenir ve Net Döviz Rezervi
varlık tarafına eklenir.
