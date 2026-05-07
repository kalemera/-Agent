---
record_type: series
id: evds:TP.BL004
title: Yurtdışı Banka Toplam YP Varlık (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL004
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB'nin yurtdışı bankalardaki toplam yabancı para
  varlıkları (mevduat + nostro hesapları) TL cinsinden. Kaynak grubu:
  MERKEZ BANKASI HAFTALIK VAZİYET. Brüt döviz rezervinin en büyük
  bileşenlerinden biri; URDL'deki "I.A.1 Döviz varlıkları" kaleminin TL
  karşılığı için temel girdi.
usage: >
  Brüt Rezerv (Milyar TL, URDL) = (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008) / 1,000,000
  Döviz Rezervi (Milyar TL) = (TP.BL003 + TP.BL004 + TP.BL008) / 1,000,000
  Brüt Döviz Standby Kalıntısı (Bin TL) = TP.AB.N07 - (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008)
  TCMB Net Döviz Rezervi varlık tarafının çekirdek kalemi.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtdışı Banka Toplam YP Varlık (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL004
**Frekans:** Haftalık
**Ham Birim:** Bin TL → ÷1,000,000 → Milyar TL

## Kullanım

TCMB'nin yurtdışı muhabir bankalardaki toplam YP varlığı. Power Query
`TcmbHaftalikRezerv` sorgusunda **Brüt Rezerv (URDL alternatif yolu)**
formülünün ana bileşenlerinden biri:

```
Brüt Rezerv = TP.BL001 (Altın) + TP.BL003 (Banknot) + TP.BL004 (Yurtdışı YP Varlık) + TP.BL008 (Döviz Menkul Kıymet)
```

Bu yol, TCMB'nin URDL haftalık ZIP yayınına alternatif olarak
**EVDS API üzerinden** brüt rezerv kompozisyonunu doğrudan üretir.
TCMB Net Döviz Rezervi formülünde de varlık tarafının ana kalemidir.
