from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from infrastructure.databases.base import Base

# Database configuration
DATABASE_URI = Config.DATABASE_URI
engine = create_engine(
    "mssql+pyodbc://sa:Aa123456@127.0.0.1,1433/FlaskApiDB"
    "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
def init_mssql(app):
    Base.metadata.create_all(bind=engine)