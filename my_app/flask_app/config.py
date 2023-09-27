import os


class Config:
    """Base config."""

    FLASK_ENV = os.environ.get("FLASK_ENV", "development")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://username:password@localhost/mydatabase"
    )


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")


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
