from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Protocol
from urllib.parse import urljoin
from urllib.request import Request, urlopen


JsonDict = dict[str, Any]


class LLMClient(Protocol):
    provider_name: str
    model_name: str

    def is_enabled(self) -> bool:
        """Return True when the client can make inference calls."""

    def generate_structured(self, prompt: str, schema: JsonDict) -> JsonDict:
        """Return a JSON object that matches the requested schema."""


@dataclass(slots=True)
class DisabledLLMClient:
    provider_name: str = "disabled"
    model_name: str = ""

    def is_enabled(self) -> bool:
        return False

    def generate_structured(self, prompt: str, schema: JsonDict) -> JsonDict:
        return {}


@dataclass(slots=True)
class OllamaChatClient:
    model_name: str
    api_key: str = ""
    base_url: str = "http://127.0.0.1:11434/api/"
    provider_name: str = "ollama_local"
    timeout_seconds: int = 60

    def is_enabled(self) -> bool:
        return bool(self.model_name)

    def generate_structured(self, prompt: str, schema: JsonDict) -> JsonDict:
        if not self.is_enabled():
            return {}
        endpoint = urljoin(self.base_url.rstrip("/") + "/", "chat")
        payload = {
            "model": self.model_name,
            "stream": False,
            "format": schema,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Use only the provided evidence. "
                        "Return a single JSON object that matches the requested schema. "
                        "Do not output prose, markdown, or explanations. "
                        "If evidence is insufficient, use empty strings or empty arrays and set a lower numeric confidence."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        }
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        request = Request(endpoint, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:  # noqa: S310
                raw = json.loads(response.read().decode("utf-8"))
        except Exception:  # noqa: BLE001
            return {}
        message = raw.get("message") or {}
        content = message.get("content")
        if isinstance(content, dict):
            return content
        if isinstance(content, str) and content.strip():
            parsed = parse_structured_content(content)
            if isinstance(parsed, dict):
                return parsed
        return {}


def parse_structured_content(content: str) -> JsonDict:
    text = content.strip()
    if not text:
        return {}
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = None
    if isinstance(parsed, dict):
        return parsed
    result: JsonDict = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        normalized_key = key.strip().strip("-").strip().strip('"').strip("'")
        if not normalized_key:
            continue
        cleaned_value = value.strip()
        if cleaned_value.casefold() in {"", "null", "none", "n/a"}:
            result[normalized_key] = ""
            continue
        if cleaned_value.casefold() in {"true", "false"}:
            result[normalized_key] = cleaned_value.casefold() == "true"
            continue
        if normalized_key == "confidence":
            lowered = cleaned_value.casefold()
            if lowered in {"low", "dusuk", "düşük"}:
                result[normalized_key] = 0.3
                continue
            if lowered in {"medium", "orta"}:
                result[normalized_key] = 0.6
                continue
            if lowered in {"high", "yuksek", "yüksek"}:
                result[normalized_key] = 0.9
                continue
            try:
                result[normalized_key] = float(cleaned_value)
                continue
            except ValueError:
                pass
        if cleaned_value.startswith("[") and cleaned_value.endswith("]"):
            try:
                array_value = json.loads(cleaned_value)
            except json.JSONDecodeError:
                array_value = None
            if isinstance(array_value, list):
                result[normalized_key] = array_value
                continue
        result[normalized_key] = cleaned_value
    return result


@dataclass(slots=True)
class OpenAICompatibleClient:
    """Generic OpenAI-compatible chat client (Qwen/DashScope, OpenAI, etc.)."""

    model_name: str
    api_key: str
    base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    provider_name: str = "qwen"
    timeout_seconds: int = 60

    def is_enabled(self) -> bool:
        return bool(self.model_name and self.api_key)

    def generate_structured(self, prompt: str, schema: JsonDict) -> JsonDict:
        if not self.is_enabled():
            return {}
        endpoint = self.base_url.rstrip("/") + "/chat/completions"
        payload = {
            "model": self.model_name,
            "response_format": {"type": "json_object"},
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Use only the provided evidence. "
                        "Return a single JSON object. "
                        "Do not output prose, markdown, or explanations. "
                        "If evidence is insufficient, use empty strings or empty arrays and set a lower numeric confidence."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        request = Request(endpoint, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:  # noqa: S310
                raw = json.loads(response.read().decode("utf-8"))
        except Exception:  # noqa: BLE001
            return {}
        choices = raw.get("choices") or []
        if not choices:
            return {}
        content = (choices[0].get("message") or {}).get("content") or ""
        if isinstance(content, dict):
            return content
        if isinstance(content, str) and content.strip():
            parsed = parse_structured_content(content)
            if isinstance(parsed, dict):
                return parsed
        return {}


def build_llm_client_from_env() -> LLMClient:
    provider = (os.getenv("LLM_PROVIDER") or "ollama").strip().casefold()
    if provider in {"", "disabled", "none"}:
        return DisabledLLMClient()

    if provider in {"qwen", "openai", "dashscope"}:
        api_key = os.getenv("QWEN_API_KEY") or os.getenv("OPENAI_API_KEY") or ""
        model = os.getenv("QWEN_MODEL") or os.getenv("OPENAI_MODEL") or os.getenv("LLM_MODEL") or ""
        base_url = (
            os.getenv("QWEN_BASE_URL")
            or os.getenv("OPENAI_BASE_URL")
            or "https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        timeout_seconds = int(os.getenv("LLM_TIMEOUT_SEC") or "60")
        if not model or not api_key:
            return DisabledLLMClient(provider_name=provider)
        return OpenAICompatibleClient(
            model_name=model,
            api_key=api_key,
            base_url=base_url,
            provider_name=provider,
            timeout_seconds=timeout_seconds,
        )

    if provider != "ollama":
        return DisabledLLMClient(provider_name=provider)

    api_key = os.getenv("OLLAMA_API_KEY") or os.getenv("OLLAMA_CLOUD_API_KEY") or ""
    model = os.getenv("OLLAMA_MODEL") or os.getenv("LLM_MODEL") or ""
    local_base_url = os.getenv("OLLAMA_BASE_URL") or os.getenv("OLLAMA_HOST") or ""
    cloud_base_url = os.getenv("OLLAMA_CLOUD_BASE_URL") or "https://ollama.com/api/"
    timeout_seconds = int(os.getenv("OLLAMA_TIMEOUT_SEC") or "60")
    if not model:
        return DisabledLLMClient()
    inferred_provider = "ollama_cloud" if model.endswith("-cloud") else "ollama_local"
    if local_base_url:
        return OllamaChatClient(
            model_name=model,
            api_key="",
            base_url=local_base_url,
            provider_name=inferred_provider,
            timeout_seconds=timeout_seconds,
        )
    if api_key:
        return OllamaChatClient(
            model_name=model,
            api_key=api_key,
            base_url=cloud_base_url,
            provider_name="ollama_cloud",
            timeout_seconds=timeout_seconds,
        )
    return OllamaChatClient(
        model_name=model,
        api_key="",
        base_url="http://127.0.0.1:11434/api/",
        provider_name=inferred_provider,
        timeout_seconds=timeout_seconds,
    )
