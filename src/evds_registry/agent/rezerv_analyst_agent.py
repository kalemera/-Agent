"""RezervAnalystAgent — TCMB rezerv durumu için intent-driven analist agent.

BaseAnalystAgent'tan extend eder. TUFEAnalystAgent ile aynı pattern'i kullanır.

Kullanım:
    from evds_registry.rezerv import run_pipeline
    from evds_registry.agent.rezerv_analyst_agent import RezervAnalystAgent

    snapshot = run_pipeline(raw_evds, raw_urdl, raw_pdf)
    agent = RezervAnalystAgent(snapshot)

    print(agent.handle("Bu hafta brüt rezerv ne kadar?"))

═══════════════════════════════════════════════════════════════════════════════
GENISLETME — KENDIN INTENT EKLE
═══════════════════════════════════════════════════════════════════════════════

```python
from evds_registry.agent.rezerv_analyst_agent import RezervAnalystAgent
from evds_registry.agent.base_analyst import IntentDefinition

class MyRezervAgent(RezervAnalystAgent):
    INTENTS = RezervAnalystAgent.INTENTS + [
        IntentDefinition(
            name="ozel_metrik",
            keywords=[["yeni", "metrik"]],
            priority=5,
            description="Özel metrik analizi",
        ),
    ]

    def _handle_ozel_metrik(self, snapshot_date):
        return self._build_response(
            intent="ozel_metrik",
            text="Custom yanıt",
            snapshot_date=snapshot_date,
        )
```
"""

from __future__ import annotations

import datetime as _dt

import pandas as pd

from ..rezerv import RezervSnapshot
from .base_analyst import (
    AnalystResponse,
    BaseAnalystAgent,
    IntentDefinition,
)


# Backwards-compat alias — eski test'lerde kullanıldı
RezervAnalystResponse = AnalystResponse


