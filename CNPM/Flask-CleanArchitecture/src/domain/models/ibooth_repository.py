from typing import List, Optional
from domain.models.booth import Booth
from infrastructure.models.booth_model import BoothModel
from abc import ABC, abstractmethod

class IBoothRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BoothModel]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, booth_id: int) -> Optional[BoothModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, booth_data: Booth) -> BoothModel:
        raise NotImplementedError

    @abstractmethod
    def update(self, booth_id: int, booth_data: Booth) -> Optional[BoothModel]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, booth_id: int) -> bool:
        raise NotImplementedError
