from src.domain.models.vote import Vote

class VoteRepository:
    def __init__(self):
        self.votes = []  # In-memory storage, replace with DB logic

    def add_vote(self, vote: Vote):
        self.votes.append(vote)
        return vote

    def get_vote(self, vote_id: int):
        for vote in self.votes:
            if vote.id == vote_id:
                return vote
        return None

    def get_votes_by_food(self, food_id: int):
        return [vote for vote in self.votes if vote.food_id == food_id]

    def get_votes_by_event(self, event_id: int):
        return [vote for vote in self.votes if vote.event_id == event_id]

    def delete_vote(self, vote_id: int):
        self.votes = [vote for vote in self.votes if vote.id != vote_id]
