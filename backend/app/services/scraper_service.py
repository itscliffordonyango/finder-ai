from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.job_repository import JobRepository
from app.scrapers.remoteok import RemoteOKScraper


class ScraperService:

    def __init__(self, db: AsyncSession):
        self.repository = JobRepository(db)

    async def refresh_jobs(self):

        scraper = RemoteOKScraper()

        jobs = await scraper.scrape()

        added = 0

        for job in jobs:

            existing = await self.repository.get_by_url(
                job["url"]
            )

            if existing:
                continue

            await self.repository.create(**job)

            added += 1

        return {
            "jobs_added": added,
            "total_found": len(jobs),
        }