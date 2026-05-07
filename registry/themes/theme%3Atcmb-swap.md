---
record_type: theme
id: theme:tcmb-swap
title: TCMB Swap İşlemleri ve Pozisyonları
status: approved
description: >
  TCMB'nin döviz, altın ve TL karşılığı swap işlemlerini takip eden tema.
  M.B. (Merkez Bankası kanalı) swap'ları, BIST swap'ları, taraflı (counterparty)
  swap işlemleri, geleneksel ve miktar ihaleleri, altın swap'ları kapsar.
  Hem URDL aylık (II.2 + II.3) hem TCMB Taraflı Swap günlük PDF kaynaklarını
  içerir. theme:reserves'in swap odaklı dikey kesişimi — rezerv tahmininden
  bağımsız olarak swap politikası ve pozisyon analizi için kullanılır.
series_ids:
- evds:TP.DOVVARNC.K14
- evds:TP.DOVVARNC.K18
- evds:TP.DOVVARNC.K22
- evds:TP.DOVVARNC.K23
indicator_ids:
- derived:tcmb-mb-swap-toplam
- derived:tcmb-pdf-gunluk-swap-net
- derived:tcmb-pdf-gunluk-altin-swap-net
- derived:tcmb-swap-haric-net-altin
- derived:tcmb-swap-haric-net-doviz
- derived:tcmb-swap-haric-net-rezerv-gunluk
- derived:tcmb-swap-haric-net-rezerv-urdl
source_dependency_ids:
- source:tcmb-urdl-zip
- source:tcmb-tarafli-swap-pdf
questions:
- "TCMB toplam swap stoku şu an ne kadar?"
- "M.B. swap (açık + fazla) bu hafta nasıl?"
- "BIST swap ve taraflı swap pozisyonları nasıl?"
- "TCMB altın swap pozisyonu büyüyor mu küçülüyor mu?"
- "Günlük PDF ile haftalık URDL swap rakamları arasındaki tutarsızlıklar nelerden kaynaklanıyor?"
- "M.B. swap ile non-MB FX swap toplamlarının kompozisyonu nasıl?"
- "Pre-2021 dönemde altın swap'lar nasıl izleniyor (PDF olmadığı dönem)?"
---
# TCMB Swap İşlemleri ve Pozisyonları

## Açıklama

TCMB'nin tüm swap pozisyonlarını izleyen ayrı bir tema. `theme:reserves`
ana teması rezerv odaklı kapsamlı bir kesim sunarken, bu tema spesifik
olarak **swap politikası ve pozisyon analizi** için odaklanmıştır.

İki kaynaktan birleşik veri: günlük PDF (taraflı + tüm kanallar) ve
aylık URDL (II.2 forward/swap + II.3 diğer).

## Swap Kanalları

```
1. M.B. (Merkez Bankası) Swap
   ├── II.2.a Açık (kısa)  → TP.DOVVARNC.K18
   └── II.2.b Fazla (uzun) → TP.DOVVARNC.K22
   └── Toplam M.B. = K18 + K22

2. Non-MB Döviz Swap
   ├── BIST Swap Piyasası
   ├── TCMB Döviz Karşılığı TL Swap Geleneksel İhale
   ├── TCMB Döviz Karşılığı TL Swap Miktar İhale
   └── TCMB Taraflı Swap (counterparty-specific)

3. Altın Swap
   ├── TCMB TL Karşılığı Altın Swap (CBRT Tur)
   └── TCMB Döviz Karşılığı Altın Swap

4. Toplam Stok (Excel/PDF "TOPLAM" sütunu)
   = Tüm yukarıdakilerin alım yönlü ve satım yönlü stokları
```

## Veri Kaynakları

| Kaynak | Frekans | Kapsam | İşaret |
|---|---|---|---|
| **`source:tcmb-tarafli-swap-pdf`** | Günlük | Tüm swap kanalları (taraflı detay dahil) | PDF: pozitif (alım net) |
| **`source:tcmb-urdl-zip`** | Haftalık | URDL II.2 (M.B. açık/fazla) + II.3 (diğer) | URDL: negatif (rezerv şişirici) |
| **`evds:TP.DOVVARNC.K14/K18/K22/K23`** | Aylık | URDL aylık fallback | URDL: negatif |

## Swap Pozisyonu Analizi Hesapları

```
1) M.B. Swap Toplam (URDL aylık ya da haftalık)
   = TP.DOVVARNC.K18 + TP.DOVVARNC.K22

2) Non-MB FX Swap (URDL fallback)
   = SwapToplam (K14) - MBSwap (K18+K22)

3) PDF Günlük Net Swap (Toplam)
   = TOPLAM_STOK_AlimYonlu - TOPLAM_STOK_SatimYonlu

4) PDF Günlük Altın Swap Net
   = ALTIN_TL_AlimYonlu_Stok - ALTIN_TL_SatimYonlu_Stok

5) Swap Hariç Hesaplar (rezerv kalitesi düzeltmesi için)
   - SH Net Altın (PDF öncelikli, URDL II.3 fallback)
   - SH Net Döviz (M.B. her zaman URDL, non-MB PDF veya URDL fallback)
   - SH Net Rezerv = SH Net Altın + SH Net Döviz (Günlük)
   - SH Net Rezerv (URDL Standart) = NIR + SwapToplam + DigerSwap
```

## İşaret Kuralı (Çok Kritik!)

İki kaynak birbirine **ZIT** işaret konvansiyonu kullanır:

| Kaynak | Net Pozisyon İşareti | Düzeltme Yönü |
|---|---|---|
| **PDF** | Pozitif (TCMB net alacaklı) | NetRezerv **− PDF** |
| **URDL** | Negatif (rezerv şişirici) | NetRezerv **+ URDL** |

Sonuç matematiksel olarak aynı düzeltme; işaret farkı kaynağa özgü.

## Önemli Tarih Notları

- **~2021:** PDF'te altın swap kalemleri görünmeye başladı.
  Pre-2021 → URDL II.3 (TP.DOVVARNC.K23) fallback
- **20.03.2026 patch:** PDF'te eksik tarih, 19.03.2026 satırı kopyalanır
  ve tarihi değiştirilir (hardcoded — Python port'ta dinamik yapılmalı)

## RezervAnalystAgent Intent Bağlantısı

Aşağıdaki intent'ler bu temadan beslenir:

| Intent | Beslenen Indicator |
|---|---|
| `swap_breakdown` | Tüm swap series + 4 SH indicator |
| `swap_haric_rezerv` | SH Net Rezerv (Günlük + URDL) |
| `altin_swap_durum` | PDF günlük altın swap |
| `mb_swap_durum` | M.B. Swap Toplam |
