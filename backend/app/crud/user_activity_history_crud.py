from typing import Optional
from models.user_activity_history_model import UserActivityHistory
from db.database import SessionLocal
from pydantic import EmailStr


def create_user_activity_history(
    user_id: str,
    email: EmailStr,
    activity_type: str,
    description: Optional[str] = None,
    ip_address: Optional[str] = None,
    user_agent: Optional[str] = None,
    location: Optional[str] = None,
):
    db = SessionLocal()
    try:
        history = UserActivityHistory(
            user_id=user_id,
            email=email,
            activity_type=activity_type,
            description=description,
            ip_address=ip_address,
            user_agent=user_agent,
            location=location,
        )
        db.add(history)
        db.commit()
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()
