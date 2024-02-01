from pydantic import BaseModel


class FilePayload(BaseModel):
    """Сериализатор для метода создания файла"""

    file_name: str
    path: str
    text: str = ""


class DirPayload(BaseModel):
    """Сериализатор для метода создания директории"""

    dir_name: str
    path: str


class ChmodPayload(BaseModel):
    """Сериализатор для метода изменения маски разрешений"""

    object_name: str
    mask: int


class ChownPayload(BaseModel):
    """Сериализатор для метода изменения владельца"""

    object_name: str
    owner: str


class DeletePayload(BaseModel):
    """Сериализатор для метода удаления файла или директории"""

    object_name: str


class ListPayload(BaseModel):
    """Сериализатор для вывода содержимого директории"""

    object_name: str
