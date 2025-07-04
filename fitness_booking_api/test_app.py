from fastapi.testclient import TestClient # type: ignore
from main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_book_class():
    payload = {
        "class_id": 1,
        "client_name": "Satyam Pal",
        "client_email": "12345satyampal@gmail.com"
    }
    response = client.post("/book", json=payload)
    assert response.status_code == 200
    assert response.json()["client_email"] == "12345satyampal@gmail.com"

def test_get_bookings():
    response = client.get("/bookings?email=12345satyampal@gmail.com")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
