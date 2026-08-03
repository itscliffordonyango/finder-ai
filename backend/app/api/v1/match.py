from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.match import JobMatchResponse
from app.services.match_service import MatchService

router = APIRouter()


@router.get(
    "/{resume_id}",
    response_model=list[JobMatchResponse],
)
async def match_jobs(
    resume_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = MatchService(db)

    return await service.match_jobs(resume_id)