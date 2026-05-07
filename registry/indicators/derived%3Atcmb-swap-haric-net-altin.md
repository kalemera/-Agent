---
record_type: indicator
id: derived:tcmb-swap-haric-net-altin
title: TCMB Swap Hariç Net Altın Rezervi (Milyar USD)
status: approved
input_ids:
- evds:TP.BL002
- evds:TP.BL132
- evds:TP.BL136
- evds:TP.BL089
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.BL001
- evds:TP.AB.C1
- evds:TP.BL0021
- source:tcmb-tarafli-swap-pdf
- evds:TP.DOVVARNC.K23
formula_expression: 'IF(PDFAltinSwap != null, NetAltinRezervi − PDFAltinSwap, NetAltinRezervi + DigerSwapURDL)'
formula_description: PDF (TcmbTarafliSwap) günlük altın swap'ı varsa net altından çıkarır; yoksa URDL II.3 (Diğer Swap) ile toplar (URDL negatif).
output_frequency: weekly
output_unit: Milyar USD
economic_meaning: >
  Altın swap pozisyonlarından arındırılmış net altın rezervi. TCMB altın
  swap yaparak rezerv düşüşünü gizleyebileceği için, altın swap'ları net
  altından çıkarmak gerçek altın rezervinin daha şeffaf bir göstergesini verir.
  PDF (günlük detay) öncelikli; PDF olmadığı pre-2021 tarihlerde URDL aylık
  fallback kullanılır.
validation_note: >
  İşaret kuralı kritik. PDF altın swap pozitif çıkar (TCMB net alacaklı), o yüzden
  Net Altın'dan çıkarılır. URDL II.3 negatif olarak gelir (rezervi şişirici), o yüzden
  toplama yapılır. İki yol kavramsal olarak aynı düzeltmeyi yapar farklı işaret yönünden.
  PDF data integrity (manifest hatası tarih patch'i) bu hesaba doğrudan etkili.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
- theme:tcmb-swap
---
# TCMB Swap Hariç Net Altın Rezervi (Milyar USD)

## Formül (İki Yollu)

```python
SH Net Altın = (
    NetAltinRezervi - PDFAltinSwapNet         if PDFAltinSwapNet != null
    NetAltinRezervi + DigerSwapURDL_K23       if PDFAltinSwapNet == null  (fallback)
    NetAltinRezervi                            if her ikisi de null
)
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1948-1960):

```python
WithSwapHaricAltin = "Swap Hariç Net Altın Rezervi (Milyar USD)"
    each
        let
            netAltin = TCMB Net Altın Rezervi,
            goldPdf  = Tcmb Günlük Altın Swap Net Alım (PDF),
            goldUrdl = Diğer Swap Büyüklüğü (URDL II.3 / TP.DOVVARNC.K23)
        in
            if netAltin = null then null
            else if goldPdf <> null then netAltin - goldPdf       # PDF varsa
            else if goldUrdl <> null then netAltin + goldUrdl     # URDL fallback
            else netAltin                                          # Hiçbiri yoksa
```

## İşaret Kuralı (Kritik!)

URDL ve PDF birbirine **TERS YÖNDE** işaret kullanır:

| Kaynak | Net Pozisyon İşareti | Düzeltme |
|---|---|---|
| **PDF** | Pozitif (TCMB alacaklı) | NetAltin **− PDF** |
| **URDL II.3** | Negatif (rezervi şişiren) | NetAltin **+ URDL** |

Sonuç matematiksel olarak aynı: gerçek net altın pozisyonuna döner.

## İki Yolun Karşılaştırması

| Özellik | PDF Yolu | URDL Yolu |
|---|---|---|
| Frekans | Günlük | Aylık (haftalık ZIP'ten) |
| Detay | Tüm altın swap kanalları | Sadece "II.3 Diğer" toplam |
| Kapsam | 2021+ | Tarihsel sürekli |
| Güvenilirlik | PDF format değişebilir | EVDS standart |

## Pre-2021 Davranış

PDF'te altın swap kalemi yoktur (~2021 öncesi). Bu tarihler için
URDL fallback otomatik devreye girer. URDL'nin "Diğer Swap" kalemi
tüm non-MB swap'ları içerdiği için sadece altın değil tüm "diğer"
swap'lar düzeltilir — bu pre-2021 için pratikte yeterli yaklaşımdır.

## Ekonomik Anlam

Altın swap, TCMB'nin altın karşılığında kısa vadeli döviz fonlama
sağladığı bir araçtır. Brüt rezerv değişmez ama swap vade sonunda
döviz iade edilmesi gerekir. Bu yükümlülüğü görmezden gelen bir
"net altın" hesabı, gerçek dışı yüksek görünüm yaratır.

SH Net Altın bu çarpıtmayı düzelterek **TCMB'nin tamamen serbest
tasarrufundaki altın rezervini** gösterir.

## SH NUR ile İlişki

```
SH Net Uluslararası Rezerv (Günlük) = SH Net Altın + SH Net Döviz
```

`derived:tcmb-swap-haric-net-rezerv-gunluk` tarafından kullanılır.
