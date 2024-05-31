import uuid
from sqlalchemy import CHAR, Column
from db.database import Base
from sqlalchemy.dialects.mysql import LONGTEXT

class URL(Base):
    __tablename__ = "URLS"
    id = Column(CHAR(32), primary_key=True, default=lambda: uuid.uuid4().hex, unique=True, nullable=False)
    long_url = Column(LONGTEXT, index=True)
    short_url = Column(LONGTEXT, unique=True, index=True)