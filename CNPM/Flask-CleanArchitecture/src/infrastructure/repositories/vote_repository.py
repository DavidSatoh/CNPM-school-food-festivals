from typing import List, Optional
from src.domain.models.vote import Vote
from infrastructure.models.vote_model import VoteModel
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from src.domain.models.ivote_repository import IVoteRepository

class VoteRepository(IVoteRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def add_vote(self, vote: Vote) -> VoteModel:
        # xác thực vote có tồn tại chưa
        existing_vote = self.get_vote(vote.id)
        if existing_vote:
            raise ValueError("Vote already exists")

        vote_model = VoteModel(
            user_id=vote.user_id,
            food_id=vote.food_id,
            event_id=vote.event_id,
            value=vote.value
        )
        self.session.add(vote_model)
        self.session.commit()
        self.session.refresh(vote_model)
        return vote_model

    def get_vote(self, vote_id: int) -> Optional[VoteModel]:
        return self.session.query(VoteModel).filter(VoteModel.id == vote_id).first()

    def get_votes_by_food(self, food_id: int) -> List[VoteModel]:
        return self.session.query(VoteModel).filter(VoteModel.food_id == food_id).all()

    def get_votes_by_event(self, event_id: int) -> List[VoteModel]:
        return self.session.query(VoteModel).filter(VoteModel.event_id == event_id).all()

    def delete_vote(self, vote_id: int):
        vote = self.get_vote(vote_id)
        if vote:
            try:
                self.session.delete(vote)
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                raise e
