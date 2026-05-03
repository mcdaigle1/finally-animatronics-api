from fastapi import FastAPI, Response

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

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)