class RezervAnalystAgent(BaseAnalystAgent):
    """TCMB rezerv durumu için intent-driven yanıt agent'i.

    BaseAnalystAgent'tan extend eder. 8 intent destekler.
    """

    AGENT_NAME = "RezervAnalyst"
    AGENT_DESCRIPTION = "TCMB uluslararası rezerv durumu ve swap pozisyon analizi"

    # Sütun adları — subclass override edebilir
    COL_BRUT_TOPLAM = "AB.TOPLAM"   # Milyon USD
    COL_BRUT_ALTIN = "AB.C1"
    COL_BRUT_DOVIZ = "AB.C2"
    COL_BL0021 = "BL0021"
    COL_DOVVARNC_K14 = "DOVVARNC.K14"
    COL_DOVVARNC_K18 = "DOVVARNC.K18"
    COL_DOVVARNC_K22 = "DOVVARNC.K22"
    COL_DOVVARNC_K23 = "DOVVARNC.K23"
    # Calculated frame sütunları
    COL_NET_ALTIN = "NetAltinUSD"
    COL_NET_DOVIZ = "NetDovizUSD"
    COL_BRUT_TL_URDL = "BrutRezervTL_URDL"
    COL_SH_NET_ALTIN = "SHNetAltin"
    COL_SH_NET_ALTIN_LEGACY = "SH_NetAltin"
    COL_SH_NET_DOVIZ = "SHNetDoviz"
    COL_SH_NET_DOVIZ_LEGACY = "SH_NetDoviz"
    COL_SH_GUNLUK = "SHNetRezervGunluk"
    COL_SH_URDL = "SHNetRezervURDL"
    COL_BILANCO_NET_DOVIZ = "BilancoNetDovizPozisyonu"
    COL_BILANCO_TAHMINI = "BilancoTahminiNetRezerv"
    COL_MB_SWAP_TOPLAM = "MBSwapToplam"

    INTENTS: list[IntentDefinition] = [
        IntentDefinition(
            name="swap_haric_rezerv",
            keywords=[
                ["swap", "hariç"], ["swap", "haric"],
                ["sh", "rezerv"],
                ["swap'sız"], ["swapsız"],
            ],
            priority=5,  # En yüksek öncelik — "swap hariç net rezerv" bilinmeli
            description="Swap hariç net rezerv (SH Net Altın + SH Net Döviz + günlük/URDL)",
        ),
        IntentDefinition(
            name="gunluk_tahmin",
            keywords=[
                ["günlük", "tahmin"], ["gunluk", "tahmin"],
                ["bilanço", "tahmin"], ["bilanco", "tahmin"],
                ["günlük", "rezerv"], ["gunluk", "rezerv"],
                ["analitik", "bilanço"], ["analitik", "bilanco"],
            ],
            priority=8,
            description="Günlük analitik bilanço bazlı rezerv tahmini",
        ),
        IntentDefinition(
            name="tarihsel_karsilastirma",
            keywords=[
                ["yıl başı"], ["yil basi"],
                ["ybb"],
                ["aylık", "değişim"], ["aylik", "degisim"],
                ["haftalık", "değişim"], ["haftalik", "degisim"],
            ],
            priority=10,
            description="Tarihsel değişim — haftalık / aylık / YBB",
        ),
        IntentDefinition(
            name="swap_breakdown",
            keywords=[
                ["swap", "büyüklük"], ["swap", "buyukluk"],
                ["swap", "stok"],
                ["mb", "swap"], ["m.b.", "swap"],
            ],
            priority=12,
            description="TCMB swap pozisyonları (M.B. + diğer + altın)",
        ),
        IntentDefinition(
            name="altin_kompozisyon",
            keywords=[
                ["altın"], ["altin"], ["gold"],
            ],
            priority=15,
            description="Altın rezerv kompozisyonu (Brüt / Net / SH)",
        ),
        IntentDefinition(
            name="doviz_kompozisyon",
            keywords=[
                ["döviz", "kompozisyon"], ["doviz", "kompozisyon"],
                ["fx", "reserve"],
                ["döviz", "rezerv"], ["doviz", "rezerv"],
            ],
            priority=18,
            description="Döviz rezerv kompozisyonu (Brüt / Net / SH)",
        ),
        IntentDefinition(
            name="net_rezerv_durum",
            keywords=[
                ["net", "rezerv"],
                ["net", "uluslararası"], ["net", "uluslararasi"],
                ["nir"], ["nur"],
            ],
            priority=20,
            description="Net Uluslararası Rezerv (NIR) ve bileşenleri",
        ),
        IntentDefinition(
            name="brut_rezerv_durum",
            keywords=[
                ["brüt", "rezerv"], ["brut", "rezerv"],
                ["gross", "reserve"],
                ["toplam", "rezerv"],
            ],
            priority=50,  # En son fallback
            description="Brüt rezerv durumu",
        ),
    ]

    # ------------------------------------------------------------------
    # _latest_date override — RezervSnapshot.calculated kullanılır
    # ------------------------------------------------------------------

    def _latest_date(self) -> _dt.date | None:
        """Son **anlamlı** tarihi bulur.

        Pipeline patch_missing_dates() sentetik tarihler ekleyebildiği için
        son satır tamamen NaN olabilir. Bu durumda son non-NaN Net Altın/Döviz
        satırı kullanılır, yoksa son satır fallback.
        """
        if self.snapshot is None:
            return None
        c = getattr(self.snapshot, "calculated", None)
        if not (isinstance(c, pd.DataFrame) and not c.empty):
            return None

        anchor_cols = [self.COL_NET_ALTIN, self.COL_NET_DOVIZ]
        available = [col for col in anchor_cols if col in c.columns]
        if available:
            mask = c[available].notna().any(axis=1)
            if mask.any():
                idx = c.index[mask][-1]
                if isinstance(idx, pd.Timestamp):
                    return idx.date()

        idx = c.index[-1]
        if isinstance(idx, pd.Timestamp):
            return idx.date()
        return None

    # ------------------------------------------------------------------
    # Yardımcı: dataframe'ler + format
    # ------------------------------------------------------------------

    def _raw(self) -> pd.DataFrame:
        if self.snapshot is None:
            return pd.DataFrame()
        return getattr(self.snapshot, "raw", pd.DataFrame())

    def _calc(self) -> pd.DataFrame:
        if self.snapshot is None:
            return pd.DataFrame()
        return getattr(self.snapshot, "calculated", pd.DataFrame())

    @staticmethod
    def _fmt_usd(value: float | None) -> str:
        return BaseAnalystAgent.format_number(value, "milyar USD")

    @staticmethod
    def _fmt_change(diff: float | None) -> str:
        return BaseAnalystAgent.format_change(diff, "milyar USD")

    @staticmethod
    def _date_str(d: _dt.date | None) -> str:
        return d.isoformat() if d else "?"

    # ------------------------------------------------------------------
    # Intent Handlers
    # ------------------------------------------------------------------

    def _handle_brut_rezerv_durum(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Brüt Rezerv durumu — TP.AB.TOPLAM bazlı."""
        raw = self._raw()
        latest = self.safe_get(raw, self.COL_BRUT_TOPLAM)  # Milyon USD

        if latest is None:
            latest_mr = self.safe_get(self._calc(), self.COL_BRUT_TL_URDL)
            text = (
                f"Brüt rezerv (TP.AB.TOPLAM) verisi bulunamadı.\n"
                f"URDL alternatif yolu (BL toplamı): "
                f"{self._fmt_usd(latest_mr)} (Milyar TL bazlı tahmin)"
                if latest_mr is not None else
                "Brüt rezerv verisi bulunamadı."
            )
            return self._build_response(
                intent="brut_rezerv_durum",
                text=text,
                snapshot_date=snapshot_date,
            )

        latest_milyar = latest / 1000.0
        change_w = self.change_from_n_periods_ago(raw, self.COL_BRUT_TOPLAM, n=1)
        change_w_milyar = (change_w / 1000.0) if change_w is not None else None

        text = (
            f"Brüt Rezerv: {latest_milyar:.2f} milyar USD ({self._date_str(snapshot_date)})\n"
            f"Önceki döneme göre: {self._fmt_change(change_w_milyar)}"
        )

        return self._build_response(
            intent="brut_rezerv_durum",
            text=text,
            data={
                "brut_rezerv_milyar_usd": latest_milyar,
                "haftalik_degisim": change_w_milyar,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_net_rezerv_durum(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Net Uluslararası Rezerv (NIR) durumu."""
        calc = self._calc()
        net_altin = self.safe_get(calc, self.COL_NET_ALTIN)
        net_doviz = self.safe_get(calc, self.COL_NET_DOVIZ)

        nir = (net_altin + net_doviz) if (net_altin is not None and net_doviz is not None) else None

        text = (
            f"Net Uluslararası Rezerv (NIR) — {self._date_str(snapshot_date)}\n"
            f"  Net Altın Rezervi: {self._fmt_usd(net_altin)}\n"
            f"  Net Döviz Rezervi: {self._fmt_usd(net_doviz)}\n"
            f"  Toplam NIR: {self._fmt_usd(nir)}"
        )

        return self._build_response(
            intent="net_rezerv_durum",
            text=text,
            data={
                "net_altin_milyar_usd": net_altin,
                "net_doviz_milyar_usd": net_doviz,
                "nir_milyar_usd": nir,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_swap_haric_rezerv(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Swap Hariç Net Rezerv durumu."""
        calc = self._calc()

        sh_altin = self.safe_get(calc, self.COL_SH_NET_ALTIN)
        if sh_altin is None:
            sh_altin = self.safe_get(calc, self.COL_SH_NET_ALTIN_LEGACY)

        sh_doviz = self.safe_get(calc, self.COL_SH_NET_DOVIZ)
        if sh_doviz is None:
            sh_doviz = self.safe_get(calc, self.COL_SH_NET_DOVIZ_LEGACY)

        sh_total_g = self.safe_get(calc, self.COL_SH_GUNLUK)
        sh_total_u = self.safe_get(calc, self.COL_SH_URDL)

        text = (
            f"Swap Hariç Net Rezerv — {self._date_str(snapshot_date)}\n"
            f"  SH Net Altın: {self._fmt_usd(sh_altin)}\n"
            f"  SH Net Döviz: {self._fmt_usd(sh_doviz)}\n"
            f"  SH NUR (Günlük PDF bazlı): {self._fmt_usd(sh_total_g)}\n"
            f"  SH NUR (URDL standart): {self._fmt_usd(sh_total_u)}"
        )

        return self._build_response(
            intent="swap_haric_rezerv",
            text=text,
            data={
                "sh_net_altin_milyar_usd": sh_altin,
                "sh_net_doviz_milyar_usd": sh_doviz,
                "sh_nur_gunluk_milyar_usd": sh_total_g,
                "sh_nur_urdl_milyar_usd": sh_total_u,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_gunluk_tahmin(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Günlük analitik bilanço bazlı tahmin."""
        calc = self._calc()
        net_doviz_pos = self.safe_get(calc, self.COL_BILANCO_NET_DOVIZ)
        tahmini_net = self.safe_get(calc, self.COL_BILANCO_TAHMINI)

        text = (
            f"Günlük Bilanço Tahminleri — {self._date_str(snapshot_date)}\n"
            f"  Net Döviz Pozisyonu (A02-A11-A14-A13): {self._fmt_usd(net_doviz_pos)}\n"
            f"  Tahmini Net Rezerv (A02-A11-A14, kamu hariç): {self._fmt_usd(tahmini_net)}\n"
            f"\n"
            f"NOT: Bu tahminler haftalık vaziyet yayını gecikirken kullanılan günlük proxy'lerdir."
        )

        return self._build_response(
            intent="gunluk_tahmin",
            text=text,
            data={
                "net_doviz_pozisyonu_milyar_usd": net_doviz_pos,
                "tahmini_net_rezerv_milyar_usd": tahmini_net,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_altin_kompozisyon(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Altın rezerv kompozisyonu — Brüt / Net / SH."""
        from ..rezerv.config import GRAM_PER_TROY_OZ
        raw = self._raw()
        calc = self._calc()

        brut_altin_usd = self.safe_get(raw, self.COL_BRUT_ALTIN)  # Milyon USD
        brut_altin_milyar = brut_altin_usd / 1000.0 if brut_altin_usd is not None else None
        net_altin = self.safe_get(calc, self.COL_NET_ALTIN)

        sh_altin = self.safe_get(calc, self.COL_SH_NET_ALTIN)
        if sh_altin is None:
            sh_altin = self.safe_get(calc, self.COL_SH_NET_ALTIN_LEGACY)

        bl0021 = self.safe_get(raw, self.COL_BL0021)
        troy_ons = (bl0021 / GRAM_PER_TROY_OZ) if bl0021 is not None else None
        ton = bl0021 / 1_000_000.0 if bl0021 is not None else None

        text_parts = [
            f"Altın Rezerv Kompozisyonu — {self._date_str(snapshot_date)}",
            f"  Brüt Altın Rezervi: {self._fmt_usd(brut_altin_milyar)}",
            f"  Net Altın Rezervi:  {self._fmt_usd(net_altin)}",
            f"  SH Net Altın:       {self._fmt_usd(sh_altin)}",
        ]
        if troy_ons is not None and ton is not None:
            text_parts.append(
                f"  Miktar: {troy_ons / 1e6:.2f} milyon troy ons (≈ {ton:.0f} ton)"
            )

        return self._build_response(
            intent="altin_kompozisyon",
            text="\n".join(text_parts),
            data={
                "brut_altin_milyar_usd": brut_altin_milyar,
                "net_altin_milyar_usd": net_altin,
                "sh_altin_milyar_usd": sh_altin,
                "altin_ton": ton,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_doviz_kompozisyon(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """Döviz rezerv kompozisyonu — Brüt / Net / SH."""
        raw = self._raw()
        calc = self._calc()

        brut_doviz_usd = self.safe_get(raw, self.COL_BRUT_DOVIZ)  # Milyon USD
        brut_doviz_milyar = brut_doviz_usd / 1000.0 if brut_doviz_usd is not None else None
        net_doviz = self.safe_get(calc, self.COL_NET_DOVIZ)

        sh_doviz = self.safe_get(calc, self.COL_SH_NET_DOVIZ)
        if sh_doviz is None:
            sh_doviz = self.safe_get(calc, self.COL_SH_NET_DOVIZ_LEGACY)

        text = (
            f"Döviz Rezerv Kompozisyonu — {self._date_str(snapshot_date)}\n"
            f"  Brüt Döviz Rezervi: {self._fmt_usd(brut_doviz_milyar)}\n"
            f"  Net Döviz Rezervi:  {self._fmt_usd(net_doviz)}\n"
            f"  SH Net Döviz:       {self._fmt_usd(sh_doviz)}"
        )

        return self._build_response(
            intent="doviz_kompozisyon",
            text=text,
            data={
                "brut_doviz_milyar_usd": brut_doviz_milyar,
                "net_doviz_milyar_usd": net_doviz,
                "sh_doviz_milyar_usd": sh_doviz,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_swap_breakdown(self, snapshot_date: _dt.date | None) -> AnalystResponse:
        """TCMB swap pozisyonları kırılımı."""
        raw = self._raw()
        calc = self._calc()

        toplam = self.safe_get(raw, self.COL_DOVVARNC_K14)
        mb_acik = self.safe_get(raw, self.COL_DOVVARNC_K18)
        mb_fazla = self.safe_get(raw, self.COL_DOVVARNC_K22)
        diger = self.safe_get(raw, self.COL_DOVVARNC_K23)
        mb_toplam = self.safe_get(calc, self.COL_MB_SWAP_TOPLAM)
        if mb_toplam is None and mb_acik is not None and mb_fazla is not None:
            mb_toplam = mb_acik + mb_fazla

        text = (
            f"TCMB Swap Pozisyonları — {self._date_str(snapshot_date)}\n"
            f"  Toplam Swap (URDL aylık):   {self._fmt_usd(toplam)}\n"
            f"  M.B. Açık Swap:             {self._fmt_usd(mb_acik)}\n"
            f"  M.B. Fazla Swap:            {self._fmt_usd(mb_fazla)}\n"
            f"  M.B. Swap Toplam (K18+K22): {self._fmt_usd(mb_toplam)}\n"
            f"  Diğer Swap (II.3):          {self._fmt_usd(diger)}"
        )

        return self._build_response(
            intent="swap_breakdown",
            text=text,
            data={
                "toplam_swap": toplam,
                "mb_acik_swap": mb_acik,
                "mb_fazla_swap": mb_fazla,
                "mb_swap_toplam": mb_toplam,
                "diger_swap": diger,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_tarihsel_karsilastirma(
        self, snapshot_date: _dt.date | None
    ) -> AnalystResponse:
        """Tarihsel değişim — haftalık / aylık / YBB."""
        raw = self._raw()

        change_1 = self.change_from_n_periods_ago(raw, self.COL_BRUT_TOPLAM, n=1)
        change_4 = self.change_from_n_periods_ago(raw, self.COL_BRUT_TOPLAM, n=4)

        ybb_change: float | None = None
        if self.COL_BRUT_TOPLAM in raw.columns and not raw.empty:
            latest_ts = raw.index[-1]
            year_start = pd.Timestamp(latest_ts.year, 1, 1)
            year_start_data = raw[raw.index <= year_start][self.COL_BRUT_TOPLAM]
            if len(year_start_data) > 0:
                ybb_base = year_start_data.iloc[-1]
                ybb_change = float(raw[self.COL_BRUT_TOPLAM].iloc[-1] - ybb_base)

        def _to_milyar(v: float | None) -> str:
            return self._fmt_change(v / 1000.0) if v is not None else self._fmt_change(None)

        text = (
            f"Brüt Rezerv Tarihsel Değişim — {self._date_str(snapshot_date)}\n"
            f"  Haftalık (1 dönem): {_to_milyar(change_1)}\n"
            f"  Aylık (~4 dönem):   {_to_milyar(change_4)}\n"
            f"  Yıl Başından Beri (YBB): {_to_milyar(ybb_change)}"
        )

        return self._build_response(
            intent="tarihsel_karsilastirma",
            text=text,
            data={
                "haftalik_degisim": change_1 / 1000.0 if change_1 is not None else None,
                "aylik_degisim": change_4 / 1000.0 if change_4 is not None else None,
                "ybb_degisim": ybb_change / 1000.0 if ybb_change is not None else None,
            },
            snapshot_date=snapshot_date,
        )


# =============================================================================
# Backwards-Compat Module-Level API
# =============================================================================

def classify_intent(query: str) -> str | None:
    """Module-level classify_intent — eski test'ler için backwards-compat.

    Yeni kod için RezervAnalystAgent(snapshot).classify_intent(query) kullanın.
    """
    # Geçici instance ile classify çağır (snapshot None toleranslı)
    _agent = RezervAnalystAgent(snapshot=None)
    return _agent.classify_intent(query)
