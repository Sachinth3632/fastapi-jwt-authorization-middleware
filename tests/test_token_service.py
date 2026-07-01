from auth.token_service import create_token, verify_token

def test_token_service():
    user_info = {
    "id": "1",
    "username": "testuser",
    "auth_type": "local"
    }
    create_token_result = create_token(user_info)
    verify_token_result = verify_token(create_token_result)
    print("token", verify_token_result)

    assert verify_token_result["data"]["username"] == "testuser"