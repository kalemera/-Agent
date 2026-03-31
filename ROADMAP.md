# EVDS Registry — Ana Yol Haritası

> Son güncelleme: 2026-03-31
> Durum: Phase 0 tamamlandı, Phase 1 devam ediyor

## Proje Amacı

Bir ekonomistin kullandığı EVDS (TCMB) veri setlerini yönetebilen, hangi verilerin nereden alındığını, hangi verilerden nelerin türetildiğini ve çıkarım yapıldığını kalıcı olarak saklayan akıllı bir agent sistemi.

## Mimari Karar: 2 Agent

```
┌─────────────────────────────────────────────────┐
│           ANLAM KATMANI (bu proje)               │
│           evds-registry                          │
│  • Seri kayıt ve onay iş akışı                  │
│  • Bilgi grafiği (seri→indikatör→tema)           │
│  • Notebook analizi ve semantik bellek           │
│  • Qwen LLM ile anlamsal çıkarım                 │
└─────────────────────────────────────────────────┘
                      ▲ ▼
┌─────────────────────────────────────────────────┐
│           VERİ KATMANI                           │
│           evds-mcp (harici repo)                 │
│  • Canlı TCMB EVDS verisi                        │
│  • OLS, ARIMA, korelasyon analizi               │
│  • Claude MCP protokolü üzerinden               │
└─────────────────────────────────────────────────┘
```

**Kaynak:** https://github.com/orhoncan/evds-mcp

## Mevcut Durum (2026-03-31)

| Katman | Kayıt Sayısı | Durum |
|--------|-------------|-------|
| Series | 206 onaylı | ✅ Sağlam |
| Memory rules | 224 onaylı | ✅ Sağlam |
| Proposals | 269 bekliyor | ⚠️ Tıkalı |
| Indicators | 2 onaylı | ❌ Neredeyse boş |
| Themes | 2 onaylı | ❌ Neredeyse boş |
| Source deps | 0 onaylı | ❌ CLI komutu yeni eklendi |

## Faz Özeti

| Faz | Başlık | Durum | Detay |
|-----|--------|-------|-------|
| **0** | Altyapı | ✅ Tamamlandı | [→](docs/roadmap/phase-0-altyapi.md) |
| **1** | Tıkalı Kanalları Aç | 🔄 Devam ediyor | [→](docs/roadmap/phase-1-kanal.md) |
| **2** | Genelleme | ⏳ Bekliyor | [→](docs/roadmap/phase-2-genelleme.md) |
| **3** | evds-mcp Entegrasyonu | ⏳ Bekliyor | [→](docs/roadmap/phase-3-evds-mcp.md) |
| **4** | Akıllı Agent | ⏳ Uzun vade | [→](docs/roadmap/phase-4-agent.md) |

## LLM Konfigürasyonu

```bash
# .env dosyası oluştur
LLM_PROVIDER=qwen
QWEN_API_KEY=sk-...
QWEN_MODEL=qwen-turbo          # ucuz/hızlı
# QWEN_MODEL=qwen-plus         # daha iyi kalite
# QWEN_MODEL=qwen-max          # en iyi kalite
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

## Hızlı Başlangıç

```bash
# Kurulum
pip install -e .

# Bekleyen draft'ları onayla
registry review-drafts
registry approve-draft <id>

# Yeni kaynak bağımlılığı ekle
registry add-source-dependency-draft \
  --title "MKK Yatırımcı Verileri" \
  --description "Manuel inline veri" \
  --usage "Yurt içi yatırımcı sayısı hesabında kullanılır" \
  --source-kind manual_inline \
  --requiredness required

# Notebook analizi
registry analyze-notebook --notebook path/to/notebook.ipynb

# Semantik çıkarım (LLM gerekli)
registry infer-notebook-semantics --notebook path/to/notebook.ipynb
```
