# TCMB Rezerv Hesaplamalarında Tarih Cut-off'ları ve Veri Davranış Kuralları

> **Amaç:** TCMB rezerv hesabında zaman içinde değişen seri yapıları, eksik/placeholder veriler ve özel manuel patch'leri tek bir referans dokümanda toplamak. Python pipeline ve agent geliştirmede bu cut-off'ların hesaba katılması zorunludur.

## 1) 2018-08-31 — Yurtiçi Banka Döviz Yükümlülük Ayrışması

### Davranış

EVDS'de yurtiçi bankaların TCMB'ye karşı döviz yükümlülükleri yaklaşık **2018-08-31 tarihinden itibaren** iki ayrı seriye ayrıldı:

```python
yiBank = if Tarih < #date(2018, 8, 31)
         then TP.BL085                          # Pre-2018: toplam tek kalemde
         else (TP.BL129 + TP.BL131)             # Post-2018: ayrışmış (depo + teminat)
```

| Dönem | Seri | İçerik |
|---|---|---|
| **< 2018-08-31** | TP.BL085 | Yurtiçi Banka Toplam YP Yükümlülük (depo + teminat birleşik) |
| **≥ 2018-08-31** | TP.BL129 + TP.BL131 | Depo (BL129) + Teminat (BL131) ayrı |

### Neden Önemli?

Net Döviz Rezervi formülünde **yiBank** kalemi yükümlülük tarafında yer alır. Yanlış yol seçilirse:
- Pre-2018 + post yöntem → null değer, hesap fail eder
- Post-2018 + pre yöntem → BL085 placeholder veya yanlış değer

### Etkilenen Indicator'lar

- `derived:tcmb-net-doviz-rezervi`
- `derived:tcmb-swap-haric-net-doviz`
- `derived:tcmb-swap-haric-net-rezerv-gunluk`

### Pre-2018 Teyit Toleransı

Pre-2018 dönemde BL085 içinde altın teminat (BL132) da kısmen karışık geliyordu. Bu nedenle teyit sütunu (NetAltin + NetDoviz - NIR) **~1.3 milyar USD farkı normal** kabul edilir; flag null döner.

```python
# v9 Power Query M kodu (satır 2036-2038):
elif tarih_ <> null and tarih_ < #date(2018, 8, 31)
    then null   # Pre-2018: tolerans uygula, flag verme
else
    Number.Abs(fark) <= 0.001
```

---

## 2) BL097 Pre-2018 Placeholder Filtresi

### Davranış

EVDS'de TP.BL097 (Yurtdışı Banka Toplam YP Yükümlülük) pre-2018 dönemde zaman zaman **~1,000 Bin TL** gibi sembolik placeholder değerler içerir; gerçek değer genellikle 100,000 Bin TL üzerindedir.

### Filtre Kuralı

```python
bl097Ok = BL097 != null and BL097 > 100,000   # 100K Bin TL eşiği
```

- BL097 ≤ 100K → null sayılır → yük hesabında 0 gibi işlenir
- BL097 > 100K → gerçek veri kabul edilir, fallback formülünde kullanılır

### Etkilenen Hesap

`derived:tcmb-bl140-etkin` üç katmanlı fallback:

```python
BL140Etkin = (
    BL140                              if BL140 != null
    else (BL097 - BL141Etkin)          if BL097 > 100,000 AND BL141Etkin != null
    else BL097                          if BL097 > 100,000
    else null
)
```

---

## 3) ~2021 — PDF Altın Swap Kalemi Görünmeye Başladı

### Davranış

TCMB Taraflı Swap PDF'inde altın swap kalemleri yaklaşık **2021 yılından itibaren** görünmeye başladı. Pre-2021 PDF'lerde altın swap detayı yoktur.

### Etkilenen Indicator

`derived:tcmb-swap-haric-net-altin` iki yollu fallback:

```python
SH Net Altın = (
    NetAltin - PDFAltinSwap         if PDFAltinSwap != null   # 2021+
    NetAltin + DigerSwapURDL        if PDFAltinSwap == null   # Pre-2021 fallback
    NetAltin                         if her ikisi de null
)
```

Pre-2021 dönem için URDL'in **TP.DOVVARNC.K23** ("Diğer Swap") kalemi tüm non-MB swap'ları içerdiği için pratikte yeterli yaklaşımdır.

### Tarih Hassas Kullanım

