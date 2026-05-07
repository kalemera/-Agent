"""BaseAnalystAgent + IntentDefinition + normalize_tr testleri."""

from __future__ import annotations

import pandas as pd
import pytest

from evds_registry.agent.base_analyst import (
    AnalystResponse,
    BaseAnalystAgent,
    IntentDefinition,
    normalize_tr,
)


# =============================================================================
# A) TestNormalizeTR
# =============================================================================


class TestNormalizeTR:
    def test_turkce_karakter_donusumu(self):
        assert normalize_tr("ışık") == "isik"
        assert normalize_tr("şahin") == "sahin"
        assert normalize_tr("ğüneş") == "gunes"
        assert normalize_tr("çocuk") == "cocuk"
        assert normalize_tr("öküz") == "okuz"
        assert normalize_tr("ülke") == "ulke"

    def test_lowercase_donusum(self):
        assert normalize_tr("BÜYÜK") == "buyuk"
        assert normalize_tr("Karışık") == "karisik"

    def test_bos_input(self):
        assert normalize_tr("") == ""

    def test_none_input(self):
        # normalize_tr None'u tolere etmeli (or-fallback ""): boş string döner
        assert normalize_tr(None) == ""  # type: ignore[arg-type]

    def test_karisik_alfabetik(self):
        # Küçük harf TR karakterler ASCII'ye çevrilir
        assert normalize_tr("işçi çalışıyor") == "isci calisiyor"
        assert normalize_tr("TÜFE Yıllık") == "tufe yillik"


# =============================================================================
# B) TestIntentDefinition
# =============================================================================


class TestIntentDefinition:
    def test_default_handler_adi_uretilir(self):
        idef = IntentDefinition(name="bir_intent", keywords=[["a"]])
        assert idef.handler == "_handle_bir_intent"

    def test_custom_handler_override(self):
        idef = IntentDefinition(
            name="x", keywords=[["a"]], handler="my_custom_handler"
        )
        assert idef.handler == "my_custom_handler"

    def test_priority_default_100(self):
        idef = IntentDefinition(name="x", keywords=[["a"]])
        assert idef.priority == 100

    def test_description_default_bos(self):
        idef = IntentDefinition(name="x", keywords=[["a"]])
        assert idef.description == ""


# =============================================================================
# C) TestBaseAnalystAgentBasic
# =============================================================================


class TestBaseAnalystAgentBasic:
    def test_bos_intents_ile_init_crash_etmez(self):
        agent = BaseAnalystAgent()
        assert agent.list_intents() == []

    def test_classify_bos_query_none_doner(self):
        agent = BaseAnalystAgent()
        assert agent.classify_intent("") is None

    def test_classify_no_match_none_doner(self):
        agent = BaseAnalystAgent()
        assert agent.classify_intent("merhaba dünya") is None

    def test_help_text_intent_yoksa_default_mesaj(self):
        agent = BaseAnalystAgent()
        text = agent._help_text()
        assert "Tanımlı intent yok" in text

    def test_response_intent_yoksa_help_text_doner(self):
        agent = BaseAnalystAgent()
        resp = agent.response("herhangi bir soru")
        assert isinstance(resp, AnalystResponse)
        assert resp.intent is None
        assert "intent yok" in resp.text.lower()


# =============================================================================
# D) TestIntentClassification
# =============================================================================


