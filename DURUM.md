# Proje Durumu

> Son güncelleme: 2026-04-22

## Neredeyiz?

Faz 5a tamamlandı. Kayıt Agent canlı, Econ Platform'da onay API'si hazır.

## İki Proje

| Proje | Dizin | Durum |
|-------|-------|-------|
| EVDS Registry | `İş Kodlama/İş Agentı` | ✅ Faz 5a bitti |
| Econ Platform | `Model/Econ` | ✅ /api/registry endpoint'leri hazır |

## Registry Sayıları (audit: 0 sorun)

```
series: 231  •  indicator: 62  •  theme: 18  •  source_dep: 21
```

## Kayıt Agent — Tamamlanan Bileşenler

| Bileşen | Dosya | Durum |
|---------|-------|-------|
| GapDetector | `src/evds_registry/agent/gap_detector.py` | ✅ |
| Enricher | `src/evds_registry/agent/enricher.py` | ✅ |
| DraftWriter | `src/evds_registry/agent/draft_writer.py` | ✅ |
| RegistryWriter | `src/evds_registry/agent/registry_writer.py` | ✅ |
| MCP Gap Hook | `src/evds_registry/mcp_server.py` | ✅ |
| Econ Platform API | `Model/Econ/routers/registry.py` | ✅ |

## Kayıt Agent Akışı

```
registry_fetch("TP.BILINMEYEN.X01")
  → GapDetector: registry'de yok
  → Enricher: EVDS catalog'dan metadata çek, LLM ile tema öner
  → DraftWriter: drafts/ klasörüne yaz (flag'li)
  → Yanıtta gap_drafts bildirimi

GET /api/registry/drafts   → bekleyen taslaklar
POST /api/registry/approve → onayla → registry'e yaz
POST /api/registry/reject  → reddet → sil
```

## Sıradaki: Faz 5b — Analiz Agent'ları

```
Faz 5b  →  Cari / TÜFE / Rezerv / Beklenti Agent
Faz 5c  →  Orkestratör
Faz 5d  →  Econ Platform'a /api/chat entegrasyonu
```

## Test Durumu

```
tests/agent/ → 23 test, 23 PASS
```

## Teknik Hazırlık

| Bileşen | Durum |
|---------|-------|
| EVDS Registry MCP | ✅ Hazır (6 tool + gap detection) |
| Kayıt Agent | ✅ Hazır |
| Qwen API | ✅ Çalışıyor (dashscope-intl) |
| GitHub remote | ✅ https://github.com/kalemera/-Agent.git |
| EVDS API | ✅ Key ayarlı |

## Bilinen Tuzaklar

- **YAML colon:** `title` alanında `:` varsa `"..."` içine al, yoksa YAML patlar
- **Qwen endpoint:** `dashscope-intl.aliyuncs.com` (uluslararası), `dashscope.aliyuncs.com` değil
- **REGISTRY_ROOT:** `Model/Econ/.env` dosyasına eklenmeli (gitignore'da, elle yönetilir)
