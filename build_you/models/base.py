from sqlalchemy import Column, Integer, DateTime
from build_you.utils.datetime import datetime_now_tz

from sqlalchemy.ext.declarative import declared_attr


class BaseModel(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__tablename__.lower()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    create = Column(DateTime, default=datetime_now_tz)
    update = Column(DateTime, default=None, nullable=True)
