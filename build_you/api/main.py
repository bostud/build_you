from fastapi import FastAPI

app = FastAPI()


@app.post('/')
async def main():
    return {'status': 'OK'}
