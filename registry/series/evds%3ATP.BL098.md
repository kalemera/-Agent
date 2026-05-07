---
record_type: series
id: evds:TP.BL098
title: IMF Rezerv Pozisyonu (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL098
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — Türkiye'nin IMF nezdindeki rezerv pozisyonunun
  TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. IMF
  rezerv pozisyonu, Türkiye'nin IMF kotasının ödenmiş döviz kısmıdır
  ve istenildiğinde geri çekilebilir; rezerv varlık niteliği taşır.
usage: >
  IMF Rezerv Pozisyonu (Milyar USD) = (TP.BL098 / 1,000,000) / İmaEdilenUSDTL
  Resmi rezerv kompozisyonu raporlamasında bağımsız bir kalemdir.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# IMF Rezerv Pozisyonu (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL098
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Türkiye'nin IMF nezdindeki rezerv pozisyonu. IMF üye ülke kotasının
döviz cinsi ödenmiş kısmıdır ve istenildiğinde çekilebilir; bu nedenle
rezerv **varlık** niteliği taşır.

```
IMF Rezerv Pozisyonu (Milyar USD) = (TP.BL098 / 1,000,000) / İmaEdilenUSDTL
```

## SDR ile Ayrım

| Seri | Niteliği | Net Hesaba Etkisi |
|---|---|---|
| **TP.BL098 (IMF Rezerv Pozisyonu)** | Varlık | Brüt rezerve dahil olabilir |
| **TP.BL099 (SDR Tahsisatı)** | Yükümlülük | Net döviz rezervinde düşülür |
| **TP.BL093 (Uluslararası Kuruluşlar)** | Yükümlülük (mevduat) | Net döviz rezervinde düşülür |

Bu üçü farklı kavramlardır ve rezerv hesabında farklı işlevlere sahiptir.

## URDL Aylık Eşleşmesi

URDL aylık fallback'teki **TP.REZVARPD.K8 "IMF Rezerv Pozisyonu
(Milyar USD)"** kalemiyle aynı kavramı temsil eder.
