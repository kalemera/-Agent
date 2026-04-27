---
record_type: theme
id: theme:cari-denge
title: Cari Islemler Hesabi
status: approved
description: Turkiye odemeler dengesi cari islemler hesabi analizi — cari acik, ticaret dengesi, hizmetler, enerji/altin etkisi, finans hesaplari, ozet tablo (18x6)
series_ids:
- evds:TP.HARICCARIACIK.K1
- evds:TP.HARICCARIACIK.K8
- evds:TP.HARICCARIACIK.K10
- evds:TP.ODANA6.Q01
- evds:TP.ODANA6.Q13
- evds:TP.ODEAYRSUNUM6.Q32
- evds:TP.ODEAYRSUNUM6.Q41
indicator_ids:
- derived:altin-net
- derived:enerji-net
- derived:cari-denge-hizmet-net
- derived:yilliklandirilmis-cari
- derived:hizmet-dengesi-bpm6
- derived:gelir-dengesi-net
- derived:dogrudan-yatirim-net
- derived:portfoy-yatirim-net
- derived:diger-yatirim-net
- derived:yolcu-seyahat-net
chart_ids:
- chart:cari-denge-altin-enerji-haric
- chart:cari-denge-karsilastirma
- chart:cari-denge-altin-enerji-etki
- chart:cari-denge-gelirler
source_dependency_ids: []
questions:
- Cari acik ne kadar?
- Enerji ve altin haric cari denge ne durumda?
- Finans hesaplari nasil?
- Hizmetler dengesi ne durumda?
- Yolcu ve seyahat dengesi ne kadar?
- Turizm geliri cari dengeye ne kadar katki yapiyor?
- Yilliklandirilmis cari denge trendi nasil?
- Dogrudan yatirimlar net pozisyonu nedir?
- Portfoy yatirimlari nasil seyrediyor?
- Diger yatirimlar (bankalar, TCMB, hazine) ne durumda?
- Net hata ve noksan ne kadar?
---
# Cari Islemler Hesabi

## Aciklama

Turkiye odemeler dengesi cari islemler hesabi analizi. EVDS API'den iki veri grubu kullanilir:
- **bie_odeayrsunum6** (203 seri) — BPM6 standart sunum, aylik detayli
- **bie_odana6** (36 seri) — BPM6 analitik sunum, ozet kalemler

Ozet tablo (18 satir x 6 sutun) pipeline: `pipelines/cari_denge_ozet.py`
Cikti: `Cari Denge Tablo/outputs/tables/sunum_tablosu.json` + `.html`

## Veri Gruplari

### bie_odana6 — Analitik Sunum (36 seri)
| Kod | Seri Adi |
|-----|----------|
| TP.ODANA6.Q01 | 1.Cari Islemler Hesabi (toplam) |
| TP.ODANA6.Q02 | 1.1.Ihracat |
| TP.ODANA6.Q03 | 1.2.Ithalat |
| TP.ODANA6.Q04 | 1.a.Mal Dengesi |
| TP.ODANA6.Q05 | 1.3.Hizmet Gelirleri |
| TP.ODANA6.Q06 | 1.4.Hizmet Giderleri |
| TP.ODANA6.Q07 | 1.b.Mal ve Hizmet Dengesi |
| TP.ODANA6.Q08 | 1.5.Birincil Yatirim Kaynakli Gelirler |
| TP.ODANA6.Q09 | 1.6.Birincil Yatirim Kaynakli Giderler |
| TP.ODANA6.Q10 | 1.c.Mal, Hizmet ve Birincil Gelir Dengesi |
| TP.ODANA6.Q11 | 1.7.Ikincil Yatirim Kaynakli Gelirler |
| TP.ODANA6.Q12 | 2.Sermaye Hesabi |
| TP.ODANA6.Q13 | 3.Finans Hesabi (toplam) |
| TP.ODANA6.Q14 | 3.1.Dogrudan Yatirimlar: Net Varlik Edinimi |
| TP.ODANA6.Q15 | 3.2.Dogrudan Yatirimlar: Net Yukumluluk Olusumu |
| TP.ODANA6.Q16 | 3.3.Portfoy Yatirimlari: Net Varlik Edinimi |
| TP.ODANA6.Q17 | 3.4.Portfoy Yatirimlari: Net Yukumluluk Olusumu |
| TP.ODANA6.Q18 | 3.4.1.Hisse Senetleri |
| TP.ODANA6.Q19 | 3.4.2.Borc Senetleri |
| TP.ODANA6.Q20 | 3.5.Diger Yatirimlar: Net Varlik Edinimi |
| TP.ODANA6.Q21 | 3.5.1.Merkez Bankasi (Net Varlik) |
| TP.ODANA6.Q22 | 3.5.2.Genel Hukumet (Net Varlik) |
| TP.ODANA6.Q23 | 3.5.3.Bankalar (Net Varlik) |
| TP.ODANA6.Q24 | 3.5.4.Diger Sektorler (Net Varlik) |
| TP.ODANA6.Q25 | 3.6.Diger Yatirimlar: Net Yukumluluk Olusumu |
| TP.ODANA6.Q26 | 3.6.1.Merkez Bankasi (Net Yukumluluk) |
| TP.ODANA6.Q27 | 3.6.2.Genel Hukumet (Net Yukumluluk) |
| TP.ODANA6.Q28 | 3.6.3.Bankalar (Net Yukumluluk) |
| TP.ODANA6.Q29 | 3.6.4.Diger Sektorler (Net Yukumluluk) |
| TP.ODANA6.Q30 | Cari, Sermaye ve Finans Hesaplari |
| TP.ODANA6.Q31 | 4.Net Hata ve Noksan |
| TP.ODANA6.Q32 | Genel Denge |
| TP.ODANA6.Q33 | 5.Rezerv Varliklar |
| TP.ODANA6.Q34 | 5.1.Resmi Rezervler |
| TP.ODANA6.Q35 | 5.2.Uluslararasi Para Fonu Kredileri |
| TP.ODANA6.Q36 | 5.3.Odemeler Dengesi Finansmani |

