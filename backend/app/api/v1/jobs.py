from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.job import JobResponse
from app.services.job_service import JobService
from app.services.scraper_service import ScraperService
from app.schemas.pagination import PaginatedJobsResponse

router = APIRouter()


@router.get(
    "/",
    response_model=PaginatedJobsResponse,
)
async def list_jobs(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    keyword: str | None = Query(None),
    company: str | None = Query(None),
    location: str | None = Query(None),
    remote: bool | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    service = JobService(db)

    if any([keyword, company, location, remote is not None]):
        return await service.search_jobs(
            keyword=keyword,
            company=company,
            location=location,
            remote=remote,
            page=page,
            limit=limit,
        )

    return await service.list_jobs(
        page=page,
        limit=limit,
    )

@router.post("/refresh")
async def refresh_jobs(
    db: AsyncSession = Depends(get_db),
):
    service = ScraperService(db)

    return await service.refresh_jobs()