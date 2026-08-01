from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import TimestampMixin

from sqlalchemy.orm import relationship

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    full_name: Mapped[str] = mapped_column(String(255))

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    resumes = relationship(
    "Resume",
    backref="user",
    cascade="all, delete-orphan",
    )

    password_hash: Mapped[str] = mapped_column(String(255))