def test_create_telemetry_success(auth_client):
    response = auth_client.post(
        "/api/telemetry",
        json={
            "vehicle_id": "VH-1001",
            "speed_kmh": 66.5,
            "battery_level": 81,
            "latitude": 23.1291,
            "longitude": 113.2644,
        },
    )

    assert response.status_code == 202

    body = response.json()
    assert body["accepted"] is True
    assert body["vehicle_id"] == "VH-1001"
    assert body["event_id"].startswith("TEL-")


def test_create_telemetry_rejects_invalid_battery_level(auth_client):
    response = auth_client.post(
        "/api/telemetry",
        json={
            "vehicle_id": "VH-1001",
            "speed_kmh": 66.5,
            "battery_level": 120,
            "latitude": 23.1291,
            "longitude": 113.2644,
        },
    )

    assert response.status_code == 422


def test_create_telemetry_rejects_invalid_location(auth_client):
    response = auth_client.post(
        "/api/telemetry",
        json={
            "vehicle_id": "VH-1001",
            "speed_kmh": 66.5,
            "battery_level": 81,
            "latitude": 123.0,
            "longitude": 113.2644,
        },
    )

    assert response.status_code == 422
