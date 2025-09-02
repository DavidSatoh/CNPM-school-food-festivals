from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
from infrastructure.models.student_model import StudentModel
from infrastructure.models.booth_model import BoothModel


class BoothMemberModel(Base):
    __tablename__ = 'booth_members'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(StudentModel.__tablename__ + '.id'), nullable=False)
    booth_id = Column(Integer, ForeignKey(BoothModel.__tablename__ + '.id'), nullable=False)
    role = Column(String(50), nullable=False)
