from fastapi import FastAPI
from build_you.middleware.auth import AuthMiddleware


app = FastAPI()
app.add_middleware(AuthMiddleware)


@app.get('/')
async def company(
    data: None,
):
    return {'status': 200}


@app.post('/')
async def create_company(
    data: None,
):
    return {'status': 200}
