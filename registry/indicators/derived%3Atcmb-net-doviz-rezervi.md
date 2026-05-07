---
record_type: indicator
id: derived:tcmb-net-doviz-rezervi
title: TCMB Net Döviz Rezervi (Milyar USD)
status: approved
input_ids:
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
- evds:TP.AB.N07
- evds:TP.BL085
- evds:TP.BL129
- evds:TP.BL131
- evds:TP.BL086
- evds:TP.BL088
- evds:TP.BL090
- evds:TP.BL092
- evds:TP.BL093
- evds:TP.BL140
- evds:TP.BL097
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.BL099
- evds:TP.BL117
- evds:TP.BL118
- evds:TP.BL001
- evds:TP.BL002
- evds:TP.AB.C1
- evds:TP.BL0021
formula_expression: '((Varlık_TL − Yükümlülük_TL) / 1000000) / İmaEdilenUSDTL'
formula_description: 'Varlık = BL003+BL004+BL008+StandbyKalintisi; Yükümlülük = yiBank+BL086+BL088+BL090+BL092+BL093+BL140Etkin+BL099+BL117+BL118; yiBank pre-2018 BL085, post-2018 BL129+BL131.'
output_frequency: weekly
output_unit: Milyar USD
economic_meaning: >
  TCMB'nin yükümlülüklerden arındırılmış net döviz rezervi USD karşılığı. Brüt
  döviz varlıkları + standby kalıntısından, yurtiçi/yurtdışı banka mevduatları,
  zorunlu karşılıklar, IMF ve diğer kalemler düşülür. NIR'ın altın olmayan
  bileşeni; rezerv kalitesinin ana göstergesi.
validation_note: >
  Pre-2018 (Tarih < 2018-08-31): yiBank için BL085 kullanılır (BL129+BL131
  ayrışmamış). Pre-2018 BL085 içinde altın teminat (BL132) da kısmen yer aldığı
  için teyit sütunu (NetAltin + NetDoviz - NIR) ~1.3 milyar USD sapma gösterebilir.
  Post-2018: yiBank = BL129 + BL131. Tüm bağımlılıklar aynı tarihte mevcut olmalı.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
---
# TCMB Net Döviz Rezervi (Milyar USD)

## Formül (En Karmaşık Hesap)

```
yiBank = if Tarih < 2018-08-31 then TP.BL085
         else (TP.BL129 + TP.BL131)

Varlık (Bin TL) = TP.BL003 + TP.BL004 + TP.BL008 + StandbyKalintisi

Yükümlülük (Bin TL) =
    yiBank
  + TP.BL086    # Yurtdışı Banka YP Mevduat
  + TP.BL088    # Döviz ZK
  + TP.BL090    # Diğer Döviz Mevduat
  + TP.BL092    # İşçi Dövizleri
  + TP.BL093    # Uluslararası Kuruluşlar
  + BL140Etkin  # Yurtdışı Banka Döviz Yük. (3-katmanlı fallback)
  + TP.BL099    # SDR Tahsisatı
  + TP.BL117    # Akreditifler
  + TP.BL118    # Alınan Krediler

Net Döviz Ara (Bin TL) = Varlık - Yükümlülük

Net Döviz (Milyar USD) = (Net Döviz Ara / 1.000.000) / İmaEdilenUSDTL
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1486-1533):

```python
T_NetDovizAra = "TCMB Net Döviz Rezervi Ara (Bin TL)"
    each
        let
            # Varlık
            bl003    = BL003, bl004 = BL004, bl008 = BL008,
            kalinti  = StandbyKalintisi,
            varlik   = List.Sum(List.RemoveNulls({bl003, bl004, bl008, kalinti})),

            # Yükümlülük (pre-2018 fallback)
            tarih_  = Tarih,
            yiBank  = if tarih_ < #date(2018, 8, 31)
                      then BL085
                      else List.Sum(List.RemoveNulls({BL129, BL131})),
            yuk = List.Sum(List.RemoveNulls({
                yiBank, BL086, BL088, BL090, BL092, BL093,
                BL140Etkin, BL099, BL117, BL118
            }))
        in
            if List.Count(varlikKalemler) = 0 then null
            else varlik - yuk

T_NetDovizUSD = ((NetDovizAra / 1000000) / İmaEdilenUSDTL)
```

## Tarih Kırılımı: Pre-2018 vs Post-2018

EVDS'de TP.BL129 (Yurtiçi Banka Döviz Depo) ve TP.BL131 (Yurtiçi Banka
Döviz Teminat) yaklaşık **2018-08-31** tarihinden itibaren ayrı seriler
olarak yayımlanmaya başladı. Öncesinde:

| Dönem | yiBank kalemi | Açıklama |
|---|---|---|
| Tarih < 2018-08-31 | TP.BL085 | Toplam tek kalemde |
| Tarih ≥ 2018-08-31 | TP.BL129 + TP.BL131 | Ayrışmış (depo + teminat) |

## Pre-2018 Teyit Sapma Toleransı

```
Teyit Farkı = NetAltin + NetDoviz - NIR
```

- Post-2018: |Fark| ≤ 0.001 Milyar USD beklenir
- Pre-2018: BL085 içinde altın teminat (BL132) kısmen karışık olduğu için
  ~1.3 milyar USD sapma normal; teyit flag null döner (M kod satır 2036-2038)

## Ekonomik Anlam

Net döviz, TCMB'nin yabancı para cinsi serbest tasarruflu rezervidir.
Bankaların TCMB'de tuttuğu döviz hesapları, ZK'lar, akreditifler vs.
TCMB'nin değil bankaların/sistemin parası. Bu kalemler düşüldüğünde
TCMB'nin kendi net döviz pozisyonu ortaya çıkar.

## NIR ile İlişki

```
NIR (Milyar USD) = TCMB Net Altın Rezervi + TCMB Net Döviz Rezervi
                                            ↑
                                  Bu indicator
```

## Swap Hariç Versiyonu

```
SH Net Döviz = NetDoviz + MBSwapURDL - PDFFXSwap (PDF varsa)
             = NetDoviz + MBSwapURDL + (SwapTotURDL - MBSwapURDL) (URDL fallback)
```
Bkz. `derived:tcmb-swap-haric-net-doviz`.
