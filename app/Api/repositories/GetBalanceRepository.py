from sqlalchemy.orm import Session
from sqlalchemy import func
from models.User import User
from models.Expense import Expense
from models.GroupMember import GroupMember
from models.ExpenseSplit import ExpenseSplit
from models.Settlement import Settlement

class GetBalanceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_balance(self,Group: int):

        members = (
            self.db.query(User)
            .join(GroupMember, GroupMember.user_id == User.id)
            .filter(GroupMember.group_id == Group)
            .all()
        )

        balances = []

        for member in members:
            total_paid = self.db.query(
                func.coalesce(func.sum(Expense.total_amount), 0).filter(Expense.payer_id == member.id, Expense.group_id == Group).scalar()
            )

            total_owed = self.db.query(
                func.coalesce(func.sum(ExpenseSplit.amount_owed), 0)
            ).join(Expense, Expense.id == ExpenseSplit.expense_id).filter(ExpenseSplit.user_id == member.id, Expense.group_id == Group).scalar()


            settlements_paid = self.db.query(
                func.coalesce(func.sum(Settlement.amount), 0)
            ).filter(Settlement.payer_id == member.id, Settlement.group_id == Group).scalar()

            settlements_received = self.db.query(
                func.coalesce(func.sum(Settlement.amount), 0)
            ).filter(Settlement.receiver_id == member.id, Settlement.group_id == Group).scalar()

            net_balance = (total_paid + settlements_paid) - (total_owed + settlements_received)

            balances.append({
                "user_id": member.id,
                "full_name": member.full_name,
                "net_balance": round(net_balance, 2)
            })

            return balances
