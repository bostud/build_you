import enum
from sqlalchemy import Column, String, JSON, Enum, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from build_you.models.base import BaseModel
from build_you.database import Base


class BuildObject(BaseModel, Base):
    __tablename__ = 'build_object'

    class Status(enum.Enum):
        NEW = 1
        WORKING = 2
        READY = 3
        CLOSE = 4

    address = Column(String(length=350))
    name = Column(String(length=255))
    description = Column(Text, default=None, nullable=True)
    status = Column(Enum(Status), default=Status.NEW)
    company_id = Column(Integer, ForeignKey('company.id'))
    settings = Column(JSON, default={}, nullable=True)
    contact = Column(Text)
