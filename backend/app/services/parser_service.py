from pathlib import Path

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.parsers.parser_service import ParserService
from app.repositories.resume_repository import ResumeRepository


class ResumeParserService:
    def __init__(self, db: AsyncSession):
        self.repository = ResumeRepository(db)

    async def parse_resume(
        self,
        resume_id: int,
    ):
        resume = await self.repository.get_by_id(
            resume_id
        )

        if resume is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found",
            )

        backend_root = Path(__file__).resolve().parents[2]

        file_path = backend_root / resume.file_path

        text = ParserService.parse(
            str(file_path)
        )

        await self.repository.save_extracted_text(
            resume,
            text,
        )

        return {
            "resume_id": resume.id,
            "text": text,
        }