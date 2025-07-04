from db.database import Base
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
import uuid
import datetime


class UserActivityHistory(Base):
    __tablename__ = "user_activity_histories"

    id: Mapped[str] = mapped_column(
        String(32), primary_key=True, default=lambda: uuid.uuid4().hex, unique=True
    )
    user_id: Mapped[str] = mapped_column(String(32), index=True)
    activity_type: Mapped[str] = mapped_column(
        String(50), nullable=True
    )  # LOGIN, UPDATE, DELETE 등
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    ip_address: Mapped[str] = mapped_column(String(50), nullable=True)
    user_agent: Mapped[str] = mapped_column(String(255), nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
