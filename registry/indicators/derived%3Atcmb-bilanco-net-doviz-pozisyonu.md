---
record_type: indicator
id: derived:tcmb-bilanco-net-doviz-pozisyonu
title: TCMB Günlük Bilanço Net Döviz Pozisyonu (Milyar USD)
status: approved
input_ids:
- evds:TP.AB.A02
- evds:TP.AB.A11
- evds:TP.AB.A14
- evds:TP.AB.A13
- evds:TP.DK.USD.A.YTL
formula_expression: ((TP.AB.A02 - TP.AB.A11 - TP.AB.A14 - TP.AB.A13) / 1000000) / TP.DK.USD.A.YTL
formula_description: Günlük analitik bilançoda Dış Varlıklar - Dış Yükümlülükler - Bankalar Döviz Mevduatı - Kamu/Diğer Döviz Mevduatı, USD/TL ile Milyar USD'ye çevrilir.
output_frequency: daily
output_unit: Milyar USD
economic_meaning: >
  TCMB'nin günlük analitik bilançosundan türetilen net döviz pozisyonu.
  Dış varlıklardan, hem dış (yurtdışı) hem iç (banka + kamu) döviz
  yükümlülükleri çıkarılır. Haftalık vaziyet (TcmbHaftalikRezerv)
  yayınlanmadan önce günlük rezerv hareketlerinin **proxy göstergesi**
  olarak kullanılır.
validation_note: >
  Tüm beş seri günlük frekansta. Kur (TP.DK.USD.A.YTL) hafta sonu/tatil
  null olabilir → forward fill veya önceki günün kuru. Bin TL → Milyar USD
  birim çarpanı: ÷1.000.000 sonra ÷kur. Haftalık vaziyet ile ay sonlarında
  tutarlılık karşılaştırılabilir.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
---
# TCMB Günlük Bilanço Net Döviz Pozisyonu (Milyar USD)

## Formül

```
Net Döviz Pozisyonu (Milyar USD) =
    ((TP.AB.A02 - TP.AB.A11 - TP.AB.A14 - TP.AB.A13) / 1.000.000) / TP.DK.USD.A.YTL
     [Dış Varlık] [Dış Yük]  [Banka YP] [Kamu YP]    [Bin TL→Milyar TL] [USD/TL]
```

Bileşenler:
- **TP.AB.A02**: Dış Varlıklar (varlık tarafı)
- **TP.AB.A11**: Dış Yükümlülükler (dışa karşı)
- **TP.AB.A14**: Bankalar Döviz Mevduatı (içe karşı banka)
- **TP.AB.A13**: Kamu ve Diğer Döviz Mevduatı (içe karşı kamu/diğer)

## Power Query Karşılığı

`TcmbGunlukBilanco_USD_Swap` M kodu (satır 854-863):

```python
#"Added Custom" = Table.AddColumn(
    SwapNetZero,
    "Net Döviz Pozisyonu",
    each
        [#"Dış Varlıklar (Milyar USD)"]
        - [#"Dış Yükümlülükler (Milyar USD)"]
        - [#"Bankalar Döviz Mevduatı (Milyar USD)"]
        - [#"Kamu ve Diğer Döviz Mevduatı (Milyar USD)"]
)
```

(Önceki adımda her TL kalem ÷kur ile Milyar USD'ye dönüşüyor satır 611-649.)

## Günlük vs Haftalık Rezerv İzleme

| Frekans | Seri | Yayın Gecikmesi |
|---|---|---|
| **Günlük** | TP.AB.A02/A11/A13/A14 (analitik bilanço) | T+1 (ertesi iş günü) |
| **Haftalık** | TP.BL00X (haftalık vaziyet) | Cuma kapanışı, ertesi hafta yayın |

Haftalık veri yayımlanmadan önce **günlük bilanço** rezervin yönünü
gösteren erken proxy verir. Bu yüzden Excel'in "Özet" sayfası bu
seri üzerinden günlük tahminler yapar.

## Tahmini Net Rezerv ile İlişki

```
Net Döviz Pozisyonu = A02 - A11 - A14 - A13   (4 kalem)
Tahmini Net Rezerv  = A02 - A11 - A14         (3 kalem, kamu mevduat hariç)
```

İki tahmin arasındaki fark Kamu ve Diğer Döviz Mevduatı (A13)
büyüklüğüdür. Tahmini Net Rezerv kullanıcı tercihine göre alternatif
proxy olarak hesaplanabilir (`derived:tcmb-bilanco-tahmini-net-rezerv`).

## Ekonomik Anlam

Bu indicator, TCMB'nin günlük net döviz pozisyon değişimini izler.
Brüt rezerv kompozisyonu değişmiş olabilir ama net pozisyon değişimi
doğrudan rezerv kalitesini gösterir. Politika tartışmalarında günlük
"rezerv eridi/arttı" yorumlarının dayanağıdır.
