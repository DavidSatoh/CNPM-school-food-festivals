from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.models.vote import Vote

class IVoteRepository(ABC):
    @abstractmethod
    def add_vote(self, vote: Vote) -> Vote:
        pass

    @abstractmethod
    def get_vote(self, vote_id: int) -> Optional[Vote]:
        pass

    @abstractmethod
    def get_votes_by_food(self, food_id: int) -> List[Vote]:
        pass

    @abstractmethod
    def get_votes_by_event(self, event_id: int) -> List[Vote]:
        pass

    @abstractmethod
    def delete_vote(self, vote_id: int):
        pass
