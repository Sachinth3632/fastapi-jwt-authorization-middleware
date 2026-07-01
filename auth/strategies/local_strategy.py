import json
from fastapi import HTTPException
from auth.strategies.base import AuthStrategy
from auth.token_service import create_token
from models.user import LoginRequest, User
from scripts.hash_password import verify_password

class LocalStrategy(AuthStrategy):
    def authenticate(self, data: LoginRequest):
        with open("data/users.json", "r") as file:
            users = json.load(file)
        for user in users:
            if user["username"] == data.username:
                password_valid = verify_password( data.password, user["hashed_password"])
                if not password_valid:
                    raise HTTPException( status_code=401, detail="Invalid password")
                if not user["is_active"]:
                    raise HTTPException( status_code=403, detail="Inactive user")
                user_object = User( id=user["id"], username=user["username"], auth_type=user["auth_type"], is_active=user["is_active"], is_superuser=user["is_superuser"], user_permissions=user.get("user_permissions", []))
                token = create_token(user_object.model_dump())
                return { "access_token": token, "token_type": "Bearer", "user": user_object}
        raise HTTPException( status_code=401, detail="Invalid username")