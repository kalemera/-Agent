---
record_type: series
id: evds:TP.AB.A13
title: Kamu ve Diğer Döviz Mevduatı (Bin TL) — Analitik Bilanço P.1ba
status: approved
source: evds
source_version: evds2
ticker: TP.AB.A13
frequency: daily
unit: Bin TL
catalog_group: MERKEZ BANKASI ANALİTİK BİLANÇOSU
description: >
  TCMB analitik bilançosunun P.1ba satırı — kamu kurumları (Hazine,
  belediye, KİT, vb.) ve diğer banka dışı kuruluşların TCMB'deki döviz
  mevduatlarının Bin TL karşılığı. Kaynak grubu: MERKEZ BANKASI
  ANALİTİK BİLANÇOSU. Net Döviz Pozisyonu hesabının dördüncü kalemidir;
  Tahmini Net Rezerv hesabında ise hariç tutulur (volatilitesi yüksek).
usage: >
  Kamu Döviz Mevduatı (Milyar TL) = TP.AB.A13 / 1.000.000
  Kamu Döviz Mevduatı (Milyar USD) = (TP.AB.A13 / 1.000.000) / TP.DK.USD.A.YTL
  Net Döviz Pozisyonu = TP.AB.A02 - TP.AB.A11 - TP.AB.A14 - TP.AB.A13   (A13 dahil)
  Tahmini Net Rezerv  = TP.AB.A02 - TP.AB.A11 - TP.AB.A14                (A13 hariç)
  Power Query: TcmbGunlukBilanco sorgusunda 4. ana seri.
official_url: ''
theme_ids:
- theme:reserves
- theme:banking-balance-sheet
- theme:net-reserve-estimate
indicator_ids:
- derived:tcmb-bilanco-net-doviz-pozisyonu
- derived:tcmb-bilanco-tahmini-net-rezerv
---
# Kamu ve Diğer Döviz Mevduatı (Bin TL) — Analitik Bilanço P.1ba

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI ANALİTİK BİLANÇOSU
**Ticker:** TP.AB.A13
**Frekans:** Günlük (iş günü)
**Ham Birim:** Bin TL → ÷1.000.000 → Milyar TL

## Kullanım

TCMB'de banka dışı kuruluşların döviz mevduatları:

```
P.1ba Kamu ve Diğer Döviz Mevduatı
  - Hazine ve Maliye Bakanlığı döviz hesapları
  - Belediye / KİT döviz mevduatları
  - Kamu bankaları döviz işlem hesapları (eğer banka mevduatından ayrıysa)
  - Diğer banka dışı kuruluş döviz mevduatları
```

## Power Query Karşılığı

`TcmbGunlukBilanco` M kodu (satır 468):

```python
Series = "TP.AB.A02-TP.AB.A11-TP.AB.A14-TP.AB.A13-TP.DK.USD.A.YTL"
# A13 → "Kamu ve Diğer Döviz Mevduatı (Milyar TL)"
```

## İki Yorumlama Arasındaki Anahtar Kalem

A13'ün dahil edilip edilmemesi günlük rezerv tahmininin **felsefi
tercih** noktasıdır:

| Hesap | A13 Durumu | Yorum |
|---|---|---|
| **Net Döviz Pozisyonu** | Dahil | Tüm iç-dış döviz yükümlülükleri (tutucu) |
| **Tahmini Net Rezerv** | Hariç | Sadece banka kanalı (kamu volatilitesi filtreli) |

## Volatilite Profili

Kamu mevduatları kısa vadeli yüksek volatilite gösterebilir:
- **Hazine borçlanma günleri**: Eurobond ihraç + repo işlemleri
- **Hazine harcama günleri**: Maaş, yatırım, döviz cinsi ödemeler
- **Ay sonu kapanışları**: Hesap düzeltmeleri
- **KİT operasyonları**: Petrol/gaz alım swap'ları

Bu nedenle bazı analistler A13'ü hariç tutarak "yapısal" net rezerv
hareketini izlemeyi tercih ederler.

## Haftalık Vaziyet ile İlişki

A13 yaklaşık olarak haftalık vaziyetin BL090 (Diğer Döviz Mevduat) +
BL092 (İşçi Dövizleri) toplamına denk gelir, ama tam eşitlik değildir.

```
A13 ≈ TP.BL090 + TP.BL092 + (kısmen BL093)
```

A13 günlük frekansta kamu/diğer mevduatın **toplam** trendini, BL serileri
ise haftalık detay kırılımını verir.

## Excel "Özet" Sayfasında Kullanımı

Excel "Özet" tablo 1 sütun H'de "Kamu ve Diğer Döviz Mevduatı (B2b)"
olarak yer alır; günlük/haftalık/aylık değişim ve YBB metrikleri bu
sütundan hesaplanır.
