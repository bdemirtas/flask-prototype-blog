import pytest

from kodpanik.core import create_app
from kodpanik.core import db as _db


@pytest.fixture(scope="session")
def app():
    app = create_app(config="kodpanik.core.config.test_settings")
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope="session")
def db(app):
    _db.app = app
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.fixture(scope="session")
def client(app):
    client = app.test_client()
    return client


@pytest.fixture(scope="function")
def session(db):
    conn = db.engine.connect()
    txn = conn.begin()
    options = dict(bind=conn, binds={})
    sess = db.create_scoped_session(options=options)
    sess.begin_nested()
    db.session = sess
    yield sess
    sess.remove()
    txn.rollback()
    conn.close()
