import os
import tempfile

import pytest

from app import create_app
from app.extensions import db as _db
from tests.factories import WidgetFactory


@pytest.fixture(scope="module")
def app():
    db_fd, db_path = tempfile.mkstemp()
    config = {
        "API_TITLE": "Test",
        "API_VERSION": "v1.0",
        "OPENAPI_VERSION": "3.0.2",
        "OPENAPI_URL_PREFIX": "/",
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "TESTING": True,
    }
    app = create_app(config=config)
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def db(app):
    with app.app_context():
        yield _db


@pytest.fixture(scope="function")
def init_db(app, db):
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()


@pytest.fixture(autouse=True)
def set_factory_session(db):
    WidgetFactory._meta.sqlalchemy_session = db.session
