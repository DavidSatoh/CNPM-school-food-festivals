from infrastructure.models.booth_member import BoothMemberModel
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from typing import List
from domain.models.transaction import Transaction
from infrastructure.models.transaction_mode import TransactionModel


class TransactionRepository:
    def __init__(self, db_session: Session = session):
        self.db_session = db_session

    def create_transaction(self, transaction: Transaction) -> Transaction:
        transaction_model = TransactionModel.from_orm(transaction)
        self.db_session.add(transaction_model)
        self.db_session.commit()
        self.db_session.refresh(transaction_model)
        return transaction_model.to_orm()

    def get_transaction(self, transaction_id: int) -> Transaction:
        return self.db_session.query(TransactionModel).filter(TransactionModel.id == transaction_id).first()

    def get_all_transactions(self) -> List[TransactionModel]:
        return self.db_session.query(TransactionModel).all()

    def update_transaction(self, transaction: TransactionModel) -> TransactionModel:
        self.db_session.merge(transaction)
        self.db_session.commit()
        return transaction

    def delete_transaction(self, transaction: TransactionModel) -> None:
        self.db_session.delete(transaction)
        self.db_session.commit()
