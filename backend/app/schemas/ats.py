from pydantic import BaseModel


class ATSResponse(BaseModel):
    overall_score: int

    categories: dict[str, int]

    feedback: list[str]