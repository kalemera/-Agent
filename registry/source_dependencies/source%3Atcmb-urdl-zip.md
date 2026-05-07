---
record_type: source_dependency
id: source:tcmb-urdl-zip
title: TCMB Uluslararası Rezervler ve Döviz Likiditesi (Haftalık ZIP)
status: approved
source_kind: web_scrape_zip
requiredness: optional
source_uri: 'https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Odemeler+Dengesi+ve+Ilgili+Istatistikler/Uluslararasi+Rezervler+ve+Doviz+Likiditesi/'
local_hint: ''
description: >
  TCMB'nin IMF SDDS standardına göre haftalık yayımladığı
  "Uluslararası Rezervler ve Döviz Likiditesi" tablosu.
  ZIP içinde Excel — IMF şablonu bölüm II.2.a'dan swap yükümlülüğü (FX swap
  net drain) ve bölüm II.3'ten diğer yükümlülükler alınır.
  EVDS'de bu serinin yalnızca aylık versiyonu mevcut; haftalık analiz
  için bu kaynak veya TP.BL* türev yaklaşımı gereklidir.
usage: >
  Excel co-worker yaklaşımı: TcmbHaftalikSwap Power Query ile TCMB sayfasındaki
  en güncel ZIP linki otomatik bulunur, indirilir, parse edilir.
  II.2.a satırı → Ana Swap; II.3 satırı → Diğer Swap.
  Toplam = -(Ana Swap + Diğer Swap), haftalık frekans, güne filldown uygulanır.
alternative_path: >
  TP.BL* (MERKEZ BANKASI HAFTALIK VAZİYET EVDS serileri) kullanılarak türev
  yolla aynı net rezerv ve swap değerlerine ulaşılabilir. Bu yol EVDS API
  üzerinden standart şekilde çalışır; ZIP scrape kırılganlığı yoktur.
validation_note: >
  EVDS aylık seri referansı için bkz. TcmbAylıkRezerv_Altin_Swap (fallback).
  Haftalık ZIP yoksa aylık değer en son haftaya filldown yapılır.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
- theme:tcmb-swap
indicator_ids: []
---
# TCMB Uluslararası Rezervler ve Döviz Likiditesi (Haftalık ZIP)

## Kaynak Türü

web_scrape_zip — TCMB web sitesinden haftalık otomatik indirme

## Zorunluluk

optional — TP.BL* türev yolu alternatif olarak kullanılabilir

## Kaynak URI

https://www.tcmb.gov.tr/.../Uluslararasi+Rezervler+ve+Doviz+Likiditesi/

## Açıklama

TCMB haftalık "Uluslararası Rezervler ve Döviz Likiditesi" tablosu.
IMF SDDS standardı — tüm merkez bankaları aynı şablonu kullanır.

Şablon yapısı (ilgili bölümler):
- **II.2.a**: Forward/vadeli + FX swap pozisyonları → TCMB'nin swap yükümlülüğü
- **II.3**: Diğer koşullu yükümlülükler

Swap değeri net rezervden düşülür → swap hariç net rezerv elde edilir.

## Alternatif Erişim Yolu

TP.BL* (Haftalık Vaziyet EVDS) serilerinden türev hesaplamalarla
aynı değerlere ulaşılabilir. Bu yol daha güvenilirdir (EVDS standart API).
