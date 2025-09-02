from domain.models.food import Food
from infrastructure.models.food_model import FoodModel
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from domain.models.ifood_repository import IFoodRepository
from typing import List, Optional

class FoodRepository(IFoodRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def get_all(self) -> List[FoodModel]:
        return self.session.query(FoodModel).all()

    def get_by_id(self, food_id: int) -> Optional[FoodModel]:
        return self.session.query(FoodModel).filter(FoodModel.id == food_id).first()

    def create(self, booth_id: int, food_data: Food) -> FoodModel:
        food = FoodModel(
            id=None, 
            name=food_data.name,
            price=food_data.price,
            booth_id=booth_id
        )
        self.session.add(food)
        self.session.commit()
        self.session.refresh(food)
        return food

    def update(self, food_id: int, food_data: Food) -> FoodModel:
        food = self.get_by_id(food_id)
        if not food:
            return None
        food.name = food_data.name
        food.price = food_data.price
        try:
            self.session.merge(food)
        except Exception as e:
            self.session.rollback()
            return None
        self.session.commit()
        return food

    def delete(self, food_id: int):
        food = self.get_by_id(food_id)
        if not food:
            return False
        self.session.delete(food)
        self.session.commit()
        return True