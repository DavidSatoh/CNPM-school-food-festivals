class Event:
    def __init__(self, id: int, name: str, description: str, date: str, location: str):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.location = location

    def __repr__(self):
        return f"<Event {self.name}>"

class EventRepository:
    def __init__(self):
        self.events = []  # Tạm thời dùng list (có thể thay DB sau)
        self.counter = 1
    
    def create(self, name, description, date, location):
        event = Event(self.counter, name, description, date, location)
        self.events.append(event)
        self.counter += 1
        return event