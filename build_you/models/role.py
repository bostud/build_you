import enum
from sqlalchemy import Column, String, Enum, Integer

from build_you.models.base import BaseModel
from build_you.database import Base


class Role(BaseModel, Base):
    __tablename__ = 'role'

    class Status(enum.Enum):
        ACTIVE = 1
        INACTIVE = 2
        DELETED = 3

    name = Column(String(length=50))
    priority = Column(Integer, default=1)
    status = Column(Enum(Status), default=Status.ACTIVE)
