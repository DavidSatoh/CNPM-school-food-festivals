from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
from infrastructure.models.class_model import ClassModel
from infrastructure.models.event_model import EventModel

class BoothModel(Base):
    __tablename__ = 'booths'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    event_id = Column(Integer, ForeignKey(EventModel.__tablename__ + '.id'), nullable=False)
    class_id = Column(Integer, ForeignKey(ClassModel.__tablename__ + '.id'), nullable=False)
    description = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    approval_status = Column(String(50), nullable=False)