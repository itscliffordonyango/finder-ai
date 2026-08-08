import httpx

from app.ai.provider import AIProvider
from app.core.config import settings


class OllamaProvider(AIProvider):

    async def generate(
        self,
        prompt: str,
        system: str,
    ) -> str:

        payload = {
            "model": settings.OLLAMA_MODEL,
            "system": system,
            "prompt": prompt,
            "stream": False,
        }

        async with httpx.AsyncClient(
            timeout=120
        ) as client:

            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json=payload,
            )

            response.raise_for_status()

            data = response.json()

        return data["response"].strip()