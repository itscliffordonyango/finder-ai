from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.application import Application


class ApplicationRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def save_job(
        self,
        user_id: int,
        job_id: int,
    ):
        application = Application(
            user_id=user_id,
            job_id=job_id,
            status="saved",
        )

        self.db.add(application)

        await self.db.commit()

        await self.db.refresh(application)

        return application

    async def get_user_jobs(
        self,
        user_id: int,
    ):
        result = await self.db.execute(
            select(Application)
            .where(Application.user_id == user_id)
            .order_by(Application.created_at.desc())
        )

        return result.scalars().all()

    async def get(
        self,
        user_id: int,
        job_id: int,
    ):
        result = await self.db.execute(
            select(Application).where(
                Application.user_id == user_id,
                Application.job_id == job_id,
            )
        )

        return result.scalar_one_or_none()
    async def update_status(
    self,
    application: Application,
    status: str,
    ):
        application.status = status
        await self.db.commit()
        await self.db.refresh(application)
        return application

    async def delete(
        self,application: Application,
        ):
        await self.db.delete(application)
        await self.db.commit()

    async def count(
        self,
        user_id: int,
        ):
        result = await self.db.execute(
            select(Application).where(
                Application.user_id == user_id
                )
                )
        return len(result.scalars().all())
