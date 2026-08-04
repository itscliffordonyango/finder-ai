from math import ceil
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.job_repository import JobRepository


class JobService:
    def __init__(self, db: AsyncSession):
        self.repository = JobRepository(db)

    async def list_jobs(
        self,
        page: int = 1,
        limit: int = 20,
    ):
        jobs = await self.repository.get_all(
            page=page,
            limit=limit,
        )
        total = await self.repository.count()
        return {
            "page": page,
            "limit": limit,
            "total": total,
            "pages": ceil(total / limit) if total else 0,
            "jobs": jobs,
        }

    async def create_job(self, **kwargs):
        existing = await self.repository.get_by_url(kwargs["url"])

        if existing:
            return existing

        return await self.repository.create(**kwargs)

    async def search_jobs(
        self,
        keyword: str | None = None,
        company: str | None = None,
        location: str | None = None,
        remote: bool | None = None,
        page: int = 1,
        limit: int = 20,
    ):
        jobs = await self.repository.search(
            keyword=keyword,
            company=company,
            location=location,
            remote=remote,
        )
        total = len(jobs)
        start = (page - 1) * limit
        end = start + limit
        jobs = jobs[start:end]
        
        return {
            "page": page,
            "limit": limit,
            "total": total,
            "pages": ceil(total / limit) if total else 0,
            "jobs": jobs,
        }
