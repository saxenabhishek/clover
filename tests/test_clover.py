from fastapi.testclient import TestClient
from starlette import responses
from clover import app

client = TestClient(app)


def test_alive():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == "Backend API is up"


# def test_create_user():
#     response = client.post("/api/users/make_user", json={"name": "TestClient", "passw": "SuperSecret"})
#     print(response.json())
#     assert response.status_code == 201
#     assert response.json()["inserted_id"]


def test_create_duplicate_user():
    response = client.post("/api/users/make_user", json={"name": "TestClient", "passw": "SuperSecret"})
    assert response.status_code == 400
    assert response.json() == {"detail": "User Aleady exists"}
