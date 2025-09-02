from domain.models.ifood_repository import IFoodRepository
from domain.models.food import Food


class FoodService:
    def __init__(self, food_repository: IFoodRepository):
        self.food_repository = food_repository

    def list_foods(self):
        return self.food_repository.get_all()

    def get_food(self, food_id: int):
        return self.food_repository.get_by_id(food_id)

    def create_food(self, food_data: Food):
        return self.food_repository.create(food_data)

    def update_food(self, food_id: int, food_data: Food):
        return self.food_repository.update(food_id, food_data)

    def delete_food(self, food_id: int):
        return self.food_repository.delete(food_id)