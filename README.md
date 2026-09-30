# Async/Concurrency API Demo

A small FastAPI project demonstrating asynchronous programming and concurrency in Python using `async`, `await`, `asyncio.sleep()`, and `asyncio.gather()`.

## Project Structure

```text
async-api-demo/
├── main.py
├── requirements.txt
├── tests/
│   └── test_main.py
├── .gitignore
└── README.md
```

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

Open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Root

```text
GET /
```

Checks that the API is running.

### Sequential

```text
GET /sequential
```

Runs the three tasks one after another.

Expected execution time is approximately:

```text
2 + 3 + 1 = 6 seconds
```

### Concurrent

```text
GET /concurrent
```

Runs the three tasks concurrently with `asyncio.gather()`.

Expected execution time is approximately:

```text
max(2, 3, 1) = 3 seconds
```

Actual timings can vary slightly because of system overhead.

## What to Compare

Call both endpoints from Swagger UI and compare the `time_seconds` values.

Example sequential response:

```json
{
  "mode": "sequential",
  "time_seconds": 6.01
}
```

Example concurrent response:

```json
{
  "mode": "concurrent",
  "time_seconds": 3.01
}
```

## Run Tests

```bash
pytest
```

## Concepts Demonstrated

- `async` functions
- `await`
- `asyncio.sleep()`
- `asyncio.gather()`
- FastAPI async endpoints
- Sequential execution
- Concurrent execution
- Execution-time comparison
- Basic API testing

## Important Concept

Asynchronous programming is particularly useful for I/O-bound work such as network requests, database operations, file operations, and API calls.
Concurrency is not the same as CPU parallelism. This project demonstrates concurrent handling of simulated I/O-bound tasks.

## Monitoring & Logging

The application includes a basic monitoring and logging system using Python's built-in logging module.

Logging Features
- Logs incoming API requests and HTTP methods.
- Logs response status codes and request execution time.
- Logs important application events and task execution.
- Logs errors and exceptions with traceback information.
- Uses different log levels such as INFO and ERROR.
- Includes a /health endpoint for basic application health monitoring.
- Logs are available in the terminal when running locally and through Docker logs when running in a container.

### Example Logs
2026-09-30 17:40:23,026 - INFO - Request: GET /health
2026-09-30 17:40:23,027 - INFO - Health check accessed
2026-09-30 17:40:23,028 - INFO - Response: GET /health - 200 - 0.00s

## Docker Logs

When running the application with Docker, logs can be viewed using:

`docker logs async-api-container`

This allows API activity, task execution, errors, and request performance to be monitored directly from the container logs.

## References

- https://www.youtube.com/watch?v=K56nNuBEd0c&xstg=CAMSEBUJ_b-oH-PhF0yjBgaukzY%3D
- https://fastapi.tiangolo.com/async/
- https://testdriven.io/blog/python-concurrency-parallelism/
- https://medium.com/@oladayo_7133/asynchronous-programming-in-python-speeding-up-your-code-with-concurrency-df69be5f1807
- https://medium.com/@mcgeejasond/devops-monitoring-and-logging-explained-939c3b5e17c4
