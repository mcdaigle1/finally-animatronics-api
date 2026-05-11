from fastapi import FastAPI, Response, Request
from datetime import datetime, UTC

import json

app = FastAPI(title="hello-api")

LOG_FILE = "/data/requests.jsonl"

@app.get("/")
def hello(request: Request) -> dict[str, str]:
    log_entry = {
        "timestamp": datetime.now(UTC).isoformat(),
        "client_host": request.client.host if request.client else None,
        "method": request.method,
        "headers": dict(request.headers),
        "url": str(request.url)
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    with open(LOG_FILE, "r") as f:
        log_contents = f.read()


    return {
        "message": "Hello, world",
        "requests": log_contents
    }

@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/readyz")
def readyz() -> dict[str, str]:
    return {"status": "ready"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)