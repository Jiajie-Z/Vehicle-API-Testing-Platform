from fastapi import FastAPI

from app.routes import auth, vehicles, telemetry, alerts

app = FastAPI(
    title="Vehicle Connectivity API",
    version="1.0.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(vehicles.router, prefix="/api/vehicles", tags=["vehicles"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["alerts"])
app.include_router(telemetry.router, prefix="/api/telemetry", tags=["telemetry"])
