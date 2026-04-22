---
record_type: indicator
id: derived:diger-yatirim-net
title: Diğer Yatırımlar Net (Bankalar + TCMB + Hazine + Özel Sektör)
status: approved
input_ids:
- evds:TP.ODANA6.Q20
- evds:TP.ODANA6.Q25
formula_expression: Q25 - Q20
formula_description: Net Yükümlülük Oluşumu eksi Net Varlık Edinimi
output_frequency: monthly
output_unit: Milyon USD
economic_meaning: >
  Bankalar, TCMB, Genel Hükümet ve Diğer Sektörlerin yurt dışı borçlanma/geri ödeme netleşmesi.
  Alt kalemler (3.5/3.6 seriler): Merkez Bankası, Genel Hükümet, Bankalar, Banka Dışı Sektörler.
  Swap, döviz swap ve dış borç roll-over dinamiklerini yansıtır.
validation_note: bie_odana6 veri grubundan — BPM6 analitik sunum. Alt kalem hesabı 3.5.x (varlık) ve 3.6.x (yükümlülük) prefix'i ile yapılır.
theme_ids:
- theme:cari-denge
- theme:external-financing
- theme:reserves-and-liquidity
---
# Diğer Yatırımlar Net

## Formül (Toplam)
Q25 (Net Yükümlülük) − Q20 (Net Varlık)

## Alt Kalem Formülleri (BPM6 Prefixleri)
| Alt Kalem | Varlık | Yükümlülük | Formül |
|-----------|--------|-----------|--------|
| Merkez Bankası | 3.5.1 (Q21) | 3.6.1 (Q26) | Q26 − Q21 |
| Genel Hükümet | 3.5.2 (Q22) | 3.6.2 (Q27) | Q27 − Q22 |
| Bankalar | 3.5.3 (Q23) | 3.6.3 (Q28) | Q28 − Q23 |
| Diğer Sektörler | 3.5.4 (Q24) | 3.6.4 (Q29) | Q29 − Q24 |

## Hesaplama Notu
Kod: `presentation_table.py::extract_row_value`
- Toplam: calculation="other_investment"
- Alt kalemler: calculation="cb_net" / "gov_net" / "banks_net" / "other_sectors_net"
- Sütun arama: `find_column_by_keywords(df, [kurum_adi, "3.5"])` varlık için, `["3.6"]` yükümlülük için
- **Önemli**: Eski BPM5 kodu "C.12"/"C.13" BPM6'da geçersiz — "3.5"/"3.6" kullanılır
