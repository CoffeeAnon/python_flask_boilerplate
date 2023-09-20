import os
from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .routes import api as hello_world

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_pyfile("config.py")
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "app.db"
    )
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(
        title="Hello World API",
        version="0.1",
        description="This is a hello world API",
        # All API metadatas
    )

    with app.app_context():
        # Register blueprints
        api.init_app(app)
        api.add_namespace(hello_world, path="/hello_world")
        # app.register_blueprint(bp_hello_world)

    return app
