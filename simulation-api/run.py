import os
from pathlib import Path

import uvicorn
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    port = int(os.getenv("SIMULATION_API_PORT", "8000"))
    if not 1 <= port <= 65535:
        raise ValueError("SIMULATION_API_PORT must be between 1 and 65535.")
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)
