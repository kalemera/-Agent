---
record_type: indicator
id: derived:tcmb-bl141-etkin
title: TCMB Yurtdışı Banka Altın Yükümlülük Etkin Değer
status: approved
input_ids:
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.BL002
- evds:TP.BL0021
formula_expression: 'IF(TP.BL141 != null, TP.BL141, TP.BL142 * ((TP.BL002 * 1000) / TP.BL0021) / 1000)'
formula_description: Gerçek BL141 verisi varsa onu kullan, yoksa BL142 (gram) × İmaEdilenGramAltinTL / 1000 ile türet.
output_frequency: weekly
output_unit: Bin TL
economic_meaning: >
  Yurtdışı banka altın yükümlülüğünün her tarih için tutarlı izlenebilmesi
  amacıyla iki kaynak yolla hesaplanan "etkin" değer. EVDS'de TP.BL141
  her hafta dolu değildir; eksik tarihlerde TP.BL142 (gram) ve İma Edilen
  Gram Altın TL Fiyatı ile türetme yapılır. Net Altın Rezervi formülünün
  yükümlülük tarafında bu değer kullanılır.
validation_note: >
  Gerçek BL141 öncelikli; null ise türetilen formül devreye girer. Eğer
  her ikisi de null ise sonuç null. BL142 backfill (ilk geçerli değerin
  başlangıçtaki nulllar için kullanımı) bu hesabın öncesinde uygulanır.
theme_ids:
- theme:reserves
---
# TCMB Yurtdışı Banka Altın Yükümlülük Etkin Değer

## Formül

```python
Türetilen = TP.BL142 × İmaEdilenGramAltinTL / 1000
          = TP.BL142 × ((TP.BL002 × 1000) / TP.BL0021) / 1000

Etkin = if TP.BL141 != null then TP.BL141 else Türetilen
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1310-1331):

```python
# 1) Önce türetilen
T_BL141Turetilen = "Yurtdışı Banka Altın Yükümlülük Türetilen (Bin TL)"
    each
        let gram  = BL142,
            fiyat = İmaEdilenGramAltinTL
        in if gram = null or fiyat = null then null
           else (gram * fiyat) / 1000

# 2) Sonra etkin (gerçek öncelikli)
T_BL141Etkin = "Yurtdışı Banka Altın Yükümlülük Etkin (Bin TL)"
    each
        let gercek    = BL141,
            turetilen = "Yurtdışı Banka Altın Yükümlülük Türetilen (Bin TL)"
        in if gercek <> null then gercek else turetilen
```

## Neden Etkin Değer?

EVDS'de **TP.BL141** her tarih için yayımlanmaz (özellikle erken
tarihlerde boşluklar var). Time series'in sürekli olabilmesi için iki
kaynak yöntem birleştirilir:

| Tarih Durumu | Hangi yol kullanılır |
|---|---|
| BL141 dolu | BL141 (gerçek değer) |
| BL141 null, BL142 dolu | Türetilen (gram × fiyat) |
| Her ikisi null | null (atla) |

## BL142 Backfill Detayı

Türetilen yola girmeden önce BL142'ye ayrı bir backfill uygulanır:
- **İlk geçerli BL142 değeri** zaman serisinin başındaki tüm null
  tarihlere doldurulur (M kodu satır 1268-1277).
- Bu, BL142 yayını başlamadan önceki dönemlerde de türetilmiş değer
  hesaplanmasını sağlar.

## Kullanım: Net Altın Formülü

```
TCMB Net Altın Rezervi Ara (Bin TL) =
    TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + BL141_Etkin)
                                                  ↑
                                      Bu indicator burada
```
