from starlette.middleware.base import BaseHTTPMiddleware , RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

class AuthorizeRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.url.path in ("/docs"):
            return await call_next(request)