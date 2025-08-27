from src.domain.models.vote import Vote
from src.infrastructure.repositories.vote_repository import VoteRepository

class VoteService:
    def __init__(self, repository: VoteRepository):
        self.repository = repository

    def create_vote(self, user_id: int, food_id: int, event_id: int, score: int):
        # Validate score
        if score < 1 or score > 5:
            raise ValueError("Score must be between 1 and 5")
        vote = Vote(id=len(self.repository.votes)+1, user_id=user_id, food_id=food_id, event_id=event_id, score=score)
        return self.repository.add_vote(vote)

    def get_vote(self, vote_id: int):
        return self.repository.get_vote(vote_id)

    def get_votes_by_food(self, food_id: int):
        return self.repository.get_votes_by_food(food_id)

    def get_votes_by_event(self, event_id: int):
        return self.repository.get_votes_by_event(event_id)

    def delete_vote(self, vote_id: int):
        self.repository.delete_vote(vote_id)
