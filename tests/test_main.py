from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_concurrent():
    response = client.get("/concurrent")
    assert response.status_code == 200
    assert response.json()["mode"] == "concurrent"
    assert len(response.json()["results"]) == 3
