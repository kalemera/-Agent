# Faz 4 — Akıllı Agent 🤖

> Durum: Uzun vade
> Hedef: Projenin asıl amacı — ekonomistin veri setlerini yönetebilen, öğrenen bir agent

## Vizyon

```
Ekonomist yeni bir Jupyter notebook açar.
Agent:
  1. Notebook'u otomatik tarar
  2. Bilinen serileri tanır, bilinmeyenler için öneri üretir
  3. "Bu 3 seri daha önce DTH'de de kullanmışsın, aynı rol mü?" diye sorar
  4. Onay alır, registry'i günceller
  5. Canlı veriyi çekip formülü doğrular
  6. Rapor üretir

Ekonomist hiç CLI komutu yazmak zorunda kalmaz.
```

## Görevler

### 4.1 Doğal Dil Arayüzü

Claude Code'u registry'e bağla — ekonomist Türkçe sorabilsin:

```
"Enflasyon serilerini listele"
→ registry show-map theme:enflasyon

"DTH notebook'unda hangi seriler aktif kullanılıyor?"
→ registry review-proposals --notebook DTH_Blg_V7 --status approved

"TP.AB.A01 ne için kullanılıyordu?"
→ registry show-map evds:TP.AB.A01
```

**Nasıl çalışır:**
- Claude Code'un MCP üzerinden registry CLI'ını çağırması
- Ya da registry'i MCP server olarak expose etmek (bkz. 4.3)

### 4.2 Otomatik Notebook Tarama

Yeni notebook eklenince otomatik tetiklensin:

```bash
# Watched klasör
registry watch notebooks/ --auto-analyze --auto-propose
```

**Akış:**
```
Yeni .ipynb tespit edildi
  → analyze-notebook (ticker extraction)
  → infer-notebook-semantics (LLM öneriler)
  → Bilinmeyen ticker'lar için evds_ara ile EVDS araması
  → Düşük confidence'lı öneriler → manuel review kuyruğu
  → Yüksek confidence'lı öneriler → auto-approve kuyruğu
```

### 4.3 Registry'i MCP Server Olarak Yayınla

evds-mcp gibi, registry de bir MCP server olabilir. Claude doğrudan sorabilir:

**Araçlar:**
```
registry_search(query: str) → seri/indikatör/tema arama
registry_get(id: str) → kayıt detayı
registry_map(id: str) → bağlantı grafiği
registry_add_draft(record: dict) → yeni draft oluştur
registry_approve(id: str) → draft onayla
```

**Fayda:** Claude Code hem evds-mcp hem registry-mcp'yi aynı anda kullanabilir.

### 4.4 Çatışma ve Tutarsızlık Dedektörü

Bilgi grafiği büyüdükçe tutarsızlıklar ortaya çıkabilir:

```bash
registry audit

# Çıktı:
# ⚠️ ÇAKIŞMA: TP.AB.A01 — DTH'de 'input', Rzrv'de 'reference'
# ⚠️ EKSİK: derived:reel-faiz input_ids içinde evds:TP.FAIZ.A01 var ama registry'de yok
# ⚠️ KOPUK: theme:doviz-politikasi — bağlı seri yok
# ✓ 204 seri tutarlı
```

### 4.5 Otomatik Rapor Üretici

```bash
registry report --theme enflasyon --period 2024-Q4

# Çıktı (Markdown):
# ## Enflasyon Raporu — 2024 Q4
# ### Kullanılan Seriler
# - TP.TUFE.* — TÜFE endeks serileri (canlı veri: ...)
# ### Türetilen İndikatörler
# - derived:yillik-enflasyon = ((T/T-12) - 1) * 100
# ### Grafik
# [mermaid chart buraya]
```

### 4.6 Öğrenen Bellek

Ekonomist bir kez "Bu seri kur politikası temasına girer" dediğinde, agent benzer serileri otomatik o temaya önersin:

```
Ekonomist: "TP.AB.A01 → tema:doviz-politikasi"
Agent öğrenir: "TP.AB.* ailesi genellikle doviz-politikasi temasına girer"
Yeni notebook'ta TP.AB.A17 görülünce → otomatik öneri: "doviz-politikasi?"
```

Bu mekanizma zaten `registry/memory/` klasöründe başlangıç seviyesinde var (224 memory rule). Genişletilmesi gerekiyor.

## Teknoloji Seçimi

| İhtiyaç | Seçenek | Not |
|---------|---------|-----|
| MCP server | FastMCP (evds-mcp gibi) | En kolay yol |
| Doğal dil anlama | Claude API (claude-sonnet-4-6) | Qwen yerine Claude |
| Embedding/arama | sentence-transformers | Semantic seri arama için |
| Scheduled tasks | Cron / watched folder | Notebook takibi |

## Başarı Kriterleri

- [ ] Ekonomist Türkçe soru sorabilir, registry cevap verir
- [ ] Yeni notebook otomatik analiz ediliyor
- [ ] registry-mcp server çalışıyor, Claude bağlanabiliyor
- [ ] `registry audit` tutarsızlıkları raporluyor
- [ ] Öğrenen bellek yeni ticker önerilerinde kullanılıyor
