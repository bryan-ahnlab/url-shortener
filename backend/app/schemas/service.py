import datetime
from typing import Optional
from pydantic import BaseModel


class ShortenUrlRequest(BaseModel):
    long_url: str
    description: Optional[str] = None


class ShortenUrlResponse(ShortenUrlRequest):
    id: str
    short_url: str
    created_at: datetime.datetime


class RedirectUrl(BaseModel):
    short_url: str
