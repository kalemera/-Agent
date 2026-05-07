"""BaseAnalystAgent — genişletilebilir analist agent çekirdeği.

Hem RezervAnalystAgent hem TUFEAnalystAgent (ve gelecekte
CariAnalystAgent, BeklentiAnalystAgent vb.) bu base'den extend eder.

═══════════════════════════════════════════════════════════════════════════════
YENİ INTENT NASIL EKLENİR — ÖRNEK
═══════════════════════════════════════════════════════════════════════════════

```python
from .base_analyst import BaseAnalystAgent, IntentDefinition

class MyAgent(BaseAnalystAgent):
    INTENTS = [
        IntentDefinition(
            name="benim_intent_im",
            keywords=[
                ["yeni", "kelime"],     # 'yeni VE kelime' VE'leri (her ikisi de geçmeli)
                ["alternatif"],          # alternatif tek kelime grubu
            ],
            handler="_handle_benim_intent",
            priority=10,                  # düşük sayı önce kontrol edilir
        ),
    ]

    def _handle_benim_intent(self, snapshot_date):
        return self._build_response(
            intent="benim_intent_im",
            text="Benim cevabım buraya",
            data={"deger": 123.45},
            snapshot_date=snapshot_date,
        )
```

═══════════════════════════════════════════════════════════════════════════════
MEVCUT BIR INTENT'I DEGISTIRMEK ICIN
═══════════════════════════════════════════════════════════════════════════════

Subclass'ta aynı isimli handler method'unu override et. Keywords'ü değiştirmek
istersen INTENTS listesini override et veya `add_intent()` ile yeni IntentDefinition
ekle. `remove_intent()` ile kaldırabilirsin.

═══════════════════════════════════════════════════════════════════════════════
"""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from typing import Any

import pandas as pd


# =============================================================================
# Intent Tanımı — Tek bir intent'ın yapısı
# =============================================================================

@dataclass
class IntentDefinition:
    """Bir intent'ın tanımı.

    Args:
        name: Intent adı (snake_case). Handler method adı `_handle_{name}` olur.
        keywords: Liste of liste. Her iç liste 'AND' grubu — tüm kelimeleri içermeli.
                  Örn: [["yıllık", "tüfe"], ["enflasyon"]] →
                  "yıllık VE tüfe" YA DA "enflasyon" → match.
        handler: Çağırılacak method adı. Default: `_handle_{name}`.
        priority: Sıralama (düşük sayı önce kontrol edilir). Default: 100.
        description: Kullanıcıya yardım metninde gösterilecek özet.
    """
    name: str
    keywords: list[list[str]]
    handler: str = ""
    priority: int = 100
    description: str = ""

    def __post_init__(self):
        if not self.handler:
            self.handler = f"_handle_{self.name}"


# =============================================================================
# Yapılandırılmış Yanıt
# =============================================================================

@dataclass
class AnalystResponse:
    """Agent yanıtının yapılandırılmış hali.

    Args:
        intent: Tanımlanan intent adı veya None (no match).
        text: Kullanıcıya gösterilecek metin.
        data: Yapılandırılmış sayısal veriler (UI için).
        snapshot_date: Snapshot'ın hangi tarihi temsil ettiği.
    """
    intent: str | None
    text: str
    data: dict[str, Any] = field(default_factory=dict)
    snapshot_date: _dt.date | None = None


# =============================================================================
# TR Karakter Normalizasyonu
# =============================================================================

_TR_REPLACEMENTS = [
    ("ı", "i"), ("ş", "s"), ("ğ", "g"),
    ("ç", "c"), ("ö", "o"), ("ü", "u"),
]


def normalize_tr(text: str) -> str:
    """TR karakter + lowercase normalize.

    Klasik karakterleri ASCII karşılıklarına çevirir, lowercase yapar.
    Intent eşleşme öncesi her iki tarafta uygulanır.
    """
    s = (text or "").lower()
    for tr, en in _TR_REPLACEMENTS:
        s = s.replace(tr, en)
    return s


# =============================================================================
# Base Class
# =============================================================================

