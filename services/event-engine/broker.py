from fastapi import FastAPI
from typing import List
import datetime

app = FastAPI(
    title="AGP Event Engine",
    description="Event processing and communication service",
    version="1.0.0"
)

event_store: List[dict] = []


@app.get("/")
def root():
    return {
        "service": "AGP Event Engine",
        "status": "running",
        "timestamp": datetime.datetime.utcnow()
    }


@app.post("/event")
def publish_event(event_type: str, payload: str):
    event = {
        "type": event_type,
        "payload": payload,
        "timestamp": datetime.datetime.utcnow()
    }

    event_store.append(event)

    return {
        "message": "event published",
        "event": event
    }


@app.get("/events")
def get_events():
    return {
        "events": event_store
    }
