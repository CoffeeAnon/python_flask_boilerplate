import os


class Config:
    """Base config."""

    FLASK_ENV = os.environ.get("FLASK_ENV", "development")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get(
            "PROD_DATABASE_URL", "postgresql://username:password@localhost/mydatabase"
        )
        + "?sslmode=require"
    )


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    TESTING = True
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    DB_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "data", "app.db"
    )
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"


class TestingConfig(Config):
    """Testing configuration."""

    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}
