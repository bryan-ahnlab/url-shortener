from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func
from db.database import Base
import uuid
import datetime


class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id: Mapped[str] = mapped_column(
        String(32),
        primary_key=True,
        default=lambda: uuid.uuid4().hex,
        unique=True,
    )
    long_url: Mapped[str] = mapped_column(String(2048))
    short_url: Mapped[str] = mapped_column(String(16), unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
