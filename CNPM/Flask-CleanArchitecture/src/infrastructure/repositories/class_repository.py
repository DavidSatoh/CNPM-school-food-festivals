from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import List, Optional
from domain.models.iclass_repository import IClassRepository
from domain.models.classes import Classes
from infrastructure.models.class_model import ClassModel


class ClassRepository(IClassRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def get_all(self) -> List[ClassModel]:
        return self.session.query(ClassModel).all()

    def get_by_id(self, class_id: int) -> Optional[ClassModel]:
        return self.session.query(ClassModel).filter(ClassModel.id == class_id).first()

    def create(self, class_data: Classes) -> ClassModel:
        class_ = ClassModel(
            id=None,
            name=class_data.name,
        )
        self.session.add(class_)
        self.session.commit()
        self.session.refresh(class_)
        return class_

    def update(self, class_id: int, class_data: Classes) -> Optional[ClassModel]:
        class_ = self.get_by_id(class_id)
        if not class_:
            return None
        class_.name = class_data.name
        try:
            self.session.merge(class_)
        except Exception as e:
            self.session.rollback()
            return None
        self.session.commit()
        return class_

    def delete(self, class_id: int) -> bool:
        class_ = self.get_by_id(class_id)
        if not class_:
            return False
        self.session.delete(class_)
        self.session.commit()
        return True