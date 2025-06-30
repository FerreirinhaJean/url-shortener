"""Create url table

Revision ID: f14dcb49f1b3
Revises:
Create Date: 2025-06-27 17:29:16.689116

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "f14dcb49f1b3"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "url",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("url", sa.String(length=250), nullable=False),
        sa.Column("url_code", sa.String(length=250), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("url")
