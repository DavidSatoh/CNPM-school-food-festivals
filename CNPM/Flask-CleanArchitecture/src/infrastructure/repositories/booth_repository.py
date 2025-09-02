from infrastructure.models.booth_model import BoothModel
from domain.models.ibooth_repository import IBoothRepository
from domain.models.booth import Booth
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import List, Optional


class BoothRepository(IBoothRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def get_all(self) -> List[BoothModel]:
        return self.session.query(BoothModel).all()

    def get_by_id(self, booth_id: int) -> Optional[BoothModel]:
        return self.session.query(BoothModel).filter(BoothModel.id == booth_id).first()

    def create(self, booth_data: Booth) -> BoothModel:
        booth = BoothModel(
            id=None,
            name=booth_data.name,
            event_id=booth_data.event_id,
            class_id=booth_data.class_id,
            description=booth_data.description,
            location=booth_data.location,
            approval_status=booth_data.approval_status
        )
        self.session.add(booth)
        self.session.commit()
        self.session.refresh(booth)
        return booth

    def update(self, booth_id: int, booth_data: Booth) -> BoothModel:
        booth = self.get_by_id(booth_id)
        if not booth:
            return None
        booth.name = booth_data.name
        booth.location = booth_data.location
        booth.description = booth_data.description
        booth.approval_status = booth_data.approval_status
        try:
            self.session.merge(booth)
        except Exception as e:
            self.session.rollback()
            return None
        self.session.commit()
        return booth

    def delete(self, booth_id: int):
        booth = self.get_by_id(booth_id)
        if not booth:
            return False
        self.session.delete(booth)
        self.session.commit()
        return True