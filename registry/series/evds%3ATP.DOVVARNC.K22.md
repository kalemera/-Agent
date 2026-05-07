---
record_type: series
id: evds:TP.DOVVARNC.K22
title: TCMB M.B. (Fazla) Swap Büyüklüğü (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.DOVVARNC.K22
frequency: monthly
unit: Milyar USD
catalog_group: DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
description: >
  TCMB Merkez Bankası kanalından gerçekleştirilen "fazla" pozisyon
  swap stoku Milyar USD karşılığı. Kaynak grubu: DÖVİZ VARLIK VE
  YÜKÜMLÜLÜK TABLOSU. URDL II.2.b.iii kalemiyle eşleşir; M.B. swap
  stokunun pozitif (fazla) bileşenini temsil eder.
usage: >
  TCMB M.B. Swap Büyüklüğü (toplam) = K18 (Açık) + K22 (Fazla)
  TcmbAylıkRezerv_Altin_Swap sorgusunda bu hesap M kodunda yapılır.
official_url: ''
theme_ids:
- theme:reserves
- theme:tcmb-swap
indicator_ids: []
---
# TCMB M.B. (Fazla) Swap Büyüklüğü (Milyar USD)

## Kaynak

**EVDS Grubu:** DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
**Ticker:** TP.DOVVARNC.K22
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

TCMB Merkez Bankası kanalından kullanılan swap işlemlerinin "fazla"
(net pozitif pozisyon) bileşenidir. URDL'deki "II.2.b.iii Forward,
future ve swap pozisyonu" kaleminde fazla yönlü değerlere karşılık
gelir.

## TCMB M.B. Swap Hesabı

`TcmbAylıkRezerv_Altin_Swap` M kodunda toplam M.B. swap büyüklüğü
şöyle hesaplanır:

```python
# M kodu satır 1093:
TCMB M.B. Swap Büyüklüğü = TP.DOVVARNC.K18 (Açık) + TP.DOVVARNC.K22 (Fazla)
```

Daha sonra K18 ve K22 ham sütunları bilanço çıktısından **silinir**
(satır 1094) — sadece toplam M.B. Swap kalır.

## URDL Eşleşmesi

| Kalem | URDL Maddesi |
|---|---|
| **K18 (Açık)** | II.2.a.iii Forward/future/swap (açık) |
| **K22 (Fazla)** | II.2.b.iii Forward/future/swap (fazla) |
| **Toplam M.B. Swap** | K18 + K22 = II.2 toplamı |

Haftalık dünyada bu eşleşme `ContainsAllMatcher({"II.2.a.iii"})` ve
`ContainsAllMatcher({"II.2.b.iii"})` ile aranır (M kodu satır 1707-1712).

## Swap Hariç Net Döviz Formülünde Yeri

```
mbAdj = MB Döviz Swap (Toplam)             # K18 + K22 toplamı
Swap Hariç Net Döviz = NetDoviz + mbAdj - PDFFXSwap (PDF varsa)
```

İşaret kuralı: URDL'den gelen değerler net alımı NEGATİF gösterir
(rezerv şişikliği için), bu yüzden toplama (`+ mbAdj`) ile düzeltme
yapılır.
