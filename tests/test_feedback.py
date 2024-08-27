from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_feedback():
    feedback = [
            {
                "type": "product",
                "score": 1,
                "description": "HORRIBLE",
                "date": "2024-08-28T14:00:00"
            },
            {
                "type": "service",
                "score": 1,
                "description": "Odio el producto",
                "date": "2024-08-28T14:05:00"
            }
    ]
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
    print('ANALYZE FEEDBACK: ',response.json()) 

    assert response.status_code == 200
    assert "insights" in response.json()
    assert len(response.json()["insights"]) > 0  # Verificar que hay algo en la respuesta

def test_analyze_all_feedbacks_together():
    feedbacks = [
        {
            "type": "product",
            "score": 5,
            "description": "Great product!",
            "date": "2024-08-26T14:00:00"
        },
        {
            "type": "service",
            "score": 1,
            "description": "Poor customer service.",
            "date": "2024-08-26T14:05:00"
        },
        {
            "type": "delivery",
            "score": 4,
            "description": "Fast delivery, but packaging was damaged.",
            "date": "2024-08-26T14:10:00"
        }
    ]

    response = client.post("/feedback/analyze_all_together/", json=feedbacks)

    print(response.status_code)
    print('ANALYZE ALL TOGETHER TEST: ',response.json())

    assert response.status_code == 200
    assert "insights" in response.json()
    assert len(response.json()["insights"]) > 0



