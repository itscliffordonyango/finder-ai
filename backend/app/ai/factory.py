from app.ai.openai_provider import OpenAIProvider
from app.ai.gemini_provider import GeminiProvider
from app.ai.ollama_provider import OllamaProvider

from app.core.config import settings


def get_ai_provider():

    if settings.AI_PROVIDER == "openai":
        return OpenAIProvider()

    if settings.AI_PROVIDER == "gemini":
        return GeminiProvider()

    if settings.AI_PROVIDER == "ollama":
        return OllamaProvider()

    raise ValueError(
        f"Unsupported AI provider: {settings.AI_PROVIDER}"
    )