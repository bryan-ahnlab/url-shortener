import uuid
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func
from db.database import Base


class UserActivityHistory(Base):
    __tablename__ = "user_activity_histories"

    id: Mapped[str] = mapped_column(
        String(32), primary_key=True, default=lambda: uuid.uuid4().hex, unique=True
    )
    user_id: Mapped[str] = mapped_column(String(32), index=True)
    email: Mapped[str] = mapped_column(String(255))
    activity_type: Mapped[str] = mapped_column(String(50))  # LOGIN, UPDATE, DELETE 등
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    ip_address: Mapped[str] = mapped_column(String(50), nullable=True)
    user_agent: Mapped[str] = mapped_column(String(255), nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    activity_time: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
