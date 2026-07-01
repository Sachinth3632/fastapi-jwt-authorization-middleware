from datetime import datetime, timedelta, timezone
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
import os
from dotenv import load_dotenv

load_dotenv()
key_variable = os.getenv("JWT_SECRET")
algorithm_variable = os.getenv("JWT_ALGORITHM")
expiry_minutes = int(os.getenv("JWT_EXPIRY_MINUTES"))

def create_token(user_info):
    current_time = datetime.now(timezone.utc)
    additional_time = timedelta(minutes=expiry_minutes)
    expiry_time = current_time + additional_time
    payload = user_info.copy()
    payload["sub"] = user_info["id"]
    payload["exp"] = expiry_time
    token = jwt.encode(payload, key_variable, algorithm= algorithm_variable)
    return token

def verify_token(token):
    try:
        decoded_payload = jwt.decode(token, key_variable, algorithms=[algorithm_variable])
        return { "message": "Valid token", "data": decoded_payload}
    except ExpiredSignatureError:
        print("TOKEN EXPIRED")
        return {"message": "token Expired"}
    except JWTError as error:
        print("JWT ERROR =", error)
        return {"message": "Invalid token"}