## Ozet Tablo Yapisi (18 satir x 6 sutun)

18 satir:
1. Cari Islemler Hesabi (toplam — TP.ODANA6.Q01)
2. Mal Dengesi (TP.ODANA6.Q04)
3. Hizmetler Dengesi (Q05 - Q06)
4. Yolcu ve Seyahat (Q32+Q41 — TP.ODEAYRSUNUM6.Q32 + TP.ODEAYRSUNUM6.Q41)
5. Gelir Dengesi (Q08 - Q09 + Q11)
6. Finans Hesaplari (TP.ODANA6.Q13)
7. Dogrudan Yatirimlar (Q15 - Q14)
8. Portfoy Yatirimlari (Q17 - Q16)
9. Hisse Senedi (Q18)
10. Tahvil / Borc Senetleri (Q19)
11. Net Varlik Edinimi (Q16)
12. Diger Yatirimlar (Q25 - Q20)
13. Merkez Bankasi (Q26 - Q21)
14. Genel Hukumet (Q27 - Q22)
15. Bankalar (Q28 - Q23)
16. Banka Disi Sektorler (Q29 - Q24)
17. Net Hata Noksan (TP.ODANA6.Q31)
18. TCMB Rezerv Degisimi (bie_odeayrsunum6'dan, *-1)

6 sutun: Aylik/Guncel, Aylik/Gecen Yil, Yilliklandirilmis/Guncel, Yilliklandirilmis/Onceki Ay, YBD/Guncel, YBD/Onceki Ay

## Seriler (Ozet)

- evds:TP.HARICCARIACIK.K1 — Cari Islemler Hesabi (aylik, milyon USD)
- evds:TP.HARICCARIACIK.K8 — Altin Haric Cari (aylik, milyon USD)
- evds:TP.HARICCARIACIK.K10 — Enerji+Altin Haric Cari (aylik, milyon USD)
- evds:TP.ODANA6.Q01 — 1.Cari Islemler Hesabi (analitik sunum toplamı)
- evds:TP.ODANA6.Q13 — 3.Finans Hesabi (analitik sunum toplamı)
- evds:TP.ODEAYRSUNUM6.Q32 — 1.2.3.1.Yolcu (tasimaci yolcu, bie_odeayrsunum6)
- evds:TP.ODEAYRSUNUM6.Q41 — 1.2.4.Seyahat (turizm/seyahat, bie_odeayrsunum6)

## Indikatorler

- derived:altin-net — Altinin cari dengeye net etkisi
- derived:enerji-net — Enerjinin cari dengeye net etkisi
- derived:cari-denge-hizmet-net — Hizmet ve gelir dengesi
- derived:yilliklandirilmis-cari — 12 aylik kumulatif cari denge
- derived:yolcu-seyahat-net — Yolcu+Seyahat turizm_sum (Q32+Q41)

## Pipeline Notlari

- `bie_odeayrsunum6` cekildikten sonra 2 saniye sleep (EVDS rate limit)
- Sutun adlari `.str.strip()` ile temizlenir (EVDS prefix slash birakir)
- Turk karakter karsilastirmasi `_tr_normalize()` ile yapilir (I/i/I/i sorununu cozuyor)
- BPM6 alt kalem prefix: varlik=3.5.x, yukumluluk=3.6.x (eski BPM5: C.12/C.13)
- `pipelines/cari_denge_ozet.py` calistirmak ozet tablo + 4 analiz grafigi + gelirler grafigi uretir
- Grafik cikti dizini: `Cari Denge Tablo/outputs/charts/` — web: `/charts/cari-denge/`
- Ozet tablo PNG cikti: `Cari Denge Tablo/outputs/tables/sunum_tablosu.png` — web: `/charts/cari-denge-tables/`
- 4 grafik: cari_denge_altin_enerji_haric, cari_denge_karsilastirma, cari_denge_altin_enerji_etki, cari_denge_gelirler

## Analiz Sorulari

- Cari acik ne kadar?
- Enerji ve altin haric cari denge ne durumda?
- Finans hesaplari nasil?
- Hizmetler dengesi ne durumda?
- Yolcu ve seyahat dengesi ne kadar? (TP.ODEAYRSUNUM6.Q32 + Q41)
- Turizm geliri cari dengeye ne kadar katki yapiyor?
- Yilliklandirilmis cari denge trendi nasil?
- Dogrudan yatirimlar net pozisyonu nedir?
- Portfoy yatirimlari nasil seyrediyor?
- Diger yatirimlar (bankalar, TCMB, hazine) ne durumda?
- Net hata ve noksan ne kadar?
