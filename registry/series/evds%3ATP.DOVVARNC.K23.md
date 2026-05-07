---
record_type: series
id: evds:TP.DOVVARNC.K23
title: TCMB Diğer Swaplar Büyüklüğü (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.DOVVARNC.K23
frequency: monthly
unit: Milyar USD
catalog_group: DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
description: >
  TCMB'nin Merkez Bankası kanalı dışındaki diğer swap stoklarının aylık
  Milyar USD karşılığı (BIST swap, taraflı swap, altın swap, vb.).
  Kaynak grubu: DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU. URDL'deki "II.3
  Diğer" kalemine karşılık gelir; non-MB swap stokunu temsil eder.
usage: >
  Swap Hariç Net Altın hesabında PDF (TcmbTarafliSwapPdf_Table) verisi
  yoksa fallback olarak kullanılır:
  Swap Hariç Net Altın = NetAltin + TP.DOVVARNC.K23 (URDL Diğer)
official_url: ''
theme_ids:
- theme:reserves
- theme:tcmb-swap
indicator_ids: []
---
# TCMB Diğer Swaplar Büyüklüğü (Milyar USD)

## Kaynak

**EVDS Grubu:** DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
**Ticker:** TP.DOVVARNC.K23
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

TCMB'nin Merkez Bankası swap kanalı dışındaki tüm diğer swap
stoklarını içerir:
- BIST üzerinden döviz/TL swap işlemleri
- TCMB Taraflı Swap işlemleri (yurtdışı muhabir bankalarla)
- Altın swap işlemleri (TL karşılığı altın swap)
- Diğer swap pozisyonları

URDL'deki "II.3. Diğer" kalemine karşılık gelir.

## Swap Hariç Net Altın Formülünde Kritik Rolü

`TcmbHaftalikRezerv` M kodunda Swap Hariç Net Altın hesabı **iki yollu**
yapılır:

```python
Swap Hariç Net Altın = (
    NetAltin - PDFAltinSwap                  if PDF varsa (2021+)
    NetAltin + TP.DOVVARNC.K23 (URDL Diğer)  if PDF yoksa (pre-2021 fallback)
)
```

**İşaret kuralı:** URDL'deki K23 değeri net swap stokunu **negatif**
gösterir (rezervi şişik gösterir), bu yüzden toplama (`+ K23`) ile
gerçek net altın hesabına geri dönülür.

## Haftalık ZIP Eşleşmesi

Haftalık URDL ZIP'inde bu kalem **`ExactMatcher("II.3. Diğer")`** ile
yakalanır (M kodu satır 1747).

## Excel'deki "TCMB Diğer Swaplar Büyüklüğü"

`TcmbAylıkRezerv_Altin_Swap` çıktısında **"TCMB Diğer Swaplar Büyüklüğü
(Milyar USD)"** sütunu doğrudan bu seriden gelir.
