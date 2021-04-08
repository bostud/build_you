from pydantic import BaseModel


class AuthBase(BaseModel):
    email: str
    password: str


class AuthLogin(AuthBase):
    remember_me: bool


class AuthSuccess(BaseModel):
    cookie_token: str
