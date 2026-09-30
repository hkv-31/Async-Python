from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_sequential():
    response = client.get("/sequential")
    assert response.status_code == 200
    assert response.json()["mode"] == "sequential"
    assert len(response.json()["results"]) == 3

def test_concurrent():
    response = client.get("/concurrent")
    assert response.status_code == 200
    assert response.json()["mode"] == "concurrent"
    assert len(response.json()["results"]) == 3