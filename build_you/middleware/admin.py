from fastapi import Response, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from build_you.middleware.auth import is_auth_token_valid


class AdminMiddleware(BaseHTTPMiddleware):
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

