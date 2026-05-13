from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user
from app.data_store import ALERTS, VEHICLES, utc_now
from app.models import AlertCreate, AlertResponse

router = APIRouter()


@router.post("", response_model=AlertResponse, status_code=status.HTTP_201_CREATED)
def create_alert(
    payload: AlertCreate,
    current_user: dict = Depends(get_current_user),
) -> AlertResponse:
    vehicle = VEHICLES.get(payload.vehicle_id)

    if not vehicle or vehicle["owner"] != current_user["username"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found",
        )

    alert = AlertResponse(
        alert_id=f"ALT-{len(ALERTS) + 1:04d}",
        created_at=utc_now(),
        **payload.model_dump(),
    )

    ALERTS.append(alert.model_dump())

    return alert


@router.get("", response_model=list[AlertResponse])
def list_alerts(current_user: dict = Depends(get_current_user)) -> list[AlertResponse]:
    owned_vehicle_ids = {
        vehicle["vehicle_id"]
        for vehicle in VEHICLES.values()
        if vehicle["owner"] == current_user["username"]
    }

    return [
        AlertResponse(**alert)
        for alert in ALERTS
        if alert["vehicle_id"] in owned_vehicle_ids
    ]
