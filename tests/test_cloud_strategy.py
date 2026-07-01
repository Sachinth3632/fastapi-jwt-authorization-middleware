from auth.strategies.cloud_strategy import CloudStrategy
from models.user import LoginRequest

def test_cloud_strategy():
    data = LoginRequest(
        auth_type="cloud",
        username="devteam@dev-livis.ai",
        password="123@Devs"
    )
    cloud_object = CloudStrategy()
    result = cloud_object.authenticate(data)
    print(result)
    assert "access_token" in result