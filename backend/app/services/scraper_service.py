from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.job_repository import JobRepository
from app.scrapers.remoteok import RemoteOKScraper
from app.scrapers.weworkremotely import WeWorkRemotelyScraper


class ScraperService:

    def __init__(self, db: AsyncSession):
        self.repository = JobRepository(db)

    async def refresh_jobs(self):

        scrapers = [
            RemoteOKScraper(),
            WeWorkRemotelyScraper()
        ]

        jobs_added = 0
        total_found = 0

        for scraper in scrapers:
            try:
                jobs = await scraper.scrape()
            except Exception as exc:
                print(f"{scraper.__class__.__name__} failed: {exc}")
                continue

            total_found += len(jobs)
            
            for job in jobs:
                existing = await self.repository.get_by_url(job["url"])
                if existing:
                    continue
                await self.repository.create(**job)
                jobs_added += 1
