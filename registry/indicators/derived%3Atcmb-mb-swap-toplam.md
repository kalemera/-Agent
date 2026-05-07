---
record_type: indicator
id: derived:tcmb-mb-swap-toplam
title: TCMB Merkez Bankası Swap Toplam Büyüklüğü (URDL Aylık)
status: approved
input_ids:
- evds:TP.DOVVARNC.K18
- evds:TP.DOVVARNC.K22
formula_expression: TP.DOVVARNC.K18 + TP.DOVVARNC.K22
formula_description: URDL II.2.a (Açık) ve II.2.b (Fazla) yönlü M.B. swap pozisyonları toplamı.
output_frequency: monthly
output_unit: Milyar USD
economic_meaning: >
  TCMB Merkez Bankası kanalından kullanılan tüm swap pozisyonlarının toplam
  stoku. URDL'in II.2 (Forward, future ve swap pozisyonu) bölümündeki açık
  ve fazla yönlü kalemlerin toplamı. Net Döviz Rezervi'nden çıkarılarak Swap
  Hariç Net Döviz Rezervi elde etmek için kullanılır.
validation_note: >
  K18 + K22 ham sütunları toplandıktan sonra Excel'de orjinal iki sütun silinir
  (TcmbAylıkRezerv_Altin_Swap M kodu satır 1093-1094); sadece toplam M.B. Swap
  saklanır. URDL aylık seriden gelir; haftalık ZIP'te II.2.a.iii + II.2.b.iii
  matcher'ları ile haftalık karşılığı hesaplanır.
theme_ids:
- theme:reserves
- theme:tcmb-swap
---
# TCMB Merkez Bankası Swap Toplam Büyüklüğü (URDL Aylık)

## Formül

```
TCMB M.B. Swap Toplam = TP.DOVVARNC.K18 + TP.DOVVARNC.K22
                        [Açık yönlü]      [Fazla yönlü]
```

## Power Query Karşılığı

`TcmbAylıkRezerv_Altin_Swap` M kodu (satır 1093-1094):

```python
#"Added Custom" = Table.AddColumn(
    #"Swap Null Satırları Kaldır",
    "TCMB M.B. Swap Büyüklüğü (Milyar USD)",
    each [#"TCMB M.B. (Açık) Swap Büyüklüğü (Milyar USD)"]
       + [#"TCMB M.B. (Fazla) Swap Büyüklüğü (Milyar USD)"]
)

# Toplandıktan sonra ham sütunlar silinir
#"Removed Columns" = Table.RemoveColumns(#"Added Custom",
    {"TCMB M.B. (Açık) Swap Büyüklüğü (Milyar USD)",
     "TCMB M.B. (Fazla) Swap Büyüklüğü (Milyar USD)"}
)
```

## Haftalık Karşılığı

Haftalık dünyada bu hesap URDL ZIP'inden iki ayrı satır toplanarak yapılır:

```python
MB_Swap_Haftalik = ContainsAllMatcher({"II.2.a.iii"}) + ContainsAllMatcher({"II.2.b.iii"})
```

(M kodu satır 1707-1712)

## URDL Yapısı

```
II.2 Forward, future ve swap pozisyonu
  ├── II.2.a Açık (Short)
  │   └── II.2.a.iii ... → TP.DOVVARNC.K18
  └── II.2.b Fazla (Long)
      └── II.2.b.iii ... → TP.DOVVARNC.K22
```

## Kullanım: Swap Hariç Net Döviz

```
mbAdj = MBSwapToplam (URDL aylık veya haftalık)
SH Net Döviz = NetDoviz + mbAdj - PDFDovizSwap   (PDF varsa)
             = NetDoviz + mbAdj + (SwapTotURDL - mbAdj)  (URDL fallback)
```

İşaret kuralı: URDL'de net pozisyon NEGATİF gösterilir (rezervi şişirir),
o yüzden toplama (`+ mbAdj`) ile düzeltilir.
