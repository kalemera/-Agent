from __future__ import annotations

from evds_registry.llm import DisabledLLMClient, build_llm_client_from_env


def test_build_llm_client_from_env_prefers_local_when_model_is_set(monkeypatch):
    monkeypatch.delenv("OLLAMA_API_KEY", raising=False)
    monkeypatch.delenv("OLLAMA_CLOUD_API_KEY", raising=False)
    monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)
    monkeypatch.delenv("OLLAMA_HOST", raising=False)
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    monkeypatch.setenv("OLLAMA_MODEL", "deepseek-r1:latest")

    client = build_llm_client_from_env()

    assert client.provider_name == "ollama_local"
    assert client.model_name == "deepseek-r1:latest"
    assert client.is_enabled() is True


def test_build_llm_client_from_env_uses_cloud_when_api_key_is_present(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    monkeypatch.setenv("OLLAMA_MODEL", "gpt-oss:20b")
    monkeypatch.setenv("OLLAMA_API_KEY", "test-key")
    monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)
    monkeypatch.delenv("OLLAMA_HOST", raising=False)

    client = build_llm_client_from_env()

    assert client.provider_name == "ollama_cloud"
    assert client.model_name == "gpt-oss:20b"
    assert client.is_enabled() is True


def test_build_llm_client_from_env_disables_when_model_missing(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    monkeypatch.delenv("OLLAMA_MODEL", raising=False)
    monkeypatch.delenv("LLM_MODEL", raising=False)
    monkeypatch.delenv("OLLAMA_API_KEY", raising=False)
    monkeypatch.delenv("OLLAMA_CLOUD_API_KEY", raising=False)

    client = build_llm_client_from_env()

    assert isinstance(client, DisabledLLMClient)
