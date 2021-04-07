import enum
from sqlalchemy import Column, String, JSON, Enum
from sqlalchemy.orm import relationship

from build_you.models.base import BaseModel
from build_you.database import Base


class User(BaseModel, Base):
    __tablename__ = 'user'

    class Status(enum.Enum):
        ACTIVE = 1
        INACTIVE = 2
        DELETED = 3

    first_name = Column(String(length=50))
    last_name = Column(String(length=150))
    email = Column(String(length=150), unique=True)
    phone = Column(String(length=13), default=None, nullable=True)
    settings = Column(JSON, default={})
    status = Column(Enum(Status), default=Status.ACTIVE)
    password = Column(String(length=255), index=True)
    api_token = Column(String(length=256), default=None, nullable=True)

