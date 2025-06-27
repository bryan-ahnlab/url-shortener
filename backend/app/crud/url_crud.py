from utils.base62 import shorten_uuid
from db.database import SessionLocal

from models.url_model import Url
from schemas.url_schema import ShortenUrlRequest, RedirectUrl


def create_url(request: ShortenUrlRequest):
    db = SessionLocal()
    try:
        short_url = shorten_uuid()
        while db.query(Url).filter(Url.short_url == short_url).first() is not None:
            short_url = shorten_uuid()

        data = Url(
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


def read_url(request: RedirectUrl):
    db = SessionLocal()
    try:
        data = db.query(Url).filter(Url.short_url == request.short_url).first()

        return data
    except Exception as error:
        raise error
    finally:
        db.close()
