from sqlalchemy import select, or_ , func
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
    async def get_all(
    self,
    page: int = 1,
    limit: int = 20,
    ):
        offset = (page - 1) * limit
        result = await self.db.execute(
        select(Job)
        .order_by(Job.created_at.desc())
        .offset(offset)
        .limit(limit)
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

    async def get_by_id(
        self,
        job_id: int,
    ):
        result = await self.db.execute(
            select(Job).where(Job.id == job_id)
        )
    
        return result.scalar_one_or_none()

    
    async def search(
        self,
        keyword: str | None = None,
        company: str | None = None,
        location: str | None = None,
        remote: bool | None = None,
    ):
        query = select(Job)

        if keyword:
            query = query.where(
                or_(
                    Job.title.ilike(f"%{keyword}%"),
                    Job.description.ilike(f"%{keyword}%"),
                    Job.skills.ilike(f"%{keyword}%"),
                    )
                )

        if company:
            query = query.where(
                Job.company.ilike(f"%{company}%")
            )

        if location:
            query = query.where(
                Job.location.ilike(f"%{location}%")
            )

        if remote is not None:
            query = query.where(
                Job.is_remote == remote
            )

        query = query.order_by(
            Job.created_at.desc()
        )

        result = await self.db.execute(query)

        return result.scalars().all()

    async def count(self):
        result = await self.db.execute(
            select(func.count(Job.id))
    )
        return result.scalar_one()
