from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.job import JobResponse
from app.services.job_service import JobService
from app.services.scraper_service import ScraperService

router = APIRouter()


@router.get(
    "/",
    response_model=list[JobResponse],
)
async def list_jobs(
    keyword: str | None = Query(None),
    company: str | None = Query(None),
    location: str | None = Query(None),
    remote: bool |None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    service = JobService(db)

    if any([keyword, company, location, remote is not None]):
        return await service.search_jobs(
            keyword=keyword,
            company=company,
            location=location,
            remote=remote,
        )

    return await service.list_jobs()


@router.post("/refresh")
async def refresh_jobs(
    db: AsyncSession = Depends(get_db),
):
    service = ScraperService(db)

    return await service.refresh_jobs()