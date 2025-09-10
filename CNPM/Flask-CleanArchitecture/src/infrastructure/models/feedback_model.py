from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from infrastructure.databases.base import Base
from infrastructure.models.user_model import UserModel
from infrastructure.models.course_model import CourseModel


class FeedbackModel(Base):
    __tablename__ = 'feedbacks'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)

    feedback_text = Column(String(255))
    evaluation = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 
    course_id = Column(Integer, ForeignKey(CourseModel.__tablename__ + '.id'))
    user_id = Column(Integer, ForeignKey(UserModel.__tablename__ + '.id'))