from fastapi import Header, HTTPException, status

from app.data_store import USERS

TOKEN_PREFIX = "vehicle-demo-token"


def create_token(username: str) -> str:
    return f"{TOKEN_PREFIX}:{username}"


def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token",
        )

    token = authorization.removeprefix("Bearer ").strip()

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
