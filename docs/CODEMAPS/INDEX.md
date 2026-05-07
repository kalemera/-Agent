# CODEMAPS Index

**Last Updated:** 2026-05-07

Otomatik üretilen mimari haritalar. Her dosya tek bir alt-sistemi tarif eder.

## Dizin

| Codemap | Konu | Modül Kökü |
|---|---|---|
| [rezerv-pipeline.md](rezerv-pipeline.md) | TCMB rezerv pipeline (fetcher → transformer → calculator → validator) | `src/evds_registry/rezerv/` |
| [agent-system.md](agent-system.md) | Analist agent çekirdeği + TÜFE/Rezerv subclass'ları | `src/evds_registry/agent/` |

## Üretim Metodu

`tldr` CLI bu sistemde kurulu değil. Codemap'ler Python `ast` modülü ile çıkarıldı:
- Modül docstring'leri
- Class / function imzaları
- 1 satırlık özet docstring

## İlgili Dokümantasyon

- `docs/registry-notes/` — Tasarım kararları + cut-off listeleri (sayfa modülü değil, kalsın)
- `docs/superpowers/plans/` — Plan/spec dokümanları (codemap'ten ayrı)
- `docs/roadmap/` — Yol haritası
- `DURUM.md` — Güncel durum + yapılacaklar listesi
