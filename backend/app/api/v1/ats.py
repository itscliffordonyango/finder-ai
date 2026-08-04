from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.ats import ATSResponse
from app.services.ats_service import ATSService

router = APIRouter()


@router.get(
    "/{resume_id}",
    response_model=ATSResponse,
)
async def ats_score(
    resume_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = ATSService(db)

    return await service.analyze(
        resume_id
    )