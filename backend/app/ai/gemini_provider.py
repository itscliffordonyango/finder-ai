from google import genai
from google.genai import types

from app.ai.provider import AIProvider
from app.core.config import settings


class GeminiProvider(AIProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )

    async def generate(
        self,
        prompt: str,
        system: str,
    ) -> str:

        response = await self.client.aio.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=0.7,
            ),
        )

        return response.text.strip()