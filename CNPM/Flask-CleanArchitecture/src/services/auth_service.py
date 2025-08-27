from repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, user_name, password):
        user = self.user_repo.get_by_username(user_name)
        if user and check_password_hash(user.password, password):
            return user
        return None

    def register(self, user_name, password, role='user'):
        if self.user_repo.get_by_username(user_name):
            return None
        hashed_pw = generate_password_hash(password)
        return self.user_repo.create_user(user_name, hashed_pw, role)