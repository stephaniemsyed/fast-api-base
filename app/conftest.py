from fastapi import FastAPI
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def app():
    """Create a FastAPI app for testing."""

    app = FastAPI()

    return app


@pytest.fixture(scope="function")
def client(app):
    """Create a test client that uses the override_get_db fixture to return a session."""

    with TestClient(app) as test_client:
        yield test_client
