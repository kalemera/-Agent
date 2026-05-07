---
record_type: theme
id: theme:net-reserve-estimate
title: Net Rezerv Tahmini ve Swap Hariç Net Rezerv
status: approved
description: >
  TCMB Net Uluslararası Rezervi (NIR) ve swap hariç net rezerv hesabı için
  gerekli tüm seriler, türev indicator'lar ve günlük bilanço-bazlı tahminler.
  theme:reserves'in NET odaklı alt kümesi — sadece yükümlülüklerden arındırılmış
  ve swap düzeltmesi yapılmış kavramlar bu temaya dahildir. Brüt rezerv ölçütleri
  (TP.AB.TOPLAM, TP.AB.C1, TP.AB.C2, TP.AB.N07) bu temaya DAHİL DEĞİLDİR.
series_ids:
- evds:TP.AB.A02
- evds:TP.AB.A11
- evds:TP.AB.A13
- evds:TP.AB.A14
- evds:TP.DK.USD.A.YTL
- evds:TP.AB.N06
- evds:TP.BL001
- evds:TP.BL002
- evds:TP.BL0021
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
- evds:TP.BL085
- evds:TP.BL086
- evds:TP.BL088
- evds:TP.BL089
- evds:TP.BL090
- evds:TP.BL092
- evds:TP.BL093
- evds:TP.BL097
- evds:TP.BL099
- evds:TP.BL117
- evds:TP.BL118
- evds:TP.BL129
- evds:TP.BL131
- evds:TP.BL132
- evds:TP.BL136
- evds:TP.BL140
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.DOVVARNC.K14
- evds:TP.DOVVARNC.K18
- evds:TP.DOVVARNC.K22
- evds:TP.DOVVARNC.K23
indicator_ids:
- derived:tcmb-implied-fx-usd
- derived:tcmb-bl141-etkin
- derived:tcmb-bl140-etkin
- derived:tcmb-standby-kalintisi
- derived:tcmb-net-altin-rezervi
- derived:tcmb-net-doviz-rezervi
- derived:tcmb-mb-swap-toplam
- derived:tcmb-pdf-gunluk-swap-net
- derived:tcmb-pdf-gunluk-altin-swap-net
- derived:tcmb-swap-haric-net-altin
- derived:tcmb-swap-haric-net-doviz
- derived:tcmb-swap-haric-net-rezerv-gunluk
- derived:tcmb-swap-haric-net-rezerv-urdl
- derived:tcmb-bilanco-net-doviz-pozisyonu
- derived:tcmb-bilanco-tahmini-net-rezerv
source_dependency_ids:
- source:tcmb-urdl-zip
- source:tcmb-tarafli-swap-pdf
questions:
- "TCMB'nin gerçek (swap hariç) net rezervi ne kadar?"
- "NIR (Net Uluslararası Rezerv) ile swap hariç hesap arasındaki fark ne?"
- "Günlük analitik bilanço net döviz pozisyon değişimi nasıl?"
- "Net altın rezervi içinde altın swap'ı düşülmüş mü?"
- "Pre-2018 dönemde net rezerv hesabı neden farklı?"
- "PDF günlük swap verisi olmadığı zaman fallback nasıl çalışıyor?"
---
# Net Rezerv Tahmini ve Swap Hariç Net Rezerv

## Açıklama

`theme:reserves` ana temasının **NET odaklı alt kümesi**. Sadece yükümlülüklerden
arındırılmış (NET) ve swap düzeltmesi yapılmış (SH) kavramları içerir.
Brüt rezerv ölçütleri (TP.AB.TOPLAM, C1, C2, N07) bu temaya dahil değildir.

## Tema Üyeliği Kuralı

| Kavram | Bu Tema | theme:reserves |
|---|---|---|
| Brüt Rezerv (TP.AB.TOPLAM) | ❌ | ✅ |
| Brüt Altın (TP.AB.C1) | ❌ | ✅ |
| Brüt Döviz (TP.AB.C2) | ❌ | ✅ |
| Brüt Standby (TP.AB.N07) | ❌ | ✅ |
| **Net Uluslararası Rezerv (TP.AB.N06)** | ✅ | ✅ |
| **Net Altın Rezervi (derived)** | ✅ | ✅ |
| **Net Döviz Rezervi (derived)** | ✅ | ✅ |
| **SH Net Rezerv (derived)** | ✅ | ✅ |
| **Günlük Bilanço Net Pozisyon (derived)** | ✅ | ✅ |

Bu tema, brüt ve net kavramların karıştırılmamasını sağlamak için
ayrı tutulur.

## NET Hesap Zinciri

```
Net Altın = TP.BL002 - (BL132 + BL136 + BL089 + BL141Etkin)
                       altın yükümlülükler

Net Döviz = (BL003+BL004+BL008+StandbyKalintisi) -
            (yiBank + BL086 + BL088 + BL090 + BL092 + BL093 +
             BL140Etkin + BL099 + BL117 + BL118)

NIR (TP.AB.N06) ≈ Net Altın + Net Döviz

SH Net Altın = Net Altın - PDFAltinSwap (PDF varsa) | + DigerSwapURDL (fallback)
SH Net Döviz = Net Döviz + MBSwapURDL - PDFFXSwap (PDF varsa) | + URDL fallback

SH Net Rezerv (Günlük) = SH Net Altın + SH Net Döviz
SH Net Rezerv (URDL Standart) = NIR + SwapToplam + DigerSwap
```

## Günlük Bilanço Tahmini

NIR yayını (haftalık) gecikirken günlük analitik bilançodan proxy:

```
Net Döviz Pozisyonu (4 kalem) = A02 - A11 - A14 - A13
Tahmini Net Rezerv (3 kalem)  = A02 - A11 - A14   (kamu mevduat hariç)
```

İki yorumlama da geçerli; A13 (kamu mevduat) volatilitesi yorumlama tercihi.

## Source Dependencies

- **`source:tcmb-urdl-zip`** — Haftalık URDL ZIP (II.2 ve II.3 swap kalemleri)
- **`source:tcmb-tarafli-swap-pdf`** — Günlük TCMB Taraflı Swap PDF (PDF'te swap detayı)
