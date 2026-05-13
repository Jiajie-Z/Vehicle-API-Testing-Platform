from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user
from app.data_store import TRIPS, VEHICLES, utc_now
from app.models import Trip, VehicleStatus, VehicleSummary

router = APIRouter()


def _get_owned_vehicle(vehicle_id: str, username: str) -> dict:
    vehicle = VEHICLES.get(vehicle_id)

    if not vehicle or vehicle["owner"] != username:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found",
        )

    return vehicle


@router.get("", response_model=list[VehicleSummary])
def list_vehicles(current_user: dict = Depends(get_current_user)) -> list[VehicleSummary]:
    return [
        VehicleSummary(**vehicle)
        for vehicle in VEHICLES.values()
        if vehicle["owner"] == current_user["username"]
    ]


@router.get("/{vehicle_id}/status", response_model=VehicleStatus)
def get_vehicle_status(
    vehicle_id: str,
    current_user: dict = Depends(get_current_user),
) -> VehicleStatus:
    vehicle = _get_owned_vehicle(vehicle_id, current_user["username"])

    return VehicleStatus(
        vehicle_id=vehicle["vehicle_id"],
        online=vehicle["online"],
        battery_level=vehicle["battery_level"],
        odometer_km=vehicle["odometer_km"],
        locked=not vehicle["online"],
        location={"latitude": 23.1291, "longitude": 113.2644}
        if vehicle["online"]
        else None,
        updated_at=utc_now(),
    )


@router.get("/{vehicle_id}/trips", response_model=list[Trip])
def list_vehicle_trips(
    vehicle_id: str,
    current_user: dict = Depends(get_current_user),
) -> list[Trip]:
    _get_owned_vehicle(vehicle_id, current_user["username"])

    return [Trip(**trip) for trip in TRIPS.get(vehicle_id, [])]
