from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base

class EventModel(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)

    def __repr__(self):
        return f"<Event {self.name}>"