from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_open_user_profile() -> None:
    response = client.get("/api/v1/users/1/profile")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "student_qadam"


def test_submit_game() -> None:
    payload = {
        "user_id": 1,
        "task_name": "FastAPI қабаттары",
        "correct_answers": 9,
        "total_questions": 10,
    }
    response = client.post("/api/v1/game/submit", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["score"] == 90
    assert data["rank_label"] == "Үздік (Алтын қадам)"


def test_invalid_score_returns_400() -> None:
    payload = {
        "user_id": 1,
        "task_name": "Қате тест",
        "correct_answers": 15,
        "total_questions": 10,
    }
    response = client.post("/api/v1/game/submit", json=payload)
    assert response.status_code == 400

