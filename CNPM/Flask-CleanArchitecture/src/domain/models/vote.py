class Vote:
    def __init__(self, id: int, user_id: int, food_id: int, event_id: int, score: int):
        self.id = id
        self.user_id = user_id
        self.food_id = food_id
        self.event_id = event_id
        self.score = score

    def __repr__(self):
        return f"<Vote {self.id} - User {self.user_id} - Food {self.food_id}>"