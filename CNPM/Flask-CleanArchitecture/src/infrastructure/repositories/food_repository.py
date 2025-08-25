from domain.models.food import Food

class FoodRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Food).all()

    def get_by_id(self, food_id):
        return self.session.query(Food).filter(Food.id == food_id).first()

    def create(self, food_data):
        food = Food(
            id=None, 
            name=food_data['name'],
            description=food_data['description'],
            price=food_data['price'],
            category=food_data['category'],
            event_id=food_data['event_id']
        )
        self.session.add(food)
        self.session.commit()
        return food

    def update(self, food_id, food_data):
        food = self.get_by_id(food_id)
        if not food:
            return None
        food.name = food_data['name']
        food.description = food_data['description']
        food.price = food_data['price']
        food.category = food_data['category']
        food.event_id = food_data['event_id']
        self.session.commit()
        return food

    def delete(self, food_id):
        food = self.get_by_id(food_id)
        if not food:
            return False
        self.session.delete(food)
        self.session.commit()
        return True