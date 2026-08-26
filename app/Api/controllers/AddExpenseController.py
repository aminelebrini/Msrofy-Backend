from services.AddExpenseService import AddExpenseService

class AddExpenseController:
    def __init__(self, db):
        self.db = db
        self.add_expense = AddExpenseService(self.db)

    def add_expense(self,payer, group_id, title, totalAmount):
        return self.add_expense(payer, group_id, title, totalAmount)