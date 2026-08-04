from app.scrapers.remoteok import RemoteOKScraper


class ScraperManager:
    def __init__(self):
        self.scrapers = [
            RemoteOKScraper(),
            # WeWorkRemotelyScraper(),
            # IndeedScraper(),
            # LinkedInScraper(),
        ]

    async def scrape_all(self):
        jobs = []

        for scraper in self.scrapers:
            try:
                jobs.extend(await scraper.scrape())
            except Exception as e:
                print(
                    f"{scraper.__class__.__name__} failed: {e}"
                )

        return jobs