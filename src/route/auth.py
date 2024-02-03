from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from src.models.user import Users
from src.schemas.user import User

route_auth = Blueprint('Auth', __name__)


@route_auth.route('/register', methods=['POST'])
def register():
    """Регистрация пользователя"""

    user = User(**request.json)

    hashed_password = generate_password_hash(user.password)

    # проверка существования пользователя в БД
    if Users.find_by_username(username=user.username):
        return jsonify({'message': 'User exist'})

    # регистрация нового пользователя
    user_db = Users(username=user.username, password=hashed_password)
    user_db.save_to_db()

    # генерация токена
    access_token = create_access_token(identity=user.username)
    return jsonify({'access_token': access_token})


@route_auth.route('/login', methods=['POST'])
def login():
    """Вход для получения/обновления токена доступа"""

    user = User(**request.json)

    # проверка существования пользователя в БД
    current_user = Users.find_by_username(user.username)

    if not current_user:
        return jsonify({"message": "User doesn't exist"})

    else:
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': access_token})
