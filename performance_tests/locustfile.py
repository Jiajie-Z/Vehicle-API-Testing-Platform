from random import choice, uniform

from locust import HttpUser, between, task


class VehicleApiUser(HttpUser):
    wait_time = between(0.5, 2.0)

    def on_start(self) -> None:
        response = self.client.post(
            "/api/auth/login",
            json={
                "username": "test_driver",
                "password": "Drive@123",
            },
        )
        response.raise_for_status()

        token = response.json()["token"]
        self.headers = {
            "Authorization": f"Bearer {token}",
        }
        self.vehicle_ids = ["VH-1001", "VH-1002"]

    @task(5)
    def query_vehicle_status(self) -> None:
        vehicle_id = choice(self.vehicle_ids)
        self.client.get(
            f"/api/vehicles/{vehicle_id}/status",
            headers=self.headers,
        )

    @task(3)
    def list_vehicle_trips(self) -> None:
        self.client.get(
            "/api/vehicles/VH-1001/trips",
            headers=self.headers,
        )

    @task(2)
    def upload_telemetry(self) -> None:
        self.client.post(
            "/api/telemetry",
            headers=self.headers,
            json={
                "vehicle_id": "VH-1001",
                "speed_kmh": round(uniform(0, 120), 1),
                "battery_level": choice(range(20, 96)),
                "latitude": 23.1291,
                "longitude": 113.2644,
            },
        )

    @task(1)
    def create_alert(self) -> None:
        self.client.post(
            "/api/alerts",
            headers=self.headers,
            json={
                "vehicle_id": "VH-1001",
                "alert_type": "tire_pressure",
                "severity": "medium",
                "message": "Tire pressure fluctuation detected",
            },
        )
