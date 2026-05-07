"""TUFEAnalystAgent — TÜFE/enflasyon sorularına cevap veren analist agent.

═══════════════════════════════════════════════════════════════════════════════
HIZLI KULLANIM
═══════════════════════════════════════════════════════════════════════════════

```python
import pandas as pd
from evds_registry.agent.tufe_analyst_agent import TUFEAnalystAgent, TUFESnapshot

# Snapshot kendi pipeline'ından gelir veya elle hazırlanır
snapshot = TUFESnapshot(
    data=pd.DataFrame({
        "tufe_genel": [100.0, 102.5, 105.0, 107.8],
        "tufe_yillik_pct": [65.0, 62.5, 58.3, 55.1],
        "tufe_aylik_pct": [3.5, 2.5, 2.4, 2.7],
        "cekirdek_b_yillik": [60.0, 58.0, 55.0, 52.0],
        "cekirdek_c_yillik": [58.0, 56.0, 53.0, 50.0],
    }, index=pd.date_range("2026-02-01", periods=4, freq="MS")),
)

agent = TUFEAnalystAgent(snapshot=snapshot)

print(agent.handle("Bu ay yıllık TÜFE ne kadar?"))
# → "TÜFE Yıllık: 55.10%, Aylık: +2.70%"

print(agent.handle("Çekirdek enflasyon nedir?"))
# → Çekirdek B + C grupları
```

═══════════════════════════════════════════════════════════════════════════════
GENISLETME — KENDIN INTENT EKLE
═══════════════════════════════════════════════════════════════════════════════

İki yöntem:

### Yöntem 1: Subclass yarat (kalıcı değişiklik için tercih edilir)

```python
from evds_registry.agent.tufe_analyst_agent import TUFEAnalystAgent
from evds_registry.agent.base_analyst import IntentDefinition

class MyTUFEAgent(TUFEAnalystAgent):
    INTENTS = TUFEAnalystAgent.INTENTS + [
        IntentDefinition(
            name="ozel_grup_analizi",
            keywords=[
                ["gıda", "enflasyon"],
                ["food", "inflation"],
            ],
            handler="_handle_ozel_grup",
            priority=15,
            description="Belirli grup enflasyon analizi",
        ),
    ]

    def _handle_ozel_grup(self, snapshot_date):
        gida = self.safe_get(self.snapshot.data, "gida_yillik")
        return self._build_response(
            intent="ozel_grup_analizi",
            text=f"Gıda enflasyonu: {self.format_number(gida, '%')}",
            data={"gida_yillik": gida},
            snapshot_date=snapshot_date,
        )
```

### Yöntem 2: Runtime'da ekle (geçici değişiklik için)

```python
agent = TUFEAnalystAgent(snapshot=snapshot)
agent.add_intent(IntentDefinition(
    name="hizli_test",
    keywords=[["test"]],
    handler="_handle_test",
    priority=5,
))

def my_handler(self, snapshot_date):
    return self._build_response(intent="hizli_test", text="Test cevabı")

# Method'u dinamik bağla
import types
agent._handle_test = types.MethodType(my_handler, agent)
```

═══════════════════════════════════════════════════════════════════════════════
SNAPSHOT YAPISI
═══════════════════════════════════════════════════════════════════════════════

TUFESnapshot.data DataFrame'i için beklenen sütunlar (varsayılan handler'lar
şu adları arar; subclass override edebilir):

| Sütun | İçerik | Örnek |
|---|---|---|
| `tufe_genel` | TÜFE endeksi | 107.85 |
| `tufe_yillik_pct` | Yıllık % değişim | 55.10 |
| `tufe_aylik_pct` | Aylık % değişim | 2.70 |
| `cekirdek_b_yillik` | Çekirdek B yıllık | 52.00 |
| `cekirdek_c_yillik` | Çekirdek C yıllık | 50.00 |
| `gida_yillik` | Gıda grubu yıllık | (opsiyonel) |
| `enerji_yillik` | Enerji grubu yıllık | (opsiyonel) |
| `hizmet_yillik` | Hizmet grubu yıllık | (opsiyonel) |

Eksik sütunlar için handler "veri yok" döner (crash etmez).

═══════════════════════════════════════════════════════════════════════════════
"""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass

import pandas as pd

from .base_analyst import (
    AnalystResponse,
    BaseAnalystAgent,
    IntentDefinition,
)


