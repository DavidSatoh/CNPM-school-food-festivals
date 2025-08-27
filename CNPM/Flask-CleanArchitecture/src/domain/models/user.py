from sqlalchemy import Column, Integer, String
from infrastructure.databases.mssql import Base

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default='user')  