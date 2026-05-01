from fastapi import FastAPI

app = FastAPI(title="hello-api")

@app.get("/")

def hello() -> dict[str, str]:
    return {"message": "Hello, world"}

@app.get("/healthz")

def healthz() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/readyz")

def readyz() -> dict[str, str]:
    return {"status": "ready"}