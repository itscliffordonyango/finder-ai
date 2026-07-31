from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume_service import ResumeService

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