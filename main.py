import json
from fastapi import FastAPI, HTTPException, Request
from models.user import LoginRequest, CreateUserRequest
from auth.strategies.local_strategy import LocalStrategy
from auth.strategies.cloud_strategy import CloudStrategy
from middleware.auth_middleware import auth_middleware
from scripts.hash_password import hash_password
from fastapi.security import HTTPBearer
from fastapi import Depends


app = FastAPI()
#security = HTTPBearer()

@app.middleware("http")
async def middleware_handler(request, call_next):
    return await auth_middleware(request, call_next)

@app.get("/")
def home():
    return {"message": "API Running"}

#@app.get("/me", dependencies=[Depends(security)])
def me(request: Request):
    return {"user": request.state.user}

@app.get("/health")
def health():
    return {"status":"ok"}

#@app.post("/users/local", dependencies=[Depends(security)])
def create_local_user(request: Request, data: CreateUserRequest):
    current_logged_in_user = request.state.user
    if current_logged_in_user.auth_type == "cloud" and current_logged_in_user.is_superuser == True:
            with open("data/users.json", "r") as files:
                users = json.load(files)
                for user in users:
                    if user["username"] == data.username:
                        raise HTTPException(status_code=409, detail="resource already exists")
            hash_password_to_store = hash_password(data.password)
            new_user = { "id": len(users) + 1, "username": data.username, "hashed_password": hash_password_to_store, "is_active": True, "user_permissions": [], "is_superuser": False, "auth_type": "local"}
            users.append(new_user)
            with open("data/users.json", "w") as files:
                json.dump(users, files)
            return {"message": "registered"}
    raise HTTPException(status_code=403, detail="Forbidden")

@app.post("/auth/login")
def login(data: LoginRequest):
    if data.auth_type == "local":
        local_object = LocalStrategy()
        return local_object.authenticate(data)
    if data.auth_type == "cloud":
        cloud_object = CloudStrategy()
        return cloud_object.authenticate(data)
    else:
        raise HTTPException( status_code=400, detail="Invalid auth_type")