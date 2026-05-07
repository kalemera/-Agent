---
record_type: series
id: evds:TP.DOVVARNC.K18
title: TCMB M.B. (Açık) Swap Büyüklüğü (Milyar USD)
status: approved
source: evds
source_version: evds2
ticker: TP.DOVVARNC.K18
frequency: monthly
unit: Milyar USD
catalog_group: DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
description: >
  TCMB Merkez Bankası kanalından gerçekleştirilen "açık" pozisyon swap
  stoku Milyar USD karşılığı. Kaynak grubu: DÖVİZ VARLIK VE YÜKÜMLÜLÜK
  TABLOSU. URDL II.2.a.iii kalemiyle eşleşir; M.B. swap stokunun açık
  (negatif/borçlu) bileşenini temsil eder. TP.DOVVARNC.K22 (Fazla) ile
  birlikte toplam M.B. swap büyüklüğünü oluşturur.
usage: >
  TCMB M.B. Swap Büyüklüğü (toplam) = K18 (Açık) + K22 (Fazla)
  Swap Hariç Net Döviz formülünde mbAdj olarak kullanılır.
official_url: ''
theme_ids:
- theme:reserves
- theme:tcmb-swap
indicator_ids: []
---
# TCMB M.B. (Açık) Swap Büyüklüğü (Milyar USD)

## Kaynak

**EVDS Grubu:** DÖVİZ VARLIK VE YÜKÜMLÜLÜK TABLOSU
**Ticker:** TP.DOVVARNC.K18
**Frekans:** Aylık
**Ham Birim:** Milyon USD → ÷1000 → Milyar USD

## Kullanım

TCMB Merkez Bankası kanalından kullanılan swap işlemlerinin "açık"
(net negatif pozisyon) bileşenidir. URDL'deki "II.2.a.iii Forward,
future ve swap pozisyonu" kaleminde açık (kısa) yönlü değerlere
karşılık gelir.

## TCMB M.B. Swap Hesabı

`TcmbAylıkRezerv_Altin_Swap` M kodunda toplam M.B. swap büyüklüğü
şöyle hesaplanır:

```python
# M kodu satır 1093:
TCMB M.B. Swap Büyüklüğü = TP.DOVVARNC.K18 (Açık) + TP.DOVVARNC.K22 (Fazla)
```

K18 ve K22 ham sütunları toplandıktan sonra çıktıdan **silinir**
(satır 1094) — sadece toplam M.B. Swap kalır.

## URDL Eşleşmesi

| Kalem | URDL Maddesi | Yön |
|---|---|---|
| **K18 (Açık)** | II.2.a.iii Forward/future/swap | Açık (kısa) |
| **K22 (Fazla)** | II.2.b.iii Forward/future/swap | Fazla (uzun) |

Haftalık dünyada `ContainsAllMatcher({"II.2.a.iii"})` matcher'ı ile
URDL ZIP içeriğinde aranır (M kodu satır 1709).

## Swap Hariç Net Döviz Formülünde Yeri

```
mbAdj = MB Döviz Swap = K18 + K22                # Toplam M.B. swap
Swap Hariç Net Döviz = NetDoviz + mbAdj - PDFFXSwap   (PDF varsa)
```

## Önceki Kayıt Düzeltmesi

Bu seri kaydı önceden hatalı bir semantik öneriyle ("2.2.1.3.Dört Ay
Bir Yıl Arası") oluşturulmuştu. v9 Excel Power Query M kodunun
incelenmesi sonrası gerçek tanımının "TCMB M.B. (Açık) Swap Büyüklüğü"
olduğu netleşmiş ve düzeltilmiştir.
