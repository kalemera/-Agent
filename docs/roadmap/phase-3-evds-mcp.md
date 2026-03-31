# Faz 3 — evds-mcp Entegrasyonu ⏳

> Durum: Bekliyor (Faz 2 tamamlanınca başlar)
> Kaynak repo: https://github.com/orhoncan/evds-mcp

## Mimari

Bu iki proje birbirinin rakibi değil, tamamlayıcısıdır:

```
Kullanıcı sorusu
      │
      ▼
evds-registry (anlam katmanı)
  "Bu seri nedir? Hangi temaya girer? Nasıl türetilir?"
  206 seri + 224 memory rule + indikatör/tema grafiği
      │
      ▼
evds-mcp (veri katmanı)
  "Bu seriyi TCMB'den getir, analiz et, tahmin yap"
  evds_ara → evds_meta → evds_cek → evds_analiz
      │
      ▼
TCMB EVDS API
```

## evds-mcp'nin 4 Aracı

| Araç | Ne Yapar | Kullanım Senaryosu |
|------|---------|-------------------|
| `evds_ara` | Keyword ile seri ara | Yeni notebook'taki bilinmeyen ticker'ı keşfet |
| `evds_meta` | Seri metadata'sını getir | Draft onayı sırasında ticker doğrula |
| `evds_cek` | Veri çek + dönüştür | Canlı veri ile indikatör hesapla |
| `evds_analiz` | OLS, ARIMA, korelasyon | Registry'deki formülü canlı veriyle doğrula |

## Görevler

### 3.1 evds-mcp'yi Claude Code'a MCP Olarak Bağla

**Kurulum:**
```bash
# evds-mcp'yi kur
git clone https://github.com/orhoncan/evds-mcp
cd evds-mcp
uv sync

# .env içine EVDS_API_KEY ekle
echo "EVDS_API_KEY=your_key_here" >> .env
```

**Claude Code MCP konfigürasyonu** (`.claude/settings.local.json`'a ekle):
```json
{
  "mcpServers": {
    "evds": {
      "command": "uv",
      "args": ["run", "evds-mcp"],
      "cwd": "/path/to/evds-mcp",
      "env": {
        "EVDS_API_KEY": "..."
      }
    }
  }
}
```

### 3.2 Draft Onayında Canlı Ticker Doğrulama

**Sorun:** Şu an `StubEVDSAdapter` sadece `NotImplementedError` fırlatıyor. Ticker'ın EVDS'de gerçekten var olup olmadığı kontrol edilmiyor.

**Dosya:** `src/evds_registry/source_adapters.py`

**Çözüm:** evds-mcp'nin `evds_meta` aracını `approve-draft` akışına bağla:
```python
# approve-draft sırasında
def validate_ticker_exists(ticker: str) -> bool:
    # evds-mcp'ye evds_meta sorgusu gönder
    # EVDS'de bulunmayan ticker → uyarı ver ama engelleme
    ...
```

**Not:** Sert engelleme değil, yumuşak uyarı — bazı seri kodları henüz EVDS'de olmayabilir.

### 3.3 Registry → MCP Köprüsü: `fetch-series` Komutu

**Yeni komut:** `registry fetch-series <ticker|indicator_id>`

Registry'deki bir seriyi ya da indikatörü alır, evds-mcp üzerinden canlı veriyi çeker:

```bash
# Tek seri
registry fetch-series evds:TP.DK.USD.A --start 2024-01 --end 2024-12

# İndikatör (birden fazla seri → hesaplama)
registry fetch-series derived:reel-faiz-orani

# Çıktı formatları
registry fetch-series evds:TP.DK.USD.A --format json
registry fetch-series evds:TP.DK.USD.A --format csv --out data/usd_tl.csv
```

### 3.4 Otomatik show-map Zenginleştirme

`show-map` çıktısına canlı veri özeti ekle:

```bash
registry show-map TP.DK.USD.A --live

# Çıktı:
# evds:TP.DK.USD.A — USD/TRY Döviz Kuru
#   ├── Tema: tema:kur-politikasi
#   ├── İndikatörde kullanılan: derived:reel-efektif-kur
#   ├── Canlı: Son değer 32.45 (2024-12-31), trend: ↑
#   └── Frekans: günlük
```

### 3.5 Metadata Cache Senkronizasyonu

`sync-evds-catalog` komutunu evds-mcp'nin `evds_meta` aracıyla destekle. Şu an EVDS API'ye direkt bağlanıyor — evds-mcp üzerinden gitmek daha tutarlı.

## Başarı Kriterleri

- [ ] evds-mcp Claude Code'a MCP olarak bağlı ve çalışıyor
- [ ] `approve-draft` sırasında ticker EVDS'de kontrol ediliyor (soft validation)
- [ ] `fetch-series` komutu tek seri için çalışıyor
- [ ] `show-map --live` canlı özet veriyor
- [ ] `sync-evds-catalog` evds-mcp üzerinden çalışıyor
