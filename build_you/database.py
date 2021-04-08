from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLALCHEMY_DATABASE_URL = "postgresql://buildu:12344321@localhost:5432/buildu"

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf8')
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
