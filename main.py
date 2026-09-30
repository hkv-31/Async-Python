import asyncio
import time
from fastapi import FastAPI, Request
from logger import logger

app = FastAPI(title="Async API Demo")

#Log requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    logger.info(f"Request: {request.method} {request.url.path}")
    try:
        response = await call_next(request)
        elapsed = time.perf_counter() - start
        logger.info(
            f"Response: {request.method} {request.url.path} "
            f"- {response.status_code} - {elapsed:.2f}s"
        )
        return response
    except Exception:
        elapsed = time.perf_counter() - start
        logger.exception(
            f"Request failed: {request.method} {request.url.path} "
            f"- {elapsed:.2f}s"
        )
        raise

#Simulated task
async def simulated_task(name: str, delay: int):
    logger.info(f"Starting {name} with {delay}s delay")
    await asyncio.sleep(delay)
    logger.info(f"Completed {name}")
    return {"task": name, "delay": delay, "status": "completed"}

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Async API is running"}

@app.get("/health")
async def health():
    logger.info("Health check accessed")
    return {"status": "healthy"}

@app.get("/sequential")
async def sequential():
    logger.info("Sequential execution started")
    start = time.perf_counter()
    results = []
    results.append(await simulated_task("Task 1", 2))
    results.append(await simulated_task("Task 2", 3))
    results.append(await simulated_task("Task 3", 1))
    elapsed = time.perf_counter() - start
    logger.info(f"Sequential execution completed in {elapsed:.2f}s")
    return {
        "mode": "sequential",
        "results": results,
        "time_seconds": round(elapsed, 2)
    }

@app.get("/concurrent")
async def concurrent():
    logger.info("Concurrent execution started")
    start = time.perf_counter()
    results = await asyncio.gather(
        simulated_task("Task 1", 2),
        simulated_task("Task 2", 3),
        simulated_task("Task 3", 1)
    )
    elapsed = time.perf_counter() - start
    logger.info(f"Concurrent execution completed in {elapsed:.2f}s")
    return {
        "mode": "concurrent",
        "results": results,
        "time_seconds": round(elapsed, 2)
    }

'''To test errors: 
@app.get("/error")
async def error():
    logger.error("Test error triggered")
    raise Exception("Test exception")'''