from datetime import datetime

from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    filename: str
    original_filename: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }