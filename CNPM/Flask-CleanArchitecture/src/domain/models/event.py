class Event:
    def __init__(self, id: int, name: str, description: str, date: str, location: str):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.location = location

    def __repr__(self):
        return f"<Event {self.name}>"