class BaseAnalystAgent:
    """Tüm analist agent'lar için temel sınıf.

    Subclass yapısı:
        class MyAgent(BaseAnalystAgent):
            INTENTS = [IntentDefinition(...), ...]

            def _handle_my_intent(self, snapshot_date):
                ...

    Public API:
        agent = MyAgent(snapshot=...)
        text  = agent.handle("kullanıcı sorusu")        # str döner
        resp  = agent.response("kullanıcı sorusu")      # AnalystResponse döner

    Genişletme API'si:
        agent.add_intent(IntentDefinition(...))
        agent.remove_intent("eski_intent_adi")
        agent.list_intents()
    """

    # Subclass'lar bu listeyi override eder
    INTENTS: list[IntentDefinition] = []

    # Subclass'lar isim/açıklama sağlayabilir
    AGENT_NAME: str = "BaseAnalyst"
    AGENT_DESCRIPTION: str = "Genel analist agent base"

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(self, snapshot: Any | None = None):
        """
        Args:
            snapshot: Veri snapshot'u — agent'a özgü tip.
                      Subclass init'inde tip kontrolü yapılabilir.
        """
        self.snapshot = snapshot
        # Class INTENTS'i instance kopyası — runtime modifikasyonu için
        self._intents: list[IntentDefinition] = list(self.INTENTS)
        self._sort_intents()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def handle(self, query: str) -> str:
        """Soru → metin yanıt."""
        return self.response(query).text

    def response(self, query: str) -> AnalystResponse:
        """Soru → yapılandırılmış yanıt."""
        intent = self.classify_intent(query)
        snapshot_date = self._latest_date()

        if intent is None:
            return AnalystResponse(
                intent=None,
                text=self._help_text(),
                snapshot_date=snapshot_date,
            )

        handler_name = self._get_intent_def(intent).handler
        handler = getattr(self, handler_name, None)
        if handler is None:
            return AnalystResponse(
                intent=intent,
                text=f"Intent '{intent}' için handler tanımlı değil ({handler_name}).",
                snapshot_date=snapshot_date,
            )
        return handler(snapshot_date)

    def classify_intent(self, query: str) -> str | None:
        """Sorudan intent çıkar. Hiçbir match yoksa None.

        Priority sırasına göre kontrol edilir; ilk match döner.
        """
        if not query:
            return None
        q_norm = normalize_tr(query)

        for intent_def in self._intents:
            for keyword_group in intent_def.keywords:
                if all(normalize_tr(kw) in q_norm for kw in keyword_group):
                    return intent_def.name
        return None

    # ------------------------------------------------------------------
    # Genişletme API
    # ------------------------------------------------------------------

    def add_intent(self, intent_def: IntentDefinition) -> None:
        """Yeni intent ekle (runtime'da)."""
        # Aynı isimde varsa güncelle, yoksa ekle
        existing = self._get_intent_def(intent_def.name, raise_if_missing=False)
        if existing:
            self._intents.remove(existing)
        self._intents.append(intent_def)
        self._sort_intents()

    def remove_intent(self, name: str) -> bool:
        """Intent'i kaldır. Bulunduysa True döner."""
        existing = self._get_intent_def(name, raise_if_missing=False)
        if existing is None:
            return False
        self._intents.remove(existing)
        return True

    def list_intents(self) -> list[IntentDefinition]:
        """Mevcut tüm intent tanımlarını priority sırasında döner."""
        return list(self._intents)

    # ------------------------------------------------------------------
    # Subclass Hook'ları (override edilebilir)
    # ------------------------------------------------------------------

    def _latest_date(self) -> _dt.date | None:
        """Snapshot'tan son tarihi çıkar.

        Default: snapshot.calculated.index[-1] denenir.
        Subclass kendi snapshot tipine göre override etmeli.
        """
        if self.snapshot is None:
            return None
        # RezervSnapshot benzeri yapı dener
        for attr in ["calculated", "data", "raw"]:
            df = getattr(self.snapshot, attr, None)
            if isinstance(df, pd.DataFrame) and not df.empty:
                idx = df.index[-1]
                if isinstance(idx, pd.Timestamp):
                    return idx.date()
        return None

    def _help_text(self) -> str:
        """Hiçbir intent eşleşmediğinde gösterilen yardım metni.

        Subclass override edebilir. Default: tüm intent açıklamalarını listeler.
        """
        if not self._intents:
            return f"{self.AGENT_NAME}: Tanımlı intent yok."

        lines = [f"{self.AGENT_NAME}: Sorunuzu anlayamadım. Şu konularda yardımcı olabilirim:"]
        for d in self._intents:
            label = d.description or d.name
            lines.append(f"  - {label}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Yardımcı method'lar (subclass'lar yararlanabilir)
    # ------------------------------------------------------------------

    def _build_response(
        self,
        intent: str,
        text: str,
        data: dict | None = None,
        snapshot_date: _dt.date | None = None,
    ) -> AnalystResponse:
        """Subclass handler'ları kolay AnalystResponse oluşturmak için."""
        return AnalystResponse(
            intent=intent,
            text=text,
            data=data or {},
            snapshot_date=snapshot_date,
        )

    @staticmethod
    def safe_get(df: pd.DataFrame, col: str, idx: int = -1) -> float | None:
        """DataFrame'den güvenli skaler değer al. Eksikse None.

        Args:
            df: Hedef DataFrame.
            col: Sütun adı.
            idx: Pozisyonel index. Default: -1 (son satır).
        """
        if df is None or df.empty or col not in df.columns:
            return None
        try:
            v = df[col].iloc[idx]
            return float(v) if pd.notna(v) else None
        except (KeyError, IndexError, ValueError, TypeError):
            return None

    @staticmethod
    def change_from_n_periods_ago(
        df: pd.DataFrame, col: str, n: int = 1
    ) -> float | None:
        """Son değer ile N dönem öncesi değer arasındaki fark."""
        if df is None or df.empty or col not in df.columns or len(df) <= n:
            return None
        latest = df[col].iloc[-1]
        earlier = df[col].iloc[-n - 1]
        if pd.isna(latest) or pd.isna(earlier):
            return None
        return float(latest - earlier)

    @staticmethod
    def format_number(value: float | None, unit: str = "", decimals: int = 2) -> str:
        """Sayıyı formatlı string'e çevir. None ise 'veri yok'."""
        if value is None or pd.isna(value):
            return "veri yok"
        formatted = f"{value:.{decimals}f}"
        return f"{formatted} {unit}".strip()

    @staticmethod
    def format_change(diff: float | None, unit: str = "") -> str:
        """Değişim sayısını işaretli string'e çevir."""
        if diff is None or pd.isna(diff):
            return "(önceki dönem yok)"
        sign = "+" if diff >= 0 else ""
        formatted = f"{sign}{diff:.2f}"
        return f"{formatted} {unit}".strip()

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _sort_intents(self) -> None:
        """Intent listesini priority'ye göre sırala (düşük sayı önce)."""
        self._intents.sort(key=lambda d: d.priority)

    def _get_intent_def(
        self, name: str, raise_if_missing: bool = True
    ) -> IntentDefinition | None:
        """İsme göre IntentDefinition döner."""
        for d in self._intents:
            if d.name == name:
                return d
        if raise_if_missing:
            raise KeyError(f"Intent '{name}' tanımlı değil.")
        return None
