from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

settings = get_settings()


engine = create_engine(
    f"{settings.db_provider}://{settings.user}:{settings.password}@{settings.db_url}"
)

SessionLocal = sessionmaker(
    autoflush=False, bind=engine
)
Base = declarative_base()


def create_db_and_tables(engine):
    Base.metadata.create_all(bind=engine)
