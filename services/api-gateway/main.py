from fastapi import FastAPI
import requests

app = FastAPI(
    title="AGP API Gateway",
    description="Central entry point for AGP Platform services",
    version="1.0.0"
)

INTELLIGENCE_ENGINE_URL = "http://localhost:8001"
EVENT_ENGINE_URL = "http://localhost:8002"


@app.get("/")
def root():
    return {
        "service": "AGP API Gateway",
        "status": "running"
    }


@app.get("/intelligence/{input_data}")
def intelligence_route(input_data: str):
    response = requests.get(
        f"{INTELLIGENCE_ENGINE_URL}/decision",
        params={"input_data": input_data}
    )
    return response.json()


@app.post("/event")
def publish_event(event_type: str, payload: str):
    response = requests.post(
        f"{EVENT_ENGINE_URL}/event",
        params={"event_type": event_type, "payload": payload}
    )
    return response.json()
