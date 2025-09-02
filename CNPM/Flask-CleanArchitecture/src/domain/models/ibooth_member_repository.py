from abc import ABC, abstractmethod
from typing import List
from domain.models.boot_member import BoothMember
class IBoothMemberRepository(ABC):
    @abstractmethod
    def get_by_student_id(self, student_id: int) -> List[BoothMember]:
        pass

    @abstractmethod
    def create_booth_member(self, booth_member: BoothMember) -> BoothMember:
        pass

    @abstractmethod
    def update_role(self, booth_member: BoothMember, new_role: str) -> BoothMember:
        pass

    @abstractmethod
    def delete_booth_member(self, booth_member: BoothMember) -> None:
        pass
