from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
from infrastructure.models.class_model import ClassModel
from infrastructure.models.event_model import EventModel
from domain.models.booth import Booth

class BoothModel(Base):
    __tablename__ = 'booths'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    event_id = Column(Integer, ForeignKey(EventModel.__tablename__ + '.id'), nullable=False)
    class_id = Column(Integer, ForeignKey(ClassModel.__tablename__ + '.id'), nullable=False)
    description = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    approval_status = Column(String(50), nullable=False)

    def to_orm(self) -> Booth:
        return Booth(
            id=self.id,
            name=self.name,
            event_id=self.event_id,
            class_id=self.class_id,
            description=self.description,
            location=self.location,
            approval_status=self.approval_status
        )

    @classmethod
    def from_orm(cls, booth: Booth) -> "BoothModel":
        return cls(
            id=booth.id,
            name=booth.name,
            event_id=booth.event_id,
            class_id=booth.class_id,
            description=booth.description,
            location=booth.location,
            approval_status=booth.approval_status
        )