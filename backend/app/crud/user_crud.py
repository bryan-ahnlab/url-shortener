from models.user_model import User
from db.database import SessionLocal
from passlib.hash import bcrypt


def create_user(payload):
    db = SessionLocal()
    try:
        hashed_password = bcrypt.hash(payload.password)

        new_user = User(
            email=payload.email,
            password=hashed_password,
            name=payload.name,
            phone=payload.phone,
            address=payload.address,
            birth=payload.birth,
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


def get_user_by_email(email: str):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.email == email).first()
    finally:
        db.close()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.verify(plain_password, hashed_password)


def update_user(email: str, payload):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None

        user.name = payload.name
        user.phone = payload.phone
        user.address = payload.address
        user.birth = payload.birth

        db.commit()
        db.refresh(user)

        return user
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()
