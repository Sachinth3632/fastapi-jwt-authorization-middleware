from pydantic import BaseModel
from typing import Literal

class LoginRequest(BaseModel):
    auth_type: str
    username: str
    password: str

class CreateUserRequest(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: str
    username: str
    auth_type: Literal["local", "cloud"]
    is_active: bool
    is_superuser: bool
    user_permissions: list[int] = []