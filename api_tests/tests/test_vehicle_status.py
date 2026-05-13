import json
from pathlib import Path

from jsonschema import validate


SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"


def _load_schema(name: str) -> dict:
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


def test_list_vehicles_returns_owned_vehicle_summaries(auth_client):
    response = auth_client.get("/api/vehicles")

    assert response.status_code == 200

    vehicles = response.json()
    assert len(vehicles) == 2

    for vehicle in vehicles:
        validate(vehicle, _load_schema("vehicle_schema.json"))


def test_get_online_vehicle_status(auth_client):
    response = auth_client.get("/api/vehicles/VH-1001/status")

    assert response.status_code == 200

    body = response.json()
    validate(body, _load_schema("status_schema.json"))

    assert body["vehicle_id"] == "VH-1001"
    assert body["online"] is True
    assert body["location"] is not None


def test_get_offline_vehicle_status_has_no_location(auth_client):
    response = auth_client.get("/api/vehicles/VH-1002/status")

    assert response.status_code == 200

    body = response.json()
    validate(body, _load_schema("status_schema.json"))

    assert body["online"] is False
    assert body["locked"] is True
    assert body["location"] is None


def test_unknown_vehicle_returns_404(auth_client):
    response = auth_client.get("/api/vehicles/VH-404/status")

    assert response.status_code == 404
    assert response.json()["detail"] == "Vehicle not found"


def test_list_vehicle_trips(auth_client):
    response = auth_client.get("/api/vehicles/VH-1001/trips")

    assert response.status_code == 200

    trips = response.json()
    assert len(trips) >= 1

    for trip in trips:
        validate(trip, _load_schema("trip_schema.json"))
