---
record_type: series
id: evds:TP.AB.A11
title: Dış Yükümlülükler (Bin TL) — Analitik Bilanço P.1a
status: approved
source: evds
source_version: evds2
ticker: TP.AB.A11
frequency: daily
unit: Bin TL
catalog_group: MERKEZ BANKASI ANALİTİK BİLANÇOSU
description: >
  TCMB analitik bilançosunun P.1a satırı — TCMB'nin dış yükümlülükleri
  (yurtdışına karşı borç ve mevduat) Bin TL. Kaynak grubu: MERKEZ
  BANKASI ANALİTİK BİLANÇOSU. Günlük frekanstaki bu seri, dış borç ve
  yurtdışı banka mevduat yükümlülüklerini içerir; günlük rezerv tahmin
  hesabında varlık tarafından düşülen ilk yükümlülük kalemidir.
usage: >
  Dış Yükümlülükler (Milyar TL) = TP.AB.A11 / 1.000.000
  Dış Yükümlülükler (Milyar USD) = (TP.AB.A11 / 1.000.000) / TP.DK.USD.A.YTL
  Net Döviz Pozisyonu = TP.AB.A02 - TP.AB.A11 - TP.AB.A14 - TP.AB.A13
  Power Query: TcmbGunlukBilanco sorgusunda 2. ana seri.
official_url: ''
theme_ids:
- theme:reserves
- theme:banking-balance-sheet
- theme:net-reserve-estimate
indicator_ids:
- derived:tcmb-bilanco-net-doviz-pozisyonu
- derived:tcmb-bilanco-tahmini-net-rezerv
---
# Dış Yükümlülükler (Bin TL) — Analitik Bilanço P.1a

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI ANALİTİK BİLANÇOSU
**Ticker:** TP.AB.A11
**Frekans:** Günlük (iş günü)
**Ham Birim:** Bin TL → ÷1.000.000 → Milyar TL

## Kullanım

TCMB'nin yurtdışına karşı tüm yabancı para yükümlülüklerini içerir:

```
P.1a Dış Yükümlülükler
  - Yurtdışı banka mevduatları (TCMB nezdinde)
  - Uluslararası kurum yükümlülükleri (IMF, BIS, vb.)
  - Dış borç (alınan krediler, akreditifler)
  - SDR Tahsisatı yükümlülüğü
```

## Power Query Karşılığı

`TcmbGunlukBilanco` M kodu (satır 468):

```python
Series = "TP.AB.A02-TP.AB.A11-TP.AB.A14-TP.AB.A13-TP.DK.USD.A.YTL"
# A11 → "Dış Yükümlülükler (Milyar TL)"
```

## Türev Hesaplarda Yeri

```
Net Döviz Pozisyonu = A02 - A11 - A14 - A13
                          ↑
                 Bu seri yükümlülük olarak çıkarılır

Tahmini Net Rezerv = A02 - A11 - A14
```

## Haftalık Vaziyet ile İlişki

A11 (günlük) yaklaşık olarak haftalık vaziyetin yurtdışı banka ve
uluslararası kurum yükümlülük kalemlerinin toplamına denk gelir:

```
A11 ≈ TP.BL086 + TP.BL093 + TP.BL097 + TP.BL099 + TP.BL117 + TP.BL118
       (banka)  (uluslar.) (toplam)   (SDR)     (akredit) (kredi)
```

Tam eşitlik değil — kapsam farklılıkları var. A11 günlük rezerv
yönü tahmininde proxy, BL kalemleri Net Döviz Rezervi formülünde
detaylı yükümlülük analizi için.
