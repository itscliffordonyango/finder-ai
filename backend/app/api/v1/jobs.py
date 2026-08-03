from fastapi import APIRouter, Depends
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
    db: AsyncSession = Depends(get_db),
):
    service = JobService(db)

    return await service.list_jobs()

@router.post("/refresh")
async def refresh_jobs(
    db: AsyncSession = Depends(get_db),
):
    service = ScraperService(db)

    return await service.refresh_jobs()