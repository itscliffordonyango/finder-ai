from openai import AsyncOpenAI

from app.ai.provider import AIProvider
from app.core.config import settings


class OpenAIProvider(AIProvider):

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    async def generate(
        self,
        prompt: str,
        system: str,
    ) -> str:

        response = await self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()