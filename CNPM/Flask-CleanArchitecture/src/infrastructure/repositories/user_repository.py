from domain.models.user import UserModel
from infrastructure.databases.mssql import session

class UserRepository:
    def get_by_username(self, user_name):
        return session.query(UserModel).filter_by(user_name=user_name).first()

    def create_user(self, user_name, password, role='user'):
        user = UserModel(user_name=user_name, password=password, role=role)
        session.add(user)
        session.commit()
        return user