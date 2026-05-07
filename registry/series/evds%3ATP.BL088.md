---
record_type: series
id: evds:TP.BL088
title: Döviz Zorunlu Karşılıkları (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL088
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — bankaların TCMB'de tuttuğu döviz cinsi zorunlu
  karşılıkların TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK
  VAZİYET. TCMB için yükümlülük; Net Döviz Rezervi formülünde döviz
  ZK kalemini temsil eder.
usage: >
  TCMB Net Döviz Rezervi Ara = (Varlıklar) - (... + TP.BL088 + ...)
  Döviz zorunlu karşılık yükümlülüklerini temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Döviz Zorunlu Karşılıkları (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL088
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Bankaların TCMB nezdinde tuttuğu döviz cinsi zorunlu karşılıklar.
TP.BL089 (Altın ZK) ile simetrik bir yapıdadır; Net Döviz Rezervi
formülünde yükümlülük tarafının ana kalemlerinden biridir.

## Net Döviz Formülünde Yeri

```
Net Döviz Ara = (Varlıklar) - (yiBank + BL086 + TP.BL088 + BL090 + BL092 + BL093 + BL140Etkin + SDR + BL117 + BL118)
```

## Politika Değişimine Duyarlılık

Döviz ZK oranları TCMB tarafından sıkça revize edilen bir politika
aracıdır. Bu seri, ZK oranı değişikliklerine doğrudan tepki verir
ve Net Döviz Rezervi'nde sapmalara neden olabilir.
