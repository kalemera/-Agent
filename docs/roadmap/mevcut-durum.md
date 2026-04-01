# Mevcut Durum ve Kararlar

> Son güncelleme: 2026-04-01

## Mimari Kararlar

### 2 Agent Mimarisi

- **evds-registry** = anlam/bilgi katmanı (bu proje)
- **evds-mcp** = veri/analiz katmanı (https://github.com/orhoncan/evds-mcp)

### LLM: Qwen (Alibaba Cloud DashScope)

- `LLM_PROVIDER=qwen`, `QWEN_MODEL=qwen-turbo`
- Endpoint: `https://dashscope.aliyuncs.com/compatible-mode/v1`

### Öncelik Sırası

1. ~~Faz 1 (proposal backlog temizleme)~~ — **büyük ölçüde tamamlandı**
2. Faz 2 (NotebookSpec genelleme) — **sıradaki**
3. Faz 3 (evds-mcp entegrasyonu)
4. Faz 4 (akıllı agent) — uzun vade

## Tamamlanan İşler

| İş | Durum |
|----|-------|
| Qwen LLM client, .env.example, Git repo, uv | ✅ oturum 1 |
| Yol haritası yazıldı | ✅ oturum 1 |
| Faz 1.1: generate-implied-proposals + auto-approve indicator/theme | ✅ oturum 2 |
| Faz 1.2: 15 source dependency kaydı (5 notebook) | ✅ oturum 2 |
| Faz 1.3: show-map source dep gösterimi + backfill-cross-references | ✅ oturum 2 |

## Sonraki Oturumda Nereden Başlanacak

**Faz 1.4 — import-drafts CSV template güncellemesi:**

`examples/import_template.csv`'ye `source_dependency` satır desteği eklenmeli.

**46 indicator manual_review'da:**

Formula'da `evds:` input'u olmayan indicator proposal'ları `manual_review`'da. Bunlara notebook'lardan formula bilgisi çıkarılmalı. `review-proposals --status manual_review --target-type indicator` ile incelenebilir.

**Faz 2'ye geçiş:**

Faz 1 başarı kriterleri büyük ölçüde karşılandı, Faz 2 (NotebookSpec genelleme) başlanabilir.

## Bilinen Teknik Borçlar

| Sorun | Dosya | Öncelik |
|-------|-------|---------|
| `formula_expression` vs `formula_description` farkı belirsiz | records.py | Düşük |
| README path ayıraçları tutarsız | README.md | Düşük |
| Acceptance checklist'ler boş | tasks/notebook_semantics/*.md | Düşük |
| Yi_Yrlsk L1 ama dış kaynak içeriyor (L2 olmalı) | INDEX.md | Orta |
| Frekans hizalama kuralları yok | SHARED_SPEC.md | Orta (Faz 2'de) |
| StubEVDSAdapter sadece NotImplementedError | source_adapters.py | Orta (Faz 3'te) |

## Registry Sağlık Durumu

```
Güçlü katmanlar:
  ✅ Series          206 onaylı kayıt
  ✅ Memory          241 semantik kural
  ✅ Catalog         227 EVDS metadata
  ✅ Themes           17 onaylı (hedef: 10+ ✓)
  ✅ Source deps      15 onaylı (hedef: 5+ ✓)

Devam eden:
  ⚠️ Indicators       4 onaylı (hedef: 50+)
  ⚠️ Proposals       46 manual_review (indicator, input_ids eksik)
```
