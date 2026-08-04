"""create jobs table

Revision ID: d95d76ca960d
Revises: f297520ae775
Create Date: 2026-08-01 11:49:02.381440
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d95d76ca960d"
down_revision: Union[str, Sequence[str], None] = "f297520ae775"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "jobs",
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("company", sa.String(length=255), nullable=False),
        sa.Column("location", sa.String(length=255), nullable=True),
        sa.Column("employment_type", sa.String(length=100), nullable=True),
        sa.Column("experience_level", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("url", sa.Text(), nullable=False),
        sa.Column("source", sa.String(length=100), nullable=False),
        sa.Column("is_remote", sa.Boolean(), nullable=False),
        sa.Column("salary", sa.String(length=255), nullable=True),
        sa.Column("skills", sa.Text(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("url"),
    )

    op.create_index(
        op.f("ix_jobs_company"),
        "jobs",
        ["company"],
        unique=False,
    )

    op.create_index(
        op.f("ix_jobs_title"),
        "jobs",
        ["title"],
        unique=False,
    )

    op.create_index(
        op.f("ix_jobs_source"),
        "jobs",
        ["source"],
        unique=False,
    )

    op.create_index(
        op.f("ix_jobs_id"),
        "jobs",
        ["id"],
        unique=False,
    )

    # Added because Resume now inherits from BaseModel
    op.add_column(
        "resumes",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("resumes", "updated_at")

    op.drop_index(op.f("ix_jobs_id"), table_name="jobs")
    op.drop_index(op.f("ix_jobs_source"), table_name="jobs")
    op.drop_index(op.f("ix_jobs_title"), table_name="jobs")
    op.drop_index(op.f("ix_jobs_company"), table_name="jobs")

    op.drop_table("jobs")
