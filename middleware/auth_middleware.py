from fastapi.responses import JSONResponse
from auth.token_service import verify_token
from auth.strategies.cloud_strategy import cloud_session_store

async def auth_middleware(request, call_next):
    current_path = request.url.path
    if current_path in ["/", "/health", "/docs", "/openapi.json", "/auth/login"]:
        response = await call_next(request)
        return response
    authorization = request.headers.get("Authorization")
    if not authorization:
        return JSONResponse( status_code=401, content={"detail": "Token Missing"})
    split_token = authorization.split()
    if len(split_token) != 2: 
        return JSONResponse( status_code=401, content={"detail": "Invalid Authorization Header"})
    token = split_token[1]
    if token in cloud_session_store:
        request.state.user = cloud_session_store[token]["user"]
        response = await call_next(request)
        return response
    decoded_payload = verify_token(token)
    if decoded_payload["message"] == "token Expired":
        return JSONResponse( status_code=403, content={"detail": "Token Expired"})
    if decoded_payload["message"] == "Invalid token": 
        return JSONResponse( status_code=401, content={"detail": "Invalid token"})
    request.state.user = decoded_payload["data"]
    response = await call_next(request)
    return response