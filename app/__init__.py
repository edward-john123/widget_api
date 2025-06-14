import logging
from typing import Dict

from flask import Flask
from flask_smorest import Api

from .extensions import db, migrate
from .routes import blp as WidgetBlueprint
from .settings.config import Config

logging.basicConfig(
    level=logging.DEBUG if Config.FLASK_DEBUG else logging.INFO,
    format="%(asctime)s - %(message)s - %(levelname)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(Config.LOG_FILE),
    ],  # Logs to stdout
)


def create_app(config: Dict | None = None):
    app = Flask(__name__)

    if Config.FLASK_RUN_MODE != "TESTING":
        app.config.from_mapping(
            API_TITLE=Config.API_TITLE,
            API_VERSION=Config.API_VERSION,
            OPENAPI_VERSION=Config.OPENAPI_VERSION,
            OPENAPI_URL_PREFIX=Config.OPENAPI_URL_PREFIX,
            OPENAPI_SWAGGER_UI_PATH=Config.OPENAPI_SWAGGER_UI_PATH,
            OPENAPI_SWAGGER_UI_URL=Config.OPENAPI_SWAGGER_UI_URL,
            SQLALCHEMY_DATABASE_URI=Config.SQLALCHEMY_DATABASE_URI,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(config)

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)

    with app.app_context():
        db.create_all()

    # add blueprint for routes
    #
    api.register_blueprint(WidgetBlueprint)

    return app
