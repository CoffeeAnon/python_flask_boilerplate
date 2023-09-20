import pytest
from my_app.flask_app import create_app
from flask import Flask


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app: Flask):
    return app.test_client()
