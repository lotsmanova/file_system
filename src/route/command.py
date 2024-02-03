import subprocess
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.schemas.payload import FilePayload, DirPayload, ChmodPayload, ChownPayload, DeletePayload, ListPayload

route_com = Blueprint('Command', __name__)


@route_com.route('/')
@jwt_required()
def hello():
    """Приветствие пользователя"""

    return "Hello, I am very fast and efficient application!"


@route_com.route('/touch', methods=['POST'])
@jwt_required()
def create_file():
    """Создание файла"""

    # извлекаем данные из post-запроса
    payload = FilePayload(**request.json)
    path = f"{payload.path}/{payload.file_name}"

    try:
        # формируем команду bash
        bash_command = f'echo "{payload.text}" > {path}'
        subprocess.run(bash_command, shell=True, text=True, check=True)

        # возвращаем успешный ответ
        return jsonify({"message": "File created successfully"})

    except subprocess.CalledProcessError as e:
        # возвращаем сообщение об ошибке
        return jsonify({"error": str(e)})


@route_com.route('/mkdir', methods=['POST'])
@jwt_required()
def create_directory():
    """Создание директории"""

    # извлекаем данные из post-запроса
    payload = DirPayload(**request.json)
    path = f"{payload.path}/{payload.dir_name}"

    try:
        # формируем команду bash
        bash_command = f'mkdir {path}'
        subprocess.run(bash_command, shell=True, text=True, check=True)

        # возвращаем успешный ответ
        return jsonify({"message": "Directory created successfully"})

    except subprocess.CalledProcessError as e:
        # возвращаем сообщение об ошибке
        return jsonify({"error": str(e)})


@route_com.route('/chmod', methods=['POST'])
@jwt_required()
def chmod():
    """Изменение маски разрешений"""

    # извлекаем данные из post-запроса
    payload = ChmodPayload(**request.json)

    try:
        # формируем команду bash
        bash_command = f'chmod {payload.mask} {payload.object_name}'
        subprocess.run(bash_command, shell=True, text=True, check=True)

        # возвращаем успешный ответ
        return jsonify({"message": "Successfully changing the permission mask"})

    except subprocess.CalledProcessError as e:
        # возвращаем сообщение об ошибке
        return jsonify({"error": str(e)})


@route_com.route('/chown', methods=['POST'])
@jwt_required()
def chown():
    """Изменение владельца"""

    # извлекаем данные из post-запроса
    payload = ChownPayload(**request.json)

    try:
        # формируем команду bash
        bash_command = f'chown {payload.owner} {payload.object_name}'
        subprocess.run(bash_command, shell=True, text=True, check=True)

        # возвращаем успешный ответ
        return jsonify({"message": "Successfully changing the owner"})

    except subprocess.CalledProcessError as e:
        # возвращаем сообщение об ошибке
        return jsonify({"error": str(e)})


@route_com.route('/rm', methods=['DELETE'])
@jwt_required()
def delete():
    """Удаление файла или директории"""

    # извлекаем данные из post-запроса
    payload = DeletePayload(**request.json)

    try:
        # формируем команду bash
        bash_command = f'rm {payload.object_name}'
        subprocess.run(bash_command, shell=True, text=True, check=True)

        # возвращаем успешный ответ
        return jsonify({"message": "Successfully deleted"})

    except subprocess.CalledProcessError as e:
        # возвращаем сообщение об ошибке
        return jsonify({"error": str(e)})


@route_com.route('/ls', methods=['GET'])
@jwt_required()
def list_dir():
    """Вывод содержимого директории"""

    # извлекаем данные из post-запроса
    payload = ListPayload(**request.json)

    try:
        # формируем команду bash
        bash_command = f'ls {payload.object_name}'
        result = subprocess.run(bash_command, shell=True, text=True, check=True, capture_output=True)

        # возвращаем список директорий
        return jsonify({"list_directory": result.stdout.split('\n')})

    except subprocess.CalledProcessError as e:
        # возвращаем сообщение об ошибке
        return jsonify({"error": str(e)})
