from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.factory import get_ai_provider
from app.ai.prompts import COVER_LETTER_SYSTEM

from app.repositories.resume_repository import ResumeRepository
from app.repositories.job_repository import JobRepository


class CoverLetterService:

    def __init__(self, db: AsyncSession):
        self.ai = get_ai_provider()
        self.resumes = ResumeRepository(db)
        self.jobs = JobRepository(db)

    async def generate(
        self,
        resume_id: int,
        job_id: int,
    ):

        resume = await self.resumes.get_by_id(resume_id)

        if resume is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found",
            )

        job = await self.jobs.get_by_id(job_id)

        if job is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )

        if not resume.extracted_text:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Resume has not been parsed.",
            )

        prompt = f"""
Resume

{resume.extracted_text}

-----------------------------------

Job Title

{job.title}

Company

{job.company}

Job Description

{job.description}

Required Skills

{job.skills}

-----------------------------------

Write a professional personalized cover letter.
"""

        letter = await self.ai.generate(
            prompt=prompt,
            system=COVER_LETTER_SYSTEM,
        )

        return {
            "cover_letter": letter,
        }