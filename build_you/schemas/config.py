from pydantic import BaseModel


class DBBase(BaseModel):
    debug: bool
    dialect: str
    name: str
    user: str
    password: str
    host: str
    port: str
    autocommit: bool = True
    autoflush: bool = False


class AppBase(BaseModel):
    debug: bool


class ConfigBase(BaseModel):
    db: DBBase
    app: AppBase


def get_config():
    pass
