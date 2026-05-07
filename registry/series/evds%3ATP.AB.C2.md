---
record_type: series
id: evds:TP.AB.C2
title: Brüt Döviz Rezervi (Milyon USD)
status: approved
source: evds
source_version: evds2
ticker: TP.AB.C2
frequency: weekly
unit: Milyon USD
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB brüt döviz rezervinin Milyon USD karşılığı
  (altın hariç). Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET.
  TP.AB.TOPLAM (Brüt Toplam Rezerv) = TP.AB.C1 (Altın) + TP.AB.C2 (Döviz)
  özdeşliğinin döviz bileşeni. Brüt rezerv kompozisyonunun ana döviz
  kısmını verir; haftalık vaziyet türev hesaplarının birim teyidi
  ve TL bileşenleriyle (BL003+BL004+BL008) karşılaştırma için kullanılır.
usage: >
  Brüt Döviz Rezervi (Milyar USD) = TP.AB.C2 / 1000
  Birim Teyidi: TP.AB.TOPLAM ≈ TP.AB.C1 + TP.AB.C2
  TL Karşılığı Teyidi: TP.AB.C2 × kur ≈ (TP.BL003 + TP.BL004 + TP.BL008) / 1000
  Power Query: TcmbHaftalikRezerv sorgusunda Milyar USD'ye çevrilir.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Brüt Döviz Rezervi (Milyon USD)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.AB.C2
**Frekans:** Haftalık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

TCMB'nin altın hariç brüt döviz stokunun USD karşılığı. URDL'in
I.A.1 (Döviz varlıkları) kalemine denk gelir; menkul kıymetler,
mevduatlar ve banknotlar dahil tüm döviz varlık toplamını içerir.

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1117):

```python
Series = "...-TP.AB.C2-..."  # "Döviz Rezervi (Milyon USD)"
```

Sonra (satır 1352-1354):
```python
T_DovizUSD = "Döviz Rezervi (Milyar USD)"
    each
        let x = "Döviz Rezervi (Milyon USD)"
        in if x = null then null else x / 1000
```

## TP.AB.TOPLAM ile Bütünlük

```
TP.AB.TOPLAM = TP.AB.C1 + TP.AB.C2
[Brüt Toplam]   [Altın]    [Döviz]
```

Bu üçlü EVDS'den doğrudan çekildiğinde özdeşlik tutmalı; sapmalar
veri tutarsızlığına işaret eder.

## TL Karşılığı ile Çapraz Doğrulama

```
TP.AB.C2 × USD/TL_Kur ≈ (TP.BL003 + TP.BL004 + TP.BL008) / 1000  [Milyar TL]
[Milyon USD]            [Bin TL toplam]                            [Milyar TL]
```

İki yol birbirini doğrular; ufak sapmalar TCMB değerleme zaman
farkından (özellikle ay sonlarında) kaynaklanır.

## Akraba Seriler

| Seri | Birim | Frekans | Açıklama |
|---|---|---|---|
| **TP.AB.C2** | Milyon USD | Haftalık | Brüt döviz, USD doğrudan |
| **TP.BL003+BL004+BL008** | Bin TL | Haftalık | TL bileşen toplamı |
| **TP.REZVARPD.K2** | Milyar USD | Aylık | URDL "Döviz Varlıkları" |
