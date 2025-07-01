import datetime
from typing import Optional
from pydantic import BaseModel


class CreateShortUrlRequest(BaseModel):
    long_url: str
    description: Optional[str] = None


class CreateShortUrlResponse(CreateShortUrlRequest):
    id: str
    short_url: str
    created_at: datetime.datetime


class ReadShortUrlRequest(BaseModel):
    short_url: str
