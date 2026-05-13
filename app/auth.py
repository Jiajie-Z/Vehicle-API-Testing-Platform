from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.data_store import USERS

TOKEN_PREFIX = "vehicle-demo-token"

bearer_scheme = HTTPBearer()


def create_token(username: str) -> str:
    return f"{TOKEN_PREFIX}:{username}"


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict:
    token = credentials.credentials

    if not token.startswith(f"{TOKEN_PREFIX}:"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    username = token.split(":", 1)[1]
    user = USERS.get(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unknown user",
        )

    return user
