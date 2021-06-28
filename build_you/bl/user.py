from typing import Optional, List
import hashlib
from uuid import uuid4
from build_you.models import User
from sqlalchemy.orm import Session
from build_you.schemas.user import UserCreate
from build_you.schemas.auth import AuthLogin

from build_you.utils.datetime import datetime_now_tz
from datetime import timedelta


def get_users(db: Session) -> List[Optional[User]]:
    return db.query(User).all()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> Optional[User]:
    salt = create_salt()
    hash_password = hash_user_password(user.password, salt)
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash_password,
        salt=salt,
    )
    db.add(db_user)
    db.flush()
    return db_user


def create_salt() -> str:
    return str(uuid4()).replace('-', '')


def hash_user_password(password: str, salt: str) -> str:
    hash_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100_000
    ).hex()
    return hash_key


def check_user_login_credentials(
    auth: AuthLogin,
    user: User
) -> bool:
    password = hash_user_password(auth.password, user.salt)
    if password == user.password:
        return True
    return False


def create_api_token(db: Session, user: User) -> User:
    timestamp = datetime_now_tz().timestamp()
    hash_obj = hashlib.sha256(
        f"{user.email}+{user.first_name}+{create_salt()}_{timestamp}".encode()
    )
    api_token = hash_obj.hexdigest()
    user.api_token = api_token
    user.expire_datetime = datetime_now_tz() + timedelta(hours=12)
    db.flush([user])
    return user