class _DummyAgent(BaseAnalystAgent):
    """Test için dummy agent."""

    AGENT_NAME = "Dummy"
    INTENTS = [
        IntentDefinition(
            name="and_match",
            keywords=[["yıllık", "tüfe"]],
            priority=10,
        ),
        IntentDefinition(
            name="or_match",
            keywords=[["alpha"], ["beta"]],
            priority=20,
        ),
        IntentDefinition(
            name="dusuk_priority_genel",
            keywords=[["genel"]],
            priority=50,
        ),
        IntentDefinition(
            name="yuksek_priority_dar",
            keywords=[["genel", "dar"]],
            priority=5,
        ),
    ]

    def _handle_and_match(self, snapshot_date):
        return self._build_response(intent="and_match", text="and ok")

    def _handle_or_match(self, snapshot_date):
        return self._build_response(intent="or_match", text="or ok")

    def _handle_dusuk_priority_genel(self, snapshot_date):
        return self._build_response(intent="dusuk_priority_genel", text="genel ok")

    def _handle_yuksek_priority_dar(self, snapshot_date):
        return self._build_response(intent="yuksek_priority_dar", text="dar ok")


class TestIntentClassification:
    def test_tek_keyword_grubu_match(self):
        agent = _DummyAgent()
        assert agent.classify_intent("yıllık tüfe ne kadar") == "and_match"

    def test_and_mantigi_eksik_kelime_match_etmez(self):
        agent = _DummyAgent()
        # Sadece "yıllık" var, "tüfe" yok → and_match olmaz
        assert agent.classify_intent("yıllık raporu") != "and_match"

    def test_or_mantigi_alternatif_grup_match(self):
        agent = _DummyAgent()
        assert agent.classify_intent("alpha geldi") == "or_match"
        assert agent.classify_intent("beta geliyor") == "or_match"

    def test_priority_dusuk_sayi_once_kontrol_edilir(self):
        agent = _DummyAgent()
        # "genel dar" hem yuksek_priority_dar (p=5) hem dusuk_priority_genel (p=50) match eder
        # dusuk priority sayı önce → yuksek_priority_dar dönmeli
        assert agent.classify_intent("genel dar konu") == "yuksek_priority_dar"

    def test_tr_normalize_match(self):
        agent = _DummyAgent()
        # Kullanıcı "yıllık" yazıyor, keyword "yıllık" olarak tanımlı —
        # her iki taraf normalize edildikten sonra eşleşmeli
        assert agent.classify_intent("YILLIK TÜFE") == "and_match"
        assert agent.classify_intent("yillik tufe") == "and_match"


# =============================================================================
# E) TestExtensionAPI
# =============================================================================


class TestExtensionAPI:
    def test_add_intent_yeni_ekler(self):
        agent = BaseAnalystAgent()
        agent.add_intent(IntentDefinition(name="yeni", keywords=[["x"]], priority=10))
        names = [d.name for d in agent.list_intents()]
        assert "yeni" in names

    def test_add_intent_ayni_isim_replace(self):
        agent = BaseAnalystAgent()
        agent.add_intent(
            IntentDefinition(name="yeni", keywords=[["a"]], priority=10)
        )
        agent.add_intent(
            IntentDefinition(name="yeni", keywords=[["b"]], priority=20)
        )
        intents = agent.list_intents()
        assert len(intents) == 1
        assert intents[0].priority == 20
        assert intents[0].keywords == [["b"]]

    def test_remove_intent_varsa_true_doner(self):
        agent = BaseAnalystAgent()
        agent.add_intent(IntentDefinition(name="silinecek", keywords=[["a"]]))
        result = agent.remove_intent("silinecek")
        assert result is True
        assert all(d.name != "silinecek" for d in agent.list_intents())

    def test_remove_intent_yoksa_false_doner(self):
        agent = BaseAnalystAgent()
        assert agent.remove_intent("yok") is False

    def test_list_intents_priority_sirali(self):
        agent = BaseAnalystAgent()
        agent.add_intent(IntentDefinition(name="b", keywords=[["b"]], priority=50))
        agent.add_intent(IntentDefinition(name="a", keywords=[["a"]], priority=10))
        agent.add_intent(IntentDefinition(name="c", keywords=[["c"]], priority=30))
        names = [d.name for d in agent.list_intents()]
        assert names == ["a", "c", "b"]


# =============================================================================
# F) TestHandlerDispatch
# =============================================================================


