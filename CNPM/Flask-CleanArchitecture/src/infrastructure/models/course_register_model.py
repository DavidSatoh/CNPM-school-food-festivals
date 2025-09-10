from sqlalchemy import Column, ForeignKey, Integer
from infrastructure.databases.base import Base
from infrastructure.models.user_model import UserModel
from infrastructure.models.course_model import CourseModel

class CourseRegisterModel(Base):
    __tablename__ = 'course_register'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey(UserModel.__tablename__ + '.id'))
    course_id = Column(Integer, ForeignKey(CourseModel.__tablename__ + '.id'))