import datetime
from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
    phone: str
    address: str
    birth: datetime.date


class CreateUserResponse(CreateUserRequest):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ReadUserRequest(BaseModel):
    id: str


class ReadUserResponse(ReadUserRequest):
    email: EmailStr
    password: str
    name: str
    phone: str
    address: str
    birth: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UpdateUserRequest(BaseModel):
    id: str
    email: EmailStr
    password: str
    name: str
    phone: str
    address: str
    birth: datetime.date


class UpdateUserResponse(UpdateUserRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class DeleteUserRequest(BaseModel):
    id: str
    email: EmailStr
    password: str


class DeleteUserResponse(DeleteUserRequest):
    name: str
    phone: str
    address: str
    birth: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime


class LoginUserRequest(BaseModel):
    email: EmailStr
    password: str


class LoginUserResponse(LoginUserRequest):
    id: str
    email: EmailStr
    name: str
    phone: str
    address: str
    birth: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime
