from pydantic import BaseModel

from app.schemas.job import JobResponse


class DashboardResponse(BaseModel):

    user_id: int

    ats_score: int

    applications: int

    recommended_jobs: list[JobResponse]

    saved_jobs: int