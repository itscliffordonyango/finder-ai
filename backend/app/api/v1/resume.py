from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume_service import ResumeService

from app.services.parser_service import ResumeParserService

router = APIRouter()


@router.post(
    "/upload",
    response_model=ResumeResponse,
)
async def upload_resume(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):

    service = ResumeService(db)

    return await service.upload_resume(
        user_id=1,
        file=file,
    )

@router.post("/{resume_id}/parse")
async def parse_resume(
    resume_id: int,
    db: AsyncSession = Depends(get_db),
):

    service = ResumeParserService(db)

    return await service.parse_resume(
        resume_id
    )