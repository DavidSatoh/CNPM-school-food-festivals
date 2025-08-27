class Food:
    def __init__(self, id: int, name: str, description: str, price: float, category: str, event_id: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.event_id = event_id

    def __repr__(self):
        return f"<Food {self.name}>"