PDF veri tarih başlangıcı genellikle 2021-01-04 civarındadır. Tam başlangıç tarihi PDF'in mevcut olmasına bağlıdır; `TcmbTarafliSwapPdf_Table` sorgusu PDF'i her seferinde yeniden çeker.

---

## 4) BL142 Backfill (İlk Geçerli Değer Yayma)

### Davranış

TP.BL142 (Yurtdışı Banka Altın Yükümlülük, Safi Gram) verisinin **ilk geçerli değeri** zaman serisinin başındaki tüm null tarihlere doldurulur (yalnızca BAŞLANGIÇ yönünde).

### Power Query Karşılığı (M kodu satır 1268-1277)

```python
BL142List  = Table.Column(Sorted0, "Yurtdışı Banka Altın Yükümlülük (Safi Gram)")
FirstBL142 = let nz = List.RemoveNulls(BL142List)
             in if List.Count(nz) > 0 then nz{0} else null

BL142Filled = Table.TransformColumns(Sorted0, {
    {"Yurtdışı Banka Altın Yükümlülük (Safi Gram)",
     each if _ = null then FirstBL142 else _,
     type number}
})
```

### Sebep

BL142 yayını başlamadan önceki dönemlerde de **türetilmiş Bin TL karşılığı** hesaplanabilsin diye:

```python
Türetilen (Bin TL) = TP.BL142 × İmaEdilenGramAltinTL / 1000
```

Eğer BL142 başlangıçta null ise türetilen hesap fail eder; backfill bu sorunu çözer.

### Önemli Sınır

Backfill yalnızca **BAŞLANGIÇ** yönündedir. Orta veya son tarihlerdeki nulllar **ASLA** doldurulmaz — gerçek veri eksikliğini gizlememek için.

### Python Port Önerisi

```python
df['BL142_filled'] = df['BL142'].copy()
first_valid_idx = df['BL142'].first_valid_index()
if first_valid_idx is not None:
    first_valid_value = df.loc[first_valid_idx, 'BL142']
    # Sadece başlangıçtaki null'ları doldur
    df.loc[:first_valid_idx, 'BL142_filled'] = df.loc[:first_valid_idx, 'BL142_filled'].fillna(first_valid_value)
```

---

## 5) 20.03.2026 → 19.03.2026 Hardcoded Patch (PDF)

### Davranış

TCMB Taraflı Swap PDF'inde **20.03.2026 tarihinin verisi eksik**. Excel M kodu bu eksikliği şu kuralla telafi eder:

- 19.03.2026 satırı kopyalanır
- Tarihi 20.03.2026 olarak yeniden etiketlenir
- Sonuç tabloya eklenir

### Power Query Karşılığı (M kodu satır 2536-2558)

```python
MissingDate  = #date(2026, 3, 20)
SourceDate   = #date(2026, 3, 19)

AlreadyHasMissing = List.Contains(Table.Column(AddAltinNet, "Tarih"), MissingDate)

SourceRow = Table.SelectRows(AddAltinNet, each [Tarih] = SourceDate)

PatchedRow =
    if Table.RowCount(SourceRow) = 0 then null
    else Table.TransformColumns(SourceRow, {{"Tarih", each MissingDate, type date}})

AddNet2 =
    if AlreadyHasMissing or PatchedRow = null
    then AddAltinNet                       # Zaten varsa veya kaynak yoksa dokunma
    else Table.Combine({AddAltinNet, PatchedRow})
```

### Python Port Önerisi (Dinamik)

Hardcoded date yerine, eksik tarihleri otomatik tespit eden algoritma:

```python
def patch_missing_dates(df, expected_freq='B'):
    """Beklenen iş günü frekansında eksik tarihleri önceki gün verisi ile doldur."""
    expected_dates = pd.date_range(df.index.min(), df.index.max(), freq=expected_freq)
    missing = expected_dates.difference(df.index)
    for missing_date in missing:
        prior_date = df.index[df.index < missing_date].max()
        if pd.notna(prior_date):
            new_row = df.loc[prior_date].copy()
            new_row.name = missing_date
            df = pd.concat([df, new_row.to_frame().T])
    return df.sort_index()
```

---

## 6) Sentetik Bilanço Satırı (TcmbGunlukBilanco_USD_Swap)

### Davranış

Haftalık vaziyetin Cuma kapanışı bazen günlük bilançoda eksik olabiliyor (örn. resmi tatil). Bu durumda M kodu son geçerli iş gününün bilanço değerlerini kullanarak sentetik bir satır oluşturur.

