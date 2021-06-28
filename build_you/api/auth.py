from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from build_you.database import get_db
from build_you.schemas import user as user_schemas
from build_you.schemas import auth as auth_schemas
from build_you.bl import user as user_bl
from build_you.bl import auth as auth_bl

app = FastAPI()


@app.post('/register', response_model=user_schemas.User)
async def register(
    user: user_schemas.UserCreate,
    db: Session = Depends(get_db),
):
    if not user_bl.get_user_by_email(db, user.email):
        return user_bl.create_user(db, user)
    else:
        raise HTTPException(status_code=400, detail="Email already registered")


@app.post('/login', response_model=auth_schemas.AuthSuccess)
async def login(
    data: auth_schemas.AuthLogin,
    db: Session = Depends(get_db),
):
    if user := user_bl.get_user_by_email(db, data.email):
        if user_bl.check_user_login_credentials(data, user):
            model_user = user_bl.create_api_token(db, user)
            return {
                "api_token": model_user.api_token,
                "expire": model_user.expire_datetime,
            }
    raise HTTPException(status_code=403, detail='Email or password is wrong')


@app.post('/logout')
async def logout(
    data: auth_schemas.AuthLogout,
):
    await auth_bl.logout_user(data.api_token)
    return JSONResponse({'status': 'OK'})
