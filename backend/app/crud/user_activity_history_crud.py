from db.database import SessionLocal

from models.user_activity_history_model import UserActivityHistory
from schemas.user_activity_history_schema import (
    CreateUserActivityHistoryRequest,
    ReadUserActivityHistoryRequest,
    UpdateUserActivityHistoryRequest,
    DeleteUserActivityHistoryRequest,
    ReadUserActivityHistoryByUserIdRequest,
)


def create_user_activity_history(
    request: CreateUserActivityHistoryRequest,
):
    db = SessionLocal()
    try:
        new_history = UserActivityHistory(
            user_id=request.user_id,
            activity_type=request.activity_type,
            description=request.description,
            ip_address=request.ip_address,
            user_agent=request.user_agent,
            location=request.location,
        )
        db.add(new_history)
        db.commit()
        db.refresh(new_history)

        return new_history
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()


def read_user_activity_history(
    request: (
        ReadUserActivityHistoryRequest
        | UpdateUserActivityHistoryRequest
        | DeleteUserActivityHistoryRequest
    ),
):
    db = SessionLocal()
    try:
        return (
            db.query(UserActivityHistory)
            .filter(UserActivityHistory.id == request.id)
            .first()
        )
    finally:
        db.close()


def update_user_activity_history(request: UpdateUserActivityHistoryRequest):
    db = SessionLocal()
    try:
        user_activity_history = (
            db.query(UserActivityHistory)
            .filter(UserActivityHistory.id == request.id)
            .first()
        )
        if not user_activity_history:
            return None

        if request.user_id:
            user_activity_history.user_id = request.user_id
        if request.activity_type:
            user_activity_history.activity_type = request.activity_type
        if request.description:
            user_activity_history.description = request.description
        if request.ip_address:
            user_activity_history.ip_address = request.ip_address
        if request.user_agent:
            user_activity_history.user_agent = request.user_agent
        if request.location:
            user_activity_history.location = request.location

        db.commit()
        db.refresh(user_activity_history)

        return user_activity_history
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()


def delete_user_activity_history(request: DeleteUserActivityHistoryRequest):
    db = SessionLocal()
    try:
        user_activity_history = (
            db.query(UserActivityHistory)
            .filter(UserActivityHistory.id == request.id)
            .first()
        )
        if not user_activity_history:
            return None

        db.delete(user_activity_history)
        db.commit()

        return user_activity_history
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()


def read_user_activity_history_by_user_id(
    request: ReadUserActivityHistoryByUserIdRequest,
):
    db = SessionLocal()
    try:
        return (
            db.query(UserActivityHistory)
            .filter(UserActivityHistory.user_id == request.user_id)
            .all()
        )
    finally:
        db.close()
