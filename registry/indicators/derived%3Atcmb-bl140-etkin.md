---
record_type: indicator
id: derived:tcmb-bl140-etkin
title: TCMB Yurtdışı Banka Döviz Yükümlülük Etkin Değer
status: approved
input_ids:
- evds:TP.BL140
- evds:TP.BL097
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.BL002
- evds:TP.BL0021
formula_expression: 'IF(TP.BL140 != null, TP.BL140, IF(TP.BL097 > 100000 AND BL141Etkin != null, TP.BL097 - BL141Etkin, IF(TP.BL097 > 100000, TP.BL097, null)))'
formula_description: Gerçek BL140 öncelikli; yoksa BL097 - BL141Etkin türetilen; her ikisi de yoksa BL097 (placeholder filtreli); aksi null.
output_frequency: weekly
output_unit: Bin TL
economic_meaning: >
  Yurtdışı banka döviz yükümlülüğünün tutarlı izlenmesi için üç katmanlı
  fallback ile hesaplanan etkin değer. EVDS'de TP.BL140 boşken TP.BL097
  (toplam YP yükümlülük) - TP.BL141Etkin (altın yük.) ile türetilir. Pre-2018
  placeholder değerler (BL097 < 100K) filtrelenerek atlanır.
validation_note: >
  Pre-2018 dönemde TP.BL097 ~1000 Bin TL gibi placeholder değerler içerir;
  100,000 eşiği bu çöp veriyi filtreler. Üç katman da null verirse hesap null
  döner; Net Döviz formülünde bu durumda kalem yükümlülük toplamına 0 olarak girer.
theme_ids:
- theme:reserves
---
# TCMB Yurtdışı Banka Döviz Yükümlülük Etkin Değer

## Formül (3 Katmanlı Fallback)

```python
BL140Etkin = (
    TP.BL140                            if TP.BL140 != null
    else (TP.BL097 - BL141Etkin)        if TP.BL097 > 100,000 AND BL141Etkin != null
    else TP.BL097                        if TP.BL097 > 100,000
    else null                            # pre-2018 placeholder filtresi
)
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1470-1484):

```python
T_BL140Etkin = "Yurtdışı Banka Döviz Yükümlülük Etkin (Bin TL)"
    each
        let
            bl140  = BL140,
            bl097  = BL097,
            bl141e = BL141Etkin,
            bl097Ok = bl097 <> null and bl097 > 100000
        in
            if bl140 <> null then bl140
            else if bl097Ok and bl141e <> null then bl097 - bl141e
            else if bl097Ok then bl097
            else null
```

## Üç Fallback Katmanı

| Öncelik | Koşul | Değer | Yorum |
|---|---|---|---|
| 1 | BL140 dolu | BL140 | Gerçek veri |
| 2 | BL097 > 100K AND BL141Etkin var | BL097 - BL141Etkin | Toplam YP'den altın yük. düşülmüş |
| 3 | BL097 > 100K | BL097 | Sadece toplam YP (altın yük. yok varsayımı) |
| 4 | (hiçbiri) | null | Pre-2018 çöp / data eksik |

## Pre-2018 Placeholder Sorunu

EVDS'de pre-2018 dönemde TP.BL097 zaman zaman ~1,000 Bin TL (yaklaşık
100 milyon TL) gibi sembolik placeholder değerler içerir; gerçek değer
genellikle 100.000 Bin TL (100 milyar TL) üzerindedir. Bu nedenle:

```python
bl097Ok = BL097 != null and BL097 > 100,000
```

Bu eşik altındaki değerler **veri yok** olarak işlenir (null döner) ve
yük hesabında 0 gibi etki gösterir.

## Kullanım: Net Döviz Formülü

```
TCMB Net Döviz Rezervi Ara (Bin TL) =
    (BL003 + BL004 + BL008 + StandbyKalintisi) -
    (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140_Etkin + SDR + BL117 + BL118)
                                                  ↑
                                      Bu indicator burada
```

## BL097 Sembolik Bütünlük

```
BL097 (Toplam YP Yükümlülük) ≈ BL140 (Döviz) + BL141 (Altın)
```

İkinci fallback katmanı bu özdeşliği kullanarak BL140'ı türetir.