### Power Query Karşılığı (M kodu satır 717-739)

```python
MakeSyntheticBilancoRecord = (missingDate as date) as nullable record =>
    let
        PriorRows = Table.SelectRows(BilancoUSD_Buffer, each [Tarih] < missingDate),
        LastRow = if Table.IsEmpty(PriorRows)
                  then null
                  else PriorRows{Table.RowCount(PriorRows) - 1},
        SyntheticRecord =
            if LastRow = null
            then null
            else Record.Combine({[Tarih = missingDate], Record.RemoveFields(LastRow, {"Tarih"})})
    in
        SyntheticRecord
```

### Etkilenen Hesap

Günlük analitik bilanço bazlı tahminler — özellikle haftalık rezerv hesaplarıyla join sırasında.

---

## 7) URDL vs PDF İşaret Kuralı

### Kritik Konvansiyon Farkı

Aynı swap kavramı için iki kaynak **TERS işaret** kullanır:

| Kaynak | Net Pozisyon İşareti | Düzeltme Yönü |
|---|---|---|
| **URDL** | NEGATİF (rezervi şişirici) | NetRezerv **+ URDL** |
| **PDF** | POZİTİF (TCMB net alacaklı) | NetRezerv **− PDF** |

### Kaynak (M kodu satır 1940-1944)

```python
# 12) SWAP HARİÇ NET REZERV
# İşaret kuralı:
#   URDL (haftalık/aylık): net alım = negatif → NIR'a EKLEME yapar
#                          (rezerv şişik görünür) → toplama doğru düzeltme
#   PDF: net alım = pozitif → NIR'dan ÇIKARMA yapar (gerçek alacaklı)
```

### Pratik Sonuç

```python
# SH Net Altın
if PDFAltinSwap is not None:
    SH_NetAltin = NetAltin - PDFAltinSwap     # PDF: çıkarma
else:
    SH_NetAltin = NetAltin + DigerSwap_URDL   # URDL: toplama (URDL negatif)

# SH Net Döviz
mbAdj = MBSwap_URDL  # Her zaman URDL'den
if PDFFXSwap is not None:
    SH_NetDoviz = NetDoviz + mbAdj - PDFFXSwap        # M.B. URDL toplama, PDF çıkarma
else:
    fxUrdl = SwapTotURDL - MBSwap_URDL
    SH_NetDoviz = NetDoviz + mbAdj + fxUrdl          # Her ikisi URDL: toplama
```

---

## 8) Ana Test Vakaları (Python Pipeline için)

Pipeline implementasyonunda aşağıdaki test vakaları **mutlaka** kontrol edilmeli:

| # | Test Vakası | Beklenen Davranış |
|---|---|---|
| 1 | Tarih = 2017-01-15 | yiBank = BL085, teyit flag null |
| 2 | Tarih = 2018-09-01 | yiBank = BL129+BL131, teyit ≤ 0.001 |
| 3 | Tarih = 2018-08-30 (cusp) | yiBank = BL085 |
| 4 | Tarih = 2018-08-31 | yiBank = BL129+BL131 (≥ kullanır) |
| 5 | BL097 = 1000 (placeholder) | BL140Etkin null veya BL140 fallback |
| 6 | BL097 = 250000 (gerçek) | BL140Etkin = BL097-BL141Etkin |
| 7 | BL142 başlangıçta null | İlk geçerli değer backfill |
| 8 | BL142 ortada null | Null kalır (backfill uygulamamalı) |
| 9 | Tarih = 2020-06-01 (pre-2021) | PDF altın swap null → URDL fallback |
| 10 | Tarih = 2022-06-01 (post-2021) | PDF altın swap kullanılır |
| 11 | Tarih = 2026-03-20 (eksik) | 19.03 verisi kopyalanır |
| 12 | Resmi tatil (haftalık ZIP yok) | Sentetik bilanço kaydı yaratılır |

---

## Referanslar

- **v9 Power Query M kodu:** `Excels/_v9_extracted/_section1.m`
- **Excel dosyası:** `Excels/Rezerv_Apko_queryleri_korunmus_v9.xlsm`
- **Memory:** `~/.claude/projects/.../memory/project_evds_registry.md`

## Versiyon Geçmişi

| Tarih | Değişiklik |
|---|---|
| 2026-05-05 | İlk versiyon, v9 Excel'den türetildi |
