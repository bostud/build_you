from fastapi import FastAPI
from build_you.api import company
from build_you.api import user
from build_you.api import auth
from build_you.api import main

from fastapi.middleware.cors import CORSMiddleware

from build_you import models
from build_you.database import engine

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/company', company.app, name='company')
app.mount('/user', user.app, name='user')
app.mount('/auth', auth.app, name='auth')
app.mount('/main', main.app, name='main')
