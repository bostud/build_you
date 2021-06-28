from fastapi import Response, Request
from fastapi.responses import JSONResponse
from starlette.datastructures import Headers
from starlette.middleware.base import BaseHTTPMiddleware
from build_you.bl.auth import is_valid_api_token

AUTH_TOKEN_KEY_NAME = 'X-AUTH-TOKEN'
AUTH_TOKEN_DELIMITER = '-'


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        headers = request.headers
        res = await is_auth_token_valid(headers)
        if res:
            return await call_next(request)
        else:
            return JSONResponse(
                {'error': 'Invalid authorization'},
                status_code=403,
            )


async def is_auth_token_valid(headers: Headers) -> bool:
    x_auth_token = await get_x_auth_token(headers)
    if x_auth_token and await is_valid_format_auth_token(x_auth_token):
        return await is_valid_api_token(
            await get_user_id(x_auth_token),
            await get_auth_token(x_auth_token)
        )
    return False


async def get_x_auth_token(headers: Headers) -> str:
    return headers.get(AUTH_TOKEN_KEY_NAME.lower(), '')


async def get_auth_token(x_auth_token: str) -> str:
    return x_auth_token.split(AUTH_TOKEN_DELIMITER)[-1]


async def get_user_id(x_auth_token: str) -> int:
    return int(x_auth_token.split(AUTH_TOKEN_DELIMITER)[0])


async def is_valid_format_auth_token(x_auth_token: str) -> bool:
    return len(str(x_auth_token).split(AUTH_TOKEN_DELIMITER)) > 1


def async_auth_middleware(call_next):
    async def _wrapper_(request: Request, *args, **kwargs):
        headers = request.headers
        res = await is_auth_token_valid(headers)
        if res:
            return await call_next(request)
        else:
            return JSONResponse(
                {'error': 'Invalid authorization'},
                status_code=403,
            )
    return _wrapper_
