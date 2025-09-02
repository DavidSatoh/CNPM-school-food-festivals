from sqlalchemy import Column, ForeignKey, Integer, DateTime
from infrastructure.databases.base import Base
from infrastructure.models.booth_model import BoothModel

class TransactionModel(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    booth_id = Column(Integer, ForeignKey(BoothModel.__tablename__ + '.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
