from fastapi import FastAPI
from app.routers import users
from fastapi.testclient import TestClient
import pytest  # noqa: F401


class TestUsers:
    @pytest.fixture(scope="module", autouse=True)
    def add_router_to_app(self, app: FastAPI) -> FastAPI:
        app.include_router(users.router)
        return app

    def test_read_users(self, app: FastAPI, client: TestClient):
        response = client.get("/users/")
        assert response.status_code == 200
        assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]

    def test_read_user_me(self, app: FastAPI, client: TestClient):
        response = client.get("/users/me")
        assert response.status_code == 200
        assert response.json() == {"username": "fakecurrentuser"}

    def test_read_user(self, faker, app: FastAPI, client: TestClient):
        random_username = faker.user_name()
        response = client.get(f"/users/{random_username}")
        assert response.status_code == 200
        assert response.json() == {"username": random_username}
