import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "OK"

def test_message():
    client = app.test_client()
    response = client.get("/api/message")
    assert response.status_code == 200
    assert "message" in response.json
