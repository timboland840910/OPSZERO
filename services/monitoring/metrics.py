from fastapi import FastAPI
import datetime
import psutil

app = FastAPI(
    title="AGP Monitoring Service",
    description="System monitoring and metrics for AGP Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "AGP Monitoring",
        "status": "running",
        "timestamp": datetime.datetime.utcnow()
    }

@app.get("/metrics")
def metrics():
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "timestamp": datetime.datetime.utcnow()
    }
