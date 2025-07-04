from pydantic import EmailStr
from db.database import SessionLocal

from models.user_model import User
from schemas.user_schema import (
    CreateUserRequest,
    ReadUserRequest,
    UpdateUserRequest,
    DeleteUserRequest,
)

from passlib.hash import bcrypt


def create_user(request: CreateUserRequest):
    db = SessionLocal()
    try:
        hashed_password = bcrypt.hash(request.password)

        new_user = User(
            email=request.email,
            password=hashed_password,
            name=request.name,
            phone=request.phone,
            address=request.address,
            birth=request.birth,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()


def read_user_by_email(email: EmailStr):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.email == email).first()
    finally:
        db.close()


def read_user(request: ReadUserRequest | UpdateUserRequest | DeleteUserRequest):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.id == request.id).first()
    finally:
        db.close()


def update_user(request: UpdateUserRequest):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == request.id).first()

        if not user:
            return None

        if request.email:
            user.email = request.email
        if request.password:
            user.password = bcrypt.hash(request.password)
        if request.name:
            user.name = request.name
        if request.phone:
            user.phone = request.phone
        if request.address:
            user.address = request.address
        if request.birth:
            user.birth = request.birth

        db.commit()
        db.refresh(user)

        return user
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()


def delete_user(request: DeleteUserRequest):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == request.id).first()

        if not user:
            return None

        db.delete(user)
        db.commit()
        return user
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.verify(plain_password, hashed_password)
