import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class CreateUserActivityHistoryRequest(BaseModel):
    user_id: str
    activity_type: Optional[str] = None
    description: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    location: Optional[str] = None


class CreateUserActivityHistoryResponse(CreateUserActivityHistoryRequest):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ReadUserActivityHistoryRequest(BaseModel):
    id: str


class ReadUserActivityHistoryResponse(ReadUserActivityHistoryRequest):
    user_id: str
    activity_type: str
    description: str
    ip_address: str
    user_agent: str
    location: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UpdateUserActivityHistoryRequest(BaseModel):
    id: str
    user_id: Optional[str] = None
    email: Optional[EmailStr] = None
    activity_type: Optional[str] = None
    description: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    location: Optional[str] = None


class UpdateUserActivityHistoryResponse(UpdateUserActivityHistoryRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class DeleteUserActivityHistoryRequest(BaseModel):
    id: str


class DeleteUserActivityHistoryResponse(DeleteUserActivityHistoryRequest):
    user_id: str
    activity_type: str
    description: str
    ip_address: str
    user_agent: str
    location: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ReadUserActivityHistoryByUserIdRequest(BaseModel):
    user_id: str


class ReadUserActivityHistoryByUserIdResponse(ReadUserActivityHistoryByUserIdRequest):
    user_id: str
    activity_type: str
    description: str
    ip_address: str
    user_agent: str
    location: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
