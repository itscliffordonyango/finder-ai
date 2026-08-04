from pydantic import BaseModel

from app.schemas.job import JobResponse


class JobMatchResponse(BaseModel):
    score: float
    job: JobResponse