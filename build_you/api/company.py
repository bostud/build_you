from fastapi import APIRouter


router = APIRouter(
    prefix='/company',
    tags=['company'],
    responses={418: {'description': 'Test'}}
)


@router.get('/')
async def company():
    return {'status': 200}
