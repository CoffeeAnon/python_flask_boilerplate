import os
import toml
from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from .routes import api as hello_world
from .database import db
from .config import config

migrate = Migrate()

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    if os.environ.get("FLASK_ENV") == "production":
        config_name = "production"
    else:
        config_name = "development"  # default to development
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Load metadata from pyproject.toml
    with open("pyproject.toml", "r") as f:
        metadata = toml.load(f)["tool"]["poetry"]

        api = Api(
            title=metadata["name"],
            version=metadata["version"],
            description=metadata.get("description", ""),
            # All API metadatas
        )

    with app.app_context():
        # Register namespaces
        api.init_app(app)
        api.add_namespace(hello_world, path="/hello_world")
        # app.register_blueprint(bp_hello_world)

    return app
