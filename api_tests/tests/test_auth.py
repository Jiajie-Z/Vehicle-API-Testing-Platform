def test_login_success_returns_bearer_token(client):
    response = client.login("test_driver", "Drive@123")

    assert response.status_code == 200

    body = response.json()
    assert body["token_type"] == "Bearer"
    assert body["token"].startswith("vehicle-demo-token:")
    assert body["display_name"] == "Test Driver"


def test_login_rejects_wrong_password(client):
    response = client.login("test_driver", "wrong-password")

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


def test_protected_api_rejects_missing_token(client):
    response = client.get("/api/vehicles")

    assert response.status_code in [401, 403]
