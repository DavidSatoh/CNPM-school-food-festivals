
class Food:
    def __init__(self, id: int, name: str, description: str, price: float, event_id: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.event_id = event_id

    def __repr__(self):
        return f"<Food {self.name}>"