"""Orchestrator — Çoklu analist agent yönlendirici.

═══════════════════════════════════════════════════════════════════════════════
AMAÇ
═══════════════════════════════════════════════════════════════════════════════

Birden fazla domain-spesifik analist agent (RezervAnalystAgent,
TUFEAnalystAgent, ...) için tek giriş noktası. Kullanıcı sorusunu önce
**domain'e** yönlendirir, sonra ilgili agent'ın kendi intent
classifier'ına devreder.

İki seviyeli sınıflandırma:

    "Brüt rezerv ne kadar?"
        ↓
    [Orchestrator] domain → "rezerv"
        ↓
    [RezervAnalystAgent] intent → "brut_rezerv_durum"
        ↓
    handler → metin yanıt

═══════════════════════════════════════════════════════════════════════════════
ROUTING ÖRNEKLERİ
═══════════════════════════════════════════════════════════════════════════════

| Soru                              | Domain | Intent (downstream)         |
|-----------------------------------|--------|-----------------------------|
| "Brüt rezerv ne kadar?"           | rezerv | brut_rezerv_durum           |
| "Yıllık enflasyon nasıl?"         | tufe   | tufe_yillik                 |
| "Çekirdek TÜFE B grubu"           | tufe   | cekirdek_tufe               |
| "Swap hariç net rezerv"           | rezerv | swap_haric_rezerv           |
| "TCMB altın stoku"                | rezerv | altin_kompozisyon           |
| "Aylık tüfe değişim"              | tufe   | tufe_aylik                  |
| "NIR ne durumda?"                 | rezerv | net_rezerv_durum            |
| "Fiyat endeksi"                   | tufe   | tufe_genel_durum            |

═══════════════════════════════════════════════════════════════════════════════
KULLANIM
═══════════════════════════════════════════════════════════════════════════════

```python
from evds_registry.agent.orchestrator import Orchestrator
from evds_registry.rezerv import run_pipeline as run_rezerv_pipeline
from evds_registry.agent.tufe_analyst_agent import TUFESnapshot

rezerv_snap = run_rezerv_pipeline(raw_evds, raw_urdl, raw_pdf)
tufe_snap = TUFESnapshot(data=tufe_df)

orch = Orchestrator(snapshots={"rezerv": rezerv_snap, "tufe": tufe_snap})

print(orch.handle("Brüt rezerv ne kadar?"))
print(orch.handle("Yıllık enflasyon nasıl?"))

# Yapılandırılmış yanıt
resp = orch.response("Aylık tüfe değişim")
# {"domain": "tufe", "intent": "tufe_aylik", "text": "...",
#  "data": {...}, "snapshot_date": date(2026, 4, 1)}
```

═══════════════════════════════════════════════════════════════════════════════
GENİŞLETME — YENİ AGENT EKLEMEK
═══════════════════════════════════════════════════════════════════════════════

```python
from evds_registry.agent.orchestrator import register_agent
from evds_registry.agent.cari_analyst_agent import CariAnalystAgent

register_agent(
    domain_name="cari",
    agent_cls=CariAnalystAgent,
    keywords=[["cari", "açık"], ["cari", "denge"], ["current", "account"]],
)

orch = Orchestrator(snapshots={..., "cari": cari_snap})
```

═══════════════════════════════════════════════════════════════════════════════
"""

from __future__ import annotations

import datetime as _dt
from typing import Any

from .base_analyst import BaseAnalystAgent, normalize_tr
from .rezerv_analyst_agent import RezervAnalystAgent
from .tufe_analyst_agent import TUFEAnalystAgent


# =============================================================================
# Registries — modul seviyesinde, runtime genişletilebilir
# =============================================================================

AGENT_REGISTRY: dict[str, type] = {
    "rezerv": RezervAnalystAgent,
    "tufe": TUFEAnalystAgent,
}


