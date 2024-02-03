from src.config import db


class Users(db.Model):
    """Модель пользователя для БД"""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def save_to_db(self):
        # сохранение в БД
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        # проверка существования пользователя в БД
        return cls.query.filter_by(username=username).first()
