import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api():
    """Общая сессия для всех тестов."""
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    session.base_url = BASE_URL
    yield session
    session.close()
