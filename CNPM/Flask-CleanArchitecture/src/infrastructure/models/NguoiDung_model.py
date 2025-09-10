from sqlalchemy import Column, Integer, String, DateTime, Boolean
from infrastructure.databases.base import Base

class UserModel(Base):
    __tablename__ = 'NguoiDung'
    # __table_args__ = {'extend_existing': True}  # Thêm dòng này

    NguoiDungID = Column(Integer, primary_key=True)
    TenNguoiDung = Column(String(50), nullable=False)
    MatKhau = Column(String(18), nullable=False)
    Email = Column(String(76), nullable = False)
    HocSinhID = Column(String(10), nullable=False)
    LopID=Column(String(10), nullable=False)
    status = Column(Boolean, nullable=False)
    NgayTao = Column(DateTime, nullable=False)
    NgayCapNhat = Column(DateTime)