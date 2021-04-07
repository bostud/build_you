from fastapi import FastAPI
from build_you.api import company
from build_you.api import user

from build_you import models
from build_you.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(company.router)
app.include_router(user.router)
