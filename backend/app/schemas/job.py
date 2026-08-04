from pydantic import BaseModel


class JobResponse(BaseModel):

    id: int

    title: str

    company: str

    location: str | None

    employment_type: str | None

    experience_level: str | None

    description: str

    url: str

    source: str

    is_remote: bool

    salary: str | None

    skills: str | None

    model_config = {
        "from_attributes": True
    }