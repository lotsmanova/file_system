import logging

from flask import Flask
from flask_jwt_extended import JWTManager
from src.config import SQLALCHEMY_DATABASE_URI, SECRET_AUTH, db
from src.route.auth import route_auth
from src.route.command import route_com


def create_app():

    app = Flask(__name__)

    # Конфигурация приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['JWT_SECRET_KEY'] = SECRET_AUTH

    # Инициализация базы данных
    db.init_app(app)

    # Инициализация JWT
    jwt = JWTManager(app)

    # Настройка логгера
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                        handlers=[
                            logging.FileHandler('app.log'),
                            logging.StreamHandler()
                        ])

    # Регистрация маршрутов
    app.register_blueprint(route_auth)
    app.register_blueprint(route_com)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
