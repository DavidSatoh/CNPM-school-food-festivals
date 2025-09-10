from sqlalchemy import Column, Integer, String
from infrastructure.databases.base import Base



class ClassModel(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)