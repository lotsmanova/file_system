import pytest
from src.config import db, DB_USER, DB_PASS, DB_HOST, DB_NAME_TEST
from src.main import create_app


@pytest.fixture(scope="session")
def test_client():

    # fixture initial app and db
    app = create_app()
    # create test database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME_TEST}'
    with app.test_client() as client:
        with app.app_context():
            # create table
            db.create_all()
            yield client
            # remove session
            db.session.remove()
