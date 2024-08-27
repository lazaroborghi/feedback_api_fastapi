from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_feedback():
    feedback = {
        "feedbacks": [
            {
                "type": "product",
                "score": 5,
                "description": "Great product!",
                "date": "2024-08-26T14:00:00"
            },
            {
                "type": "service",
                "score": 4,
                "description": "Good service.",
                "date": "2024-08-26T14:05:00"
            }
        ]
    }
    response = client.post("/feedback/", json=feedback)
    assert response.status_code == 200
    assert "ids" in response.json()
