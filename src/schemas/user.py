from pydantic import BaseModel


class User(BaseModel):
    """Модель для регистрации пользователя"""

    username: str
    password: str
