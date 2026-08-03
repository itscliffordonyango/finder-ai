from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.job import Job


class JobRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, **kwargs):

        job = Job(**kwargs)

        self.db.add(job)

        await self.db.commit()

        await self.db.refresh(job)

        return job

    async def get_all(self):

        result = await self.db.execute(
            select(Job)
            .order_by(Job.created_at.desc())
        )

        return result.scalars().all()

    async def get_by_url(
        self,
        url: str,
    ):

        result = await self.db.execute(
            select(Job).where(Job.url == url)
        )

        return result.scalar_one_or_none()