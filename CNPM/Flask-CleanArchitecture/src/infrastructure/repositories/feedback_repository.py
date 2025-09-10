from src.domain.models.feedback import Feedback
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session

class FeedbackRepository:
    def __init__(self, session: Session = session):
        self.session = session

    def add_feedback(self, feedback: Feedback):
        self.session.add(feedback)
        self.session.commit()
        self.session.refresh(feedback)
        return feedback

    def get_feedback(self, feedback_id: int):
        return self.session.query(Feedback).filter(Feedback.id == feedback_id).first()

    def get_feedbacks_by_food(self, food_id: int):
        return self.session.query(Feedback).filter(Feedback.food_id == food_id).all()

    def get_feedbacks_by_event(self, event_id: int):
        return self.session.query(Feedback).filter(Feedback.event_id == event_id).all()

    def delete_feedback(self, feedback_id: int):
        feedback = self.get_feedback(feedback_id)
        if feedback:
            try:
                self.session.delete(feedback)
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                raise e
