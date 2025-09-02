from infrastructure.models.user_model import UserModel
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import Optional
from domain.models.iuser_repository import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def get_by_username(self, user_name: str) -> Optional[UserModel]:
        return self.session.query(UserModel).filter_by(user_name=user_name).first()

    def create_user(self, user_name: str, password: str, role: str = 'user') -> UserModel:
        user = UserModel(user_name=user_name, password=password, role=role)
        existing_user = self.get_by_username(user_name)
        if existing_user:
            raise ValueError("User already exists")
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user