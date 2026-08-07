from pydantic import BaseModel


class CoverLetterRequest(BaseModel):
    resume_id: int
    job_id: int


class CoverLetterResponse(BaseModel):
    cover_letter: str