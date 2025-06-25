import datetime
from typing import Optional
from pydantic import BaseModel


class ShortenURLRequest(BaseModel):
    long_url: str
    description: Optional[str] = None


class ShortenURLResponse(ShortenURLRequest):
    id: str
    short_url: str
    created_at: datetime.datetime


class RedirectURL(BaseModel):
    short_url: str
