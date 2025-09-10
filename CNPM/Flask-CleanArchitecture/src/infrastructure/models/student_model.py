from sqlalchemy import Column, Integer, String, ForeignKey
from infrastructure.databases.base import Base
from infrastructure.models.class_model import ClassModel
from domain.models.student import Student

class StudentModel(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey(ClassModel.__tablename__ + '.id'), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

    @classmethod
    def from_orm(cls, student: Student) -> "StudentModel":
        return cls(
            id=student.id,
            class_id=student.class_id,
            name=student.name,
            email=student.email,
        )

    def to_orm(self) -> Student:
        return Student(
            id=self.id,
            class_id=self.class_id,
            name=self.name,
            email=self.email,
        )
