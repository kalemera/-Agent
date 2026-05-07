---
record_type: series
id: evds:TP.REZVARPD.K7
title: Merkezi Türkiye'nin Dışında Olan Bankalar (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K7
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB'nin yurtdışı bankalarda tuttuğu döviz
  mevduatlarının Milyar USD karşılığı. Kaynak grubu: ULUSLARARASI
  REZERVLER VE DÖVİZ LİKİDİTESİ. K4 (Toplam Nakit ve Mevduatlar)
  üç alt bileşeninden üçüncüsüdür ve genellikle en büyük olanıdır.
usage: >
  Aylık fallback olarak yurtdışı banka mevduat varlıkları izleme.
  TP.BL004 (haftalık Yurtdışı Banka Toplam YP Varlık) ile akraba.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Merkezi Türkiye'nin Dışında Olan Bankalar (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K7
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL'deki "I.A.1.b.iii Merkezi rapor eden ülke dışında yer alan
bankalar" alt kaleminin aylık değeri. TCMB'nin yurtdışı muhabir
bankalardaki nostro hesapları ve mevduatlarını gösterir.

## Haftalık Vaziyet Akrabası

Bu seri **TP.BL004 (Yurtdışı Banka Toplam YP Varlık)** haftalık
serisinin USD karşılığıdır. İkisi neredeyse aynı kavramı temsil eder
fakat farklı kanaldan gelir:

| Seri | Frekans | Birim | Kaynak |
|---|---|---|---|
| **TP.REZVARPD.K7** | Aylık | Milyar USD | URDL EVDS API |
| **TP.BL004** | Haftalık | Bin TL | Haftalık Vaziyet EVDS API |

K4 = K5 + K6 + K7 alt toplamlarda K7 genellikle en büyük kalemdir;
TCMB rezerv yönetiminin önemli bir kısmı yurtdışı muhabir bankalarda
tutulur.
