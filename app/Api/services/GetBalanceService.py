from repositories.GetBalanceRepository import GetBalanceRepository

class GetBalanceService:
    def __init__(self, db):
        self.db = db
        self.get_balance_repository = GetBalanceRepository(db)

    def get_balance(self, Group: int):
        return self.get_balance_repository.get_balance(Group)