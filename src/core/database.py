from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

from src.account.models.user import Base
from src.core.config import settings
from sqlalchemy.orm import sessionmaker, Session



sync_engine = create_engine(settings.db.db_sync_url, echo=True)

sync_session_maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine
)


def get_sync_session():
    with Session(sync_engine) as session:
        return session


# Base.metadata.create_all(sync_engine)