from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.analysis import ResumeAnalysisResponse
from app.services.analysis_service import AnalysisService

router = APIRouter()


@router.get(
    "/{resume_id}/{job_id}",
    response_model=ResumeAnalysisResponse,
)
async def analyze_resume(
    resume_id: int,
    job_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = AnalysisService(db)

    return await service.analyze(
        resume_id,
        job_id,
    )