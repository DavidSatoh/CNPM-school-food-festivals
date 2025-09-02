from sqlalchemy import Column, Integer, String, ForeignKey
from infrastructure.databases.base import Base
from infrastructure.models.class_model import ClassModel

class StudentModel(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey(ClassModel.__tablename__ + '.id'), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
