---
record_type: series
id: evds:TP.REZVARPD.K1
title: Resmi Rezerv Varlıkları (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.REZVARPD.K1
frequency: monthly
unit: Milyar USD
catalog_group: ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
description: >
  IMF SDDS standardına uygun yayınlanan URDL (Uluslararası Rezervler
  ve Döviz Likiditesi) tablosunun **aylık** versiyonu — TCMB'nin resmi
  rezerv varlıklarının toplamı. Kaynak grubu: ULUSLARARASI REZERVLER
  VE DÖVİZ LİKİDİTESİ. Haftalık frekansta TCMB sayfasından ZIP olarak
  yayımlanan veriye karşılık aylık geçmişe dönük zaman serisi sağlar.
usage: >
  TcmbAylıkRezerv_Altin_Swap sorgusunda haftalık veri eksikliklerinde
  fallback olarak kullanılır. Ham birim Milyon USD olduğu için ÷1000
  ile Milyar USD'ye çevrilir.
official_url: ''
theme_ids:
- theme:reserves
indicator_ids: []
---
# Resmi Rezerv Varlıkları (Milyar USD)

## Kaynak

**EVDS Grubu:** ULUSLARARASI REZERVLER VE DÖVİZ LİKİDİTESİ (URDL)
**Ticker:** TP.REZVARPD.K1
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

URDL tablosunun "I.A. Resmi rezerv varlıkları" kalemi. Toplam brüt
rezerv tutarını, IMF SDDS standartlarına uygun şekilde verir.

`TcmbAylıkRezerv_Altin_Swap` sorgusunda haftalık ZIP scrape başarısız
olduğunda veya geçmişe dönük analiz için fallback olarak kullanılır.

## EVDS Aylık vs TCMB Sayfası Haftalık

URDL verisi TCMB tarafından **iki farklı kanaldan** yayımlanır:

| Kanal | Frekans | Erişim |
|---|---|---|
| **TCMB sayfası ZIP** | Haftalık | Web scrape (TcmbHaftalikSwap sorgusu) |
| **EVDS API (TP.REZVARPD)** | Aylık | Bu seri |

Haftalık veriler güncel rezerv izleme için kritiktir, aylık seri ise
geçmişe dönük (15+ yıl) tutarlı zaman serisi sağlar. Bu projedeki
ana kullanım haftalık olduğundan TP.REZVARPD aylık serileri **fallback**
rolündedir.

## URDL TP.REZVARPD Serileri

K1-K11 aralığında 11 alt kalem yer alır:
- K1 (bu seri): Resmi Rezerv Varlıkları (toplam)
- K2: Döviz Varlıkları (MB alım/satım konusu)
- K3: Menkul Kıymetler
- K4: Toplam Nakit ve Mevduatlar
- K5: Diğer MB, BIS ve IMF
- K6: Merkezi Türkiye'de Olan Bankalar
- K7: Merkezi Türkiye'nin Dışında Olan Bankalar
- K8: IMF Rezerv Pozisyonu
- K9: SDR'lar
- K10: Resmi Altın Rezervleri
- K11: Saf Altın (Milyar Troy Ons)
