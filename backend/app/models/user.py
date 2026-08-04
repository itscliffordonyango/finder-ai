from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(
        String(255)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255)
    )