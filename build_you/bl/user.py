from typing import Optional, List
from build_you.models import User
from sqlalchemy.orm import Session
from build_you.schemas.user import UserCreate


def get_users(db: Session) -> List[Optional[User]]:
    return db.query(User).all()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> Optional[User]:
    salt, password = hash_user_password(user.password)
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=password,
        salt=salt,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def hash_user_password(password: str) -> str:
    return password


def check_user_login_credentials(email: str, password: str):
    pass
