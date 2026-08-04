from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.ats import calculate_ats_score
from app.repositories.resume_repository import ResumeRepository


class ATSService:
    def __init__(self, db: AsyncSession):
        self.repository = ResumeRepository(db)

    async def analyze(
        self,
        resume_id: int,
    ):
        resume = await self.repository.get_by_id(
            resume_id
        )

        if resume is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found",
            )

        return calculate_ats_score(
            resume.extracted_text
        )