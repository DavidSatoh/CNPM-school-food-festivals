class User:
    def __init__(self, user_name: str, password: str, role: str = 'user'):
        self.user_name = user_name
        self.password = password
        self.role = role