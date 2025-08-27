from src.domain.models.feedback import Feedback
from src.infrastructure.repositories.feedback_repository import FeedbackRepository

class FeedbackService:
    def __init__(self, repository: FeedbackRepository):
        self.repository = repository

    def create_feedback(self, user_id: int, content: str, event_id: int = None, food_id: int = None):
        if not content or len(content.strip()) == 0:
            raise ValueError("Content must not be empty")
        feedback = Feedback(id=len(self.repository.feedbacks)+1, user_id=user_id, content=content, event_id=event_id, food_id=food_id)
        return self.repository.add_feedback(feedback)

    def get_feedback(self, feedback_id: int):
        return self.repository.get_feedback(feedback_id)

    def get_feedbacks_by_food(self, food_id: int):
        return self.repository.get_feedbacks_by_food(food_id)

    def get_feedbacks_by_event(self, event_id: int):
        return self.repository.get_feedbacks_by_event(event_id)

    def delete_feedback(self, feedback_id: int):
        self.repository.delete_feedback(feedback_id)
