from abc import ABC, abstractmethod
from .todo import Todo
from typing import List, Optional
from .food import Food
from domain.models.food import Food

class IFoodRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Food]:
        pass

    @abstractmethod
    def get_by_id(self, food_id: int) -> Optional[Food]:
        pass

    @abstractmethod
    def create(self, food_data: Food) -> Food:
        pass

    @abstractmethod
    def update(self, food_id: int, food_data: Food) -> Optional[Food]:
        pass

    @abstractmethod
    def delete(self, food_id: int) -> bool:
        pass
