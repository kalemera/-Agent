---
record_type: series
id: evds:TP.REZVARPD.K11
title: Saf Altın (Milyar Troy Ons)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K11
frequency: monthly
unit: Milyar Troy Ons
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  URDL aylık — TCMB'nin sahip olduğu saf altın miktarı (milyar troy ons
  cinsinden). Kaynak grubu: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ.
  Birim "Milyar Troy Ons" görünse de aslında bu IMF SDDS standardındaki
  fiziksel miktar gösterimidir (1 troy ons = 31.1034768 gram).
usage: >
  Aylık fallback olarak fiziksel altın miktarı izleme.
  Haftalık akraba: TP.BL0021 / 31.1034768 (Troy ons hesaplaması).
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Saf Altın (Milyar Troy Ons)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K11
**Frekans:** Aylık
**Ham Birim:** Milyar Troy Ons

## Kullanım

URDL'deki "I.A.2.a Saf altın (milyon troy ons)" kaleminin aylık değeri.
TCMB'nin sahip olduğu altının fiziksel miktarını verir; fiyat
dalgalanmalarından bağımsız bir miktar göstergesidir.

## Birim Notu

EVDS'de seri başlığı "Milyar Troy Ons" şeklinde görünse de pratikte
**Milyon Troy Ons** ölçeğinde değer döner. Bu IMF SDDS tablo gösterim
geleneğinden gelir; ÷1000 dönüşümü yapılırsa "Milyar troy ons"
oranıyla uyumlu hale gelir.

## Haftalık Vaziyet ile İlişki

Haftalık vaziyet tarafında saf altın miktarı **gram** cinsi olarak
TP.BL0021 üzerinden çekilir; troy ons karşılığı şu formülle bulunur:

```
Altın (Troy Ons) = TP.BL0021 / 31.1034768
```

K11 ile bu hesabın sonucu yakın değerler vermelidir (frekans farkından
kaynaklı küçük sapmalarla).

## Fiyat İzleme Amacı

K10 (USD karşılığı) / K11 (miktar) bölümü ile **uluslararası ons altın
fiyatı** dolaylı olarak elde edilebilir; tarihsel altın fiyatı serisinin
çapraz kontrolünde kullanılabilir.
