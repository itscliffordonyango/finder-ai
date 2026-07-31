import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.paths import RESUME_UPLOAD_DIR
from app.repositories.resume_repository import ResumeRepository


class ResumeService:

    def __init__(self, db: AsyncSession):
        self.repository = ResumeRepository(db)

    async def upload_resume(
        self,
        user_id: int,
        file: UploadFile,
    ):

        allowed = {
            ".pdf",
            ".docx",
        }

        extension = Path(file.filename).suffix.lower()

        if extension not in allowed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unsupported file type",
            )

        filename = f"{uuid.uuid4()}{extension}"

        destination = RESUME_UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        return await self.repository.create(
            user_id=user_id,
            filename=filename,
            original_filename=file.filename,
            file_path=f"uploads/resumes/{filename}",
        )