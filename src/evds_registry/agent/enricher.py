from __future__ import annotations
from dataclasses import dataclass
from ..records import Record
from ..llm import LLMClient


def detect_source_type(record_id: str) -> str:
    """Infers data source from record ID prefix."""
    rid = record_id.strip().lower()
    if rid.startswith("evds:") or rid.startswith("tp."):
        return "evds"
    if rid.startswith("source:tufe") or rid.startswith("source:yufe"):
        return "tuik"
    if rid.startswith("source:"):
        return "source"
    if rid.startswith("derived:"):
        return "derived"
    if rid.startswith("theme:"):
        return "theme"
    return "unknown"


@dataclass(slots=True)
class EnrichmentFlag:
    field: str
    level: str   # "red" | "yellow"
    message: str

    def to_dict(self) -> dict[str, str]:
        return {"field": self.field, "level": self.level, "message": self.message}


@dataclass(slots=True)
class EnrichmentResult:
    record: Record
    flags: list[EnrichmentFlag]
    confidence: float
    source_type: str


CONFIDENCE_CATALOG_HIT = 0.5
CONFIDENCE_LLM_HIGH = 0.85
CONFIDENCE_LLM_LOW = 0.4
CONFIDENCE_NO_CATALOG = 0.2


@dataclass(slots=True)
class Enricher:
    llm: LLMClient
    catalog: dict[str, Record]       # catalog:evds2:TICKER → Record
    known_themes: list[str]          # existing theme IDs

    def enrich(self, record_id: str, context_hint: str = "") -> EnrichmentResult:
        source_type = detect_source_type(record_id)
        flags: list[EnrichmentFlag] = []
        record: Record = {
            "id": record_id,
            "record_type": "series",
            "status": "draft",
            "title": record_id,
            "source": source_type if source_type != "unknown" else "",
            "source_version": "evds2" if source_type == "evds" else "",
            "ticker": record_id.replace("evds:", "") if source_type == "evds" else "",
            "frequency": "",
            "unit": "",
            "description": "",
            "usage": "",
            "official_url": "",
            "theme_ids": [],
            "indicator_ids": [],
        }
        confidence = CONFIDENCE_NO_CATALOG

        if source_type == "evds":
            ticker = record_id.replace("evds:", "")
            catalog_key = f"catalog:evds2:{ticker}"
            catalog_entry = self.catalog.get(catalog_key)
            if catalog_entry:
                record["title"] = str(catalog_entry.get("title") or ticker).strip()
                record["frequency"] = str(catalog_entry.get("frequency") or "").strip()
                record["unit"] = str(catalog_entry.get("unit") or "").strip()
                record["description"] = str(catalog_entry.get("title") or "").strip()
                confidence = CONFIDENCE_CATALOG_HIT
            else:
                flags.append(EnrichmentFlag(
                    field="ticker",
                    level="red",
                    message=f"'{ticker}' EVDS catalog'da bulunamadı — başlık ve birim manuel girilmeli",
                ))
                confidence = CONFIDENCE_NO_CATALOG

        if self.llm.is_enabled() and self.known_themes:
            themes, llm_confidence, theme_flags = self._infer_themes(record, context_hint)
            record["theme_ids"] = themes
            if llm_confidence >= 0.7:
                confidence = max(confidence, llm_confidence)
            else:
                flags.extend(theme_flags)
        else:
            flags.append(EnrichmentFlag(
                field="theme_ids",
                level="yellow",
                message="LLM kapalı — tema manuel seçilmeli",
            ))

        if ":" in record["title"] and not (record["title"].startswith('"') and record["title"].endswith('"')):
            record["title"] = f'"{record["title"]}"'

        return EnrichmentResult(
            record=record,
            flags=flags,
            confidence=confidence,
            source_type=source_type,
        )

    def _infer_themes(
        self, record: Record, context_hint: str
    ) -> tuple[list[str], float, list[EnrichmentFlag]]:
        prompt = (
            f"Seri başlık: {record['title']}\n"
            f"Ticker: {record.get('ticker', '')}\n"
            f"Bağlam: {context_hint}\n\n"
            f"Mevcut temalar: {', '.join(self.known_themes)}\n\n"
            "Bu serinin ait olduğu temaları ve güven skorunu döndür."
        )
        schema = {
            "type": "object",
            "properties": {
                "theme_ids": {"type": "array", "items": {"type": "string"}},
                "confidence": {"type": "number"},
                "reasoning": {"type": "string"},
            },
        }
        raw = self.llm.generate_structured(prompt, schema)
        theme_ids = [t for t in raw.get("theme_ids", []) if t in self.known_themes]
        llm_confidence = float(raw.get("confidence", 0.5))
        flags: list[EnrichmentFlag] = []
        if llm_confidence < 0.7:
            flags.append(EnrichmentFlag(
                field="theme_ids",
                level="yellow",
                message=f"Tema güven skoru düşük ({llm_confidence:.2f}) — kontrol et",
            ))
        if len(theme_ids) > 2:
            flags.append(EnrichmentFlag(
                field="theme_ids",
                level="yellow",
                message=f"{len(theme_ids)} tema önerildi — daraltmayı düşün",
            ))
        return theme_ids, llm_confidence, flags
