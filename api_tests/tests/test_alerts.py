import json
from pathlib import Path

from jsonschema import validate


SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"


def _load_schema(name: str) -> dict:
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


def test_create_alert_success(auth_client):
    response = auth_client.post(
        "/api/alerts",
        json={
            "vehicle_id": "VH-1001",
            "alert_type": "battery_low",
            "severity": "medium",
            "message": "Battery level below configured threshold",
        },
    )

    assert response.status_code == 201

    body = response.json()
    validate(body, _load_schema("alert_schema.json"))

    assert body["vehicle_id"] == "VH-1001"
    assert body["alert_id"].startswith("ALT-")


def test_create_alert_rejects_invalid_alert_type(auth_client):
    response = auth_client.post(
        "/api/alerts",
        json={
            "vehicle_id": "VH-1001",
            "alert_type": "unknown_alert",
            "severity": "medium",
            "message": "Invalid alert type should fail",
        },
    )

    assert response.status_code == 422


def test_create_alert_rejects_unknown_vehicle(auth_client):
    response = auth_client.post(
        "/api/alerts",
        json={
            "vehicle_id": "VH-404",
            "alert_type": "device_offline",
            "severity": "high",
            "message": "Vehicle should not exist",
        },
    )

    assert response.status_code == 404
