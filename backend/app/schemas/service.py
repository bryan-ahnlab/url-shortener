import datetime
from typing import Optional
from pydantic import BaseModel

class CreateURL(BaseModel):    
    long_url: str
    description: Optional[str] = None

class ReadURL(BaseModel):
    id: str
    short_url: str
    description: Optional[str] = None
    created_at: datetime.datetime