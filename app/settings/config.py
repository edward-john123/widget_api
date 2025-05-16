import os

from dotenv import load_dotenv


load_dotenv()

# DB PATH SETTINGS
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
db_dir = os.path.join(basedir, "db")
os.makedirs(db_dir, exist_ok=True)
DATABASE_URL = f"sqlite:///{os.path.join(db_dir, 'widgets.db')}"

# LOG FILE PATH SETTINGS
log_dir = os.path.join(basedir, "logs")
os.makedirs(log_dir, exist_ok=True)
LOG_FILE = os.path.join(log_dir, "widget_api.log")


class Config:
    # API Spec
    API_TITLE = os.getenv("API_TITLE", "Widget REST API")
    API_VERSION = os.getenv("API_VERSION", "v1")
    OPENAPI_VERSION = os.getenv("OPENAPI_VERSION", "3.0.2")
    OPENAPI_URL_PREFIX = os.getenv("OPENAPI_URL_PREFIX", "/")
    OPENAPI_SWAGGER_UI_PATH = os.getenv("OPENAPI_SWAGGER_UI_PATH", "/swagger-ui")
    OPENAPI_SWAGGER_UI_URL = os.getenv(
        "OPENAPI_SWAGGER_UI_URL", "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # SQLALCHEMY SETTINGS
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", DATABASE_URL)
    SQLACHEMY_TRACK_MODIFICATIONS = os.getenv("SQLACHEMY_TRACK_MODIFICATIONS", False)

    # FLASK SETTINGS
    FLASK_RUN_MODE = os.getenv("FLASK_RUN_MODE", "TESTING")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", 1)

    # LOGGING
    LOG_FILE = os.getenv("LOG_FILE", LOG_FILE)
