from datetime import datetime, timezone


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

USERS = {
    "test_driver": {
        "username": "test_driver",
        "password": "Drive@123",
        "display_name": "Test Driver",
    }
}

VEHICLES = {
    "VH-1001": {
        "vehicle_id": "VH-1001",
        "vin": "LTEST00000001001",
        "model": "E-SUV Pro",
        "plate_no": "粤A12345",
        "owner": "test_driver",
        "online": True,
        "battery_level": 82,
        "odometer_km": 18642.7,
    },
    "VH-1002": {
        "vehicle_id": "VH-1002",
        "vin": "LTEST00000001002",
        "model": "E-Sedan Plus",
        "plate_no": "粤B54321",
        "owner": "test_driver",
        "online": False,
        "battery_level": 36,
        "odometer_km": 9430.2,
    },
}


TRIPS = {
    "VH-1001": [
        {
            "trip_id": "TRIP-9001",
            "start_time": "2026-05-01T08:30:00Z",
            "end_time": "2026-05-01T09:05:00Z",
            "distance_km": 18.4,
            "avg_speed_kmh": 31.5,
            "energy_used_kwh": 3.2,
        },
        {
            "trip_id": "TRIP-9002",
            "start_time": "2026-05-02T18:10:00Z",
            "end_time": "2026-05-02T18:44:00Z",
            "distance_km": 16.1,
            "avg_speed_kmh": 28.9,
            "energy_used_kwh": 2.9,
        },
    ],
    "VH-1002": [],
}

ALERTS: list[dict] = []
TELEMETRY_EVENTS: list[dict] = []
