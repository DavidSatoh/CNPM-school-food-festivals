from typing import List, Optional
from domain.models.classes import Classes
from infrastructure.models.class_model import ClassModel
from abc import ABC, abstractmethod

class IClassRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ClassModel]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, class_id: int) -> Optional[ClassModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, class_data: Classes) -> ClassModel:
        raise NotImplementedError

    @abstractmethod
    def update(self, class_id: int, class_data: Classes) -> Optional[ClassModel]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, class_id: int) -> bool:
        raise NotImplementedError
