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

1. ~~Faz 1 (proposal backlog temizleme)~~ — **tamamlandı**
2. ~~Faz 2 (NotebookSpec genelleme)~~ — **tamamlandı**
3. ~~Faz 3 (evds-mcp entegrasyonu)~~ — **kısmi** (API hazır, veri çekme TCMB API değişikliği bekliyor)
4. Faz 4 (akıllı agent) — **audit komutu yapıldı**, geri kalan uzun vade

## Tamamlanan İşler

| İş | Faz | Oturum |
|----|-----|--------|
| Qwen LLM client, .env.example, Git repo, uv | 0 | 1 |
| Yol haritası | 0 | 1 |
| generate-implied-proposals + auto-approve indicator/theme | 1.1 | 2 |
| 15 source dependency kaydı (5 notebook) | 1.2 | 2 |
| show-map source dep + backfill-cross-references | 1.3 | 2 |
| import-drafts CSV source_dependency desteği (test) | 1.4 | 2 |
| 7 NotebookSpec tanımlı, auto-detection çalışıyor | 2.1-2.3 | zaten vardı |
| Frekans hizalama kuralları SHARED_SPEC.md'de | 2.4 | zaten vardı |
| check-conflicts komutu (19 çakışma tespit) | 2.5 | 2 |
| EVDSAdapter (hydrate + search, TCMB v3 API) | 3.1-3.2 | 2 |
| fetch-series komutu (metadata) | 3.3 | 2 |
| approve-draft soft ticker validation | 3.2 | 2 |
| registry audit komutu | 4.4 | 2 |

## Sonraki Oturumda Nereden Başlanacak

**46 indicator manual_review:**
Formula'da `evds:` input'u olmayan indicator proposal'ları `manual_review`'da.
`review-proposals --status manual_review --target-type indicator` ile incelenebilir.

**evds-mcp kararı:**
Kullanıcı henüz kararsız. Karar verildiğinde Faz 3.3-3.5 tamamlanabilir.

**Faz 4 uzun vade:**
- Registry MCP server (4.3)
- Otomatik notebook tarama (4.2)
- Doğal dil arayüzü (4.1)
- Öğrenen bellek genişletme (4.6)

## Bilinen Teknik Borçlar

| Sorun | Dosya | Öncelik |
|-------|-------|---------|
| `formula_expression` vs `formula_description` farkı belirsiz | records.py | Düşük |
| README path ayıraçları tutarsız | README.md | Düşük |
| Acceptance checklist'ler boş | tasks/notebook_semantics/*.md | Düşük |
| TCMB evds2 data API deprecated | source_adapters.py | Orta (evds-mcp kararı bekliyor) |
| 46 indicator input_ids eksik | proposals/ | Orta |

## Registry Sağlık Durumu

```
✅ Series          206 onaylı
✅ Memory          241+ semantik kural
✅ Catalog         227 EVDS metadata
✅ Themes           16 onaylı (hedef: 10+ ✓)
✅ Source deps      15 onaylı (hedef: 5+ ✓)
✅ Audit            0 sorun

⚠️ Indicators       3 onaylı (hedef: 50+, 46 manual_review bekliyor)
```
