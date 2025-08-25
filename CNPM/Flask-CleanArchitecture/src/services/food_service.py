class FoodService:
    def __init__(self, food_repository):
        self.food_repository = food_repository

    def list_foods(self):
        return self.food_repository.get_all()

    def get_food(self, food_id):
        return self.food_repository.get_by_id(food_id)

    def create_food(self, name, description, price, category, event_id):
        food_data = {
            "name": name,
            "description": description,
            "price": price,
            "category": category,
            "event_id": event_id
        }
        return self.food_repository.create(food_data)

    def update_food(self, food_id, name, description, price, category, event_id):
        food_data = {
            "name": name,
            "description": description,
            "price": price,
            "category": category,
            "event_id": event_id
        }
        return self.food_repository.update(food_id, food_data)

    def delete_food(self, food_id):
        return self.food_repository.delete(food_id)