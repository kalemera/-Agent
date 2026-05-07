---
record_type: indicator
id: derived:tcmb-swap-haric-net-doviz
title: TCMB Swap Hariç Net Döviz Rezervi (Milyar USD)
status: approved
input_ids:
- evds:TP.BL003
- evds:TP.BL004
- evds:TP.BL008
- evds:TP.AB.N07
- evds:TP.BL129
- evds:TP.BL131
- evds:TP.BL085
- evds:TP.BL086
- evds:TP.BL088
- evds:TP.BL090
- evds:TP.BL092
- evds:TP.BL093
- evds:TP.BL140
- evds:TP.BL097
- evds:TP.BL141
- evds:TP.BL142
- evds:TP.BL099
- evds:TP.BL117
- evds:TP.BL118
- evds:TP.BL001
- evds:TP.BL002
- evds:TP.AB.C1
- evds:TP.BL0021
- evds:TP.DOVVARNC.K18
- evds:TP.DOVVARNC.K22
- evds:TP.DOVVARNC.K14
- source:tcmb-tarafli-swap-pdf
formula_expression: 'NetDovizRezervi + MBSwapURDL − (PDFFXSwap or (SwapTotURDL − MBSwapURDL))'
formula_description: 'Net Döviz''e MB URDL swap eklenir; sonra PDF günlük FX swap çıkarılır. PDF yoksa URDL non-MB FX swap (SwapTot − MBURDL) ile toplama yapılır.'
output_frequency: weekly
output_unit: Milyar USD
economic_meaning: >
  Tüm swap pozisyonlarından arındırılmış net döviz rezervi. M.B. swap
  (TCMB merkez bankası kanalı, II.2.a/b) her zaman URDL'den; non-MB FX swap
  ise tercihen PDF (günlük) yoksa URDL fallback'inden alınır. Gerçek dışı
  rezerv görünümü yaratan tüm swap düzeltmelerini ortadan kaldırır.
validation_note: >
  İki ayrı swap kanalı için iki ayrı kaynak. M.B. swap her zaman URDL II.2.a.iii
  + II.2.b.iii toplamı (K18 + K22). Non-MB FX swap PDF varsa PDF'ten, yoksa
  URDL toplam (K14) eksi M.B. (K18+K22) farkı. PDF/URDL işaret kuralları
  ters yönde olduğu için formül işaretlerinin doğru kullanımı kritik.
theme_ids:
- theme:reserves
- theme:net-reserve-estimate
- theme:tcmb-swap
---
# TCMB Swap Hariç Net Döviz Rezervi (Milyar USD)

## Formül (Karmaşık, Çok Kaynaklı)

```python
mbAdj = MBSwapURDL  # K18 + K22 (her zaman URDL'den)

# Non-MB FX swap için iki yol:
if PDFFXSwap != null:                            # 2021+ günlük PDF varsa
    SH Net Döviz = NetDoviz + mbAdj - PDFFXSwap
else:                                            # URDL fallback
    fxUrdl = SwapTotURDL - MBSwapURDL            # K14 - (K18+K22)
    SH Net Döviz = NetDoviz + mbAdj + fxUrdl
```

## Power Query Karşılığı

`TcmbHaftalikRezerv` M kodu (satır 1967-1984):

```python
WithSwapHaricDoviz = "Swap Hariç Net Döviz Rezervi (Milyar USD)"
    each
        let
            netDoviz = TCMB Net Döviz Rezervi,
            mbUrdl   = MB Döviz Swap (URDL II.2.a.iii + II.2.b.iii),
            fxPdf    = Tcmb Günlük Döviz Swap Net Alım (PDF),
            swapTot  = Swap Büyüklüğü (URDL II.2 toplam),
            mbAdj    = if mbUrdl <> null then mbUrdl else 0,
            fxUrdl   = if swapTot <> null and mbUrdl <> null
                       then swapTot - mbUrdl
                       else if swapTot <> null then swapTot else null
        in
            if netDoviz = null then null
            else if fxPdf <> null then netDoviz + mbAdj - fxPdf
            else netDoviz + mbAdj + (if fxUrdl <> null then fxUrdl else 0)
```

## İki Swap Kanalı

TCMB döviz swap'ı iki ayrı kanaldan kullanır:

| Kanal | Kapsam | Kaynak |
|---|---|---|
| **M.B. (Merkez Bankası)** | Doğrudan TCMB swap işlemleri | URDL II.2.a/b → K18+K22 |
| **Non-MB (Diğer FX)** | BIST swap, taraflı işlemler vs. | PDF veya URDL II.2 toplam farkı |

M.B. kanalı her zaman URDL'den alınır çünkü PDF'te bu kanal ayrılmaz.
Non-MB için tercih sırası: PDF (günlük detay) > URDL fallback.

## İşaret Kuralları (Çok Kritik!)

```
URDL pozisyon: NEGATİF gösterir (rezervi şişirici)
PDF pozisyon:   POZİTİF gösterir (gerçek alacaklı)

URDL'den toplama yapılır:  + mbAdj, + fxUrdl
PDF'ten çıkarma yapılır:    - fxPdf
```

İki yol matematiksel olarak aynı net düzeltmeyi yapar (yön farkı işaretle
absorbe edilir).

## Ekonomik Anlam

Swap işlemleri rezerv görüntüsünü çarpıtır:
- TCMB döviz swap yaparak kısa vadeli döviz fonlama alır
- Brüt rezerv değişmez ama vade sonunda döviz iade edilecek
- Bu yükümlülük görülmezse rezerv "şişik" gösterilir

SH Net Döviz tüm swap çarpıtmalarını giderir ve **TCMB'nin gerçekten
serbest tasarrufundaki net döviz pozisyonunu** verir.

## SH NUR ile İlişki

```
SH Net Uluslararası Rezerv (Günlük) = SH Net Altın + SH Net Döviz
```

`derived:tcmb-swap-haric-net-rezerv-gunluk` tarafından kullanılır.
