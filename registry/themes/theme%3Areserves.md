---
record_type: theme
id: theme:reserves
title: TCMB Rezervleri
status: approved
description: >
  TCMB'nin uluslararası rezerv yönetimi ile ilgili tüm seriler, türev
  indicator'lar ve veri kaynakları. Brüt rezerv izleme, net rezerv hesabı,
  swap hariç net rezerv, günlük bilanço bazlı tahmin, URDL haftalık ve
  aylık veri kaynaklarını kapsar.
series_ids:
- evds:TP.AB.A02
- evds:TP.AB.A11
- evds:TP.AB.A13
- evds:TP.AB.A14
- evds:TP.DK.USD.A.YTL
- evds:TP.AB.C1
- evds:TP.AB.C2
- evds:TP.AB.TOPLAM
- evds:TP.AB.N06
- evds:TP.AB.N07
- evds:TP.BL001
- evds:TP.BL002
- evds:TP.BL0021
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
- evds:TP.BL012
- evds:TP.BL085
- evds:TP.BL086
- evds:TP.BL088
- evds:TP.BL089
- evds:TP.BL090
- evds:TP.BL092
- evds:TP.BL093
- evds:TP.BL097
- evds:TP.BL098
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
- evds:TP.REZVARPD.K1
- evds:TP.REZVARPD.K2
- evds:TP.REZVARPD.K3
- evds:TP.REZVARPD.K4
- evds:TP.REZVARPD.K5
- evds:TP.REZVARPD.K6
- evds:TP.REZVARPD.K7
- evds:TP.REZVARPD.K8
- evds:TP.REZVARPD.K9
- evds:TP.REZVARPD.K10
- evds:TP.REZVARPD.K11
- evds:TP.DOVVARNC.K14
- evds:TP.DOVVARNC.K18
- evds:TP.DOVVARNC.K22
- evds:TP.DOVVARNC.K23
indicator_ids:
- derived:tcmb-implied-fx-usd
- derived:tcmb-implied-gram-altin-fiyat
- derived:tcmb-altin-troy-ons
- derived:tcmb-brut-rezerv-tl-urdl
- derived:tcmb-doviz-rezervi-tl-urdl
- derived:tcmb-standby-kalintisi
- derived:tcmb-bl141-etkin
- derived:tcmb-bl140-etkin
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
- "Bu hafta brüt rezerv ne kadar, geçen haftaya göre nasıl değişti?"
- "Net Uluslararası Rezerv (NIR) bu hafta nasıl?"
- "Swap hariç net rezerv kaç milyar dolar?"
- "Günlük analitik bilançoya göre rezervlerde hareket var mı?"
- "Brüt altın ve döviz rezervlerinin kompozisyonu nasıl?"
- "TCMB'nin swap pozisyonu (M.B. + diğer + altın) toplam ne kadar?"
- "URDL aylık verisi haftalık tahminle uyumlu mu?"
- "Yıl başından beri rezervler nasıl değişti (YBB)?"
---
# TCMB Rezervleri

## Açıklama

Bu tema TCMB'nin uluslararası rezerv yönetimi ile ilgili tüm seri,
türev indicator ve veri kaynaklarını kapsar. v9 Excel
(Rezerv_Apko_queryleri_korunmus_v9.xlsm) çalışmasından türetilmiş
kapsamlı bir veri haritası içerir.

## Üç Ana Erişim Yolu

```
1. EVDS Haftalık Vaziyet (TP.BL00X)    → birincil yol, EVDS API
2. URDL Haftalık ZIP (TCMB sayfası)    → çapraz teyit, web scrape
3. URDL Aylık (TP.REZVARPD)             → fallback, EVDS API
```

## Anahtar Hesaplama Zinciri

```
A) Birim Türetmeleri:
   - İma Edilen USD/TL = (BL001/AB.C1)/1000
   - İma Edilen Gram Altın TL = (BL002×1000)/BL0021
   - Troy Ons = BL0021/31.1034768

B) Brüt Rezerv (URDL alternatif yol):
   = (BL001 + BL003 + BL004 + BL008) / 1.000.000

C) Standby Kalıntısı:
   = AB.N07 - (BL001 + BL003 + BL004 + BL008)

D) Net Altın Rezervi:
   Ara = BL002 - (BL132 + BL136 + BL089 + BL141Etkin)
   USD = (Ara/1.000.000) / İmaEdilenUSDTL

E) Net Döviz Rezervi:
   Varlık = BL003 + BL004 + BL008 + StandbyKalintisi
   Yük = yiBank + BL086 + BL088 + BL090 + BL092 + BL093 + BL140Etkin + BL099 + BL117 + BL118
   yiBank = if Tarih < 2018-08-31 then BL085 else (BL129+BL131)
   Ara = Varlık - Yük
   USD = (Ara/1.000.000) / İmaEdilenUSDTL

F) NIR Teyit:
   |NetAltin + NetDoviz - AB.N06| ≤ 0.001 (post-2018)

G) Swap Hariç:
   SH Net Altın = NetAltin - PDFAltinSwap (PDF varsa) | NetAltin + DigerSwapURDL (fallback)
   SH Net Döviz = NetDoviz + mbAdj - PDFFXSwap (PDF varsa) | + URDL fallback
   SH Net Rezerv (Günlük) = SH Net Altın + SH Net Döviz
   SH Net Rezerv (URDL) = NIR + SwapToplam + DigerSwap
```

## Source Dependencies

- **`source:tcmb-urdl-zip`** — Haftalık URDL ZIP scrape
- **`source:tcmb-tarafli-swap-pdf`** — Günlük TCMB Taraflı Swap PDF

## Önemli Tarihler / Cut-offs

- **2018-08-31:** TP.BL129/BL131 ayrışması (öncesinde BL085 toplamı)
- **~2021:** PDF'te altın swap kalemleri görünmeye başladı
- **BL097 placeholder:** >100,000 Bin TL eşiği (pre-2018 çöp filtre)
- **20.03.2026 patch:** PDF'te eksik tarih, 19.03 satırından kopyalanır

## Analiz Soruları (Agent Tarafı)

Sorulan sorular agent-driven yanıt için input'tur. RezervAnalystAgent
şu intent'leri destekleyecek:

| Intent | Anlam |
|---|---|
| `brut_rezerv_durum` | Brüt rezerv mevcut + değişim |
| `net_rezerv_durum` | NIR + bileşen kırılımı |
| `swap_haric_rezerv` | SH Net Rezerv + swap detay |
| `gunluk_tahmin` | Bilanço-bazlı günlük proxy |
| `altin_kompozisyon` | Brüt/Net/SH altın detay |
| `doviz_kompozisyon` | Brüt/Net/SH döviz detay |
| `swap_breakdown` | M.B. + diğer + altın swap |
| `tarihsel_karsilastirma` | YBB / haftalık / aylık |
