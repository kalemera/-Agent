---
record_type: series
id: evds:TP.AB.N06
title: Net Uluslararası Rezervler — NIR (Bin TL)
status: approved
source: evds
source_version: evds2
ticker: TP.AB.N06
frequency: weekly
unit: Bin TL
catalog_group: MERKEZ BANKASI HAFTALIK VAZİYET
description: >
  Haftalık Vaziyet — TCMB Net Uluslararası Rezervlerinin (NIR / NUR)
  Bin TL karşılığı. Kaynak grubu: MERKEZ BANKASI HAFTALIK VAZİYET.
  IMF Standby tanımına uygun olarak yayımlanan resmi NIR — TCMB'nin
  brüt rezervinden tüm yükümlülükler düşülmüş halidir. Swap Hariç Net
  Rezerv hesaplarının URDL standart varyantında doğrudan girdi.
usage: >
  NIR (Milyar USD) = (TP.AB.N06 / 1.000.000) / İmaEdilenUSDTL
  SH Net Rezerv (URDL) = NIR + SwapToplam (URDL) + DigerSwap (URDL)
  Teyit: NIR ≈ TCMB Net Altın Rezervi + TCMB Net Döviz Rezervi
  Power Query: TcmbHaftalikRezerv sorgusunda Milyar USD'ye çevrilir
  ve teyit sütunuyla bileşen toplamı kontrol edilir.
official_url: ''
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
indicator_ids:
- derived:tcmb-swap-haric-net-rezerv-urdl
---
# Net Uluslararası Rezervler — NIR (Bin TL)

## Kaynak

**EVDS Grubu:** MERKEZ BANKASI HAFTALIK VAZİYET
**Ticker:** TP.AB.N06
**Frekans:** Haftalık
**Ham Birim:** Bin TL → İmaEdilenUSDTL ile USD'ye

## Kullanım

TCMB Net Uluslararası Rezervi'nin (NIR) resmi tek-seri kaynağı.
URDL haftalık ZIP'inde "2A Net Uluslararası Rezervler" satırına denk
gelir; brüt rezervden tüm yabancı para yükümlülüklerin (banka mevduat,
ZK, IMF taahhütleri, dış borç) düşülmüş hali.

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1122):

```python
Series = "...-TP.AB.N06-..."  # "Net Uluslararası Rezerv (Bin TL)"
```

Sonra (satır 1418-1427):

```python
T_NIR_USD = "Net Uluslararası Rezerv (Milyar USD)"
    each
        let nir = TP.AB.N06,
            fx  = İmaEdilenUSDTL
        in if nir = null or fx = null or fx = 0 then null
           else (nir / 1000000) / fx
```

## Bileşen Teyit (Tutarlılık Kontrolü)

NIR'ın doğru hesaplanıp hesaplanmadığı bileşen toplamı ile çapraz
denetlenir:

```
Teyit Farkı = TCMB Net Altın + TCMB Net Döviz - NIR

Post-2018 (>= 2018-08-31): |Fark| ≤ 0.001 Milyar USD beklenir
Pre-2018: BL085 içinde altın teminat karışık → ~1.3 milyar USD tolerans
```

(M kodu satır 2016-2039)

## Üç Versiyonun Karşılaştırması

| Versiyon | Hesaplama | Anlam |
|---|---|---|
| **TP.AB.N06 (resmi)** | EVDS doğrudan | TCMB'nin yayımladığı resmi NIR |
| **Bileşen Toplamı** | NetAltin + NetDoviz | Türev hesaplı NIR |
| **SH Net Rezerv (URDL)** | NIR + Swap'lar | Swap'lardan arındırılmış |

İdeal: NIR (resmi) ≈ NetAltin + NetDoviz; sapmalar metodolojik fark
veya pre-2018 placeholder sorunu.

## SH Net Rezerv URDL Yolunda Direkt Kullanım

```
SH Net Rezerv (URDL) = NIR (TP.AB.N06) + SwapToplam + DigerSwap
                       ↑ Bu seri burası
```

Bkz. `derived:tcmb-swap-haric-net-rezerv-urdl`.

## Excel "Özet" Sayfasında Yeri

"Özet" tablo 2'de **I sütunu "Net Uluslararası Rezerv (NUR)"** olarak
yer alır; günlük/haftalık/aylık/YBB değişim metrikleri bu seriden
türeyen değer üzerinden hesaplanır.

## Politika Önemi

NIR Türkiye'nin **rezerv kalitesi** göstergesi. Brüt rezerv tüm varlık
toplamını verirken, NIR yabancı para yükümlülüklerin düşülmüş halidir
ve "TCMB'nin gerçekten elindeki net pozisyon" anlamına gelir. Negatif
veya çok düşük NIR değerleri rezerv kalitesi açısından kritik sinyaldir.
