from infrastructure.models.booth_member import BoothMemberModel
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import List
from domain.models.boot_member import BoothMember
from domain.models.ibooth_member_repository import IBoothMemberRepository


class BoothMemberRepository(IBoothMemberRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def get_by_student_id(self, student_id: int) -> List[BoothMemberModel]:
        return self.session.query(BoothMemberModel).filter_by(student_id=student_id).all()

    def create_booth_member(self, booth_member: BoothMember) -> BoothMemberModel:
        booth_member_model = BoothMemberModel(
            student_id=booth_member.student_id,
            booth_id=booth_member.booth_id,
            role=booth_member.role
        )
        self.session.add(booth_member_model)
        self.session.commit()
        self.session.refresh(booth_member_model)
        return booth_member_model

    def update_role(self, booth_member: BoothMember, new_role: str) -> BoothMemberModel:
        booth_member_model = self.session.query(BoothMemberModel).filter_by(
            student_id=booth_member.student_id,
            booth_id=booth_member.booth_id
        ).first()
        if booth_member_model:
            booth_member_model.role = new_role
            try:
                self.session.merge(booth_member_model)
            except Exception as e:
                self.session.rollback()
                raise e
            finally:
                self.session.commit()
        return booth_member_model

    def delete_booth_member(self, booth_member: BoothMember) -> None:
        booth_member_model = self.session.query(BoothMemberModel).filter_by(
            student_id=booth_member.student_id,
            booth_id=booth_member.booth_id,
        ).first()
        if booth_member_model:
            try:
                self.session.delete(booth_member_model)
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                raise e
