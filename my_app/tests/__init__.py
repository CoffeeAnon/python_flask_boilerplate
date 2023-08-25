from flask import Flask
import pytest
from my_app.flask_app import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def hello_world_bp(app):
    from my_app.flask_app.routes import hello_world_bp

    app.register_blueprint(hello_world_bp)
