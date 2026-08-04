from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    score: float

    matched_skills: list[str]

    missing_skills: list[str]

    strengths: list[str]

    recommendation: str