from fastapi import FastAPI

app = FastAPI(
    title="Vehicle Connectivity API",
    version="1.0.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
