from sqlalchemy import Column, ForeignKey, Integer, DateTime
from infrastructure.databases.base import Base
from infrastructure.models.booth_model import BoothModel
from domain.models.transaction import Transaction
class TransactionModel(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    booth_id = Column(Integer, ForeignKey(BoothModel.__tablename__ + '.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    @classmethod
    def from_orm(cls, transaction: Transaction) -> "TransactionModel":
        return cls(
            id=transaction.id,
            booth_id=transaction.booth_id,
            amount=transaction.amount,
            created_at=transaction.created_at,
        )

    def to_orm(self) -> Transaction:
        return Transaction(
            id=self.id,
            booth_id=self.booth_id,
            amount=self.amount,
            created_at=self.created_at,
        )
