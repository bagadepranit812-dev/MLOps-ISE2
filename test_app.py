from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_prediction():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={"marks": 85}
    )

    assert response.status_code == 200
    assert response.json["prediction"] == "Distinction"


def test_invalid_marks():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={"marks": 120}
    )

    assert response.status_code == 400