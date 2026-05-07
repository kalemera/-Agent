"""Project-level pytest conftest.

.env dosyasını otomatik yükler — testlerin EVDS_API_KEY ve QWEN_API_KEY gibi
credential'ları shell'e export etmeden okuyabilmesi için.
"""

from __future__ import annotations

from pathlib import Path

try:
    from dotenv import load_dotenv

    _ROOT = Path(__file__).resolve().parent.parent
    _ENV_FILE = _ROOT / ".env"
    if _ENV_FILE.exists():
        load_dotenv(_ENV_FILE, override=False)
except ImportError:
    # python-dotenv yoksa session continue — ENV var manuel yüklenmiş olabilir
    pass
