import logging
from flask import Flask
from flask_jwt_extended import JWTManager
from src.config import SQLALCHEMY_DATABASE_URI, SECRET_AUTH, db
from src.route.auth import route_auth
from src.route.command import route_com

# Настройка логгера
logging.basicConfig(level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


def create_app():
    app = Flask(__name__)

    # Конфигурация приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['JWT_SECRET_KEY'] = SECRET_AUTH

    # Инициализация базы данных
    db.init_app(app)

    # Инициализация JWT
    jwt = JWTManager(app)
    app.register_blueprint(route_auth)
    # Регистрация маршрутов
    app.register_blueprint(route_com)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
