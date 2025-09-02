from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
from infrastructure.models.booth_model import BoothModel
from infrastructure.models.user_model import UserModel

class RateModel(Base):
    __tablename__ = 'rates'

    id = Column(Integer, primary_key=True)
    booth_id = Column(Integer, ForeignKey(BoothModel.__tablename__ + '.id'), nullable=False)
    user_id = Column(Integer, ForeignKey(UserModel.__tablename__ + '.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
