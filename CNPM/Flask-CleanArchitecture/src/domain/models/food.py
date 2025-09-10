class Food:
    def __init__(self, id: int, name: str, price: float, gian_hang_id: int):
        self.id = id
        self.name = name
        self.price = price
        self.gian_hang_id = gian_hang_id

    def __repr__(self):
        return f"<Food {self.name}>"