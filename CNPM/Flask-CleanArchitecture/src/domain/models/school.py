class School:
    def __init__(self, id: int, name: str, address: str):
        self.id = id
        self.name = name
        self.address = address

    def __repr__(self):
        return f"<School {self.name}>"