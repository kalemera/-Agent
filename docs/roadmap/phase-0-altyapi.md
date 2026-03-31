# Faz 0 — Altyapı ✅ Tamamlandı

> Tamamlanma: 2026-03-31

## Yapılanlar

### 0.1 Qwen/OpenAI-compat LLM Client ✅

`src/evds_registry/llm.py` dosyasına `OpenAICompatibleClient` sınıfı eklendi.

**Desteklenen sağlayıcılar:**
- `LLM_PROVIDER=qwen` → Alibaba Cloud DashScope
- `LLM_PROVIDER=openai` → OpenAI veya uyumlu herhangi bir endpoint
- `LLM_PROVIDER=ollama` → Local veya cloud Ollama (eski davranış korundu)
- `LLM_PROVIDER=disabled` → LLM devre dışı

**Env değişkenleri (Qwen için):**
```
QWEN_API_KEY=sk-...
QWEN_MODEL=qwen-turbo | qwen-plus | qwen-max
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

### 0.2 `.env.example` ✅

Tüm konfigürasyon değişkenleri `.env.example` dosyasında belgelendi.
`.env` dosyası `.gitignore`'a eklendi — API key'ler git'e gitmez.

### 0.3 `add-source-dependency-draft` CLI Komutu ✅

`src/evds_registry/cli.py` dosyasına eklendi.

**Kullanım:**
```bash
registry add-source-dependency-draft \
  --title "MKK Yatırımcı Verileri" \
  --description "Yurt içi bireysel yatırımcı sayıları" \
  --usage "Yatırımcı profili hesaplamalarında input olarak kullanılır" \
  --source-kind manual_inline \
  --requiredness required \
  --local-hint "notebook içinde dict olarak tanımlı" \
  --theme-id theme:yatirimci-davranisi

# source-kind seçenekleri: manual_inline | web_scrape | external_file | api
# requiredness seçenekleri: required | optional
```

### 0.4 Git Repository ✅

```
git init → ilk commit (1037 dosya)
.gitignore oluşturuldu (venv, .env, __pycache__, tmp dizinleri)
```

### 0.5 `uv` Kurulumu ✅

`tldr` kod analiz aracının çalışması için gerekli Python package manager.
```
winget install astral-sh.uv
```

## Bilinen Teknik Borçlar

Faz 0 sırasında tespit edildi, sonraki fazlarda ele alınacak:

- `formula_expression` alanı hiçbir zaman doldurulmuyor, içerik hep `formula_description`'a gidiyor. İki alanın farkı belirsiz.
- README'deki path ayıraçları tutarsız (backslash/forward slash karışık).
- Tüm görev dosyalarındaki acceptance checklist'ler boş.
