# The client's file system

---

REST API предназначен для выполнения стандартных действий в файловой системе клиента. API обладает возможностью возвращать содержимое определённой директории, создавать, изменять, удалять и выводить список объектов выбранной директории.

## Технологии

---

- Python 3+
- Flask
- subprocess
- Bash
- logging
- Pydantic
- SQLAlchemy
- Alembic
- Docker
- pytest

## Запуск проекта

---

- Зависимости для проекта находятся в `requirements.txt`. Команда для установки: `pip install -r requirements.txt`;
- Файл `.env.sample` содержит необходимые переменные окружения;
- Применить миграции: `alembic upgrade head`

## Структура проекта

---

### **Endpoints**:

- [ ]  `/register.` Регистрация пользователя с получение токена доступа к защищенным endpoints.
- [ ]  `/login`. Вход в аккаунт для получения нового токена.

Защищенные **endpoints.** Для получения доступа необходимо передеать заголовок `{"Authorization": "Bearer {your_token}"}`.

- [ ]  `/`. Возвращает приветственное сообщение.
- [ ]  `/touch`.  Создать файл с заданным именем по заданному пути.
- [ ]  `/mkdir`. Создать директорию с заданным именем по заданному пути.
- [ ]  `/chmod`. Изменить маску разрешений файла или директории.
- [ ]  `/chown`. Изменить владельца файла или директории.
- [ ]  `/rm`. Удалить файл или директорию с заданным именем.
- [ ]  `/ls`. Получить содержимое директории.

**Модели SQLAlchemy:**

- [ ]  `Users`. Структура таблицы для хранения информации о зарегистрированных пользователях.

## Тестирование

---

Тесты написаны с помощью библиотеки `pytest`. Общее покрытие тестами 93 %. 

## Docker

---

Сбор контейнера: `docker compose build`

Запуск контейнера: `docker compose up`