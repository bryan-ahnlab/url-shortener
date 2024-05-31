from pydantic import BaseModel

class CreateURL(BaseModel):
    long_url: str

class ReadURL(BaseModel):
    short_url: str