from openai import AsyncOpenAI

from app.core.config import settings


class LLMClient:
    """
    Wrapper around the configured LLM provider.
    """

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    async def generate(
        self,
        prompt: str,
        system: str = "You are a professional career assistant.",
        model: str = "gpt-4.1-mini",
    ) -> str:

        response = await self.client.chat.completions.create(
            model=model,
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