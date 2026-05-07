---
record_type: indicator
id: derived:tcmb-standby-kalintisi
title: TCMB Brüt Döviz Rezerv Standby Kalıntısı
status: approved
input_ids:
- evds:TP.AB.N07
- evds:TP.BL001
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
formula_expression: TP.AB.N07 - (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008)
formula_description: IMF Standby tanımına göre brüt rezerv ile çekirdek dört kalemin toplamı arasındaki fark.
output_frequency: weekly
output_unit: Bin TL
economic_meaning: >
  IMF SDDS / Standby tanımıyla raporlanan brüt rezerv (TP.AB.N07) ile haftalık
  vaziyetin dört çekirdek kaleminin (BL001+BL003+BL004+BL008) toplamı arasındaki
  fark. Bu kalıntı, dolaylı IMF taahhütleri, özel rezerv tanımları veya
  metodolojik düzeltmeleri içerir. Pozitif değer beklenir.
validation_note: >
  Tüm beş bileşen aynı tarihte mevcut olmalı. Negatif sonuç metodolojik
  uyumsuzluğa veya veri zaman farkına işaret edebilir. Net Döviz Rezervi
  varlık tarafına eklendiği için sıfır ya da negatif kalıntı net rezervi
  düşürür — bu rapor hatasıdır, gerçek bir ekonomik durum değil.
theme_ids:
- theme:reserves
---
# TCMB Brüt Döviz Rezerv Standby Kalıntısı

## Formül

```
Standby Kalıntısı (Bin TL) = TP.AB.N07 - (TP.BL001 + TP.BL003 + TP.BL004 + TP.BL008)
                             [Standby Brüt]   [Çekirdek Bileşen Toplamı]
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1402-1415):

```python
T_StandbyKalinti = "Brüt Döviz Rezerv Standby Kalıntısı (Bin TL)"
    each
        let n07   = TP.AB.N07,
            bl001 = TP.BL001,
            bl003 = TP.BL003,
            bl004 = TP.BL004,
            bl008 = TP.BL008,
            formul = List.RemoveNulls({bl001, bl003, bl004, bl008})
        in if n07 = null or List.Count(formul) = 0 then null
           else n07 - List.Sum(formul)
```

## Ekonomik Anlam

İki farklı brüt rezerv ölçütü arasındaki fark:

| Ölçüt | Tanım | Kapsam |
|---|---|---|
| **TP.AB.N07** | IMF Standby raporlaması | IMF SDDS standardı, daha geniş |
| **BL001+BL003+BL004+BL008** | Haftalık vaziyet çekirdek toplamı | Daha dar/operasyonel |

Fark genelde:
- IMF rezerv pozisyonu (kullanılmayan kısım) farkı
- SDR varlık-yükümlülük net etkisi
- Dolaylı IMF taahhütleri
- Diğer metodolojik düzeltmeler

## Kullanım: Net Döviz Rezervi Varlık Tarafı

```
TCMB Net Döviz Rezervi Ara (Bin TL) =
    (BL003 + BL004 + BL008 + StandbyKalintisi) - Yükümlülükler
                              ↑
                  Bu indicator burada eklenir
```

Yani Standby Kalıntısı, çekirdek dört kaleme dahil edilmemiş ek varlıkları
Net Döviz hesabına dahil etmek için kullanılır.