# =============================================================================
# Snapshot
# =============================================================================

@dataclass
class TUFESnapshot:
    """TÜFE pipeline çıktısı.

    Args:
        data: TÜFE serileri ve türev hesaplar (aylık DatetimeIndex).
        metadata: Snapshot metadata (kaynak tarih, version, vs.).
    """
    data: pd.DataFrame
    metadata: dict | None = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


# =============================================================================
# Agent
# =============================================================================

class TUFEAnalystAgent(BaseAnalystAgent):
    """TÜFE/enflasyon analizi agent'i.

    BaseAnalystAgent'ın TÜFE'ye özelleşmiş alt sınıfı.
    """

    AGENT_NAME = "TUFEAnalyst"
    AGENT_DESCRIPTION = "Tüketici Fiyat Endeksi (TÜFE) ve enflasyon analizi"

    # Sütun adları — subclass override edebilir
    COL_TUFE_INDEX = "tufe_genel"
    COL_TUFE_YILLIK = "tufe_yillik_pct"
    COL_TUFE_AYLIK = "tufe_aylik_pct"
    COL_CEKIRDEK_B = "cekirdek_b_yillik"
    COL_CEKIRDEK_C = "cekirdek_c_yillik"
    COL_GIDA = "gida_yillik"
    COL_ENERJI = "enerji_yillik"
    COL_HIZMET = "hizmet_yillik"

    INTENTS: list[IntentDefinition] = [
        IntentDefinition(
            name="tufe_yillik",
            keywords=[
                ["yıllık", "tüfe"], ["yillik", "tufe"],
                ["yıllık", "enflasyon"], ["yillik", "enflasyon"],
                ["annual", "inflation"],
                ["yıllık", "değişim"], ["yillik", "degisim"],
            ],
            priority=10,
            description="Yıllık TÜFE değişimi (yıllık enflasyon)",
        ),
        IntentDefinition(
            name="tufe_aylik",
            keywords=[
                ["aylık", "tüfe"], ["aylik", "tufe"],
                ["aylık", "enflasyon"], ["aylik", "enflasyon"],
                ["monthly", "inflation"],
                ["aylık", "değişim"], ["aylik", "degisim"],
            ],
            priority=10,
            description="Aylık TÜFE değişimi (aylık enflasyon)",
        ),
        IntentDefinition(
            name="cekirdek_tufe",
            keywords=[
                ["çekirdek"], ["cekirdek"],
                ["core", "inflation"],
                ["b", "grubu"],
                ["c", "grubu"],
            ],
            priority=8,
            description="Çekirdek TÜFE (B ve C grupları)",
        ),
        IntentDefinition(
            name="kategori_kirilim",
            keywords=[
                ["gıda"], ["gida"],
                ["enerji"], ["energy"],
                ["hizmet"], ["service"],
                ["kategori", "kırılım"], ["kategori", "kirilim"],
                ["grup", "kırılım"], ["grup", "kirilim"],
            ],
            priority=12,
            description="Kategori bazlı enflasyon (gıda, enerji, hizmet, vb.)",
        ),
        IntentDefinition(
            name="tufe_genel_durum",
            keywords=[
                ["tüfe"], ["tufe"],
                ["enflasyon"], ["inflation"],
                ["fiyat", "endeksi"], ["price", "index"],
            ],
            priority=50,  # Daha geniş — diğerleri eşleşmezse fallback
            description="Genel TÜFE durumu özeti (yıllık + aylık + endeks)",
        ),
    ]

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(self, snapshot: TUFESnapshot | None = None):
        super().__init__(snapshot=snapshot)

    # ------------------------------------------------------------------
    # _latest_date override — TUFESnapshot.data kullanılır
    # ------------------------------------------------------------------

    def _latest_date(self) -> _dt.date | None:
        if self.snapshot is None:
            return None
        df = getattr(self.snapshot, "data", None)
        if isinstance(df, pd.DataFrame) and not df.empty:
            idx = df.index[-1]
            if isinstance(idx, pd.Timestamp):
                return idx.date()
        return None

    # ------------------------------------------------------------------
    # Intent Handlers
    # ------------------------------------------------------------------

    def _handle_tufe_yillik(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Yıllık TÜFE değişimi."""
        df = self._df()
        yillik = self.safe_get(df, self.COL_TUFE_YILLIK)
        change = self.change_from_n_periods_ago(df, self.COL_TUFE_YILLIK, n=1)

        date_str = self._format_date(snapshot_date)
        text = (
            f"TÜFE Yıllık Enflasyon — {date_str}\n"
            f"  Yıllık değişim: {self.format_number(yillik, '%')}\n"
            f"  Önceki aya göre: {self.format_change(change, 'puan')}"
        )

        return self._build_response(
            intent="tufe_yillik",
            text=text,
            data={
                "tufe_yillik_pct": yillik,
                "onceki_aya_gore_puan": change,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_tufe_aylik(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Aylık TÜFE değişimi."""
        df = self._df()
        aylik = self.safe_get(df, self.COL_TUFE_AYLIK)
        change = self.change_from_n_periods_ago(df, self.COL_TUFE_AYLIK, n=1)

        date_str = self._format_date(snapshot_date)
        text = (
            f"TÜFE Aylık Enflasyon — {date_str}\n"
            f"  Aylık değişim: {self.format_number(aylik, '%')}\n"
            f"  Önceki aya göre: {self.format_change(change, 'puan')}"
        )

        return self._build_response(
            intent="tufe_aylik",
            text=text,
            data={
                "tufe_aylik_pct": aylik,
                "onceki_aya_gore_puan": change,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_cekirdek_tufe(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Çekirdek TÜFE B ve C."""
        df = self._df()
        cekirdek_b = self.safe_get(df, self.COL_CEKIRDEK_B)
        cekirdek_c = self.safe_get(df, self.COL_CEKIRDEK_C)

        date_str = self._format_date(snapshot_date)
        text = (
            f"Çekirdek TÜFE — {date_str}\n"
            f"  B Grubu (Yıllık): {self.format_number(cekirdek_b, '%')}\n"
            f"  C Grubu (Yıllık): {self.format_number(cekirdek_c, '%')}"
        )

        return self._build_response(
            intent="cekirdek_tufe",
            text=text,
            data={
                "cekirdek_b_yillik": cekirdek_b,
                "cekirdek_c_yillik": cekirdek_c,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_kategori_kirilim(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Kategori (gıda, enerji, hizmet) bazlı kırılım."""
        df = self._df()
        gida = self.safe_get(df, self.COL_GIDA)
        enerji = self.safe_get(df, self.COL_ENERJI)
        hizmet = self.safe_get(df, self.COL_HIZMET)

        date_str = self._format_date(snapshot_date)
        text_parts = [f"TÜFE Kategori Kırılımı — {date_str}"]
        text_parts.append(f"  Gıda (Yıllık):   {self.format_number(gida, '%')}")
        text_parts.append(f"  Enerji (Yıllık): {self.format_number(enerji, '%')}")
        text_parts.append(f"  Hizmet (Yıllık): {self.format_number(hizmet, '%')}")

        return self._build_response(
            intent="kategori_kirilim",
            text="\n".join(text_parts),
            data={
                "gida_yillik": gida,
                "enerji_yillik": enerji,
                "hizmet_yillik": hizmet,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_tufe_genel_durum(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Genel TÜFE özet — endeks + yıllık + aylık."""
        df = self._df()
        endeks = self.safe_get(df, self.COL_TUFE_INDEX)
        yillik = self.safe_get(df, self.COL_TUFE_YILLIK)
        aylik = self.safe_get(df, self.COL_TUFE_AYLIK)

        date_str = self._format_date(snapshot_date)
        text = (
            f"TÜFE Genel Durum — {date_str}\n"
            f"  Endeks: {self.format_number(endeks)}\n"
            f"  Yıllık değişim: {self.format_number(yillik, '%')}\n"
            f"  Aylık değişim:  {self.format_number(aylik, '%')}"
        )

        return self._build_response(
            intent="tufe_genel_durum",
            text=text,
            data={
                "tufe_genel_endeks": endeks,
                "tufe_yillik_pct": yillik,
                "tufe_aylik_pct": aylik,
            },
            snapshot_date=snapshot_date,
        )

    # ------------------------------------------------------------------
    # Yardımcı Method'lar
    # ------------------------------------------------------------------

    def _df(self) -> pd.DataFrame:
        """Snapshot DataFrame'ini güvenli al."""
        if self.snapshot is None:
            return pd.DataFrame()
        return getattr(self.snapshot, "data", pd.DataFrame())

    @staticmethod
    def _format_date(d: _dt.date | None) -> str:
        return d.isoformat() if d else "?"
