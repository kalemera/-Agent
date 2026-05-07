# Analist Agent Sistemi Codemap

**Last Updated:** 2026-05-07
**Module Root:** `src/evds_registry/agent/`
**Extraction:** Python `ast`

## Amaç

Pipeline çıktılarını (`RezervSnapshot`, `TUFESnapshot`, vs.) tüketip kullanıcının
doğal dildeki sorularını intent classification ile yanıtlayan analist agent'lar.
`BaseAnalystAgent` ortak çekirdek; her domain (rezerv, tüfe, …) kendi subclass'ını
yapar.

> Kayıt yönetimi tarafındaki agent'lar (`draft_writer`, `enricher`, `gap_detector`,
> `registry_writer`) bu codemap'in kapsamı dışında — registry pipeline'ına aittir.

## Modüller

| Dosya | Sınıf / Fonksiyon | Rol |
|---|---|---|
| `base_analyst.py` | `BaseAnalystAgent`, `IntentDefinition`, `AnalystResponse` | Genişletilebilir analist çekirdeği |
| `tufe_analyst_agent.py` | `TUFEAnalystAgent`, `TUFESnapshot` | TÜFE/enflasyon (5 intent) |
| `rezerv_analyst_agent.py` | `RezervAnalystAgent`, `RezervAnalystResponse` | TCMB rezerv (8 intent) |
| `draft_writer.py`, `enricher.py`, `gap_detector.py`, `registry_writer.py` | (registry pipeline) | Kayıt agent'ları — bu codemap kapsamı dışı |

> **Not:** Bağımsız bir `orchestrator.py` modülü henüz yok. DURUM.md "Faz 7" altında
> mevcut chat orchestrator'a `RezervAnalystAgent` entegrasyonu sonraki seansa bırakılmış.

## Sınıf Hiyerarşisi

```
                    BaseAnalystAgent
                    (base_analyst.py)
                    │
                    │  INTENTS: list[IntentDefinition]
                    │  handle(query) → str
                    │  response(query) → AnalystResponse
                    │  classify_intent(query) → str | None
                    │  add_intent / remove_intent / list_intents
                    │  _build_response, safe_get, format_number, ...
                    │
        ┌───────────┴───────────┬──────────────────────┐
        ▼                       ▼                      ▼
  TUFEAnalystAgent        RezervAnalystAgent     (gelecek: CariAgent,
  (tufe_analyst_agent.py) (rezerv_analyst_      BeklentiAgent, ...)
                           agent.py)
   • 5 intent              • 8 intent (legacy)
   • IntentDefinition      • INTENT_RULES dict
     pattern               • dispatch tablosu
```

> **Migrasyon notu:** `RezervAnalystAgent` henüz `BaseAnalystAgent`'tan tam türemedi —
> kendi `_normalize_query`, `classify_intent`, `_format_*` helper'larını barındırıyor.
> `TUFEAnalystAgent` modern `IntentDefinition` API'sini kullanıyor; rezerv için aynı
> migrasyon Faz 7 kapsamında planlı.

## `BaseAnalystAgent` (base_analyst.py)

### Public API

| Sembol | Tip | Açıklama |
|---|---|---|
| `IntentDefinition` | dataclass | `name`, `keywords` (AND/OR liste), `handler`, `priority`, `description` |
| `AnalystResponse` | dataclass | `intent`, `text`, `data`, `snapshot_date` |
| `BaseAnalystAgent.__init__(snapshot)` | method | Snapshot'ı bağlar, intent listesini priority'ye göre sıralar |
| `handle(query)` | method | Sorudan metin yanıt üretir |
| `response(query)` | method | Sorudan yapılandırılmış `AnalystResponse` üretir |
| `classify_intent(query)` | method | Query'den intent çıkarır (None döner eşleşme yoksa) |
| `add_intent(intent_def)` | method | Runtime'da yeni intent ekler |
| `remove_intent(name)` | method | Intent'i kaldırır |
| `list_intents()` | method | Priority sırasında tüm intent'leri döner |

