---
record_type: series
id: evds:TP.REZVARPD.K9
title: SDR'lar (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K9
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — Türkiye'nin sahip olduğu SDR (Özel Çekme Hakkı) tutarı
  Milyar USD karşılığı. Kaynak grubu: ULUSLARARASI REZERVLER VE DÖVİZ
  LİKİDİTESİ. URDL'de SDR varlık tarafında raporlanır; TP.BL099
  (SDR Tahsisatı) yükümlülük tarafıdır — ikisi farklı kavramlardır.
usage: >
  Aylık fallback olarak SDR rezerv izleme.
  Net SDR Pozisyonu = K9 (varlık) - BL099 (tahsisat yükümlülüğü)
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# SDR'lar (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K9
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'deki "I.A.1.d SDR'lar" kaleminin aylık değeri. Türkiye'nin
sahip olduğu SDR (Special Drawing Rights — Özel Çekme Hakkı)
tutarını gösterir. Bu varlık IMF nezdinde tutulur ve gerektiğinde
döviz kullanımı için tahvil edilebilir.

## SDR Varlık vs SDR Tahsisat (Yükümlülük)

İki farklı kavramı karıştırmamak gerekir:

| Kavram | Niteliği | Seri |
|---|---|---|
| **SDR'lar (varlık)** | Türkiye'nin SDR mevcudu | TP.REZVARPD.K9 |
| **SDR Tahsisatı (yükümlülük)** | IMF'in Türkiye'ye atadığı kümülatif tahsisat | TP.BL099 |

```
Net SDR Pozisyonu = K9 (Varlık) - BL099 (Yükümlülük)
```

## 2021 SDR Tahsisatı

IMF Ağustos 2021'de en büyük SDR tahsisatını gerçekleştirdi
(~650 milyar USD küresel). Türkiye yaklaşık 6.4 milyar USD ek
SDR aldı; bu hem K9 (varlık) hem BL099 (yükümlülük) tarafında
sıçramaya neden oldu.
