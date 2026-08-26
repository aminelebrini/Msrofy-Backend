from repositories.AddExpenseRepository import AddExpenseRepository

class AddExpenseService:
    def __init__(self, db):
        self.db = db
        self.add_expense_repository = AddExpenseRepository(db)

    def add_expense(self,payer, group_id, title, totalAmount):
        return self.add_expense_repository.add_expense(self,payer, group_id, title, totalAmount)