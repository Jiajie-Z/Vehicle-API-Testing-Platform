from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user
from app.data_store import TELEMETRY_EVENTS, VEHICLES, utc_now
from app.models import TelemetryCreate, TelemetryResponse

router = APIRouter()


@router.post("", response_model=TelemetryResponse, status_code=status.HTTP_202_ACCEPTED)
def create_telemetry(
    payload: TelemetryCreate,
    current_user: dict = Depends(get_current_user),
) -> TelemetryResponse:
    vehicle = VEHICLES.get(payload.vehicle_id)

    if not vehicle or vehicle["owner"] != current_user["username"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found",
        )

    event = TelemetryResponse(
        event_id=f"TEL-{len(TELEMETRY_EVENTS) + 1:04d}",
        vehicle_id=payload.vehicle_id,
        accepted=True,
        received_at=utc_now(),
    )

    TELEMETRY_EVENTS.append({**payload.model_dump(), **event.model_dump()})

    return event
