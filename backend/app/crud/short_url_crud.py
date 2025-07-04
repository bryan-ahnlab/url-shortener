from db.database import SessionLocal

from models.short_url_model import ShortUrl

from schemas.short_url_schema import CreateShortUrlRequest, ReadShortUrlRequest

from utils.base62 import shorten_uuid


def create_short_url(request: CreateShortUrlRequest):
    db = SessionLocal()
    try:
        short_url = shorten_uuid()

        while (
            db.query(ShortUrl).filter(ShortUrl.short_url == short_url).first()
            is not None
        ):
            short_url = shorten_uuid()

        data = ShortUrl(
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


def read_short_url(request: ReadShortUrlRequest):
    db = SessionLocal()
    try:
        data = (
            db.query(ShortUrl).filter(ShortUrl.short_url == request.short_url).first()
        )

        return data
    except Exception as error:
        raise error
    finally:
        db.close()
