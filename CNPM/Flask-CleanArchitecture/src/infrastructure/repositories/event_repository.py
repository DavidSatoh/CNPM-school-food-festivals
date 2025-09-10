from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import List

from domain.models.event import Event
from infrastructure.models.event_model import EventModel

class EventRepository:
    def __init__(self, db_session: Session = session):
        self.db_session = db_session

    def create_event(self, event: Event) -> Event:
        self.db_session.add(event)
        self.db_session.commit()
        self.db_session.refresh(event)
        return event

    def get_event(self, event_id: int) -> Event:
        return self.db_session.query(EventModel).filter(EventModel.id == event_id).first()

    def get_all_events(self) -> List[Event]:
        return self.db_session.query(EventModel).all()

    def update_event(self, event: Event) -> EventModel:
        event_model = EventModel.from_orm(event)
        self.db_session.merge(event_model)
        self.db_session.commit()
        return event_model

    def delete_event(self, event: Event) -> None:
        event_model = EventModel.from_orm(event)
        self.db_session.delete(event_model)
        self.db_session.commit()
