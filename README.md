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

## References

- https://www.youtube.com/watch?v=K56nNuBEd0c&xstg=CAMSEBUJ_b-oH-PhF0yjBgaukzY%3D
- https://fastapi.tiangolo.com/async/
- https://testdriven.io/blog/python-concurrency-parallelism/
- https://medium.com/@oladayo_7133/asynchronous-programming-in-python-speeding-up-your-code-with-concurrency-df69be5f1807