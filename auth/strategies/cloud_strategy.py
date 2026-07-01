import os
import requests
from dotenv import load_dotenv
from auth.strategies.base import AuthStrategy
from models.user import LoginRequest, User
from fastapi import HTTPException

load_dotenv()
CLOUD_LOGIN_URL = os.getenv("CLOUD_LOGIN_URL")
cloud_session_store = {}
class CloudStrategy(AuthStrategy):
    def authenticate(self, data: LoginRequest):
        payload = { "user_name": data.username, "password": data.password}
        response = requests.post( CLOUD_LOGIN_URL, json=payload)
        response_data = response.json()
        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid Cloud Credentials")
        if "data" not in response_data:
            raise Exception("Invalid cloud response")
        cloud_data = response_data["data"]
        access_token = cloud_data.get("access_token")
        refresh_token = cloud_data.get("refresh_token")
        if not access_token:
            raise Exception("Access token missing")
        user = User(id=str(cloud_data.get("email")), username=cloud_data.get("email"), auth_type="cloud",is_active=True,is_superuser=cloud_data.get("is_superuser", False),user_permissions=cloud_data.get("user_permissions", []))
        cloud_session_store[access_token] = {"refresh_token": refresh_token,"user": user}
        return {"access_token": access_token,"refresh_token": refresh_token,"token_type": "Bearer","user": user}