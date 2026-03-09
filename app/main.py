import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# [BARU] Import router dari endpoints.py
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Enterprise Data Extractor API",
    description="High-performance asynchronous data extraction with built-in telemetry.",
    version="1.0.0"
)

# Middleware: The Speed Tracker
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter() 
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f} seconds"
    return response

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "message": "Engine is running smoothly.",
        "accuracy_rate": "100%"
    }

# [BARU] Daftarkan rute API dengan prefix versi (v1)
app.include_router(api_router, prefix="/api/v1", tags=["Extraction"])