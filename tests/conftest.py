import pytest

from risotto import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()
