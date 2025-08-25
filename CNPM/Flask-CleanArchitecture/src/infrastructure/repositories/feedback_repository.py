from src.domain.models.feedback import Feedback

class FeedbackRepository:
    def __init__(self):
        self.feedbacks = []  # In-memory storage, replace with DB logic

    def add_feedback(self, feedback: Feedback):
        self.feedbacks.append(feedback)
        return feedback

    def get_feedback(self, feedback_id: int):
        for feedback in self.feedbacks:
            if feedback.id == feedback_id:
                return feedback
        return None

    def get_feedbacks_by_food(self, food_id: int):
        return [fb for fb in self.feedbacks if fb.food_id == food_id]

    def get_feedbacks_by_event(self, event_id: int):
        return [fb for fb in self.feedbacks if fb.event_id == event_id]

    def delete_feedback(self, feedback_id: int):
        self.feedbacks = [fb for fb in self.feedbacks if fb.id != feedback_id]
