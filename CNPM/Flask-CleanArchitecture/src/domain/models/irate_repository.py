from typing import List, Optional
from domain.models.rate import Rate
from infrastructure.models.rate_model import RateModel
from abc import ABC, abstractmethod

class IRateRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[RateModel]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, rate_id: int) -> Optional[RateModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, rate_data: Rate) -> RateModel:
        raise NotImplementedError

    @abstractmethod
    def update(self, rate_id: int, rate_data: Rate) -> Optional[RateModel]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, rate_id: int) -> bool:
        raise NotImplementedError
