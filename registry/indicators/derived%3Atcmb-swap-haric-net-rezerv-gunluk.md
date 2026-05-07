---
record_type: indicator
id: derived:tcmb-swap-haric-net-rezerv-gunluk
title: TCMB Swap Hariç Net Rezerv (Günlük PDF Bazlı)
status: approved
input_ids:
- evds:TP.BL002
- evds:TP.BL132
- evds:TP.BL136
- evds:TP.BL089
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
- evds:TP.AB.N07
- evds:TP.BL129
- evds:TP.BL131
- evds:TP.BL085
- evds:TP.BL086
- evds:TP.BL088
- evds:TP.BL090
- evds:TP.BL092
- evds:TP.BL093
- evds:TP.BL140
- evds:TP.BL097
- evds:TP.BL099
- evds:TP.BL117
- evds:TP.BL118
- evds:TP.BL001
- evds:TP.AB.C1
- evds:TP.BL0021
- evds:TP.DOVVARNC.K18
- evds:TP.DOVVARNC.K22
- evds:TP.DOVVARNC.K14
- evds:TP.DOVVARNC.K23
- source:tcmb-tarafli-swap-pdf
formula_expression: SHNetAltin + SHNetDoviz
formula_description: Swap Hariç Net Altın + Swap Hariç Net Döviz toplamı = SH Net Uluslararası Rezerv (günlük TCMB swap'tan hesaplı versiyon).
output_frequency: weekly
output_unit: Milyar USD
economic_meaning: >
  TCMB'nin altın ve döviz swap'larından arındırılmış net uluslararası rezervi.
  Günlük PDF (TcmbTarafliSwapPdf_Table) verisi öncelikli kullanılır; bu yüzden
  "Günlük TCMB Swap'tan hesaplı" varyantı olarak adlandırılır. PDF olmayan
  tarihlerde URDL aylık fallback'i devreye girer.
validation_note: >
  Bu indicator iki alt indicator'un toplamıdır (SH Net Altın + SH Net Döviz).
  Her ikisi de PDF/URDL fallback mantığına sahip. Standart URDL versiyonu
  (`derived:tcmb-swap-haric-net-rezerv-urdl`) ile karşılaştırılarak swap
  metodoloji farklılıkları görülebilir.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
- theme:tcmb-swap
---
# TCMB Swap Hariç Net Rezerv (Günlük PDF Bazlı)

## Formül

```
SH Net Rezerv (Günlük) = SH Net Altın + SH Net Döviz
```

Bileşen indicator'lar:
- `derived:tcmb-swap-haric-net-altin`
- `derived:tcmb-swap-haric-net-doviz`

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1987-1996):

```python
WithSwapNet1 = "Swap Hariç Net Rezerv (Günlük Tcmb Swap'tan hesaplanmış)"
    each
        let altin = SH Net Altın,
            doviz = SH Net Döviz
        in if altin = null or doviz = null then null
           else altin + doviz
```

## "Günlük TCMB Swap'tan" Adının Anlamı

Bu varyant **PDF (günlük taraflı swap) verisini** öncelikli olarak kullandığı
için "günlük TCMB swap'tan hesaplı" adını alır. PDF olmayan tarihlerde
otomatik URDL fallback'e döner. Bu yüzden seri %100 PDF değildir; **PDF
öncelikli, URDL fallback'li** karma bir hesaptır.

## URDL Standart Versiyonu ile Farkı

Excel'de **iki ayrı** SH Net Rezerv hesabı tutulur:

| Versiyon | Yöntem | Tutarlılık |
|---|---|---|
| **Günlük (bu)** | SH Net Altın + SH Net Döviz | Bileşen toplamı |
| **URDL (standart)** | NIR + SwapToplam + DiğerSwap | URDL doğrudan |

İkisi yaklaşık aynı sonuç vermeli ama farklılıklar:
- Veri tarihleri (PDF günlük, URDL haftalık)
- İşaret kuralları (PDF pozitif, URDL negatif)
- Pre-2018 BL085 sapması

## Kullanım: Asıl Şeffaflık Ölçütü

Bu hesap, TCMB net rezervinin "swap'sız" gerçek büyüklüğünü gösterir.
Politika analizi ve rezerv kalitesi değerlendirmesinde temel ölçüttür.
Brüt rezerv ile bu seri arasındaki fark **swap üzerinden alınan kısa
vadeli döviz fonlama yükünü** gösterir.
