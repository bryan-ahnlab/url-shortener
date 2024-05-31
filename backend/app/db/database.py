from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def createDatabaseEngine(url: str):
    global engine
    """ The function from SQLAlchemy is used to create a database engine. It takes the database URL (SQLALCHEMY_DATABASE_URL) as an argument, which specifies the database connection details. """
    engine = create_engine(
        url,
        pool_size=20,
        max_overflow=10,
        pool_recycle=3600,
        pool_pre_ping=True,
        echo=False,
    )

    global Session
    """ Created using the sessionmaker function from SQLAlchemy's orm module. It configures the session to be used for database operations. The autocommit and autoflush parameters are set to False to ensure more control over transactions. """
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return engine

""" Defined using declarative_base from SQLAlchemy's ext.declarative module. It serves as the base class for declarative models. """
Base = declarative_base()

def SessionLocal():
    """ Returns a new session object when called. """
    return Session()

def dropDatabaseEngine():
    """ Closes the database engine when called. """
    engine.dispose()

