"""RezervAnalystAgent — TCMB rezerv durumu için intent-driven yanıt agent'i.

Kullanım:
    from evds_registry.rezerv import run_pipeline, RezervSnapshot
    from evds_registry.agent.rezerv_analyst_agent import RezervAnalystAgent

    snapshot = run_pipeline(raw_evds, raw_urdl, raw_pdf)
    agent = RezervAnalystAgent(snapshot)

    print(agent.handle("Bu hafta brüt rezerv ne kadar?"))
    # → "Brüt Rezerv: 168.9 milyar USD (2026-04-25)
    #    Önceki haftaya göre: -7.7 milyar USD"
"""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field

import pandas as pd

from ..rezerv import RezervSnapshot


# =============================================================================
# Intent Tanımları
# =============================================================================

INTENT_KEYWORDS: dict[str, list[list[str]]] = {
    # Her intent için anahtar kelime gruplari (ALL OF gerekli)
    "brut_rezerv_durum": [
        ["brüt", "rezerv"],
        ["brut", "rezerv"],
        ["gross", "reserve"],
        ["toplam", "rezerv"],
    ],
    "net_rezerv_durum": [
        ["net", "rezerv"],
        ["net", "uluslararası"],
        ["nir"],
        ["nur"],
    ],
    "swap_haric_rezerv": [
        ["swap", "hariç"],
        ["swap", "haric"],
        ["sh", "rezerv"],
        ["swap'sız"],
        ["swapsız"],
    ],
    "gunluk_tahmin": [
        ["günlük", "tahmin"],
        ["gunluk", "tahmin"],
        ["bilanço", "tahmin"],
        ["günlük", "rezerv"],
        ["analitik", "bilanço"],
    ],
    "altin_kompozisyon": [
        ["altın"],
        ["altin"],
        ["gold"],
    ],
    "doviz_kompozisyon": [
        ["döviz", "kompozisyon"],
        ["doviz", "kompozisyon"],
        ["fx", "reserve"],
        ["döviz", "rezerv"],
    ],
    "swap_breakdown": [
        ["swap", "büyüklük"],
        ["swap", "buyukluk"],
        ["swap", "stok"],
        ["mb", "swap"],
        ["m.b.", "swap"],
    ],
    "tarihsel_karsilastirma": [
        ["yıl başı"],
        ["yil basi"],
        ["ybb"],
        ["aylık", "değişim"],
        ["aylik", "degisim"],
        ["haftalık", "değişim"],
    ],
}

# Intent'lerin sıralı denemesi — özel olanlar önce
INTENT_PRIORITY: list[str] = [
    "swap_haric_rezerv",      # "swap hariç" → diğer rezerv intent'lerine kaymasın
    "gunluk_tahmin",
    "tarihsel_karsilastirma",
    "swap_breakdown",
    "altin_kompozisyon",
    "doviz_kompozisyon",
    "net_rezerv_durum",
    "brut_rezerv_durum",
]


def _normalize_query(text: str) -> str:
    """TR karakterleri normalize et + lowercase."""
    s = text.lower()
    for tr, en in [("ı", "i"), ("ş", "s"), ("ğ", "g"), ("ç", "c"), ("ö", "o"), ("ü", "u")]:
        s = s.replace(tr, en)
    return s


def classify_intent(query: str) -> str | None:
    """Sorudan intent çıkar. Hiçbir match yoksa None."""
    q_norm = _normalize_query(query)
    for intent in INTENT_PRIORITY:
        keyword_groups = INTENT_KEYWORDS[intent]
        for group in keyword_groups:
            # Bu grupta tüm kelimeler match etmeli
            if all(_normalize_query(kw) in q_norm for kw in group):
                return intent
    return None


# =============================================================================
# Output Formatlayıcılar
# =============================================================================

