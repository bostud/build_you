from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from build_you.database import get_db
from build_you.schemas import user as user_schemas
from build_you.schemas import auth as auth_schemas
from build_you.bl import user as user_bl


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/register', response_model=user_schemas.User)
def register(
    user: user_schemas.UserCreate,
    db: Session = Depends(get_db),
):
    if not user_bl.get_user_by_email(db, user.email):
        return user_bl.create_user(db, user)
    else:
        raise HTTPException(status_code=400, detail="Email already registered")


@router.post('/login', response_model=auth_schemas.AuthSuccess)
def login(
    data: auth_schemas.AuthLogin,
    db: Session = Depends(get_db),
):
    if user_bl.get_user_by_email(db, data.email):
        pass
    return
