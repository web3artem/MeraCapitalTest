import pytest
from fastapi.testclient import TestClient
from src.main import app



@pytest.fixture(scope="function")
def client():
    client = TestClient(app=app)
    yield client