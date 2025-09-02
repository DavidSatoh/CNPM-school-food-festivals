from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Float
from infrastructure.databases.base import Base

class FoodModel(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    gianHanId = Column(Integer, ForeignKey('gian_han.id'))
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
