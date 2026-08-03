from sqlalchemy import (
    String,
    Text,
    Boolean,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.models.base_model import BaseModel


class Job(BaseModel):
    __tablename__ = "jobs"

    title: Mapped[str] = mapped_column(
        String(255),
        index=True,
    )

    company: Mapped[str] = mapped_column(
        String(255),
        index=True,
    )

    location: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    experience_level: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    url: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )

    source: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    is_remote: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    salary: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )