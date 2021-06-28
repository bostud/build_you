from pydantic import BaseModel
from datetime import datetime


class AuthBase(BaseModel):
    email: str
    password: str


class AuthLogin(AuthBase):
    remember_me: bool = False


class AuthSuccess(BaseModel):
    api_token: str
    expire: datetime


class AuthLogout(BaseModel):
    api_token: str
