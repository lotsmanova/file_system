import pytest
from src.config import db
from src.main import create_app


@pytest.fixture(scope="session")
def test_client():

    # fixture initial app and db
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            # Создаем таблицы
            db.create_all()
            yield client
            # Закрываем сессию
            db.session.remove()
            db.drop_all()
