from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.job_repository import JobRepository
from app.repositories.resume_repository import ResumeRepository


class DashboardService:
    def __init__(self, db: AsyncSession):
        self.jobs = JobRepository(db)
        self.resumes = ResumeRepository(db)

    async def get_dashboard(self):
        jobs = await self.jobs.get_all()
        resumes = await self.resumes.get_all()

        total_jobs = len(jobs)
        total_resumes = len(resumes)

        matched_jobs = 0

        for resume in resumes:
            if resume.extracted_text:
                matched_jobs += 1

        return {
            "total_jobs": total_jobs,
            "total_resumes": total_resumes,
            "parsed_resumes": matched_jobs,
            "jobs_available": total_jobs,
        }