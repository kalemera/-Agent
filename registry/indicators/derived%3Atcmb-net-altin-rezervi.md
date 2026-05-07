---
record_type: indicator
id: derived:tcmb-net-altin-rezervi
title: TCMB Net Altın Rezervi (Milyar USD)
status: approved
input_ids:
- evds:TP.BL002
- evds:TP.BL132
- evds:TP.BL136
- evds:TP.BL089
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.BL001
- evds:TP.AB.C1
- evds:TP.BL0021
formula_expression: ((TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + BL141Etkin)) / 1000000) / İmaEdilenUSDTL
formula_description: Uluslararası standart altın varlığı eksi tüm altın yükümlülükleri = Net Altın (Bin TL), İma Edilen USD/TL ile Milyar USD'ye çevrilir.
output_frequency: weekly
output_unit: Milyar USD
economic_meaning: >
  TCMB'nin yükümlülüklerden arındırılmış net altın stokunun USD karşılığı.
  Brüt altın rezervinden (BL002), bankaların TCMB'de altın olarak tuttuğu
  zorunlu karşılık ve teminatlar (BL132+BL136+BL089) ile yurtdışı banka
  altın yükümlülüğü (BL141Etkin) düşülür. Bu, TCMB'nin gerçekten kendi
  serbest tasarrufundaki altın rezervidir.
validation_note: >
  Beş ham seri + iki türev (BL141Etkin, İmaEdilenUSDTL) bağımlılığı vardır.
  Pre-2018 dönemde bazı yükümlülük kalemlerinin ayrışmaması nedeniyle ufak
  hesap sapmaları olabilir; teyit sütunu (NetAltin + NetDoviz - NIR) bu sapmayı
  ölçer ve Tarih < 2018-08-31 için null/tolerant rapor verir.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
---
# TCMB Net Altın Rezervi (Milyar USD)

## Formül

```
Ara Değer (Bin TL) = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + BL141_Etkin)
                     [Varlık]    [Yurtiçi Tem.] [ROM]   [ZK]    [Yurtdışı Yük.]

Net Altın (Milyar USD) = (Ara Değer / 1.000.000) / İmaEdilenUSDTL
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1435-1459):

```python
# 1) Ara değer (Bin TL)
T_NetAltinAra = "TCMB Net Altın Rezervi Ara (Bin TL)"
    each
        let varlik = BL002,
            bl132  = BL132,
            bl136  = BL136,
            bl089  = BL089,
            bl141e = BL141Etkin,
            yuk    = List.Sum(List.RemoveNulls({bl132, bl136, bl089, bl141e}))
        in if varlik = null then null else varlik - yuk

# 2) USD karşılığı
T_NetAltinUSD = "TCMB Net Altın Rezervi (Milyar USD)"
    each
        let ara = NetAltinAra,
            fx  = İmaEdilenUSDTL
        in if ara = null or fx = null or fx = 0 then null
           else (ara / 1000000) / fx
```

## Bileşenler

### Varlık (Pozitif)

- **TP.BL002**: Uluslararası Standartta Altın (Bin TL) — TCMB'nin sahip olduğu standart altın

### Yükümlülükler (Negatif)

- **TP.BL132**: Yurtiçi Banka Altın Teminat
- **TP.BL136**: Yurtiçi Banka Altın Depo / ROM
- **TP.BL089**: Altın Zorunlu Karşılıkları
- **BL141Etkin** (`derived:tcmb-bl141-etkin`): Yurtdışı Banka Altın Yükümlülük (gerçek/türetilmiş)

## Ekonomik Anlam

Net altın, TCMB'nin "asıl olarak sahip olduğu" altın stokudur. Brüt altın
(BL002 ya da TP.BL001) içinde bankaların ZK'sı ve teminatları da var; bunlar
serbest kullanılamaz. Net altın = brüt - yükümlülük.

## NIR ile İlişki

```
NIR (Milyar USD) = TCMB Net Altın Rezervi + TCMB Net Döviz Rezervi
```

Teyit kontrolü olarak |NetAltin + NetDoviz - NIR| ≤ 0.001 Milyar USD
beklenir. Pre-2018 tolerans: ~1.3 milyar USD farkı normal kabul edilir.

## Swap Hariç Versiyonu

Daha sonra altın swap'larını çıkararak SH Net Altın hesaplanır:
```
SH Net Altın = NetAltin - PDFAltinSwap (PDF varsa)
             = NetAltin + DigerSwapURDL (PDF yoksa, fallback)
```
Bkz. `derived:tcmb-swap-haric-net-altin`.
