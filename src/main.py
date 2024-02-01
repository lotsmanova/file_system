import os

from flask import Flask, request, jsonify
import subprocess
from src.schemas import FilePayload, DirPayload, ChmodPayload, ChownPayload, DeletePayload, ListPayload

app = Flask(__name__)


@app.route('/')
def hello():
    """Приветствие пользователя"""

    return "Hello, I am very fast and efficient application!"


@app.route('/touch', methods=['POST'])
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


@app.route('/mkdir', methods=['POST'])
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


@app.route('/chmod', methods=['POST'])
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


@app.route('/chown', methods=['POST'])
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


@app.route('/rm', methods=['DELETE'])
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


@app.route('/ls', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True)