### Yardımcılar (subclass handler'ları için)

| Sembol | Açıklama |
|---|---|
| `_build_response(intent, text, data, snapshot_date)` | `AnalystResponse` üretir |
| `safe_get(df, col, idx)` | DataFrame'den güvenli skaler (eksikse None) |
| `change_from_n_periods_ago(df, col, n)` | Son değer - N dönem öncesi |
| `format_number(value, unit, decimals)` | "55.10%" gibi format (None → "veri yok") |
| `format_change(diff, unit)` | İşaretli "+2.70%" string |
| `_latest_date()` | Snapshot'tan son tarihi çıkarır |
| `_help_text()` | Hiçbir intent eşleşmediğinde gösterilen mesaj |
| `normalize_tr(text)` | TR karakter + lowercase normalize (modül seviyesi) |

## `TUFEAnalystAgent` (tufe_analyst_agent.py)

### Snapshot Şeması

`TUFESnapshot.data` DataFrame'inde beklenen sütunlar:

| Sütun | İçerik | Örnek |
|---|---|---|
| `tufe_genel` | TÜFE endeksi | 107.85 |
| `tufe_yillik_pct` | Yıllık % değişim | 55.10 |
| `tufe_aylik_pct` | Aylık % değişim | 2.70 |
| `cekirdek_b_yillik` | Çekirdek B yıllık | 52.00 |
| `cekirdek_c_yillik` | Çekirdek C yıllık | 50.00 |
| `gida_yillik` (ops) | Gıda grubu yıllık | — |
| `enerji_yillik` (ops) | Enerji grubu yıllık | — |
| `hizmet_yillik` (ops) | Hizmet grubu yıllık | — |

### Intent'ler (5 + curated keyword örnekleri)

| Intent | Handler | Örnek Sorular |
|---|---|---|
| `tufe_yillik` | `_handle_tufe_yillik` | "yıllık TÜFE", "annual inflation" |
| `tufe_aylik` | `_handle_tufe_aylik` | "aylık TÜFE", "monthly inflation" |
| `cekirdek_tufe` | `_handle_cekirdek_tufe` | "çekirdek enflasyon", "core CPI" |
| `kategori_kirilim` | `_handle_kategori_kirilim` | "gıda + enerji", "kategori bazlı" |
| `tufe_genel_durum` | `_handle_tufe_genel_durum` | "TÜFE özet", "genel enflasyon" |

> Modül docstring'i 2 ek `IntentDefinition` örneği gösteriyor (örnek subclass), pratik
> olarak şu an aktif 5 intent var; toplam `IntentDefinition(...)` referansı 7.

## `RezervAnalystAgent` (rezerv_analyst_agent.py)

### Snapshot Tipi

`RezervSnapshot` (bkz `docs/CODEMAPS/rezerv-pipeline.md`).
- `snapshot.calculated` — DataFrame (tüm hesaplanmış sütunlar)
- `snapshot.latest()` — En son tarih
- `snapshot.get_indicator(name)` — Tek bir indicator değeri

### Intent'ler (8)

| Intent | Handler | Konu |
|---|---|---|
| `brut_rezerv` | `_handle_brut_rezerv` | Brüt Rezerv (TP.AB.TOPLAM bazlı) |
| `net_rezerv` | `_handle_net_rezerv` | Net Uluslararası Rezerv (NIR) |
| `swap_haric` | `_handle_swap_haric` | Swap Hariç Net Rezerv |
| `gunluk_tahmin` | `_handle_gunluk_tahmin` | Günlük analitik bilanço bazlı tahmin |
| `altin` | `_handle_altin` | Altın kompozisyonu (Brüt / Net / SH) |
| `doviz` | `_handle_doviz` | Döviz kompozisyonu (Brüt / Net / SH) |
| `swap_breakdown` | `_handle_swap_breakdown` | TCMB swap pozisyonları kırılımı |
| `tarihsel` | `_handle_tarihsel` | Haftalık / aylık / YBB değişim |

