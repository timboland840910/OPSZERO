from fastapi import FastAPI
import datetime

app = FastAPI(
    title="AGP Intelligence Engine",
    description="Core intelligence service for AGP Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "AGP Intelligence Engine",
        "status": "running",
        "timestamp": datetime.datetime.utcnow()
    }

@app.get("/decision")
def decision(input_data: str):
    """
    Basic decision endpoint.
    Future versions will integrate AI logic.
    """

    if "scale" in input_data:
        action = "trigger autoscaling"
    elif "alert" in input_data:
        action = "notify monitoring system"
    else:
        action = "log event"

    return {
        "input": input_data,
        "decision": action
    }
