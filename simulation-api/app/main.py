from fastapi import FastAPI

app = FastAPI(title="RaceSim Simulation API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"service": "simulation-api", "status": "ok"}
