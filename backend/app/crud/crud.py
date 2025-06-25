from utils.base62 import shorten_uuid
from db.database import SessionLocal

from models.service import ShortenedURL
from schemas.service import ShortenURLRequest, RedirectURL


def create_url(request: ShortenURLRequest):
    db = SessionLocal()
    try:
        short_url = shorten_uuid()
        while (
            db.query(ShortenedURL).filter(ShortenedURL.short_url == short_url).first()
            is not None
        ):
            short_url = shorten_uuid()

        data = ShortenedURL(
            long_url=request.long_url,
            description=request.description,
            short_url=short_url,
        )
        db.add(data)
        db.commit()
        db.refresh(data)

        return data
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()


def read_url(request: RedirectURL):
    db = SessionLocal()
    try:
        data = (
            db.query(ShortenedURL)
            .filter(ShortenedURL.short_url == request.short_url)
            .first()
        )

        return data
    except Exception as error:
        raise error
    finally:
        db.close()
