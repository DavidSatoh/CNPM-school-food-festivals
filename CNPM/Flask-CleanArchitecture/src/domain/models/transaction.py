class Transaction:
    def __init__(self, id: int, amount: float, booth_id: int, created_at: int):
        self.id = id
        self.amount = amount
        self.booth_id = booth_id
        self.created_at = created_at