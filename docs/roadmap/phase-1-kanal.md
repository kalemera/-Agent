# Faz 1 — Tıkalı Kanalları Aç 🔄

> Durum: Devam ediyor
> Hedef: 269 bekleyen proposal'ı işle, bilgi grafiğini zenginleştir

## Neden Bu Faz Kritik?

Phase 1 tamamlandığında Series layer sağlam (206 kayıt) ama bilgi grafiğinin üst katmanları neredeyse boş:
- 2 indikatör, 2 tema, 0 source dependency
- 269 proposal kuyrukta bekliyor — bunların büyük çoğunluğu zaten LLM tarafından analiz edilmiş, sadece onay bekliyor

## Görevler

### 1.1 Proposal Batch Onayı

**Sorun:** `auto-approve-proposals` komutu sadece `series` tipini destekliyor. `indicator` ve `theme` proposal'ları için toplu onay yok.

**Çözüm:** `auto-approve-proposals` komutunu genişlet:
- `--target-type indicator|theme|source_dependency` desteği ekle
- Minimum confidence eşiği: `--min-confidence 0.75` (indicator/theme için biraz daha düşük olabilir)

**Dosya:** `src/evds_registry/semantic_inference.py` → `auto_approve_proposals()` fonksiyonu

**Beklenen çıktı:** 269 proposal → toplu değerlendirme → onaylanan'lar drafts'a, reddedilenler rejected'a

**Çalıştırma:**
```bash
# Bekleyen indicator proposal'larını incele
registry review-proposals --target-type indicator --min-confidence 0.70

# Toplu onayla (LLM gerekli)
registry auto-approve-proposals --target-type indicator --min-confidence 0.75
registry auto-approve-proposals --target-type theme --min-confidence 0.70
```

### 1.2 Source Dependency Kayıtlarını Gir

CLI komutu artık mevcut. Yi_Yrlsk ve diğer L2/L3 notebook'lardaki dış kaynaklar elle girilmeli.

**Bilinen source dependency'ler (tasks/notebook_semantics dosyalarından):**

| Notebook | Kaynak | Tip |
|----------|--------|-----|
| Yi_Yrlsk_Fnsl_Vrlk_V1 | MKK yatırımcı sayıları | manual_inline |
| Yi_Yrlsk_Fnsl_Vrlk_V1 | VAP scrape (opsiyonel) | web_scrape |
| Tbl_Apko | Manuel tablo verileri | manual_inline |

**Çalıştırma:**
```bash
registry add-source-dependency-draft \
  --title "MKK Bireysel Yatırımcı Sayıları" \
  --description "MKK tarafından yayımlanan yurt içi bireysel yatırımcı sayısı verileri" \
  --usage "Yi_Yrlsk notebook'unda yatırımcı profili hesaplamalarında kullanılır" \
  --source-kind manual_inline \
  --requiredness required \
  --local-hint "notebook içinde dict olarak inline tanımlı"

registry approve-draft source:mkk-bireysel-yatirimci-sayilari
```

### 1.3 show-map'e Source Dependency Göster

**Sorun:** `show-map` komutu source dependency bağlantılarını göstermiyor.

**Dosya:** `src/evds_registry/cli.py` → `handle_show_map()` fonksiyonu
`src/evds_registry/storage.py` → `load_registry()` genişletilmeli

**Beklenen çıktı:**
```
theme:yatirimci-davranisi
  series:
    evds:TP.DK.USD.A → Döviz kuru (input)
  source_dependencies:
    source:mkk-bireysel-yatirimci-sayilari → MKK verileri (required)
```

### 1.4 import-drafts'a source_dependency Desteği

**Sorun:** `normalize_import_row()` source_dependency tipini zaten destekliyor ama `import-drafts` komutunun pratik testi yapılmadı. CSV import template'i güncellenmeli.

**Dosya:** `examples/import_template.csv`

**Eklenecek sütunlar:**
```
record_type,id,title,description,usage,source_kind,requiredness,source_uri,local_hint,theme_ids,indicator_ids,validation_note
source_dependency,,MKK Verileri,Manuel veri,Yi_Yrlsk notebook'unda kullanılır,manual_inline,required,,,theme:yatirimci-davranisi,,
```

## Başarı Kriterleri

- [ ] En az 20 indicator onaylanmış
- [ ] En az 5 theme onaylanmış
- [ ] En az 3 source dependency kayıtlı ve onaylanmış
- [ ] `show-map` source dependency bağlantılarını gösteriyor
- [ ] 269 proposal'dan en az %60'ı işlenmiş (onaylı veya reddedilmiş)
