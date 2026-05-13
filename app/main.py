from fastapi import FastAPI

from app.routes import auth

app = FastAPI(
    title="Vehicle Connectivity API",
    version="1.0.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
