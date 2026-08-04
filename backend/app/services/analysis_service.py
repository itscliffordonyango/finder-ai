from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.analyzer import analyze_resume
from app.repositories.job_repository import JobRepository
from app.repositories.resume_repository import ResumeRepository


class AnalysisService:
    def __init__(self, db: AsyncSession):
        self.jobs = JobRepository(db)
        self.resumes = ResumeRepository(db)

    async def analyze(
        self,
        resume_id: int,
        job_id: int,
    ):
        resume = await self.resumes.get_by_id(
            resume_id
        )

        if resume is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found",
            )

        job = await self.jobs.get_by_id(
            job_id
        )

        if job is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )

        return analyze_resume(
            resume.extracted_text,
            job.skills,
        )