from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Url(Base):
    __tablename__ = "url"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, unique=True, default=uuid4
    )
    url: Mapped[str] = mapped_column(String(250), nullable=False)
    url_code: Mapped[str] = mapped_column(String(250), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now(UTC)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now(UTC)
    )
    status: Mapped[bool] = mapped_column(
        Boolean(), default=True, nullable=False
    )
