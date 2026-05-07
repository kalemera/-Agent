"""Kayıt Agent uçtan uca testi — notebook'tan bilinmeyen ticker tespiti."""

import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))

import json, re
TICKER_RE = re.compile(r"TP\.[A-Z0-9]+(?:\.[A-Z0-9]+)+")

from evds_registry.storage import RegistryPaths, load_registry, load_catalog
from evds_registry.llm import build_llm_client_from_env
from evds_registry.agent.gap_detector import GapDetector
from evds_registry.agent.enricher import Enricher
from evds_registry.agent.draft_writer import DraftWriter

PATHS = RegistryPaths.from_root(ROOT)

NOTEBOOK = Path(
    r"C:\Users\bthkr\OneDrive\Masaüstü\Model\Econ\notebooks\DTH_Blg_V7.ipynb"
)

print(f"\n{'='*60}")
print(f"Notebook: {NOTEBOOK.name}")
print(f"{'='*60}")

# 1. Notebook'tan ticker'ları regex ile çıkar
print("\n[1] Notebook'tan ticker'lar çıkarılıyor...")
nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
raw_text = " ".join(
    "".join(cell.get("source", []))
    for cell in nb.get("cells", [])
)
raw_tickers = sorted(set(TICKER_RE.findall(raw_text)))
print(f"    Bulunan benzersiz ticker: {len(raw_tickers)}")
if raw_tickers[:5]:
    print(f"    Örnek: {raw_tickers[:5]}")

# 2. evds: prefix'li ID'lere çevir
all_tickers = {f"evds:{t}" for t in raw_tickers}

print(f"\n[2] Toplam {len(all_tickers)} ID kontrol edilecek")

# 3. Gap detection
registry = load_registry(PATHS)
detector = GapDetector(registry=registry)
gaps = detector.find_gaps(list(all_tickers))

print(f"\n[3] Gap detection sonucu:")
print(f"    Registry'de var: {len(all_tickers) - len(gaps)}")
print(f"    Eksik (gap): {len(gaps)}")

if not gaps:
    print("\n    OK - Tum ticker'lar zaten registry'de.")
    sys.exit(0)

print(f"\n    Eksik ID'ler:")
for g in gaps:
    print(f"      - {g}")

# 4. Enrichment + draft yazma
print(f"\n[4] Enrichment çalışıyor...")
catalog = load_catalog(PATHS)
known_themes = [k for k, v in registry.items() if v["record_type"] == "theme"]
llm = build_llm_client_from_env()
enricher = Enricher(llm=llm, catalog=catalog, known_themes=known_themes)
writer = DraftWriter(paths=PATHS)

created = []
for gap_id in gaps:
    result = enricher.enrich(gap_id)
    path = writer.write_draft(result)
    created.append((gap_id, result, path))
    flag_summary = ", ".join(
        f"{f.level}:{f.field}" for f in result.flags
    ) or "temiz"
    print(f"    [{gap_id}]")
    print(f"      Başlık: {result.record['title']}")
    print(f"      Güven: {result.confidence:.2f}  |  Kaynak: {result.source_type}")
    print(f"      Flag'ler: {flag_summary}")
    print(f"      Taslak: {path.name}")

# 5. Özet
print(f"\n{'='*60}")
print(f"SONUC: {len(created)} taslak olusturuldu -> drafts/")
print(f"Onaylamak için: POST /api/registry/approve")
print(f"{'='*60}\n")
