from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.application_repository import (
    ApplicationRepository,
)


class ApplicationService:

    def __init__(self, db: AsyncSession):
        self.repository = ApplicationRepository(db)

    async def save_job(
        self,
        user_id: int,
        job_id: int,
    ):
        existing = await self.repository.get(
            user_id,
            job_id,
        )

        if existing:
            return existing

        return await self.repository.save_job(
            user_id,
            job_id,
        )

    async def list_saved(
        self,
        user_id: int,
    ):
        return await self.repository.get_user_jobs(
            user_id
        )

    async def update_status(
    self,
    user_id: int,
    job_id: int,
    status: str,):
        application = await self.repository.get(
        user_id,
        job_id,
    )
        if application is None:
            return None
        return await self.repository.update_status(
        application,
        status,
    )

    async def remove_saved_job(
        self,
        user_id: int,
        job_id: int,
    ):
        application = await self.repository.get(user_id,job_id,)
        if application is None:
            return False
        await self.repository.delete(application)
        return True