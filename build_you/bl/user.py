from typing import Optional, List
from build_you.models import User
from sqlalchemy.orm import Session
from build_you.schemas.user import UserCreate


def get_users(db: Session) -> List[Optional[User]]:
    return db.query(User).all()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> Optional[User]:
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
