import json
from auth.strategies.local_strategy import LocalStrategy
from models.user import LoginRequest
from scripts.hash_password import hash_password

def test_local_strategy():
    hashed_password = hash_password("1234")
    users = [
        {
            "id": "1",
            "username": "sachin",
            "hashed_password": hashed_password,
            "is_active": True,
            "is_superuser": False,
            "auth_type": "local"
        }
    ]
    with open("data/users.json", "w") as files:
        json.dump(users, files)
    data = LoginRequest(
        auth_type="local",
        username="sachin",
        password="1234"
    )
    local_object = LocalStrategy()
    result = local_object.authenticate(data)
    print(result)
    assert "access_token" in result