from datetime import datetime

from pydantic import BaseModel


class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class UpdateStatusRequest(BaseModel):
    status: str