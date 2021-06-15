from clover.mongo.driver import turnDBforTesting

from fastapi.testclient import TestClient
from starlette import responses
from clover import app

client = TestClient(app)
turnDBforTesting()


def test_alive():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == "Backend API is up"


def test_create_user():
    with TestClient(app) as with_client:
        response = with_client.post("/api/users/make_user", json={"name": "TestClient", "passw": "SuperSecret"})
        print(response.json())
        assert response.status_code == 201
        assert response.json()["inserted_id"]


def test_create_duplicate_user():
    with TestClient(app) as with_client:
        response = with_client.post("/api/users/make_user", json={"name": "TestClient", "passw": "SuperSecret"})
        assert response.status_code == 400
        assert response.json() == {"detail": "User Aleady exists"}


def test_delete_new_user():
    with TestClient(app) as with_client:
        response = with_client.delete("/api/users/del_user", json={"name": "TestClient", "passw": "SuperSecret"})
        assert response.status_code == 204


def test_delete_a_random_user():
    with TestClient(app) as with_client:
        response = with_client.delete("/api/users/del_user", json={"name": "TestClient1234", "passw": "NotSuperSecret"})
        assert response.status_code == 400
        assert response.json() == {"detail": "User doesn't exist"}
