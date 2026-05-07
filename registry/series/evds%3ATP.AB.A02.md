---
record_type: series
id: evds:TP.AB.A02
title: Dış Varlıklar (Bin TL) — Analitik Bilanço A.1
status: approved
source: evds
source_version: evds2
ticker: TP.AB.A02
frequency: daily
unit: Bin TL
catalog_group: MERKEZ BANKASI ANALİTİK BİLANÇOSU
description: >
  TCMB analitik bilançosunun A.1 satırı — TCMB'nin dış varlıklar toplamı
  (Bin TL). Kaynak grubu: MERKEZ BANKASI ANALİTİK BİLANÇOSU. Günlük
  frekanstaki bu seri, haftalık vaziyet (TP.BL00X) yayınlanmadan önce
  rezerv hareketlerinin erken proxy göstergesidir. Günlük Bilanço Net
  Döviz Pozisyonu hesabının ana varlık kalemidir.
usage: >
  Dış Varlıklar (Milyar TL) = TP.AB.A02 / 1.000.000
  Dış Varlıklar (Milyar USD) = (TP.AB.A02 / 1.000.000) / TP.DK.USD.A.YTL
  Net Döviz Pozisyonu = TP.AB.A02 - TP.AB.A11 - TP.AB.A14 - TP.AB.A13
  Tahmini Net Rezerv  = TP.AB.A02 - TP.AB.A11 - TP.AB.A14
  Power Query: TcmbGunlukBilanco sorgusunda 5 ana seriden ilki.
official_url: ''
theme_ids:
- theme:reserves
- theme:banking-balance-sheet
- theme:net-reserve-estimate
indicator_ids:
- derived:tcmb-bilanco-net-doviz-pozisyonu
- derived:tcmb-bilanco-tahmini-net-rezerv
---
# Dış Varlıklar (Bin TL) — Analitik Bilanço A.1

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI ANALİTİK BİLANÇOSU
**Ticker:** TP.AB.A02
**Frekans:** Günlük (iş günü)
**Ham Birim:** Bin TL → ÷1.000.000 → Milyar TL

## Kullanım

TCMB analitik bilançosunun **varlık tarafının** ana kalemi:

```
A.1 Dış Varlıklar
  - Yabancı para aktif (döviz + altın)
  - Yurtdışı muhabir hesaplar
  - Uluslararası kuruluş varlıkları
  - Diğer dış varlıklar
```

## Power Query Karşılığı

`TcmbGunlukBilanco` M kodu (satır 468):

```python
Series = "TP.AB.A02-TP.AB.A11-TP.AB.A14-TP.AB.A13-TP.DK.USD.A.YTL"
# A02 → "Dış Varlıklar (Milyar TL)"
```

## Günlük Rezerv Tahmini

`TcmbGunlukBilanco_USD_Swap` (satır 611-619) Bin TL → Milyar USD'ye:

```python
Add_USD_1 = "Dış Varlıklar (Milyar USD)"
    each
        let k = USD/TL Kur,
            v = Dış Varlıklar (Milyar TL)
        in if k = null or v = null then null else v / k
```

## Türev Hesaplarda Yeri

Bu seri iki ana derived indicator'ın varlık tarafıdır:

```
Net Döviz Pozisyonu (`derived:tcmb-bilanco-net-doviz-pozisyonu`):
    = A02 - A11 - A14 - A13       (kamu mevduat dahil)

Tahmini Net Rezerv (`derived:tcmb-bilanco-tahmini-net-rezerv`):
    = A02 - A11 - A14              (kamu mevduat hariç)
```

## Haftalık Vaziyet ile İlişki

A02 (analitik bilanço, günlük) ≠ TP.BL001+003+004+008 toplamı
(haftalık vaziyet) çünkü:
- A02 daha geniş kapsam (tüm dış varlıklar)
- BL toplamı sadece çekirdek rezerv kalemleri

İki yol farklı amaçlar için: A02 günlük proxy, BL toplamı resmi rezerv.
