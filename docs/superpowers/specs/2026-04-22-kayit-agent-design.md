# Kayıt Agent — Tasarım Spec

**Tarih:** 2026-04-22  
**Durum:** Onay bekliyor  
**Proje:** `İş Kodlama/İş Agentı`

---

## Problem

Yeni bir veri serisi veya indikatör kullanıldığında (notebook, fetch, analiz) registry'de kayıtlı olmayabilir. Şu an bu boşluk manuel fark ediliyor ve manuel dolduruluyor. Kayıt Agent bu süreci otomatize eder.

---

## Hedef Davranış

```
Bilinmeyen öğe tespit edilir
  → Qwen kaynağı + metadatayı çıkarır
  → drafts/ klasörüne şüpheli flag'lerle taslak yazar
  → Econ Platform'da bildirim gösterir
  → Kullanıcı tek tıkla onaylar / düzenler / reddeder
  → Onaylanan kayıt registry'e yazılır, audit çalışır
```

---

## Tetikleyiciler

### Trigger 1 — Fetch Gap (Faz 5a öncelik)
`registry_fetch("TP.XYZ")` çağrıldığında ticker registry'de yoksa Gap Detector devreye girer.

### Trigger 2 — Notebook Gap (Faz 5a, Trigger 1 sonrası)
`registry_analyze(notebook)` sonucunda dönen `unresolved_items` listesi varsa Gap Detector devreye girer.

> **Not:** Pasif dosya izleme (watcher) kapsam dışı — alert fatigue riski yüksek.

---

## Mimari

```
[Trigger]
    ↓
[Gap Detector]         gap_detector.py
"Bu ID registry'de var mı?"
    ↓ yok
[Source Detector]      enricher.py
"Kaynak ne? (EVDS / TÜİK / manuel / diğer)"
Qwen kod context'inden çıkarır, şüpheliyse sorar
    ↓
[Enricher]             enricher.py
• EVDS ise  → EVDS catalog'dan birim/frekans/başlık
• TÜİK ise  → source_dependency bağlantısı + pipeline notu
• Manuel    → kullanıcıdan minimal bilgi ister
• LLM       → tema önerisi + ekonomik anlam + confidence skoru
    ↓
[Draft Writer]         draft_writer.py
drafts/ klasörüne yazar
şüpheli alanlar flaglanır (confidence < 0.7 → 🟡, bulunamadı → 🔴)
    ↓
[Econ Platform API]    routers/registry.py (Model/Econ)
GET  /api/registry/drafts    → bekleyen taslakları listele
POST /api/registry/approve   → onayla → registry'e yaz
POST /api/registry/reject    → reddet → drafts'tan sil
    ↓
[Registry Writer]      registry_writer.py
registry/series/ veya indicators/ veya themes/ altına yazar
YAML'da : içeren değerleri otomatik tırnak içine alır
audit çalıştırır → 0 issue doğrular
```

---

## LLM Soyutlaması

**Kritik:** Agent Qwen'e değil `LLMClient` interface'ine bağlanır.  
`src/evds_registry/llm.py` içindeki mevcut `LLMClient` Protocol'ü kullanılır.  
`LLM_PROVIDER=qwen|ollama|disabled` — provider değişirse agent kodu değişmez.

```python
# Doğru
llm: LLMClient = build_llm_client()
llm.generate_structured(prompt, schema)

# Yanlış
client = QwenClient()  # provider'a sabitlenmiş
```

---

## Şüpheli Flaglama

| Durum | Flag | Aksiyon |
|-------|------|---------|
| Confidence < 0.7 | 🟡 | Kullanıcıya highlight göster |
| Ticker EVDS catalog'da yok | 🔴 | "Manuel gir" alanı aç |
| 2+ tema eşleşiyor | 🟡 | Seçim dropdown'u göster |
| Başlıkta `:` var | ⚙️ | Otomatik tırnak — sessiz |
| input_ids boş (non-EVDS) | ℹ️ | "Kaynak: source_dependency" notu |

---

## Bileşenler ve Sorumluluklar

| Dosya | Sorumluluk | Bağımlılıklar |
|-------|-----------|---------------|
| `agent/gap_detector.py` | ID registry'de var mı kontrol | `storage.py` |
| `agent/enricher.py` | Kaynak tespiti + metadata zenginleştirme | `llm.py`, `evds_catalog.py` |
| `agent/draft_writer.py` | Flaglı taslak oluştur, drafts/'a yaz | `records.py` |
| `agent/registry_writer.py` | Onaylanan taslağı registry'e yaz, audit çalıştır | `storage.py`, `mcp_server.py` |
| `Model/Econ/routers/registry.py` | REST API (drafts/approve/reject) | Registry modülü |

---

## Kontrol Yapısı

| Agent / Bileşen | Kontrolör | Tetikleyici |
|-----------------|----------|-------------|
| Gap Detector | `registry_fetch` / `registry_analyze` | Otomatik — her bilinmeyen ID'de |
| Enricher | Gap Detector | Gap tespit edilince |
| Draft Writer | Enricher | Enrichment tamamlanınca |
| Registry Writer | **Sadece kullanıcı onayı** | Başka tetikleyici yok |

> **Kural:** Registry Writer manuel onay olmadan asla çalışmaz.

---

## İnşa Sırası (Faz 5a)

1. `gap_detector.py` + testler
2. `enricher.py` (EVDS path önce, TÜİK sonra) + testler
3. `draft_writer.py` + testler
4. `registry_writer.py` + testler
5. `routers/registry.py` (Econ Platform API)
6. Entegrasyon testi — uçtan uca akış

---

## Kullanılacak Skill'ler ve Agent'lar

| Aşama | Skill / Agent | Kontrolör |
|-------|--------------|----------|
| Mimari onay | `architect` agent | Ana agent (ben) |
| Her modül implementasyonu | `backend-dev` agent | Ana agent |
| Her modül testi | `tdd-guide` skill + `arbiter` agent | `backend-dev` |
| Kod review | `code-reviewer` agent | Ana agent |
| Final kalite kapısı | `verifier` agent | Ana agent |
| Python kalite | `python-reviewer` agent | `code-reviewer` |

---

## Kapsam Dışı (Bu Spec'te Yok)

- Pasif dosya izleme (watcher)
- Otomatik GitHub push
- Toplu batch onay
- Frontend chat widget (Econ Platform için ayrı spec)
