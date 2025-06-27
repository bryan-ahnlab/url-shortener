import datetime
from pydantic import BaseModel, EmailStr


class SignUpRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
    phone: str
    address: str
    birth: datetime.date


class SignUpResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    phone: str
    address: str
    birth: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    id: str
    email: EmailStr
    name: str


class UpdateRequest(BaseModel):
    name: str
    phone: str
    address: str
    birth: datetime.date
