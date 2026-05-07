---
record_type: indicator
id: derived:tcmb-pdf-gunluk-swap-net
title: TCMB Günlük Swap Net Alım (PDF, Toplam)
status: approved
input_ids:
- source:tcmb-tarafli-swap-pdf
formula_expression: TOPLAM_STOK_AlimYonlu - TOPLAM_STOK_SatimYonlu
formula_description: TCMB Taraflı Swap PDF'inden toplam alım yönlü stok eksi toplam satım yönlü stok = günlük net swap pozisyonu.
output_frequency: daily
output_unit: Milyar USD
economic_meaning: >
  TCMB'nin tüm swap kanallarındaki günlük net swap pozisyonu. PDF'te alım
  yönlü ve satım yönlü stoklar ayrı sütunlarda raporlanır; net = alım - satım.
  Pozitif değer TCMB'nin döviz aldığını (TL verdiğini), negatif değer döviz
  verdiğini gösterir. Swap Hariç Net Döviz formülünde kullanılır.
validation_note: >
  PDF'te tüm rakamlar Milyon USD; M kod ÷1000 ile Milyar USD'ye çevirir.
  Alım/satım sütunları null ise 0 olarak işlenir (M kod satır 2462-2471).
  20.03.2026 manifest hatası: PDF'te eksik, 19.03.2026 verisi kopyalanır.
  PDF formatı değişirse "TOPLAM+STOK+ALIM+YÖNLÜ" matcher başarısız olabilir.
theme_ids:
- theme:reserves
- theme:tcmb-swap
---
# TCMB Günlük Swap Net Alım (PDF, Toplam)

## Formül

```
Net Alım (Milyar USD) = TOPLAM_STOK_AlımYönlü - TOPLAM_STOK_SatımYönlü
```

PDF içinde sütun adlarında "toplam + stok + alım + yönlü" ve
"toplam + stok + satım + yönlü" anahtar kelimeleri ile aranır.

## Power Query Karşılığı

`TcmbTarafliSwapPdf_Table` M kodu (satır 2442-2488):

```python
ColHasAll = (cn, words) => normalize ve all keyword içermeli

AlimCols  = List.Select(AllNumCols, ColHasAll(_, ["toplam","stok","alim","yonlu"]))
SatimCols = List.Select(AllNumCols, ColHasAll(_, ["toplam","stok","satim","yonlu"]))

AlimCol = AlimCols{0}
SatimCol = SatimCols{0}

# Null → 0 dönüşümü
ToBillion_NoNull = Table.TransformColumns(
    ColsToZero, c => if _ = null then 0 else _
)

AddNet = Table.AddColumn(
    "Tcmb Günlük Swap Net Alım (Milyar USD)",
    each
        let a = Record[AlimCol], s = Record[SatimCol]
        in if a = null or s = null then null else a - s
)
```

## PDF İçindeki Tüm Swap Kalemler

PDF "TOPLAM" sütununda tüm swap kanalları kümüle edilir:
- TCMB Döviz Karşılığı TL Swap Piyasası
- BIST Swap Piyasası
- TCMB TL Karşılığı Altın Swap Piyasası (CBRT Tur)
- TCMB Döviz Karşılığı TL Swap Geleneksel İhaleleri
- TCMB Döviz Karşılığı TL Swap Miktar İhaleleri
- TCMB Altın Karşılığı TL Swap Geleneksel İhaleleri
- TCMB Döviz Karşılığı Altın Swap Piyasası

## İşaret Kuralı

| Yön | Kaynak | Net İşaret | Yorum |
|---|---|---|---|
| **Alım** | TCMB döviz aldı, TL verdi | + | TCMB döviz alacaklı |
| **Satım** | TCMB TL aldı, döviz verdi | − | TCMB döviz borçlu |
| **Net** | Alım − Satım | − pozitif (alacaklı) | Net alacak pozisyon |

PDF'te değer **POZİTİF** çıkar genellikle (TCMB net alacaklı pozisyonda).
Bu yüzden Swap Hariç Net Döviz formülünde **çıkarılır**:

```
SH Net Döviz = NetDoviz + mbAdj - PDFNetSwap
                                  ↑ pozitif çıkarma
```

(URDL'in negatif gösterdiğinin tersi yönde)

## Tarih Patch

20.03.2026 PDF'te yok → 19.03.2026 satırı kopyalanır, tarihi değiştirilir
(M kodu satır 2536-2558). Python port'ta dinamik eksik-tarih tespitiyle
değiştirilmeli.
