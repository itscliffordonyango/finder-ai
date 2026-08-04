from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.job_repository import JobRepository
from app.scrapers.scraper_manager import ScraperManager


class ScraperService:

    def __init__(self, db: AsyncSession):
        self.repository = JobRepository(db)
        self.manager = ScraperManager()

    async def refresh_jobs(self):

        jobs = await self.manager.scrape_all()

        added = 0
        duplicates = 0

        for job in jobs:

            existing = await self.repository.get_by_url(
                job["url"]
            )

            if existing:
                duplicates += 1
                continue

            await self.repository.create(**job)

            added += 1

        return {
            "jobs_found": len(jobs),
            "jobs_added": added,
            "duplicates": duplicates,
        }