class _CustomAgent(BaseAnalystAgent):
    AGENT_NAME = "Custom"
    INTENTS = [
        IntentDefinition(name="ozel", keywords=[["test"]], priority=10),
    ]

    def _handle_ozel(self, snapshot_date):
        return self._build_response(intent="ozel", text="özel cevap")


class _MissingHandlerAgent(BaseAnalystAgent):
    AGENT_NAME = "Missing"
    INTENTS = [
        IntentDefinition(name="bos", keywords=[["test"]], priority=10),
        # `_handle_bos` tanımlı değil
    ]


class TestHandlerDispatch:
    def test_custom_handler_cagirilir(self):
        agent = _CustomAgent()
        resp = agent.response("test mesajı")
        assert resp.intent == "ozel"
        assert resp.text == "özel cevap"

    def test_handler_yoksa_anlamli_hata_mesaji(self):
        agent = _MissingHandlerAgent()
        resp = agent.response("test")
        assert resp.intent == "bos"
        assert "handler tanımlı değil" in resp.text

    def test_handle_str_doner(self):
        agent = _CustomAgent()
        text = agent.handle("test")
        assert isinstance(text, str)
        assert text == "özel cevap"


# =============================================================================
# G) TestHelperMethods
# =============================================================================


class TestHelperMethods:
    def test_safe_get_var_olan_kolon(self):
        df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
        assert BaseAnalystAgent.safe_get(df, "a") == 3.0
        assert BaseAnalystAgent.safe_get(df, "a", idx=0) == 1.0

    def test_safe_get_var_olmayan_kolon(self):
        df = pd.DataFrame({"a": [1.0]})
        assert BaseAnalystAgent.safe_get(df, "yok") is None

    def test_safe_get_bos_df(self):
        df = pd.DataFrame()
        assert BaseAnalystAgent.safe_get(df, "a") is None

    def test_safe_get_nan_deger(self):
        df = pd.DataFrame({"a": [1.0, float("nan")]})
        assert BaseAnalystAgent.safe_get(df, "a") is None  # son deger nan

    def test_safe_get_none_df(self):
        assert BaseAnalystAgent.safe_get(None, "a") is None  # type: ignore[arg-type]

    def test_change_from_n_periods_yeterli_data(self):
        df = pd.DataFrame({"a": [10.0, 20.0, 30.0]})
        # son 30, önceki 20 → fark 10
        assert BaseAnalystAgent.change_from_n_periods_ago(df, "a", n=1) == pytest.approx(
            10.0
        )

    def test_change_from_n_periods_yetersiz_data(self):
        df = pd.DataFrame({"a": [10.0]})
        assert BaseAnalystAgent.change_from_n_periods_ago(df, "a", n=1) is None

    def test_change_from_n_periods_nan_data(self):
        df = pd.DataFrame({"a": [10.0, float("nan")]})
        assert BaseAnalystAgent.change_from_n_periods_ago(df, "a", n=1) is None

    def test_format_number_none(self):
        assert BaseAnalystAgent.format_number(None) == "veri yok"

    def test_format_number_decimals(self):
        assert BaseAnalystAgent.format_number(3.14159, decimals=2) == "3.14"
        assert BaseAnalystAgent.format_number(3.14159, decimals=4) == "3.1416"

    def test_format_number_unit(self):
        assert BaseAnalystAgent.format_number(55.1, unit="%") == "55.10 %"
        # unit boşsa rstrip etkili
        assert BaseAnalystAgent.format_number(1.0) == "1.00"

    def test_format_change_pozitif(self):
        result = BaseAnalystAgent.format_change(2.5, unit="puan")
        assert result.startswith("+2.50")
        assert "puan" in result

    def test_format_change_negatif(self):
        result = BaseAnalystAgent.format_change(-1.3, unit="puan")
        assert result.startswith("-1.30")

    def test_format_change_none(self):
        assert "önceki" in BaseAnalystAgent.format_change(None).lower()
