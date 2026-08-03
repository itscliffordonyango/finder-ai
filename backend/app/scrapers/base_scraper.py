from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    async def scrape(self):
        """
        Returns a list of normalized jobs.
        """
        pass