from abc import ABC, abstractmethod


class BaseScraper(ABC):
    @abstractmethod
    async def scrape(self) -> list[dict]:
        """
        Returns a list of normalized job dictionaries.
        """
        raise NotImplementedError
