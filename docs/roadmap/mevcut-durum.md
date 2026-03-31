# Mevcut Durum ve Kararlar

> Son güncelleme: 2026-03-31

## Bu Oturumda Alınan Kararlar

### Mimari: 2 Agent

evds-registry tek başına büyütülmeyecek. evds-mcp ile çift katmanlı çalışacak:
- **evds-registry** = anlam/bilgi katmanı (bu proje)
- **evds-mcp** = veri/analiz katmanı (https://github.com/orhoncan/evds-mcp)

### LLM: Qwen (Alibaba Cloud DashScope)

Ollama Pro iptal edildi. Yeni LLM: Alibaba Cloud'un ücretsiz Qwen API'si.
- `LLM_PROVIDER=qwen`
- `QWEN_MODEL=qwen-turbo` (ücretsiz tier için)
- Endpoint: `https://dashscope.aliyuncs.com/compatible-mode/v1`
- API key `.env` dosyasına yazılacak (git'e girmez)

### Öncelik Sırası

1. Faz 1 (proposal backlog temizleme) — **şu an buradayız**
2. Faz 2 (NotebookSpec genelleme)
3. Faz 3 (evds-mcp entegrasyonu)
4. Faz 4 (akıllı agent) — uzun vade

## Bu Oturumda Yapılanlar

| İş | Dosya | Durum |
|----|-------|-------|
| Qwen LLM client | `src/evds_registry/llm.py` | ✅ |
| .env.example | `.env.example` | ✅ |
| add-source-dependency-draft | `src/evds_registry/cli.py` | ✅ |
| Git repo başlatıldı | `.git/` | ✅ |
| uv kuruldu | sistem | ✅ |
| Yol haritası yazıldı | `docs/roadmap/` | ✅ |

## Sonraki Oturumda Nereden Başlanacak

**Faz 1.1 — Proposal batch onayı:**

```bash
# 1. Bekleyen indicator proposal'larını gör
registry review-proposals --target-type indicator --status review_pending

# 2. LLM ile toplu onayla
registry auto-approve-proposals --target-type indicator --min-confidence 0.75

# 3. Theme'ler için aynısı
registry auto-approve-proposals --target-type theme --min-confidence 0.70

# 4. Kalan'ları manuel incele
registry review-proposals --status review_pending
```

**Faz 1.2 — Source dependency girişi:**

```bash
# Yi_Yrlsk ve Tbl_Apko notebook'larındaki dış kaynakları gir
# (tasks/notebook_semantics/ dosyalarından bilgileri al)
registry add-source-dependency-draft \
  --title "..." --description "..." --usage "..." \
  --source-kind manual_inline --requiredness required
```

## Bilinen Teknik Borçlar

| Sorun | Dosya | Öncelik |
|-------|-------|---------|
| `formula_expression` vs `formula_description` farkı belirsiz | records.py | Düşük |
| README path ayıraçları tutarsız | README.md | Düşük |
| Acceptance checklist'ler boş | tasks/notebook_semantics/*.md | Düşük |
| Yi_Yrlsk L1 ama dış kaynak içeriyor (L2 olmalı) | INDEX.md | Orta |
| Frekans hizalama kuralları yok | SHARED_SPEC.md | Orta (Faz 2'de) |
| StubEVDSAdapter sadece NotImplementedError | source_adapters.py | Orta (Faz 3'te) |
| auto-approve sadece 'series' tipini destekliyor | semantic_inference.py | Yüksek (Faz 1'de) |

## Registry Sağlık Durumu

```
Güçlü katmanlar:
  ✅ Series     206 onaylı kayıt
  ✅ Memory     224 semantik kural
  ✅ Catalog    227 EVDS metadata

Zayıf katmanlar (Faz 1 hedefi):
  ⚠️ Proposals  269 bekliyor — işlenmemiş
  ❌ Indicators  2 onaylı (hedef: 50+)
  ❌ Themes      2 onaylı (hedef: 10+)
  ❌ Source deps 0 onaylı (hedef: 5+)
```
