---
record_type: series
id: evds:TP.BL003
title: Yabancı Para Banknotlar YP (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL003
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yabancı para banknot tutumu (fiziksel döviz nakit)
  TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. Brüt
  döviz rezervi içindeki fiziksel banknot bileşeni; URDL alternatif
  yolu (Brüt Rezerv = BL001+BL003+BL004+BL008) ve TCMB Net Döviz Rezervi
  formülü varlık tarafının üç bileşeninden biridir.
usage: >
  Yabancı Para Banknotlar (Milyar TL) = TP.BL003 / 1.000.000
  Brüt Rezerv (URDL alternatif) = (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008) / 1.000.000
  Döviz Rezervi (URDL) = (TP.BL003 + TP.BL004 + TP.BL008) / 1.000.000
  TCMB Net Döviz Varlık = TP.BL003 + TP.BL004 + TP.BL008 + StandbyKalintisi
  Power Query: TcmbHaftalikRezerv sorgusunda Milyar TL ve Net Döviz formüllerinde.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids:
- derived:tcmb-brut-rezerv-tl-urdl
- derived:tcmb-doviz-rezervi-tl-urdl
- derived:tcmb-standby-kalintisi
- derived:tcmb-net-doviz-rezervi
- derived:tcmb-swap-haric-net-doviz
- derived:tcmb-swap-haric-net-rezerv-gunluk
---
# Yabancı Para Banknotlar YP (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL003
**Frekans:** Haftalık
**Ham Birim:** Bin TL → ÷1,000,000 → Milyar TL

## Kullanım — Üç Ana Rol

### 1) URDL Alternatif Brüt Rezerv

```
Brüt Rezerv (URDL alt.) = TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008
                                       ↑
                         Bu seri burada
```

### 2) Standby Kalıntısı Hesabı

```
Standby Kalıntısı = TP.AB.N07 - (BL001 + BL003 + BL004 + BL008)
```

### 3) TCMB Net Döviz Rezervi Varlık Tarafı

```
Net Döviz Ara = (BL003 + BL004 + BL008 + StandbyKalintisi) - Yükümlülükler
                  ↑
        Burada Net Döviz varlık baz kalemi
```

## Ekonomik Anlam

TCMB'nin kasalarında veya muhabir bankaların güvenli kasalarında
fiziksel olarak tuttuğu döviz banknot stoku. En likit rezerv
bileşeni — anında kullanıma hazır.

## TP.AB.C2 ile İlişki

```
TP.AB.C2 (Brüt Döviz Rezervi USD)
    × USD/TL Kur
    ÷ 1000
≈ (TP.BL003 + TP.BL004 + TP.BL008) / 1.000.000   [Milyar TL]
```

İki yol birbirini doğrular; sapmalar fiyatlama zaman farkından kaynaklanır.
