class Feedback:
    def __init__(self, id: int, user_id: int, content: str, event_id: int = None, food_id: int = None):
        self.id = id
        self.user_id = user_id
        self.content = content
        self.event_id = event_id
        self.food_id = food_id

    def __repr__(self):
        return f"<Feedback {self.id} - User {self.user_id}>"