---
record_type: series
id: evds:TP.AB.N07
title: Brüt Rezerv Standby (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.AB.N07
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB'nin "Standby" tanımlı brüt rezervi. Kaynak
  grubu: MERKEZ BANKASI HAFTALIK VAZİYET. Bu seri, dört çekirdek
  bileşenin (BL001 + BL003 + BL004 + BL008) toplamından farklı bir
  toplam değer döndürür; aradaki fark "Brüt Döviz Rezerv Standby
  Kalıntısı" olarak Net Döviz Rezervi varlık tarafına eklenir.
usage: >
  Brüt Döviz Rezerv Standby Kalıntısı (Bin TL) = TP.AB.N07 - (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008)
  TCMB Net Döviz Rezervi Ara (Bin TL) = (TP.BL003 + TP.BL004 + TP.BL008 + StandbyKalintisi) - Yükümlülükler
  IMF/Standby tanımı ile haftalık vaziyetin dört bileşen toplamı arasındaki kapanış kalemini içerir.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Brüt Rezerv Standby (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.AB.N07
**Frekans:** Haftalık
**Ham Birim:** Bin TL → ÷1,000,000 → Milyar TL

## Kullanım

IMF Standby tanımına göre raporlanmış brüt rezerv. Power Query
`TcmbHaftalikRezerv` sorgusunda **standby kalıntısı** hesabı için
kullanılır:

```
Brüt Döviz Rezerv Standby Kalıntısı = TP.AB.N07 - (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008)
```

Bu kalıntı, dört çekirdek bileşenin toplamı ile resmi brüt rezerv
arasındaki farkı gösterir ve TCMB Net Döviz Rezervi'nin **varlık
tarafına** eklenir:

```
TCMB Net Döviz Rezervi Ara = (BL003 + BL004 + BL008 + StandbyKalintisi) - (Toplam Döviz Yükümlülükler)
```

## Kavramsal Not

Standby tanımı, EVDS'deki haftalık vaziyetin çekirdek dört kaleminden
biraz daha geniş olabilir (örn. dolaylı IMF taahhütleri, özel kalemler).
Bu seri o farkı kapsar; ham bileşenleri tek tek izlemek yerine resmi
toplam ile çekirdek toplam arasındaki köprüyü kurmak için kullanılır.
