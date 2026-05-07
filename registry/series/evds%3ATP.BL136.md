---
record_type: series
id: evds:TP.BL136
title: Yurtiçi Banka Altın Depo ROM (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.BL136
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — yurtiçi bankaların TCMB'de tuttuğu altın depo
  hesapları (Rezerv Opsiyonu Mekanizması — ROM kapsamı dahil) TL
  karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET. TCMB Net
  Altın Rezervi formülünde altın yükümlülüklerinin bir bileşenidir.
usage: >
  TCMB Net Altın Rezervi Ara (Bin TL) =
    TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + TP.BL141Etkin)
  Yurtiçi banka altın depo / ROM yükümlülüklerini temsil eder.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Yurtiçi Banka Altın Depo ROM (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.BL136
**Frekans:** Haftalık
**Ham Birim:** Bin TL

## Kullanım

Yurtiçi bankaların TCMB'de tuttuğu altın depo hesapları. Rezerv Opsiyonu
Mekanizması (ROM) kapsamında bankaların TL zorunlu karşılıklarının bir
bölümünü altın olarak tutma hakkını içerir. TCMB için yükümlülük
niteliğindedir.

`TcmbHaftalikRezerv` sorgusunda **TCMB Net Altın Rezervi** formülünde:

```
Net Altın Ara = TP.BL002 - (TP.BL132 + TP.BL136 + TP.BL089 + TP.BL141Etkin)
                                          ↑
                                   Bu seri burada yer alır
```

## ROM Kavramı

Rezerv Opsiyonu Mekanizması, TCMB'nin 2011-2014 arasında aktif kullandığı
bir araçtır; bankalar TL zorunlu karşılıklarının belirli bir oranını
döviz veya altın olarak tutabilirler. ROM oranlarındaki değişiklikler
bu seriye yansır.
