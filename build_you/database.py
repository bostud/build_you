from typing import Iterator
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
    Session as AlchemySession,
    scoped_session,
)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLALCHEMY_DATABASE_URL = "postgresql://buildu:12344321@localhost:5432/buildu"

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf8')
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def acquire_auto_commit_session() -> Iterator[AlchemySession]:
    session: AlchemySession = Session()
    try:
        session.begin()
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        Session.remove()
