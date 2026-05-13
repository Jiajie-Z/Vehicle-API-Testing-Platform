from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)


class LoginResponse(BaseModel):
    token: str
    token_type: str = "Bearer"
    display_name: str

class VehicleSummary(BaseModel):
    vehicle_id: str
    vin: str
    model: str
    plate_no: str
    online: bool


class VehicleStatus(BaseModel):
    vehicle_id: str
    online: bool
    battery_level: int = Field(ge=0, le=100)
    odometer_km: float = Field(ge=0)
    locked: bool
    location: dict[str, float] | None
    updated_at: str


class Trip(BaseModel):
    trip_id: str
    start_time: str
    end_time: str
    distance_km: float
    avg_speed_kmh: float
    energy_used_kwh: float
