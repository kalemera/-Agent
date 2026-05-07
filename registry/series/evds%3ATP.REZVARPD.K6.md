---
record_type: series
id: evds:TP.REZVARPD.K6
title: Merkezi Türkiye'de Olan Bankalar (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K6
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB'nin merkezi Türkiye'de olan bankalar nezdinde
  tuttuğu döviz mevduatlarının Milyar USD karşılığı. Kaynak grubu:
  ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ. K4 (Toplam Nakit ve
  Mevduatlar) üç alt bileşeninden ikincisidir.
usage: >
  Aylık fallback olarak yurtiçi banka kaynaklı varlık izleme.
  K4 = K5 + K6 + K7 ilişkisinin alt kalemi.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Merkezi Türkiye'de Olan Bankalar (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K6
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'deki "I.A.1.b.ii Merkezi rapor eden ülkede yer alan bankalar"
alt kaleminin aylık değeri. TCMB'nin Türkiye'de faaliyet gösteren
bankalarda tuttuğu döviz hesaplarını gösterir.

## Yurtiçi Banka Mevduat Akrabası

Bu seri TCMB için **varlık** kalemidir (TCMB'nin yurtiçi bankalardaki
mevduatı). Bunun yükümlülük tarafındaki simetri ise haftalık vaziyet
serilerindeki **TP.BL129** (Yurtiçi Banka Döviz Depo) ve **TP.BL131**
(Yurtiçi Banka Döviz Teminat) kalemleridir — bunlar yurtiçi bankaların
TCMB'deki mevduat/teminatlarıdır (TCMB için yükümlülük).