def _format_milyar_usd(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "veri yok"
    return f"{value:.2f} milyar USD"


def _format_change(diff: float | None, unit: str = "milyar USD") -> str:
    if diff is None or pd.isna(diff):
        return "(önceki dönem yok)"
    sign = "+" if diff >= 0 else ""
    return f"{sign}{diff:.2f} {unit}"


def _safe_get(df: pd.DataFrame, col: str, idx: int = -1) -> float | None:
    if df.empty or col not in df.columns:
        return None
    try:
        v = df[col].iloc[idx]
        return float(v) if pd.notna(v) else None
    except (KeyError, IndexError, ValueError, TypeError):
        return None


def _change_from_n_periods_ago(
    df: pd.DataFrame,
    col: str,
    n: int = 1,
) -> float | None:
    """Son değer - N dönem öncesi değer."""
    if df.empty or col not in df.columns or len(df) <= n:
        return None
    latest = df[col].iloc[-1]
    earlier = df[col].iloc[-n - 1]
    if pd.isna(latest) or pd.isna(earlier):
        return None
    return float(latest - earlier)


# =============================================================================
# Agent
# =============================================================================

@dataclass
class RezervAnalystResponse:
    """Agent yanıtının yapılandırılmış hali."""
    intent: str | None
    text: str
    data: dict[str, float | None] = field(default_factory=dict)
    snapshot_date: _dt.date | None = None


class RezervAnalystAgent:
    """TCMB rezerv durumu için intent-driven yanıt agent'i.

    Her intent için bir handler method'u vardır. handle() public API'dir;
    response() yapılandırılmış yanıt döner.
    """

    def __init__(self, snapshot: RezervSnapshot):
        self.snapshot = snapshot

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def handle(self, query: str) -> str:
        """Soru alır, formatlanmış yanıt döner."""
        return self.response(query).text

    def response(self, query: str) -> RezervAnalystResponse:
        """Yapılandırılmış yanıt döner."""
        intent = classify_intent(query)
        snapshot_date = self._latest_date()

        if intent is None:
            return RezervAnalystResponse(
                intent=None,
                text=(
                    "Sorunuzu anlayamadım. Şu konularda yardımcı olabilirim:\n"
                    "- Brüt rezerv durumu\n"
                    "- Net Uluslararası Rezerv (NIR)\n"
                    "- Swap hariç net rezerv\n"
                    "- Günlük bilanço bazlı rezerv tahmini\n"
                    "- Altın / Döviz rezerv kompozisyonu\n"
                    "- TCMB swap pozisyonları (M.B. + diğer + altın)\n"
                    "- Tarihsel değişim (haftalık, aylık, yıl başı)"
                ),
                snapshot_date=snapshot_date,
            )

        handler = self._get_handler(intent)
        return handler(snapshot_date)

    # ------------------------------------------------------------------
    # Internal — handler dispatch
    # ------------------------------------------------------------------

    def _get_handler(self, intent: str):
        return {
            "brut_rezerv_durum": self._handle_brut_rezerv,
            "net_rezerv_durum": self._handle_net_rezerv,
            "swap_haric_rezerv": self._handle_swap_haric,
            "gunluk_tahmin": self._handle_gunluk_tahmin,
            "altin_kompozisyon": self._handle_altin,
            "doviz_kompozisyon": self._handle_doviz,
            "swap_breakdown": self._handle_swap_breakdown,
            "tarihsel_karsilastirma": self._handle_tarihsel,
        }[intent]

    def _latest_date(self) -> _dt.date | None:
        c = self.snapshot.calculated
        if c.empty:
            return None
        idx = c.index[-1]
        if isinstance(idx, pd.Timestamp):
            return idx.date()
        return None

    # ------------------------------------------------------------------
    # Intent Handlers
    # ------------------------------------------------------------------

    def _handle_brut_rezerv(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """Brüt Rezerv durumu — TP.AB.TOPLAM bazlı."""
        raw = self.snapshot.raw
        latest = _safe_get(raw, "AB.TOPLAM")  # Milyon USD
        if latest is None:
            latest_mr = _safe_get(self.snapshot.calculated, "BrutRezervTL_URDL")
            text = (
                f"Brüt rezerv (TP.AB.TOPLAM) verisi bulunamadı.\n"
                f"URDL alternatif yolu (BL toplamı): "
                f"{_format_milyar_usd(latest_mr)} (Milyar TL bazlı tahmin)"
                if latest_mr else
                "Brüt rezerv verisi bulunamadı."
            )
            return RezervAnalystResponse(
                intent="brut_rezerv_durum",
                text=text,
                snapshot_date=snapshot_date,
            )

        latest_milyar = latest / 1000.0
        change_w = _change_from_n_periods_ago(raw, "AB.TOPLAM", n=1)
        change_w_milyar = (change_w / 1000.0) if change_w is not None else None

        date_str = snapshot_date.isoformat() if snapshot_date else "?"
        text = (
            f"Brüt Rezerv: {latest_milyar:.2f} milyar USD ({date_str})\n"
            f"Önceki döneme göre: {_format_change(change_w_milyar)}"
        )

        return RezervAnalystResponse(
            intent="brut_rezerv_durum",
            text=text,
            data={"brut_rezerv_milyar_usd": latest_milyar, "haftalik_degisim": change_w_milyar},
            snapshot_date=snapshot_date,
        )

    def _handle_net_rezerv(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """Net Uluslararası Rezerv (NIR) durumu."""
        calc = self.snapshot.calculated
        net_altin = _safe_get(calc, "NetAltinUSD")
        net_doviz = _safe_get(calc, "NetDovizUSD")

        nir = None
        if net_altin is not None and net_doviz is not None:
            nir = net_altin + net_doviz

        date_str = snapshot_date.isoformat() if snapshot_date else "?"
        text = (
            f"Net Uluslararası Rezerv (NIR) — {date_str}\n"
            f"  Net Altın Rezervi: {_format_milyar_usd(net_altin)}\n"
            f"  Net Döviz Rezervi: {_format_milyar_usd(net_doviz)}\n"
            f"  Toplam NIR: {_format_milyar_usd(nir)}"
        )

        return RezervAnalystResponse(
            intent="net_rezerv_durum",
            text=text,
            data={
                "net_altin_milyar_usd": net_altin,
                "net_doviz_milyar_usd": net_doviz,
                "nir_milyar_usd": nir,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_swap_haric(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """Swap Hariç Net Rezerv durumu."""
        calc = self.snapshot.calculated
        # `or` yerine `is None` kullan: 0.0 değer yanlışlıkla fallback'e düşmesin
        sh_altin = _safe_get(calc, "SHNetAltin")
        if sh_altin is None:
            sh_altin = _safe_get(calc, "SH_NetAltin")
        sh_doviz = _safe_get(calc, "SHNetDoviz")
        if sh_doviz is None:
            sh_doviz = _safe_get(calc, "SH_NetDoviz")
        sh_total_g = _safe_get(calc, "SHNetRezervGunluk")
        sh_total_u = _safe_get(calc, "SHNetRezervURDL")

        date_str = snapshot_date.isoformat() if snapshot_date else "?"
        text = (
            f"Swap Hariç Net Rezerv — {date_str}\n"
            f"  SH Net Altın: {_format_milyar_usd(sh_altin)}\n"
            f"  SH Net Döviz: {_format_milyar_usd(sh_doviz)}\n"
            f"  SH NUR (Günlük PDF bazlı): {_format_milyar_usd(sh_total_g)}\n"
            f"  SH NUR (URDL standart): {_format_milyar_usd(sh_total_u)}"
        )

        return RezervAnalystResponse(
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

    def _handle_gunluk_tahmin(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """Günlük analitik bilanço bazlı tahmin."""
        calc = self.snapshot.calculated
        net_doviz_pos = _safe_get(calc, "BilancoNetDovizPozisyonu")
        tahmini_net = _safe_get(calc, "BilancoTahminiNetRezerv")

        date_str = snapshot_date.isoformat() if snapshot_date else "?"
        text = (
            f"Günlük Bilanço Tahminleri — {date_str}\n"
            f"  Net Döviz Pozisyonu (A02-A11-A14-A13): {_format_milyar_usd(net_doviz_pos)}\n"
            f"  Tahmini Net Rezerv (A02-A11-A14, kamu hariç): {_format_milyar_usd(tahmini_net)}\n"
            f"\n"
            f"NOT: Bu tahminler haftalık vaziyet yayını gecikirken kullanılan günlük proxy'lerdir."
        )

        return RezervAnalystResponse(
            intent="gunluk_tahmin",
            text=text,
            data={
                "net_doviz_pozisyonu_milyar_usd": net_doviz_pos,
                "tahmini_net_rezerv_milyar_usd": tahmini_net,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_altin(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """Altın rezerv kompozisyonu — Brüt / Net / SH."""
        raw = self.snapshot.raw
        calc = self.snapshot.calculated

        brut_altin_usd = _safe_get(raw, "AB.C1")  # Milyon USD
        brut_altin_milyar = brut_altin_usd / 1000.0 if brut_altin_usd is not None else None
        net_altin = _safe_get(calc, "NetAltinUSD")
        # `or` yerine `is None`: 0.0 değeri yanlışlıkla fallback'e düşmesin
        sh_altin = _safe_get(calc, "SHNetAltin")
        if sh_altin is None:
            sh_altin = _safe_get(calc, "SH_NetAltin")

        # Troy ons miktarı — `if X` yerine `is not None`: 0.0 ton durumu da işlenir
        bl0021 = _safe_get(raw, "BL0021")
        troy_ons = (bl0021 / 31.1034768) if bl0021 is not None else None
        ton = bl0021 / 1_000_000.0 if bl0021 is not None else None

        date_str = snapshot_date.isoformat() if snapshot_date else "?"
        text_parts = [f"Altın Rezerv Kompozisyonu — {date_str}"]
        text_parts.append(f"  Brüt Altın Rezervi: {_format_milyar_usd(brut_altin_milyar)}")
        text_parts.append(f"  Net Altın Rezervi:  {_format_milyar_usd(net_altin)}")
        text_parts.append(f"  SH Net Altın:       {_format_milyar_usd(sh_altin)}")
        if troy_ons is not None:
            text_parts.append(f"  Miktar: {troy_ons / 1e6:.2f} milyon troy ons (≈ {ton:.0f} ton)")

        return RezervAnalystResponse(
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

    def _handle_doviz(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """Döviz rezerv kompozisyonu — Brüt / Net / SH."""
        raw = self.snapshot.raw
        calc = self.snapshot.calculated

        brut_doviz_usd = _safe_get(raw, "AB.C2")  # Milyon USD
        brut_doviz_milyar = brut_doviz_usd / 1000.0 if brut_doviz_usd is not None else None
        net_doviz = _safe_get(calc, "NetDovizUSD")
        # `or` yerine `is None`: 0.0 değeri yanlışlıkla fallback'e düşmesin
        sh_doviz = _safe_get(calc, "SHNetDoviz")
        if sh_doviz is None:
            sh_doviz = _safe_get(calc, "SH_NetDoviz")

        date_str = snapshot_date.isoformat() if snapshot_date else "?"
        text = (
            f"Döviz Rezerv Kompozisyonu — {date_str}\n"
            f"  Brüt Döviz Rezervi: {_format_milyar_usd(brut_doviz_milyar)}\n"
            f"  Net Döviz Rezervi:  {_format_milyar_usd(net_doviz)}\n"
            f"  SH Net Döviz:       {_format_milyar_usd(sh_doviz)}"
        )

        return RezervAnalystResponse(
            intent="doviz_kompozisyon",
            text=text,
            data={
                "brut_doviz_milyar_usd": brut_doviz_milyar,
                "net_doviz_milyar_usd": net_doviz,
                "sh_doviz_milyar_usd": sh_doviz,
            },
            snapshot_date=snapshot_date,
        )

    def _handle_swap_breakdown(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """TCMB swap pozisyonları kırılımı."""
        raw = self.snapshot.raw
        calc = self.snapshot.calculated

        toplam = _safe_get(raw, "DOVVARNC.K14")
        mb_acik = _safe_get(raw, "DOVVARNC.K18")
        mb_fazla = _safe_get(raw, "DOVVARNC.K22")
        diger = _safe_get(raw, "DOVVARNC.K23")
        mb_toplam = _safe_get(calc, "MBSwapToplam")
        if mb_toplam is None and mb_acik is not None and mb_fazla is not None:
            mb_toplam = mb_acik + mb_fazla

        date_str = snapshot_date.isoformat() if snapshot_date else "?"
        text = (
            f"TCMB Swap Pozisyonları — {date_str}\n"
            f"  Toplam Swap (URDL aylık):   {_format_milyar_usd(toplam)}\n"
            f"  M.B. Açık Swap:             {_format_milyar_usd(mb_acik)}\n"
            f"  M.B. Fazla Swap:            {_format_milyar_usd(mb_fazla)}\n"
            f"  M.B. Swap Toplam (K18+K22): {_format_milyar_usd(mb_toplam)}\n"
            f"  Diğer Swap (II.3):          {_format_milyar_usd(diger)}"
        )

        return RezervAnalystResponse(
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

    def _handle_tarihsel(self, snapshot_date: _dt.date | None) -> RezervAnalystResponse:
        """Tarihsel değişim — haftalık / aylık / YBB."""
        raw = self.snapshot.raw

        # Haftalık ~ 1 dönem
        change_1 = _change_from_n_periods_ago(raw, "AB.TOPLAM", n=1)
        # Aylık ~ 4 dönem (haftalık veride)
        change_4 = _change_from_n_periods_ago(raw, "AB.TOPLAM", n=4)

        # YBB hesabı: yıl başına en yakın tarihteki değer
        ybb_change = None
        if "AB.TOPLAM" in raw.columns and not raw.empty:
            latest_ts = raw.index[-1]
            year_start = pd.Timestamp(latest_ts.year, 1, 1)
            year_start_data = raw[raw.index <= year_start]["AB.TOPLAM"]
            if len(year_start_data) > 0:
                ybb_base = year_start_data.iloc[-1]
                ybb_change = float(raw["AB.TOPLAM"].iloc[-1] - ybb_base)

        date_str = snapshot_date.isoformat() if snapshot_date else "?"

        def _to_milyar(v: float | None) -> str:
            return _format_change(v / 1000.0) if v is not None else _format_change(None)

        text = (
            f"Brüt Rezerv Tarihsel Değişim — {date_str}\n"
            f"  Haftalık (1 dönem): {_to_milyar(change_1)}\n"
            f"  Aylık (~4 dönem):   {_to_milyar(change_4)}\n"
            f"  Yıl Başından Beri (YBB): {_to_milyar(ybb_change)}"
        )

        return RezervAnalystResponse(
            intent="tarihsel_karsilastirma",
            text=text,
            data={
                # `if X` yerine `is not None`: 0.0 değişim de doğru rapor edilir
                "haftalik_degisim": change_1 / 1000.0 if change_1 is not None else None,
                "aylik_degisim": change_4 / 1000.0 if change_4 is not None else None,
                "ybb_degisim": ybb_change / 1000.0 if ybb_change is not None else None,
            },
            snapshot_date=snapshot_date,
        )
