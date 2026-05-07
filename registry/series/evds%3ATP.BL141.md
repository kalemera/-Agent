---
record_type: series
id: evds:TP.BL141
title: Yurtdışı Banka Altın Yükümlülük (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL141
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtdışı bankalara karşı altın yükümlülüklerin TL
  karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. EVDS'de bu
  seri tüm tarihler için dolu olmayabilir; TP.BL142 (gram cinsi) +
  İmaEdilenGramAltinTL üzerinden türetilen alternatif değer hazırlanır
  ve "Etkin" olarak gerçek değer öncelikli kullanılır.
usage: >
  Yurtdışı Banka Altın Yük. Türetilen (Bin TL) = TP.BL142 × İmaEdilenGramAltinTL / 1000
  Yurtdışı Banka Altın Yük. Etkin (Bin TL) = TP.BL141 if not null else Türetilen
  TCMB Net Altın Rezervi Ara = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + Etkin)
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtdışı Banka Altın Yükümlülük (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL141
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtdışı bankaların TCMB'de tuttuğu altın hesaplarının TL karşılığı.
TCMB Net Altın Rezervi formülünde yükümlülük tarafının dördüncü
bileşenidir.

## "Etkin" Mantığı (İki Yollu Türetme)

`TcmbHaftalikRezerv` M kodunda BL141 verisi her tarih için tam olmadığı
için **iki yollu** bir hesap kullanılır:

1. **Türetilen yol (gram bazlı):**
   ```
   Türetilen (Bin TL) = TP.BL142 (Safi Gram) × İmaEdilenGramAltinTL / 1000
   ```
2. **Etkin değer:**
   ```
   Etkin = if BL141 != null then BL141 else Türetilen
   ```

Bu yaklaşım, gerçek BL141 verisinin olduğu tarihlerde onu, olmadığı
tarihlerde gram cinsi BL142 ile fiyat çarpımı sonucu türetilen değeri
kullanmayı sağlar — böylece time series boşluksuz tamamlanır.

## Net Altın Formülünde Yeri

```
Net Altın Ara (Bin TL) = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + TP.BL141_Etkin)
```
