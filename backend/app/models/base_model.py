from datetime import UTC, datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class BaseModel(Base):
    """
    Base model inherited by every database model.
    Provides:
      - id
      - created_at
      - updated_at
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
    