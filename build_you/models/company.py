import enum
from sqlalchemy import Column, ForeignKey, String, JSON, Integer, Enum, Text
from sqlalchemy.orm import relationship

from build_you.models.base import BaseModel
from build_you.database import Base


class Company(BaseModel, Base):
    __tablename__ = 'company'

    class Status(enum.Enum):
        ACTIVE = 1
        INACTIVE = 2
        DELETED = 3

    name = Column(String(length=255), unique=True, index=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    settings = Column(JSON, default={}, nullable=True)
    status = Column(Enum(Status), default=Status.ACTIVE)

    owner = relationship('User', back_populates='companies')
    company_objects = relationship('BuildObject', back_populates='company')
