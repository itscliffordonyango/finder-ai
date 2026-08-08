from pydantic import BaseModel

from app.schemas.job import JobResponse


class JobMatchResponse(BaseModel):
    score: float
    strengths: list[str]
    missing_skills: list[str]
    recommendation: str
    reason: str
    job: JobResponse