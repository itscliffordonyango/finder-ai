from pydantic import BaseModel

from app.schemas.job import JobResponse


class PaginatedJobsResponse(BaseModel):
    page: int
    limit: int
    total: int
    pages: int
    jobs: list[JobResponse]