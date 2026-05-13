import pytest
from fastapi.testclient import TestClient

from app.main import app
from api_tests.clients.api_client import VehicleApiClient


@pytest.fixture()
def client() -> VehicleApiClient:
    return VehicleApiClient(session=TestClient(app))


@pytest.fixture()
def auth_client(client: VehicleApiClient) -> VehicleApiClient:
    client.login("test_driver", "Drive@123")
    return client
