from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db

from app.schemas.cover_letter import (
    CoverLetterRequest,
    CoverLetterResponse,
)

from app.services.cover_letter_service import (
    CoverLetterService,
)

router = APIRouter()


@router.post(
    "/generate",
    response_model=CoverLetterResponse,
)
async def generate_cover_letter(
    request: CoverLetterRequest,
    db: AsyncSession = Depends(get_db),
):

    service = CoverLetterService(db)

    return await service.generate(
        request.resume_id,
        request.job_id,
    )