"""MCP chat_with_agent + list_agent_domains tool testleri."""

from __future__ import annotations

from evds_registry.mcp_server import chat_with_agent, list_agent_domains


# =============================================================================
# chat_with_agent
# =============================================================================

class TestChatWithAgent:
    def test_rezerv_query_routes_to_rezerv_domain(self):
        result = chat_with_agent("Brüt rezerv ne kadar?")
        assert result["domain"] == "rezerv"
        assert result["snapshot_loaded"] is False
        # Snapshot yok ama help text/template metin döner
        assert isinstance(result["text"], str)
        assert "snapshot" in result["note"].lower()

    def test_tufe_query_routes_to_tufe_domain(self):
        result = chat_with_agent("Yıllık enflasyon nasıl?")
        assert result["domain"] == "tufe"
        assert result["snapshot_loaded"] is False

    def test_unknown_query_returns_help_text(self):
        result = chat_with_agent("Bana bir şiir oku")
        assert result["domain"] is None
        assert result["intent"] is None
        assert isinstance(result["text"], str)
        assert len(result["text"]) > 0

    def test_response_has_required_keys(self):
        result = chat_with_agent("Brüt rezerv")
        for key in ("domain", "intent", "text", "data", "snapshot_date", "snapshot_loaded", "note"):
            assert key in result, f"missing key: {key}"

    def test_snapshot_date_is_json_serializable(self):
        """snapshot_date None veya str olmalı (date object değil) — JSON için."""
        import json
        result = chat_with_agent("Brüt rezerv")
        # Tüm dict'in json.dumps ile serialize olabilir olmalı
        json.dumps(result)  # Raise etmez

    def test_empty_query_returns_help(self):
        result = chat_with_agent("")
        assert result["domain"] is None


# =============================================================================
# list_agent_domains
# =============================================================================

class TestListAgentDomains:
    def test_returns_dict_with_domains(self):
        result = list_agent_domains()
        assert "domains" in result
        assert isinstance(result["domains"], list)
        assert len(result["domains"]) >= 2  # rezerv + tufe

    def test_each_domain_has_required_keys(self):
        result = list_agent_domains()
        for domain in result["domains"]:
            for key in ("name", "agent_class", "description", "intents"):
                assert key in domain, f"domain {domain} missing key: {key}"

    def test_rezerv_domain_listed(self):
        result = list_agent_domains()
        names = [d["name"] for d in result["domains"]]
        assert "rezerv" in names

    def test_tufe_domain_listed(self):
        result = list_agent_domains()
        names = [d["name"] for d in result["domains"]]
        assert "tufe" in names

    def test_rezerv_has_8_intents(self):
        result = list_agent_domains()
        rezerv = next((d for d in result["domains"] if d["name"] == "rezerv"), None)
        assert rezerv is not None
        assert len(rezerv["intents"]) == 8

    def test_tufe_has_5_intents(self):
        result = list_agent_domains()
        tufe = next((d for d in result["domains"] if d["name"] == "tufe"), None)
        assert tufe is not None
        assert len(tufe["intents"]) == 5

    def test_intent_has_name_and_description(self):
        result = list_agent_domains()
        for domain in result["domains"]:
            for intent in domain["intents"]:
                assert "name" in intent
                assert "description" in intent
