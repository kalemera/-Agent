# Kisa Ozet

- Notebook: `Rzrv_Blg_V7.ipynb`
- Spec: `rzrv-blg-v7`
- Lane: `L3_manual_or_fallback`
- Toplam benzersiz ticker: `10`
- Unresolved ticker: `0`

## Kod Gruplari

- `AB`: Analitik bilanco rezerv ve yukumluluk serileri (8 seri)
- `DK`: Kur cevirim girdisi (1 seri)
- `DOVVARNC`: Dormant swap serisi adayi (1 seri)

## Dis Kaynaklar

- `source:rzrv-swap-pdf` | TCMB swap PDF | pdf_table | required_input
- `source:rzrv-manual-swap-ledger` | Manuel swap ledger | manual_inline | required_input

## Durum Etiketleri

- `derived_input`: 9
- `listed_only`: 1

## Rol Etiketleri

- `balance_sheet_line`: 7
- `stock_total`: 1
- `ratio_input`: 1
- `dormant_candidate`: 1

## Tam Ticker Eslestirme

| Ticker | Resmi Seri Adi | Baglamli Ad | Durum | Rol | Birim | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `TP.AB.A02` | A.1_DIŞ VARLIKLAR(Bin TL) | A.1_DIŞ VARLIKLAR(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A10` | P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL) | P.1_TOPLAM DÖVİZ YÜKÜMLÜLÜKLERİ(Bin TL) | derived_input | stock_total | Bin TL | - |
| `TP.AB.A11` | P.1a_Dış Yükümlülükler(Bin TL) | P.1a_Dış Yükümlülükler(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A13` | P.1ba_Kamu ve Diğer Döviz Mevduatı(Bin TL) | P.1ba_Kamu ve Diğer Döviz Mevduatı(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.A14` | P.1bb_Bankalar Döviz Mevduatı(Bin TL) | P.1bb_Bankalar Döviz Mevduatı(Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.AB.C1` | Altın(Milyon ABD Doları) | Altın(Milyon ABD Doları) | derived_input | balance_sheet_line | Milyon ABD Doları | - |
| `TP.AB.C2` | Döviz(Milyon ABD Doları) | Döviz(Milyon ABD Doları) | derived_input | balance_sheet_line | Milyon ABD Doları | - |
| `TP.AB.N06` | Net Rezerv TL (Bin TL) | Net Rezerv TL (Bin TL) | derived_input | balance_sheet_line | Bin TL | - |
| `TP.DK.USD.A.YTL` | (USD) ABD Doları (Döviz Alış) | (USD) ABD Doları (Döviz Alış) | derived_input | ratio_input | USD | - |
| `TP.DOVVARNC.K18` | Swap (Aylik, MB) | Swap (Aylik, MB) | listed_only | dormant_candidate | Aylik, MB | - |

## Source Dependency Eslestirme

| ID | Baslik | Kaynak Turu | Zorunluluk | Bagli Temalar | Bagli Gostergeler | Notlar |
| --- | --- | --- | --- | --- | --- | --- |
| `source:rzrv-swap-pdf` | TCMB swap PDF | pdf_table | required_input | theme:reserves, theme:net-reserve-estimate | - | - |
| `source:rzrv-manual-swap-ledger` | Manuel swap ledger | manual_inline | required_input | theme:net-reserve-estimate | - | - |

## Belirsizlikler

- TP.DOVVARNC.K18 aktif akis disi triple-quoted bloktan izlenir; dormant candidate olarak korunur.
- Resmi seri adlarinin bir bolumu notebook output fallback'inden gelir.
-
