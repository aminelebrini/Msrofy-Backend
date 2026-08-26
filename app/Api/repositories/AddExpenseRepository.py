from sqlalchemy.orm import Session
from models.Expense import Expense
from models.ExpenseSplit import ExpenseSplit
from models.GroupMember import GroupMember

class AddExpenseRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_expense(self,payer, group_id, title, totalAmount):

        group_members = self.db.query(GroupMember).filter(GroupMember.group_id == group_id).all()

        devide_amount = totalAmount / len(group_members)

        new_expense = Expense(
            group_id = group_id,
            payer_id =payer,
            title = title,
            total_amount = totalAmount
        )
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)

        split = []
        for member in group_members:
            expense_split = ExpenseSplit(
                expense_id = new_expense.id,
                user_id = member.user_id,
                amount_owed = devide_amount
            )

            split.append(expense_split)

        self.db.add_all(split)
        self.db.commit()
        self.db.refresh(split)

        return new_expense


        

        