---
record_type: series
id: evds:TP.AB.A14
title: Bankalar Döviz Mevduatı (Bin TL) — Analitik Bilanço P.1bb
status: approved
source: evds
source_version: evds2
ticker: TP.AB.A14
frequency: daily
unit: Bin TL
catalog_group: MERKEZ BANKASI ANALİTİK BİLANÇOSU
description: >
  TCMB analitik bilançosunun P.1bb satırı — yurtiçi ve yurtdışı bankaların
  TCMB nezdinde tuttuğu döviz mevduat hesaplarının toplam Bin TL
  karşılığı. Kaynak grubu: MERKEZ BANKASI ANALİTİK BİLANÇOSU. Günlük
  frekanstaki bu seri, bankaların TCMB'deki döviz tutumlarını izler;
  Net Döviz Pozisyonu hesabında ana yükümlülük kalemlerinden biridir.
usage: >
  Bankalar Döviz Mevduatı (Milyar TL) = TP.AB.A14 / 1.000.000
  Bankalar Döviz Mevduatı (Milyar USD) = (TP.AB.A14 / 1.000.000) / TP.DK.USD.A.YTL
  Net Döviz Pozisyonu = TP.AB.A02 - TP.AB.A11 - TP.AB.A14 - TP.AB.A13
  Tahmini Net Rezerv  = TP.AB.A02 - TP.AB.A11 - TP.AB.A14
  Power Query: TcmbGunlukBilanco sorgusunda 3. ana seri.
official_url: ''
theme_ids:
- theme:reserves
- theme:banking-balance-sheet
- theme:net-reserve-estimate
indicator_ids:
- derived:tcmb-bilanco-net-doviz-pozisyonu
- derived:tcmb-bilanco-tahmini-net-rezerv
---
# Bankalar Döviz Mevduatı (Bin TL) — Analitik Bilanço P.1bb

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI ANALİTİK BİLANÇOSU
**Ticker:** TP.AB.A14
**Frekans:** Günlük (iş günü)
**Ham Birim:** Bin TL → ÷1.000.000 → Milyar TL

## Kullanım

TCMB'de bankaların tuttuğu tüm döviz cinsi mevduat hesaplarının günlük
toplam değeri:

```
P.1bb Bankalar Döviz Mevduatı
  - Döviz Zorunlu Karşılıklar (BL088 yaklaşık karşılığı)
  - Bankaların TCMB'deki serbest döviz mevduatları
  - Bankalararası swap/teminat döviz hesapları
  - Yurtiçi ve yurtdışı banka döviz mevduatları
```

## Power Query Karşılığı

`TcmbGunlukBilanco` M kodu (satır 468):

```python
Series = "TP.AB.A02-TP.AB.A11-TP.AB.A14-TP.AB.A13-TP.DK.USD.A.YTL"
# A14 → "Bankalar Döviz Mevduatı (Milyar TL)"
```

## Türev Hesaplarda Yeri

A14 hem **Net Döviz Pozisyonu** hem **Tahmini Net Rezerv** hesaplarında
yer alır (kamu mevduat A13'ten farklı olarak her iki yorumda da düşülür):

```
Net Döviz Pozisyonu = A02 - A11 - A14 - A13   ← A14 her iki versiyonda
Tahmini Net Rezerv  = A02 - A11 - A14         ← yer alır
```

## Haftalık Vaziyet ile İlişki

A14 (günlük), haftalık vaziyetin banka mevduat kalemlerinin toplamına
yaklaşık olarak denk gelir:

```
A14 ≈ TP.BL086 + TP.BL088 + TP.BL129 + TP.BL131 + (BL085 pre-2018)
```

Yani A14 hem yurtiçi (BL129/131 veya pre-2018 BL085) hem yurtdışı
(BL086) banka YP mevduatlarını + ZK'yı (BL088) içerir.

## Politika Önemi

Banka döviz mevduatları TCMB politika araçlarından doğrudan etkilenir:
- ZK oranı değişiklikleri → A14'te ani sıçramalar
- Banka swap anlaşmaları → kısa vadeli A14 hareketi
- Bankaların FX likidite ihtiyaçları → günlük volatilite

Bu yüzden A14 günlük volatilitesi rezerv tahmininde önemli bir gürültü
kaynağıdır; ay sonlarında ZK ayarlama günleri özellikle dikkat ister.
