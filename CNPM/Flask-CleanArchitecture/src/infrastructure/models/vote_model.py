from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from infrastructure.databases.base import Base
from infrastructure.models.user_model import UserModel

class VoteModel(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(UserModel.__tablename__ + '.id'), nullable=False)
    food_id = Column(Integer, nullable=False)

