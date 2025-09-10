from sched import Event
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base
from domain.models.event import Event


class EventModel(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)

    def __repr__(self):
        return f"<Event {self.name}>"

    @classmethod
    def from_orm(cls, event: Event) -> "EventModel":
        return cls(
            id=event.id,
            name=event.name,
            description=event.description,
            date=event.date,
            location=event.location,
        )

    def to_orm(self) -> Event:
        return Event(
            id=self.id,
            name=self.name,
            description=self.description,
            date=self.date,
            location=self.location,
        )