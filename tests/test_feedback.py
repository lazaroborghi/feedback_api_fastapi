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


def test_analyze_feedback_real():
    # Feedback de ejemplo para analizar
    feedback = {
        "type": "product",
        "score": 5,
        "description": "Great product!",
        "date": "2024-08-26T14:00:00"
    }
    
    # Hacer la solicitud real al endpoint de análisis de feedback
    response = client.post("/feedback/analyze/", json=feedback)
    
    print(response.status_code)  # Imprime el código de estado
    print(response.json()) 

    assert response.status_code == 200
    assert "insights" in response.json()
    assert len(response.json()["insights"]) > 0  # Verificar que hay algo en la respuesta