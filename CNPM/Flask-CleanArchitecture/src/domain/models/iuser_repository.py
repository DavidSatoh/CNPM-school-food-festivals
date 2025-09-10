from abc import ABC, abstractmethod
from typing import Optional
from domain.models.user import User
class IUserRepository(ABC):
    @abstractmethod
    def get_by_username(self, user_name: str) -> Optional[User]:
        pass

    @abstractmethod
    def create_user(self, user_name: str, password: str, role: str = 'user') -> User:
        pass