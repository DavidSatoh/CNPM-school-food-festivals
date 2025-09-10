from typing import List, Optional
from domain.models.classes import Classes
from abc import ABC, abstractmethod

class IClassRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Classes]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, class_id: int) -> Optional[Classes]:
        raise NotImplementedError

    @abstractmethod
    def create(self, class_data: Classes) -> Classes:
        raise NotImplementedError

    @abstractmethod
    def update(self, class_id: int, class_data: Classes) -> Optional[Classes]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, class_id: int) -> bool:
        raise NotImplementedError
