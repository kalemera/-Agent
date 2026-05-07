---
record_type: indicator
id: derived:tcmb-bilanco-tahmini-net-rezerv
title: TCMB Günlük Bilanço Tahmini Net Rezerv (Milyar USD)
status: approved
input_ids:
- evds:TP.AB.A02
- evds:TP.AB.A11
- evds:TP.AB.A14
- evds:TP.DK.USD.A.YTL
formula_expression: ((TP.AB.A02 - TP.AB.A11 - TP.AB.A14) / 1000000) / TP.DK.USD.A.YTL
formula_description: Net Döviz Pozisyonu hesabının kamu mevduatı (A13) hariç versiyonu = Tahmini Net Rezerv proxy.
output_frequency: daily
output_unit: Milyar USD
economic_meaning: >
  Net Döviz Pozisyonu'nun (`derived:tcmb-bilanco-net-doviz-pozisyonu`)
  Kamu ve Diğer Döviz Mevduatı (TP.AB.A13) hariç alternatif versiyonu.
  Kamu mevduatlarının kısa vadeli volatilitesi rezerv tahminini bozabileceği
  için bazı analizlerde A13 hariç tutulur. Excel'in günlük rezerv tahmini
  bu varyantı kullanır.
validation_note: >
  Net Döviz Pozisyonu ile fark = TP.AB.A13 / 1.000.000 / kur (Milyar USD).
  Hangi yorumlama kullanılırsa kullanılsın tutarlı olunmalı; ikisi farklı
  proxy'lerdir, doğru/yanlış değil.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
---
# TCMB Günlük Bilanço Tahmini Net Rezerv (Milyar USD)

## Formül

```
Tahmini Net Rezerv = ((TP.AB.A02 - TP.AB.A11 - TP.AB.A14) / 1.000.000) / TP.DK.USD.A.YTL
                       [Dış Varlık] [Dış Yük]  [Banka YP]      [Bin TL→]  [USD/TL]
```

Net Döviz Pozisyonu formülünün kamu/diğer mevduat (TP.AB.A13) hariç
versiyonudur:

```
Tahmini Net Rezerv = Net Döviz Pozisyonu + (TP.AB.A13 / 1.000.000 / kur)
```

## Power Query Karşılığı

`TcmbGunlukBilanco_USD_Swap` M kodu (satır 865-873):

```python
#"Added Custom1" = Table.AddColumn(
    #"Added Custom",
    "Tahmini Net Rezerv",
    each
        [#"Dış Varlıklar (Milyar USD)"]
        - [#"Dış Yükümlülükler (Milyar USD)"]
        - [#"Bankalar Döviz Mevduatı (Milyar USD)"]
)
```

## Net Döviz Pozisyonu vs Tahmini Net Rezerv

| Hesap | Düşülen Kalemler | Yorum |
|---|---|---|
| **Net Döviz Pozisyonu** | A11 + A14 + **A13** | Tüm iç/dış döviz yükümlülükleri |
| **Tahmini Net Rezerv** | A11 + A14 (A13 hariç) | Banka mevduatları temel proxy |

A13 (Kamu ve Diğer Döviz Mevduatı) volatilitesi yüksek olabildiğinden
bazı analistler bu kalemi hariç tutmayı tercih eder.

## Excel "Özet" Sayfasında Kullanımı

Excel "Özet" sayfasındaki günlük dashboard tablo 1'de **J sütunu** "Brüt
Rezerv (Tahmin)" ve **K sütunu** "Net Uluslararası Rezerv (Tahmin)"
hesaplarının bir bileşeni olarak bu tahmini net rezerv kullanılır.

## Ekonomik Anlam Notu

A13'ün dahil edilip edilmemesi felsefi bir tercih:

- **A13 dahil (Net Döviz Pozisyonu)**: TCMB'nin tüm iç-dış döviz
  yükümlülüklerinden net pozisyon. Tutucu yaklaşım.
- **A13 hariç (Tahmini Net Rezerv)**: Kamu mevduatlarının kısa vadeli
  hareketinin gürültüsünü filtreleyen, bankacılık sistemine odaklı
  proxy. Excel sahibinin tercih ettiği yöntem.
