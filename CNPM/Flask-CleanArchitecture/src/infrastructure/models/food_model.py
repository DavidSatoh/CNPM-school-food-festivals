from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Float
from infrastructure.databases.base import Base
from infrastructure.models.booth_model import BoothModel


class FoodModel(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    gianHanId = Column(Integer, ForeignKey(BoothModel.__tablename__ + '.id'))
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
