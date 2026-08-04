from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.job_repository import JobRepository


class JobService:
    def __init__(self, db: AsyncSession):
        self.repository = JobRepository(db)

    async def list_jobs(self):
        return await self.repository.get_all()

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
    ):
        return await self.repository.search(
            keyword=keyword,
            company=company,
            location=location,
            remote=remote,
        )