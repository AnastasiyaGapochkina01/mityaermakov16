from fastapi import FastAPI
from pydantic import BaseModel
import os
import socket
from datetime import datetime, timezone

app = FastAPI(title="portfolio-devops-app", version="1.0.0")

class EchoIn(BaseModel):
    message: str

@app.get("/")
def root():
    return {
        "service": "portfolio-devops-app",
        "status": "ok",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "dev"),
        "version": os.getenv("APP_VERSION", "local")
    }

@app.get("/healthz")
def healthz():
    return {"status": "healthy", "time": datetime.now(timezone.utc).isoformat()}

@app.get("/api/info")
def info():
    return {
        "python": os.sys.version.split()[0],
        "hostname": socket.gethostname(),
        "app_env": os.getenv("APP_ENV", "dev"),
        "app_version": os.getenv("APP_VERSION", "local")
    }

@app.post("/api/echo")
def echo(payload: EchoIn):
    return {
        "echo": payload.message,
        "length": len(payload.message),
        "processed_at": datetime.now(timezone.utc).isoformat()
    }
