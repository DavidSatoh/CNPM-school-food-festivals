class Booth:
    def __init__(
        self,
        id: int,
        name: str,
        event_id: int,
        class_id: int,
        description: str,
        location: str,
        approval_status: str
    ):
        self.id = id
        self.name = name
        self.event_id = event_id
        self.class_id = class_id
        self.description = description
        self.location = location
        self.approval_status = approval_status