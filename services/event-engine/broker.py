from fastapi import FastAPI
import asyncio
from nats.aio.client import Client as NATS

app = FastAPI(
    title="AGP Event Engine",
    version="1.0.0"
)

nc = NATS()

@app.on_event("startup")
async def connect_nats():
    await nc.connect("nats://nats:4222")

@app.get("/")
def root():
    return {"service": "AGP Event Engine", "status": "running"}

@app.post("/event")
async def publish_event(event_type: str, payload: str):
    message = f"{event_type}:{payload}"
    await nc.publish("agp.events", message.encode())

    return {
        "status": "event published",
        "event": message
    }
