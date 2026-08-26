from sqlalchemy.orm import Session
from models.Expense import Expense
from models.ExpenseSplit import ExpenseSplit

class AddExpenseRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_expense(self,payer, group_id, title, totalAmount):
        new_expense = Expense(
            group_id = group_id,
            payer_id =payer,
            title = title,
            total_amount = totalAmount
        )
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)

        