from sqlalchemy.ext.asyncio import AsyncSession

from app.models.resume import Resume


class ResumeRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        **kwargs,
    ) -> Resume:

        resume = Resume(**kwargs)

        self.db.add(resume)

        await self.db.commit()

        await self.db.refresh(resume)

        return resume