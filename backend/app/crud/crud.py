from utils.base62 import shorten_uuid
from db.database import SessionLocal

from models.service import URL
from schemas.service import CreateURL, ReadURL

def create_url(request: CreateURL):
    db = SessionLocal()
    try:
        db_url = URL(long_url=request.long_url)
        db.add(db_url)
        db.commit()
        db.refresh(db_url)

        short_url = shorten_uuid()
        while db.query(URL).filter(URL.short_url == short_url).first() is not None:
            short_url = shorten_uuid()
        
        db_url.short_url = short_url

        db.commit()
        db.refresh(db_url)

        return db_url
    except Exception as error:
        db.rollback()  
        raise error
    finally:
        db.close()

def read_url(request: ReadURL):    
    db = SessionLocal()
    try:
        db_url = db.query(URL).filter(URL.short_url == request.short_url).first()
        return db_url    
    except Exception as error:        
        raise error
    finally:
        db.close()