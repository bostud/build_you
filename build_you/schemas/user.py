from typing import Optional

from pydantic import BaseModel, validator


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    settings: Optional[dict]

    @validator('email')
    def validate_email(cls, v):
        pass


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    api_token: Optional[str]

    class Config:
        orm_mode = True
