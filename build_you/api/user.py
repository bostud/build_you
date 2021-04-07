from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from build_you.schemas import user as user_schemas
from build_you.database import get_db
from build_you.bl import user as user_bl

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={418: {'description': 'Test'}}
)


@router.get('/', response_model=List[user_schemas.User])
async def read_users(db: Session = Depends(get_db)):
    return user_bl.get_users(db)


@router.post('/', response_model=user_schemas.User)
async def add_user(
    user: user_schemas.UserCreate,
    db: Session = Depends(get_db),
):
    if not user_bl.get_user_by_email(db, user.email):
        user_bl.create_user(db, user)
    else:
        raise HTTPException(status_code=400, detail="Email already registered")
