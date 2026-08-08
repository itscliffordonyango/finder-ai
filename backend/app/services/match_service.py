from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.matcher import calculate_match_score
from app.ai.recommender import generate_recommendation
from app.repositories.job_repository import JobRepository
from app.repositories.resume_repository import ResumeRepository
from app.ai.ranker import rank_job


class MatchService:
    def __init__(self, db: AsyncSession):
        self.jobs = JobRepository(db)
        self.resumes = ResumeRepository(db)

    async def match_jobs(
        self,
        resume_id: int,
    ):
        resume = await self.resumes.get_by_id(resume_id)

        if not resume:
            return []

        jobs = await self.jobs.get_all()

        results = []

        for job in jobs:
            score = rank_job(
                resume.extracted_text,
                job,
            )

            recommendation = generate_recommendation(
                resume.extracted_text,
                job.skills,
            )

            recommendation = generate_recommendation(
                 resume.extracted_text,
                 job.skills,)
            results.append(
                {
                    "score": score,
                    "job": job,
                    "reason": ("Strong skills match"
                               if score >= 80
                               else "Partial skills match"),
                 }

                )
            
            results.sort(
                key=lambda x: x["score"],
                reverse=True,
                )
            return results