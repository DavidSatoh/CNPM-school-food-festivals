from infrastructure.models.booth_member import BoothMemberModel
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import List
from domain.models.student import Student
from infrastructure.models.student_model import StudentModel

class StudentRepository:
    def __init__(self, db_session: Session = session):
        self.db_session = db_session

    def create_student(self, student: Student) -> StudentModel:
        student_model = StudentModel.from_orm(student)
        self.db_session.add(student_model)
        self.db_session.commit()
        self.db_session.refresh(student_model)
        return student_model


    def get_student(self, student_id: int) -> StudentModel:
        return self.db_session.query(StudentModel).filter(StudentModel.id == student_id).first()

    def get_all_students(self) -> List[StudentModel]:
        return self.db_session.query(StudentModel).all()

    def update_student(self, student: StudentModel) -> StudentModel:
        self.db_session.merge(student)
        self.db_session.commit()
        return student

    def delete_student(self, student: StudentModel) -> None:
        self.db_session.delete(student)
        self.db_session.commit()