### Modül-İçi Yardımcılar

`_normalize_query`, `classify_intent` (modül seviyesinde — sınıfa migre edilmedi),
`_format_milyar_usd`, `_format_change`, `_safe_get`, `_change_from_n_periods_ago`.
`RezervAnalystResponse` dataclass'ı `AnalystResponse` ile aynı yapıda ama ayrı duruyor.

## Kullanım Örnekleri

### TÜFE

```python
from evds_registry.agent.tufe_analyst_agent import TUFEAnalystAgent, TUFESnapshot

snapshot = TUFESnapshot(data=tufe_df)
agent = TUFEAnalystAgent(snapshot=snapshot)
print(agent.handle("Bu ay yıllık TÜFE ne kadar?"))
# → "TÜFE Yıllık: 55.10%, Aylık: +2.70%"
```

### Rezerv

```python
from evds_registry.rezerv import run_pipeline
from evds_registry.agent.rezerv_analyst_agent import RezervAnalystAgent

snapshot = run_pipeline(raw_evds, raw_urdl, raw_pdf)
agent = RezervAnalystAgent(snapshot)
print(agent.handle("Bu hafta brüt rezerv ne kadar?"))
# → "Brüt Rezerv: 168.9 milyar USD (2026-04-25)
#    Önceki haftaya göre: -7.7 milyar USD"
```

## Yeni Agent Nasıl Eklenir

### 1. Yeni domain için subclass

```python
from evds_registry.agent.base_analyst import BaseAnalystAgent, IntentDefinition

class CariAnalystAgent(BaseAnalystAgent):
    INTENTS = [
        IntentDefinition(
            name="cari_aylik",
            keywords=[
                ["cari", "aylık"],   # AND grubu
                ["current", "monthly"],
            ],
            handler="_handle_cari_aylik",
            priority=10,
        ),
    ]

    def _handle_cari_aylik(self, snapshot_date):
        val = self.safe_get(self.snapshot.data, "cari_aylik")
        return self._build_response(
            intent="cari_aylik",
            text=f"Cari açık (aylık): {self.format_number(val, ' Mr USD')}",
            data={"cari_aylik": val},
            snapshot_date=snapshot_date,
        )
```

### 2. Mevcut agent'a runtime'da intent ekle

```python
agent = TUFEAnalystAgent(snapshot=snapshot)
agent.add_intent(IntentDefinition(
    name="hizli_test",
    keywords=[["test"]],
    handler="_handle_test",
    priority=5,
))

import types
def my_handler(self, snapshot_date):
    return self._build_response(intent="hizli_test", text="Test cevabı")
agent._handle_test = types.MethodType(my_handler, agent)
```

### 3. Mevcut intent'i değiştir

Subclass'ta aynı isimli handler method'unu override et. Keyword'leri değiştirmek
istersen `INTENTS` listesini override et veya `add_intent()` / `remove_intent()`
çiftiyle dinamik yönet.

### Curated Keyword Tasarım Kuralları

`docs/registry-notes/` ve önceki seans öğrenimine (memory: `feedback_intent_routing.md`)
göre küçük modelde description-only prompt yetersiz; her intent için **2-4 keyword
grubu** + **explicit KURAL satırları** önerilir:

- Her grup AND ile bağlı (tüm kelimeler geçmeli)
- Gruplar arası OR (herhangi biri eşleşirse intent seçilir)
- TR + EN paralel grupları ekle (kullanıcı kod-switch yapıyor olabilir)
- `priority` ile çakışmaları çöz (düşük sayı önce)

## İlgili Dokümanlar

- `docs/CODEMAPS/rezerv-pipeline.md` — Snapshot üreten pipeline
- `docs/registry-notes/tcmb-rezerv-pipeline-design.md` — Pipeline tasarım kararları
- `tests/rezerv/test_agent.py` — 18 test (intent classification + handler çıktıları)