# Domain → keyword grupları. Her iç liste 'AND' grubu — tüm kelimeleri içermeli.
# Liste sırası önceliği belirler: önce daha spesifik domainler.
AGENT_DOMAIN_KEYWORDS: dict[str, list[list[str]]] = {
    "rezerv": [
        ["rezerv"],
        ["nir"],
        ["nur"],
        ["swap"],
        ["altın", "rezerv"],
        ["altin", "rezerv"],
        ["döviz", "rezerv"],
        ["doviz", "rezerv"],
        ["bilanço"],
        ["bilanco"],
        ["brüt", "rezerv"],
        ["brut", "rezerv"],
        ["analitik"],
    ],
    "tufe": [
        ["tüfe"],
        ["tufe"],
        ["enflasyon"],
        ["inflation"],
        ["çekirdek"],
        ["cekirdek"],
        ["fiyat", "endeksi"],
        ["price", "index"],
        ["yıllık", "değişim"],
        ["yillik", "degisim"],
        ["aylık", "değişim"],
        ["aylik", "degisim"],
    ],
}


def register_agent(
    domain_name: str,
    agent_cls: type,
    keywords: list[list[str]],
) -> None:
    """Yeni bir domain agent'i runtime'da kaydet.

    Args:
        domain_name: Domain anahtarı (örn. "cari").
        agent_cls: BaseAnalystAgent türevi sınıf.
        keywords: AND-gruplarının listesi.
    """
    AGENT_REGISTRY[domain_name] = agent_cls
    AGENT_DOMAIN_KEYWORDS[domain_name] = list(keywords)


def unregister_agent(domain_name: str) -> bool:
    """Bir domain'i registry'den kaldır. Bulunduysa True döner."""
    removed = False
    if domain_name in AGENT_REGISTRY:
        del AGENT_REGISTRY[domain_name]
        removed = True
    if domain_name in AGENT_DOMAIN_KEYWORDS:
        del AGENT_DOMAIN_KEYWORDS[domain_name]
        removed = True
    return removed


# =============================================================================
# Orchestrator
# =============================================================================


