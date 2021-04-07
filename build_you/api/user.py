from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from build_you.schemas import user as user_schemas
from build_you.database import get_db
from build_you.models import User

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={418: {'description': 'Test'}}
)


@router.get('/', response_model=List[user_schemas.User])
async def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post('/', response_model=user_schemas.User)
async def add_user(
    user: user_schemas.UserCreate,
    db: Session = Depends(get_db),
):
    if not db.query(User).filter(User.email == user.email).first():
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
    else:
        raise HTTPException(status_code=400, detail="Email already registered")
