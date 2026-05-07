---
record_type: indicator
id: derived:tcmb-swap-haric-net-rezerv-urdl
title: TCMB Swap Hariç Net Rezerv (URDL Standart)
status: approved
input_ids:
- evds:TP.AB.N06
- evds:TP.DOVVARNC.K14
- evds:TP.DOVVARNC.K23
- evds:TP.BL001
- evds:TP.AB.C1
formula_expression: NIR + SwapToplamURDL + DigerSwapURDL
formula_description: Net Uluslararası Rezerv'e (NIR) URDL'den gelen swap kalemlerini ekler (URDL negatif olduğu için toplama doğru düzeltmeyi yapar).
output_frequency: weekly
output_unit: Milyar USD
economic_meaning: >
  Swap Hariç Net Rezerv'in URDL kaynaklı standart versiyonu. NIR (TP.AB.N06)
  doğrudan kullanılır; URDL'in II.2 (toplam swap) ve II.3 (diğer/altın) swap
  kalemleri eklenir. Bileşen ayrıştırması gerektirmez — saf URDL tabanlı.
validation_note: >
  Bu yöntem URDL aylık verisinden çalışır; haftalık ZIP scrape başarılıysa
  aynı kavramların haftalık karşılığı kullanılır. Günlük PDF versiyonu
  (`derived:tcmb-swap-haric-net-rezerv-gunluk`) ile yaklaşık aynı sonuç
  vermeli. Sapma → veri kaynağı zaman/işaret farklarından.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
- theme:tcmb-swap
---
# TCMB Swap Hariç Net Rezerv (URDL Standart)

## Formül

```
SH Net Rezerv (URDL) = NIR + SwapToplamURDL + DigerSwapURDL
                       [TP.AB.N06]   [K14]      [K23]
```

URDL işaret kuralı: tüm swap değerleri NEGATİF gelir (rezervi şişirici), o yüzden
toplama düzeltici işlemdir.

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 2000-2009):

```python
WithSwapNet2 = "Swap Hariç Net Rezerv (Milyar USD)"
    each
        let nir   = Net Uluslararası Rezerv,
            swap  = Swap Büyüklüğü (URDL II.2 toplam),
            dswap = Diğer Swap Büyüklüğü (URDL II.3)
        in if nir = null or swap = null or dswap = null then null
           else nir + swap + dswap
```

## NIR Kaynağı

| Frekans | Kaynak |
|---|---|
| **Haftalık** | TP.AB.N06 (Net Uluslararası Rezerv, Bin TL) → İmaEdilenUSDTL ile USD'ye |
| **URDL ZIP** | URDL şablonunda doğrudan NIR satırı |
| **URDL aylık** | TP.REZVARPD K1-K11 toplamından türev |

Excel haftalık sorguda TP.AB.N06 doğrudan kullanılır.

## Günlük Versiyon ile Farkı

| Özellik | Günlük (PDF) | URDL Standart (bu) |
|---|---|---|
| Hesap yöntemi | Bileşen (SH Altın + SH Döviz) | Doğrudan toplama (NIR + Swap'lar) |
| Swap kaynağı | PDF öncelikli | %100 URDL |
| Detay | Altın/Döviz ayrı | Toplam |
| Frekans | Günlük PDF varsa günlük | URDL haftalık/aylık |

## İki Versiyon Karşılaştırma

İdeal durumda iki yol aynı sayıyı vermeli. Pratikte küçük sapmalar:
- PDF güncellenme zamanı vs URDL ZIP yayın zamanı
- İşaret tutarsızlıkları (özellikle 2021 öncesi)
- Pre-2018 BL085 sapması (sadece günlük versiyona etki eder)

## Ekonomik Anlam

URDL standart versiyonu, IMF SDDS metodolojisini doğrudan takip eden
"resmi" rezerv tanımıdır. Politika tartışmalarında ve uluslararası
karşılaştırmalarda öncelikli ölçüttür.

Günlük PDF versiyonu daha yüksek frekanslı ve detaylı analiz için
kullanılır ama metodolojik basitlik açısından URDL daha şeffaftır.
