from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: str,
    ) -> str:
        """
        Generate a response from an LLM.
        """
        pass