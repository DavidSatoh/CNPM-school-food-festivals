from sqlalchemy import Column, String
from infrastructure.databases.base import Base

class LopHocModel(Base):
    __tablename__ = 'LopHoc'
    LopHocID = Column(String(10), nullable = False, primary_key=True)
    TenLopHoc = Column(String(50), nullable=False)