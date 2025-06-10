from sqlalchemy import CHAR, Column, String
from sqlalchemy.dialects.mysql import LONGTEXT
from db.database import Base
import uuid

class URL(Base):
    __tablename__ = "URLS"
    
    id = Column(CHAR(32), primary_key=True, default=lambda: uuid.uuid4().hex, unique=True, nullable=False)
    long_url = Column(String(255), index=True)
    short_url = Column(String(255), unique=True, index=True)