class Orchestrator:
    """Çoklu analist agent yönlendirici.

    `snapshots` dict'i ile her domain için ilgili snapshot'u alır ve
    karşılık gelen agent'i otomatik instantiate eder. Snapshot
    sağlanmamış domain'ler atlanır (graceful degradation).

    Public API:
        orch = Orchestrator(snapshots={"rezerv": ..., "tufe": ...})
        text = orch.handle("kullanıcı sorusu")           # str
        resp = orch.response("kullanıcı sorusu")          # dict
        domain = orch.classify_domain("kullanıcı sorusu") # str | None

    Genişletme:
        orch.list_agents()  → kayıtlı domain isimleri
        register_agent(...) modülü ile yeni domain ekle
    """

    def __init__(self, snapshots: dict[str, Any] | None = None):
        """
        Args:
            snapshots: domain_name → snapshot dict.
                       Snapshot None ise o domain skip edilir.
        """
        self.snapshots: dict[str, Any] = dict(snapshots or {})
        self.agents: dict[str, BaseAnalystAgent] = {}

        # Dict snapshot taşıyan tüm domainleri instantiate et
        for domain_name, agent_cls in AGENT_REGISTRY.items():
            snap = self.snapshots.get(domain_name)
            if snap is None:
                # Snapshot yoksa agent'i yükleme — handle()'da açıklayıcı hata döner
                continue
            try:
                self.agents[domain_name] = agent_cls(snapshot=snap)
            except Exception:  # noqa: BLE001
                # Agent init'i fail ederse (snapshot tipi yanlışsa vs.) — atla
                # handle() bu domain'i isteyen sorularda anlamlı mesaj döner
                continue

    # ------------------------------------------------------------------
    # Domain Sınıflandırma
    # ------------------------------------------------------------------

    def classify_domain(self, query: str) -> str | None:
        """Sorudan domain çıkar. Hiçbir match yoksa None.

        Önce uzun (daha spesifik) AND-gruplarına öncelik verir; aynı uzunluk
        durumunda registry sırası belirleyicidir.
        """
        if not query or not query.strip():
            return None

        q_norm = normalize_tr(query)

        # Daha uzun (daha spesifik) AND-gruplarını önce dene.
        # Aynı uzunluktaki gruplar için registry sırası geçerli olsun.
        candidates: list[tuple[int, int, str]] = []  # (-group_len, domain_index, domain)
        for idx, (domain, groups) in enumerate(AGENT_DOMAIN_KEYWORDS.items()):
            for group in groups:
                if all(normalize_tr(kw) in q_norm for kw in group):
                    candidates.append((-len(group), idx, domain))

        if not candidates:
            return None

        candidates.sort()
        return candidates[0][2]

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def handle(self, query: str) -> str:
        """Soru → metin yanıt."""
        return self.response(query)["text"]

    def response(self, query: str) -> dict[str, Any]:
        """Yapılandırılmış yanıt döner.

        Returns:
            {
              "domain":   str | None,
              "intent":   str | None,
              "text":     str,
              "data":     dict,
              "snapshot_date": datetime.date | None,
            }
        """
        domain = self.classify_domain(query)
        if domain is None:
            return {
                "domain": None,
                "intent": None,
                "text": self._help_text(),
                "data": {},
                "snapshot_date": None,
            }

        agent = self.agents.get(domain)
        if agent is None:
            return {
                "domain": domain,
                "intent": None,
                "text": (
                    f"'{domain}' alanı için snapshot yüklenmemiş. "
                    f"Bu sorgu için Orchestrator(snapshots={{'{domain}': ...}}) ile "
                    f"snapshot sağlanmalı."
                ),
                "data": {},
                "snapshot_date": None,
            }

        # Agent'a delege — istisnaları yakala, anlamlı bir mesaja çevir
        try:
            agent_resp = agent.response(query)
        except Exception as exc:  # noqa: BLE001
            return {
                "domain": domain,
                "intent": None,
                "text": (
                    f"'{domain}' agent'i hata verdi: {type(exc).__name__}: {exc}"
                ),
                "data": {},
                "snapshot_date": None,
            }

        # AnalystResponse → dict
        return {
            "domain": domain,
            "intent": getattr(agent_resp, "intent", None),
            "text": getattr(agent_resp, "text", ""),
            "data": getattr(agent_resp, "data", {}) or {},
            "snapshot_date": getattr(agent_resp, "snapshot_date", None),
        }

    def list_agents(self) -> list[str]:
        """Aktif (snapshot'i yüklü) domain isimleri."""
        return list(self.agents.keys())

    def list_registered_domains(self) -> list[str]:
        """Tüm kayıtlı domain isimleri (snapshot bağımsız)."""
        return list(AGENT_REGISTRY.keys())

    # ------------------------------------------------------------------
    # Help Text
    # ------------------------------------------------------------------

    def _help_text(self) -> str:
        """Domain eşleşmediğinde kullanıcıya yol gösteren metin."""
        lines = [
            "Sorunuzu hangi konuya yönlendireceğimi belirleyemedim.",
            "Şu konularda yardımcı olabilirim:",
        ]

        if not AGENT_REGISTRY:
            lines.append("  (Henüz kayıtlı agent yok.)")
            return "\n".join(lines)

        for domain_name, agent_cls in AGENT_REGISTRY.items():
            agent_desc = getattr(
                agent_cls, "AGENT_DESCRIPTION", domain_name.capitalize()
            )
            agent_label = getattr(agent_cls, "AGENT_NAME", domain_name)
            mark = "✓" if domain_name in self.agents else "✗"
            lines.append(f"  [{mark}] {agent_label} — {agent_desc}")

            # Anahtar kelime ipuçları
            kw_groups = AGENT_DOMAIN_KEYWORDS.get(domain_name, [])
            if kw_groups:
                # Tek kelimelik grupları öne al, en fazla 4 göster
                singletons = [g[0] for g in kw_groups if len(g) == 1][:4]
                if singletons:
                    lines.append(f"      Örnek anahtar kelimeler: {', '.join(singletons)}")

        # Kullanıcıya yön ver
        active = self.list_agents()
        if not active:
            lines.append("")
            lines.append("UYARI: Hiçbir snapshot yüklenmedi — yanıt üretilemez.")

        return "\n".join(lines)


# =============================================================================
# Public exports
# =============================================================================

__all__ = [
    "Orchestrator",
    "AGENT_REGISTRY",
    "AGENT_DOMAIN_KEYWORDS",
    "register_agent",
    "unregister_agent",
]
