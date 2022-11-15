from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id,nombre,userName,password) -> None:
        self.id = id
        self.nombre = nombre
        self.userName = userName
        self.password = password

    @classmethod
    def check_Password(self, hashed_password,password):
        return check_password_hash(hashed_password,password)

    def convertir(password):
        return generate_password_hash(password)
