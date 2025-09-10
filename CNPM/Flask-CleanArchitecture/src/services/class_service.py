from domain.models.iclass_repository import IClassRepository
from domain.models.classes import Classes
from typing import List, Optional

class ClassService:
    def __init__(self, repository: IClassRepository):
        self.repository = repository

    def get_all_classes(self) -> List[Classes]:
        return self.repository.get_all()

    def get_class_by_id(self, class_id: int) -> Optional[Classes]:
        return self.repository.get_by_id(class_id)

    def create_class(self, class_data: Classes) -> Classes:
        return self.repository.create(class_data)

    def update_class(self, class_id: int, class_data: Classes) -> Optional[Classes]:
        return self.repository.update(class_id, class_data)

    def delete_class(self, class_id: int) -> bool:
        return self.repository.delete(class_id)
