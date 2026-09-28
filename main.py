import asyncio
import time
from fastapi import FastAPI

app = FastAPI(title="Async API Demo")

async def simulated_task(name: str, delay: int):
    await asyncio.sleep(delay)
    return {"task": name, "delay": delay, "status": "completed"}

@app.get("/")
async def root():
    return {"message": "Async API is running"}

@app.get("/sequential")
async def sequential():
    start = time.perf_counter()
    results = []
    results.append(await simulated_task("Task 1", 2))
    results.append(await simulated_task("Task 2", 3))
    results.append(await simulated_task("Task 3", 1))
    elapsed = time.perf_counter() - start
    return {"mode": "sequential", "results": results, "time_seconds": round(elapsed, 2)}

@app.get("/concurrent")
async def concurrent():
    start = time.perf_counter()
    results = await asyncio.gather(
        simulated_task("Task 1", 2),
        simulated_task("Task 2", 3),
        simulated_task("Task 3", 1)
    )
    elapsed = time.perf_counter() - start
    return {"mode": "concurrent", "results": results, "time_seconds": round(elapsed, 2)}
