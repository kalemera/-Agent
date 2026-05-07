---
record_type: indicator
id: derived:tcmb-pdf-gunluk-altin-swap-net
title: TCMB Günlük Altın Swap Net Alım (PDF)
status: approved
input_ids:
- source:tcmb-tarafli-swap-pdf
formula_expression: ALTIN_TL_AlimYonlu_Stok - ALTIN_TL_SatimYonlu_Stok
formula_description: PDF'te altın TL swap kalemleri arasında alım yönlü stok eksi satım yönlü stok = altın net swap pozisyonu.
output_frequency: daily
output_unit: Milyar USD
economic_meaning: >
  TCMB'nin altın swap kanalındaki günlük net pozisyonu. PDF'te "altın TL alım
  yönlü stok" ve "altın TL satım yönlü stok" sütunları ayrı; ikisinin farkı
  altın swap net alımını verir. Swap Hariç Net Altın Rezervi formülünde
  kullanılır (PDF varsa Net Altın'dan çıkarılır).
validation_note: >
  PDF formatı değişirse altın swap matcher'ları (altin+tl+alim/satim+yonlu+stok)
  başarısız olabilir; bu durumda fallback olarak URDL II.3 kalemi
  (TP.DOVVARNC.K23) kullanılır. Pre-2021 dönemde PDF'te altın swap kalemi
  yok; bu tarihler için yalnızca URDL fallback geçerli.
theme_ids:
- theme:reserves
- theme:tcmb-swap
---
# TCMB Günlük Altın Swap Net Alım (PDF)

## Formül

```
Altın Net Alım = ALTIN_TL_AlimYönlü_Stok - ALTIN_TL_SatimYönlü_Stok
```

PDF'te sütun adlarında **{"altin", "tl ", "alim", "yonlu", "stok"}** ve
**{"altin", "tl ", "satim", "yonlu", "stok"}** anahtar kelimeleri ile aranır.

## Power Query Karşılığı

`TcmbTarafliSwapPdf_Table` M kodu (satır 2494-2533):

```python
AltinAlimCols  = ColHasAll(_, ["altin","tl ","alim","yonlu","stok"])
AltinSatimCols = ColHasAll(_, ["altin","tl ","satim","yonlu","stok"])

AltinAlimCol  = AltinAlimCols{0} or null
AltinSatimCol = AltinSatimCols{0} or null

# Null → 0 dönüşümü
AddNet_AltinNoNull = if _=null then 0 else _

AddAltinNet = Table.AddColumn(
    "Tcmb Günlük Altın Swap Net Alım (Milyar USD)",
    each
        let a = if AltinAlimCol = null then null else Record[AltinAlimCol],
            s = if AltinSatimCol = null then null else Record[AltinSatimCol]
        in if a = null or s = null then null else a - s
)
```

## PDF Altın Swap Kalemleri

İki ayrı kanal PDF'te altın swap içerir:

1. **TCMB TL Karşılığı Altın Swap Piyasası** (CBRT Tur işlemleri)
2. **TCMB Döviz Karşılığı Altın Swap Piyasası**

İkisi PDF tablosunda farklı sütunlardır; matcher en az birini bulur ve
"altın alım stok" / "altın satım stok" sütunlarını yakalar.

## Tarih Kapsamı

| Dönem | PDF Veri | Hesap |
|---|---|---|
| ≥ 2021 (yaklaşık) | Tüm altın swap kanalları PDF'te | Bu indicator çalışır |
| < 2021 | PDF'te altın swap kalemi yok | URDL fallback (TP.DOVVARNC.K23) |

## Kullanım: Swap Hariç Net Altın

```
SH Net Altın = NetAltin - PDFAltinSwap        # PDF varsa
             = NetAltin + DigerSwapURDL       # PDF yoksa (URDL II.3 fallback)
```

İşaret kuralı:
- PDF: pozitif → çıkarma
- URDL: negatif → toplama (her ikisi de aynı düzeltmeyi yapar farklı yönde)

## Bağlam: Altın Swap'ın Önemi

Altın swap özellikle 2021-2024 yıllarında yoğunlaştı: TCMB altın
karşılığında dolar swap yaparak rezerv düşüşünü "şişik" göstermiş gibi
algılanma riski yarattı. Bu yüzden altın swap'ı net altın rezervinden
çıkarmak şeffaflık için kritik.
