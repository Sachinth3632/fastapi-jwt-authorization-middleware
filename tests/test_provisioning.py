import json
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_create_local_user():
    login_data = {
    "auth_type": "cloud",
    "username": "devteam@dev-livis.ai",
    "password": "123@Devs"
    }
    login_response = client.post("/auth/login", json=login_data)
    print(login_response.json())
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    user_data = {"username": "newuser", "password": "1234"}
    response = client.post(
        "/users/local",
        json=user_data,
        headers=headers
    )
    print(response.json())
    assert response.status_code == 403
    with open("data/users.json", "r") as files:
        users = json.load(files)
    found = False
    for user in users:
        if user["username"] == "newuser":
            found = True
    assert found == False