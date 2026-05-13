from fastapi import APIRouter, HTTPException, status

from app.auth import create_token
from app.data_store import USERS
from app.models import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest) -> LoginResponse:
    user = USERS.get(payload.username)

    if not user or user["password"] != payload.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return LoginResponse(
        token=create_token(payload.username),
        display_name=user["display_name"],
    )
