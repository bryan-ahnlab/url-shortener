from db.database import Base
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
import uuid
import datetime


class ShortUrl(Base):
    __tablename__ = "short_urls"

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
