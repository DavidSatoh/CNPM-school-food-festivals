from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import List, Optional
from domain.models.rate import Rate
from infrastructure.models.rate_model import RateModel
from domain.models.irate_repository import IRateRepository

class RateRepository(IRateRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def get_all(self) -> List[RateModel]:
        return self.session.query(RateModel).all()

    def get_by_id(self, rate_id: int) -> Optional[RateModel]:
        return self.session.query(RateModel).filter(RateModel.id == rate_id).first()

    def create(self, rate_data: Rate) -> RateModel:
        rate = RateModel(
            id=None,
            booth_id=rate_data.booth_id,
            user_id=rate_data.user_id,
            score=rate_data.score,
            comment=rate_data.comment
        )
        self.session.add(rate)
        self.session.commit()
        self.session.refresh(rate)
        return rate

    def update(self, rate_id: int, rate_data: Rate) -> Optional[RateModel]:
        rate = self.get_by_id(rate_id)
        if not rate:
            return None
        rate.booth_id = rate_data.booth_id
        rate.user_id = rate_data.user_id
        rate.score = rate_data.score
        rate.comment = rate_data.comment
        try:
            self.session.merge(rate)
        except Exception as e:
            self.session.rollback()
            return None
        self.session.commit()
        return rate

    def delete(self, rate_id: int) -> bool:
        rate = self.get_by_id(rate_id)
        if not rate:
            return False
        self.session.delete(rate)
        self.session.commit()
        return True