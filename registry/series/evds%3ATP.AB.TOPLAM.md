---
record_type: series
id: evds:TP.AB.TOPLAM
title: Brüt Rezerv Toplamı (Milyon USD)
status: approved
source: evds
source_version: evds2
ticker: TP.AB.TOPLAM
frequency: weekly
unit: Milyon USD
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB brüt rezerv toplamının (Altın + Döviz)
  Milyon USD karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET.
  Resmi rezerv raporlamasının ana göstergesi; Excel'in "Brüt Rezerv
  (Milyar USD)" sütununun ana kaynağı. Tüm rezerv izleme analizlerinde
  birincil ölçüt.
usage: >
  Brüt Rezerv (Milyar USD) = TP.AB.TOPLAM / 1000
  Bütünlük: TP.AB.TOPLAM = TP.AB.C1 (Altın) + TP.AB.C2 (Döviz)
  Power Query: TcmbHaftalikRezerv sorgusunda doğrudan Milyar USD'ye çevrilir.
official_url: ''
theme_ids:
- theme:apko-summary
- theme:external-financing
- theme:banking-balance-sheet
- theme:reserves-and-liquidity
- theme:reserves
indicator_ids: []
---
# Brüt Rezerv Toplamı (Milyon USD)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.AB.TOPLAM
**Frekans:** Haftalık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

TCMB'nin resmi brüt rezervinin USD karşılığı. **Türkiye rezerv
analizinin ana göstergesi**; tüm "Türkiye'nin rezervi X milyar dolar"
şeklindeki ifadelerin dayanağıdır.

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1115):

```python
Series = "TP.AB.TOPLAM-..."  # "Brüt Rezerv (Milyon USD)"
```

Sonra (satır 1344-1346):
```python
T_BrutUSD = "Brüt Rezerv (Milyar USD)"
    each
        let x = "Brüt Rezerv (Milyon USD)"
        in if x = null then null else x / 1000
```

## Bütünlük Özdeşliği

```
TP.AB.TOPLAM = TP.AB.C1 + TP.AB.C2
[Brüt]         [Altın]    [Döviz]
```

EVDS bu üç seriyi doğrudan yayımladığı için bütünlük çapraz teyit
edilebilir.

## Excel "Özet" Sayfasında Yeri

"Özet" tablo 2'de **F sütunu "Brüt Rezerv"** ve sütun **D "Brüt Döviz
Rezervi" + E "Brüt Altın Rezervi"** birlikte bu seriden türeyen
günlük/haftalık/aylık/YBB değişim metriklerini gösterir.

## Brüt vs Net Farkı

```
Brüt Rezerv (TP.AB.TOPLAM)  → Tüm varlık (yükümlülük çıkarılmamış)
Net Uluslararası Rezerv (NIR, TP.AB.N06) → Yükümlülükler düşülmüş
SH Net Rezerv → NIR'dan swap'lar da çıkarılmış
```

Brüt rezerv miktar bilgisi verir, ama gerçek "TCMB'nin elindeki" kavramı
için net hesaplar gereklidir.

## Çoklu Tema Üyeliği

Bu seri çok geniş bir analiz kapsamına dahildir:
- **theme:reserves** (rezerv izleme)
- **theme:apko-summary** (APKO özet raporu)
- **theme:external-financing** (dış finansman analizi)
- **theme:banking-balance-sheet** (bankacılık bilanço)
- **theme:reserves-and-liquidity** (rezerv ve likidite)
