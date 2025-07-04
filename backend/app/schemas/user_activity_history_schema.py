# schemas/user_activity_history_schema.py

import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUserActivityHistoryRequest(BaseModel):
    user_id: str
    email: EmailStr
    activity_type: str
    description: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    location: Optional[str] = None


class ReadUserActivityHistoryResponse(BaseModel):
    id: str
    user_id: str
    email: EmailStr
    activity_type: str
    description: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    location: Optional[str] = None
    created_at: datetime.datetime
