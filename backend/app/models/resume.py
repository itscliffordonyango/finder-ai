from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel


class Resume(BaseModel):
    __tablename__ = "resumes"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    filename: Mapped[str] = mapped_column(
        String(255)
    )

    original_filename: Mapped[str] = mapped_column(
        String(255)
    )

    file_path: Mapped[str] = mapped_column(
        String(500)
    )

    extracted_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )