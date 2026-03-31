# Faz 2 — Genelleme ⏳

> Durum: Bekliyor (Faz 1 tamamlanınca başlar)
> Hedef: DTH'ye özel hardcoded mantığı spec-driven mimariye dönüştür, 7 notebook'u destekle

## Sorun: Hardcoded DTH Mantığı

`src/evds_registry/notebook_analysis.py` şu an yalnızca DTH notebook'u için çalışıyor:

```python
# SADECE HPBITABLO ailesini yakalar
TICKER_PATTERN = re.compile(r"TP\.HPBITABLO[2345]\.\d+")

# 30+ satır if-else zinciri — her yeni notebook için yeni zincir gerekir
def role_for(ticker: str) -> str:
    if ticker.startswith("TP.HPBITABLO2"):
        return "input"
    if ticker == "TP.HPBITABLO5.001":
        return "calculated"
    ...
```

**Diğer 6 notebook'un kullandığı ticker aileleri:**
- `TP.BEK.*` — Beklenti anketi
- `TP.PKAUO.*` — Para ve kur
- `TP.AB.*` — Altın ve döviz
- `TP.DK.*` — Döviz kurları
- `TP.DIBSPIYDEG.*` — DİBS piyasa verileri
- `TP.EBONDPIYDEG.*` — Eurobond verileri

## Çözüm: NotebookSpec Mimarisi

### 2.1 NotebookSpec Veri Yapısı

**Yeni dosya:** `src/evds_registry/notebook_spec.py`

```python
@dataclass
class SeriesRoleRule:
    """Bir ticker pattern'ini bir role eşler."""
    pattern: str          # regex veya prefix, örn: "TP.HPBITABLO2"
    role: str             # input | calculated | reference | label | metadata
    status: str           # active | deprecated | unknown

@dataclass
class NotebookSpec:
    slug: str             # örn: "dth-blg-v7"
    display_name: str     # örn: "DTH Bilgi Notu V7"
    ticker_patterns: list[str]   # Bu notebook'ta geçen ticker regex'leri
    role_rules: list[SeriesRoleRule]
    default_role: str = "unknown"
    default_status: str = "active"
    lane: str = "L1"      # L1 | L2 | L3
```

**Spec tanımları:** `src/evds_registry/specs/` klasörü altında YAML dosyaları

```yaml
# src/evds_registry/specs/dth-blg-v7.yaml
slug: dth-blg-v7
display_name: DTH Bilgi Notu V7
lane: L1
ticker_patterns:
  - "TP\\.HPBITABLO[2345]\\.\\d+"
role_rules:
  - pattern: "TP\\.HPBITABLO2\\."
    role: input
    status: active
  - pattern: "TP\\.HPBITABLO5\\.001"
    role: calculated
    status: active
default_role: reference
default_status: active
```

### 2.2 Genel `analyze-notebook` Komutu

**Mevcut durum:**
- `analyze-dth-notebook` → sadece DTH
- `analyze-notebook --spec auto` → spec'i dosya adından tahmin etmeye çalışıyor ama gerçek genelleme yok

**Yapılacak:**
`build_notebook_analysis()` fonksiyonuna `NotebookSpec` parametresi ekle.
`--spec auto` modunda dosya adı → slug eşleştirmesi:

```python
FILENAME_TO_SPEC = {
    "DTH_Blg": "dth-blg-v7",
    "Eurobnd_Blg": "eurobnd-blg-v4",
    "PrBnk_MnklKymt": "prbunk-mnkl-kymt-v5",
    "Pys_Ktlmclr": "pys-ktlmclr-v2",
    "Rzrv_Blg": "rzrv-blg-v7",
    "Tbl_Apko": "tbl-apko",
    "Yi_Yrlsk": "yi-yrlsk-fnsl-vrlk-v1",
}
```

### 2.3 Kalan 5 Notebook Spec Dosyası

Her notebook için `tasks/notebook_semantics/0X_*.md` dosyasındaki spec bilgileri YAML'a dönüştürülecek:

| Notebook | Lane | Ticker Ailesi | Öncelik |
|----------|------|--------------|---------|
| Eurobnd_Blg_V4 | L1 | TP.EBONDPIYDEG | Yüksek |
| Rzrv_Blg_V7 | L1 | TP.AB, TP.DK | Yüksek |
| PrBnk_MnklKymt_V5 | L1 | TP.PKAUO | Orta |
| Pys_Ktlmclr_V2 | L1 | TP.BEK | Orta |
| Yi_Yrlsk_Fnsl_Vrlk_V1 | L2* | karma | Orta |
| Tbl_Apko | L3 | TP.DIBSPIYDEG + multi-freq | Düşük |

*Yi_Yrlsk L1 olarak işaretlenmiş ama dış kaynak içeriyor → L2'ye taşınmalı (bkz. REVIEW.md Sorun 11)

### 2.4 Frekans Hizalama Kuralları

Tbl_Apko notebook'u günlük/haftalık/aylık/çeyreklik verileri bir arada kullanıyor.

**SHARED_SPEC.md'ye eklenecek kurallar:**
```
Frekans hizalama:
- Yüksek frekans → düşük frekansa dönüşüm: son değer | ortalama | toplam
- Düşük frekans → yüksek frekansa dönüşüm: forward-fill (izin verilmez, doc'a not düşülür)
- İndikatör output_frequency tanımlanmalı
```

**Dosya:** `tasks/notebook_semantics/00_SHARED_SPEC.md` — §4 Frekans bölümü ekle

### 2.5 Çakışma Tespiti

Aynı ticker farklı notebook'larda farklı rol/frekans alabilir.

**Yeni komut:** `registry check-conflicts`
```
Ticker: TP.AB.A01
  DTH notebook: role=input, freq=monthly
  Rzrv notebook: role=reference, freq=monthly
  → ÇAKIŞMA: rol farklı (input vs reference)
```

**Dosya:** `src/evds_registry/cli.py` → yeni subcommand
`src/evds_registry/storage.py` → cross-notebook lookup

## Başarı Kriterleri

- [ ] `NotebookSpec` veri yapısı ve YAML loader mevcut
- [ ] DTH spec YAML dosyası oluşturulmuş ve mevcut hardcoded mantık refactor edilmiş
- [ ] En az 3 notebook için spec YAML dosyası tamamlanmış
- [ ] `analyze-notebook --spec auto` 7 notebook dosya adını tanıyor
- [ ] Frekans hizalama kuralları SHARED_SPEC.md'de tanımlı
- [ ] `check-conflicts` komutu çakışmaları raporluyor
